import grpc
import time
import random
from concurrent import futures
import sensor_pb2
import sensor_pb2_grpc

# Classe que implementa o serviço gRPC
class SensorService(sensor_pb2_grpc.SensorServiceServicer):

    def StreamSensorData(self, request_iterator, context):
        for request in request_iterator:
            # Geração de dados aleatórios para os sensores
            temperature = random.uniform(20, 40)  # Temperatura entre 20 e 40 graus
            humidity = random.uniform(30, 70)      # Umidade entre 30% e 70%
            luminosity = random.uniform(0, 100)    # Luminosidade entre 0% e 100%


            status = "OK" if temperature < 35 else "Alerta: Temperatura média acima de 35 graus!"
            # Criando a resposta com os dados gerados
            sensor_data = sensor_pb2.DashboardUpdate(
                sensor_id=request.sensor_id,
                avg_temperature=round(temperature, 2),
                avg_humidity=round(humidity, 2),
                avg_luminosity=round(luminosity, 2),
                status=status
            )

            # Envia a resposta ao cliente
            yield sensor_data
            time.sleep(0.5)  # Simula um intervalo entre as leituras

# Função para iniciar o servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_SensorServiceServicer_to_server(SensorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
