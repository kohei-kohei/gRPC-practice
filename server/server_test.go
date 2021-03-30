package main

import (
	"context"
	"gacha"
	"log"
	"net"
	"reflect"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"
)

const bufSize = 1024 * 1024

var lis *bufconn.Listener

func init() {
	lis = bufconn.Listen(bufSize)
	s := grpc.NewServer()
	gacha.RegisterGachaServer(s, &Server{})
	go func() {
		if err := s.Serve(lis); err != nil {
			log.Fatal(err)
		}
	}()
}

func bufDialer(ctx context.Context, address string) (net.Conn, error) {
	return lis.Dial()
}

func Test_getResult(t *testing.T) {
	type args struct {
		count string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{name: "normal_1", args: args{count: "1"}, want: []string{"星2"}},
		{name: "normal_2", args: args{count: "2"}, want: []string{"星2", "星3"}},
		{name: "normal_3", args: args{count: "3"}, want: []string{"星2", "星3", "星4"}},
		{name: "exception_1", args: args{count: "0"}, want: nil},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getResult(tt.args.count); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getResult() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_gachaConfig(t *testing.T) {
	type args struct {
		num int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{name: "normal_1", args: args{num: 0}, want: "星4"},
		{name: "normal_2", args: args{num: 10}, want: "星3"},
		{name: "normal_3", args: args{num: 20}, want: "星2"},
		{name: "fail_1", args: args{num: 10}, want: "星4"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := gachaConfig(tt.args.num); got != tt.want {
				t.Errorf("gachaConfig() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestServer_TotalResult(t *testing.T) {
	type args struct {
		ctx context.Context
		in  *gacha.Request
	}
	ctx := context.Background()
	tests := []struct {
		name    string
		args    args
		want    *gacha.Response
		wantErr error
	}{
		{name: "normal_1", args: args{ctx: ctx, in: &gacha.Request{Count: "1"}}, want: &gacha.Response{Result: []string{"0", "0", "0", "0"}}, wantErr: nil},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			conn, err := grpc.DialContext(ctx, "bufnet", grpc.WithContextDialer(bufDialer), grpc.WithInsecure())
			if err != nil {
				t.Fatal(err)
			}
			defer conn.Close()

			client := gacha.NewGachaClient(conn)

			got, err := client.TotalResult(tt.args.ctx, tt.args.in)
			if err != tt.wantErr {
				t.Errorf("Server.TotalResult() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got.Result, tt.want.Result) {
				t.Errorf("Server.TotalResult() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestServer_GachaResult(t *testing.T) {
	type args struct {
		ctx context.Context
		in  *gacha.Request
	}
	ctx := context.Background()
	tests := []struct {
		name    string
		args    args
		want    *gacha.Response
		wantErr error
	}{
		{name: "normal_1", args: args{ctx: ctx, in: &gacha.Request{Count: "1"}}, want: &gacha.Response{Result: []string{"星4"}}, wantErr: nil},
		{name: "normal_1", args: args{ctx: ctx, in: &gacha.Request{Count: "3"}}, want: &gacha.Response{Result: []string{"星2", "星3", "星4"}}, wantErr: nil},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			conn, err := grpc.DialContext(ctx, "bufnet", grpc.WithContextDialer(bufDialer), grpc.WithInsecure())
			if err != nil {
				t.Fatal(err)
			}
			defer conn.Close()

			client := gacha.NewGachaClient(conn)

			got, err := client.GachaResult(tt.args.ctx, tt.args.in)
			if err != tt.wantErr {
				t.Errorf("Server.TotalResult() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got.Result, tt.want.Result) {
				t.Errorf("Server.TotalResult() = %v, want %v", got, tt.want)
			}
		})
	}
}
