import grpc
import time
from concurrent import futures
import sensor_pb2
import sensor_pb2_grpc

class SensorService(sensor_pb2_grpc.SensorServiceServicer):

    def StreamSensorData(self, request_iterator, context):
        for request in request_iterator:
            temperature = request.temperature
            humidity = request.humidity
            luminosity = request.luminosity           


            status = "OK" if temperature < 35 else "Alerta: Temperatura média acima de 35 graus!"
            sensor_data = sensor_pb2.DashboardUpdate(
                sensor_id=request.sensor_id,
                avg_temperature=round(temperature, 2),
                avg_humidity=round(humidity, 2),
                avg_luminosity=round(luminosity, 2),
                status=status
            )

            yield sensor_data
            time.sleep(1.0)

def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_SensorServiceServicer_to_server(SensorService(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    print("Servidor gRPC iniciado na porta {}...".format(port))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
