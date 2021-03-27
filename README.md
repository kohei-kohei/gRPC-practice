# gRPCの勉強

client がガチャを回す回数を引数にリクエストを送り、server がその回数分の結果をまとめてレスポンスする。

## proto

protoファイルに Protocol Buffer を定義する

Go 用にビルドする
```protoc --go_out=plugins=grpc:../gacha gacha.proto```

## gacha

ビルドして生成されたコードが置かれている

## server

9000番ポートで Listen している
```go run server.go```

5%で星4、15%で星3、80%で星2が排出される
星の数が多いほどレアリティーが高い

## client

ガチャを回す回数を標準入力してからリクエストをしている
