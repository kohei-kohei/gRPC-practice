import sys

sys.path.append('../gacha')

import grpc
import gacha_pb2
import gacha_pb2_grpc

def gacha_server(stub, count):
    response = stub.GachaResult(gacha_pb2.Request(count=count))
    print('Response from server: {}'.format(response.result))

def run():
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = gacha_pb2_grpc.GachaStub(channel)
        count = input("ガチャを回す回数は? > ")
        gacha_server(stub, count)

if __name__ == '__main__':
    run()