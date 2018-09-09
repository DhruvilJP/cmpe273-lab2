"""The Python implementation of the GRPC Calculator server."""

from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def Add(self, request, context):
        return calculator_pb2.CalculatorResponse(result = request.var_a + request.var_b, var_a = request.var_a, var_b = request.var_b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)

    #port used for communication is 8080
    server.add_insecure_port('[::]:8080')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
