import sys

sys.path.append('../gacha')

import grpc
import gacha_pb2
import gacha_pb2_grpc
from flask import Flask, render_template, request

def gacha_server(count):
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = gacha_pb2_grpc.GachaStub(channel)
        response = stub.GachaResult(gacha_pb2.Request(count=count))
    
    return response.result 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET"])
def login_manager():
    results = gacha_server(request.args.get("count"))
    return render_template("result.html", results=results)

if __name__ == '__main__':
    app.run(port=8000)