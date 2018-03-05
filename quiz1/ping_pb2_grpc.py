# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ping_pb2 as ping__pb2


class PingPongStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.pong = channel.unary_unary(
        '/PingPong/pong',
        request_serializer=ping__pb2.Request.SerializeToString,
        response_deserializer=ping__pb2.Response.FromString,
        )


class PingPongServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def pong(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingPongServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'pong': grpc.unary_unary_rpc_method_handler(
          servicer.pong,
          request_deserializer=ping__pb2.Request.FromString,
          response_serializer=ping__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PingPong', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))