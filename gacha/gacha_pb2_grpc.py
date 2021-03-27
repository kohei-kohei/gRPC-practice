# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gacha_pb2 as gacha__pb2


class GachaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GachaResult = channel.unary_unary(
                '/gacha.Gacha/GachaResult',
                request_serializer=gacha__pb2.Request.SerializeToString,
                response_deserializer=gacha__pb2.Response.FromString,
                )


class GachaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GachaResult(self, request, context):
        """rpc 実行関数(引数) returns (返り値) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GachaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GachaResult': grpc.unary_unary_rpc_method_handler(
                    servicer.GachaResult,
                    request_deserializer=gacha__pb2.Request.FromString,
                    response_serializer=gacha__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gacha.Gacha', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gacha(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GachaResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gacha.Gacha/GachaResult',
            gacha__pb2.Request.SerializeToString,
            gacha__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)