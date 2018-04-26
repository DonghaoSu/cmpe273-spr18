package org.jpdna.grpchello;

import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;

@javax.annotation.Generated("by gRPC proto compiler")
public class PingPongGrpc {

  private PingPongGrpc() {}

  public static final String SERVICE_NAME = "helloworld.PingPong";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi
  public static final io.grpc.MethodDescriptor<org.jpdna.grpchello.Request,
      org.jpdna.grpchello.Response> METHOD_PONG =
      io.grpc.MethodDescriptor.create(
          io.grpc.MethodDescriptor.MethodType.UNARY,
          generateFullMethodName(
              "helloworld.PingPong", "pong"),
          io.grpc.protobuf.ProtoUtils.marshaller(org.jpdna.grpchello.Request.getDefaultInstance()),
          io.grpc.protobuf.ProtoUtils.marshaller(org.jpdna.grpchello.Response.getDefaultInstance()));

  public static PingPongStub newStub(io.grpc.Channel channel) {
    return new PingPongStub(channel);
  }

  public static PingPongBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new PingPongBlockingStub(channel);
  }

  public static PingPongFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new PingPongFutureStub(channel);
  }

  public static interface PingPong {

    public void pong(org.jpdna.grpchello.Request request,
        io.grpc.stub.StreamObserver<org.jpdna.grpchello.Response> responseObserver);
  }

  public static interface PingPongBlockingClient {

    public org.jpdna.grpchello.Response pong(org.jpdna.grpchello.Request request);
  }

  public static interface PingPongFutureClient {

    public com.google.common.util.concurrent.ListenableFuture<org.jpdna.grpchello.Response> pong(
        org.jpdna.grpchello.Request request);
  }

  public static class PingPongStub extends io.grpc.stub.AbstractStub<PingPongStub>
      implements PingPong {
    private PingPongStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PingPongStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PingPongStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PingPongStub(channel, callOptions);
    }

    @java.lang.Override
    public void pong(org.jpdna.grpchello.Request request,
        io.grpc.stub.StreamObserver<org.jpdna.grpchello.Response> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_PONG, getCallOptions()), request, responseObserver);
    }
  }

  public static class PingPongBlockingStub extends io.grpc.stub.AbstractStub<PingPongBlockingStub>
      implements PingPongBlockingClient {
    private PingPongBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PingPongBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PingPongBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PingPongBlockingStub(channel, callOptions);
    }

    @java.lang.Override
    public org.jpdna.grpchello.Response pong(org.jpdna.grpchello.Request request) {
      return blockingUnaryCall(
          getChannel().newCall(METHOD_PONG, getCallOptions()), request);
    }
  }

  public static class PingPongFutureStub extends io.grpc.stub.AbstractStub<PingPongFutureStub>
      implements PingPongFutureClient {
    private PingPongFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PingPongFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PingPongFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PingPongFutureStub(channel, callOptions);
    }

    @java.lang.Override
    public com.google.common.util.concurrent.ListenableFuture<org.jpdna.grpchello.Response> pong(
        org.jpdna.grpchello.Request request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_PONG, getCallOptions()), request);
    }
  }

  public static io.grpc.ServerServiceDefinition bindService(
      final PingPong serviceImpl) {
    return io.grpc.ServerServiceDefinition.builder(SERVICE_NAME)
      .addMethod(
        METHOD_PONG,
        asyncUnaryCall(
          new io.grpc.stub.ServerCalls.UnaryMethod<
              org.jpdna.grpchello.Request,
              org.jpdna.grpchello.Response>() {
            @java.lang.Override
            public void invoke(
                org.jpdna.grpchello.Request request,
                io.grpc.stub.StreamObserver<org.jpdna.grpchello.Response> responseObserver) {
              serviceImpl.pong(request, responseObserver);
            }
          })).build();
  }
}
