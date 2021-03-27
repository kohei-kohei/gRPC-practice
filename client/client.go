package main

import (
	"context"
	"fmt"
	"log"

	"gacha"

	"google.golang.org/grpc"
)

func main() {
	var count string
	fmt.Print("ガチャを回す回数は? > ")
	fmt.Scan(&count)

	var conn *grpc.ClientConn
	conn, err := grpc.Dial(":9000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %s", err)
	}
	defer conn.Close()

	// .protoのserviceに記述した名前
	c := gacha.NewGachaClient(conn)

	response, err := c.GachaResult(context.Background(), &gacha.Request{Count: count})
	if err != nil {
		log.Fatalf("Error when calling SayHello: %s", err)
	}
	log.Printf("Response from server: %v", response.Result)

}
