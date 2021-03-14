#!/usr/bin/python

import os
import random
import time
import traceback
from concurrent import futures

import grpc
import demo_pb2
import demo_pb2_grpc

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

from logger import getJSONLogger
logger = getJSONLogger('adservice-v2-server')


class AdServiceV2():
    # TODO:
    # Implemet the Ad service business logic
    def GetAds(self, request, context):
        return demo_pb2.AdResponse(2, "AdV2 - Items with 25 discount!")

    # Uncomment to enable the HealthChecks for the Ad service
    # Note: These are needed for the liveness and readiness probes

    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)

    def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED)


if __name__ == "__main__":
    logger.info("initializing adservice-v2")

    # TODO:
    # create gRPC server, add the Ad-v2 service and start it
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    service = AdServiceV2()
    demo_pb2_grpc.add_AdServiceServicer_to_server(service, server)

    print("Server starting on port 9556...")
    server.add_insecure_port("[::]:9556")
    server.start

    # keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

    # Uncomment to add the HealthChecks to the gRPC server to the Ad-v2 service
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
