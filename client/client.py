import sys

sys.path.append('../gacha')

import grpc
import gacha_pb2
import gacha_pb2_grpc
from flask import Flask, render_template, request

def grpc_server(count, func_name):
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = gacha_pb2_grpc.GachaStub(channel)
        if func_name == "gacha":
            response = stub.GachaResult(gacha_pb2.Request(count=count))
        elif func_name == "total":
            response = stub.TotalResult(gacha_pb2.Request(count=count))
    
    return response.result 

app = Flask(__name__)

@app.route("/")
def index():
    results = grpc_server("TotalResult", "total")
    return render_template("index.html", results=results)

@app.route("/result", methods=["GET"])
def login_manager():
    results = grpc_server(request.args.get("count"), "gacha")
    return render_template("result.html", results=results)

if __name__ == '__main__':
    app.run(port=8000)