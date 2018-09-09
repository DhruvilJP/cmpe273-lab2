"""The Python implementation of the GRPC Calculator client."""

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.CalculatorRequest(var_a = 2, var_b = 3)) #the numbers to be added are 2 and 3
        print("Addition of " + str(response.var_a) + " and " + str(response.var_b) + " is " + str(response.result))


if __name__ == '__main__':
    run()
