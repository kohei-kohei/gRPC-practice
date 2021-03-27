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

// .protoファイルに定義した関数を記述
func (s *Server) GachaResult(ctx context.Context, in *gacha.Request) (*gacha.Response, error) {
	log.Printf("Receive message body from client: %s", in.Count)

	return &gacha.Response{Result: getResult(in.Count)}, nil
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

	switch {
	case num < 5:
		result = "星4"
	case num < 20:
		result = "星3"
	default:
		result = "星2"
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
