package main

import (
	"context"
	"log"
	"math/rand"
	"net"
	"strconv"
	"time"

	"gacha"

	"google.golang.org/grpc"
)

type Server struct {
}

type TotalResult struct {
	count int
	rare4 int
	rare3 int
	rare2 int
}

var totalResult TotalResult

// .protoファイルに定義した関数を記述
func (s *Server) GachaResult(ctx context.Context, in *gacha.Request) (*gacha.Response, error) {
	log.Printf("Receive message body from client: %s", in.Count)
	return &gacha.Response{Result: getResult(in.Count)}, nil
}

func (s *Server) TotalResult(ctx context.Context, in *gacha.Request) (*gacha.Response, error) {
	log.Printf("Receive message body from client: %s", in.Count)
	var results []string
	results = append(results, strconv.Itoa(totalResult.count))
	results = append(results, strconv.Itoa(totalResult.rare4))
	results = append(results, strconv.Itoa(totalResult.rare3))
	results = append(results, strconv.Itoa(totalResult.rare2))
	return &gacha.Response{Result: results}, nil
}

func getResult(count string) []string {
	var results []string
	loopNum, _ := strconv.Atoi(count)
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < loopNum; i++ {
		num := rand.Intn(100) // 0〜99
		log.Printf("Generate random number: %d", num)
		results = append(results, gachaConfig(num))
	}

	return results
}

func gachaConfig(num int) string {
	var result string
	rare4Rate := 5
	rare3Rate := 15
	totalResult.count += 1

	switch {
	case num < rare4Rate:
		result = "星4"
		totalResult.rare4 += 1
	case num < rare4Rate+rare3Rate:
		result = "星3"
		totalResult.rare3 += 1
	default:
		result = "星2"
		totalResult.rare2 += 1
	}

	return result
}

func main() {
	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()

	// .protoのserviceに記述した名前
	gacha.RegisterGachaServer(grpcServer, &Server{})

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %s", err)
	}
}
