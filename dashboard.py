import streamlit as st
import grpc
import sensor_pb2
import sensor_pb2_grpc
import random
import pandas as pd
from TemperatureHumidity import create_temperature_humidity_chart
from Luminosity import create_luminosity_chart

# Função para gerar dados de sensores aleatórios
def generate_sensor_data():
    for _ in range(10):
        yield sensor_pb2.SensorData(
            sensor_id="sensor-01",
            temperature=random.uniform(20, 40),  # Temperatura entre 20 e 40 graus
            humidity=random.uniform(30, 70),      # Umidade entre 30% e 70%
            luminosity=random.uniform(0, 100)   # Luminosidade entre 0 e 100 lux
        )
        
        # Sensor 2 (Luminosidade)
        yield sensor_pb2.SensorData(
            sensor_id="sensor-02",
            temperature=random.uniform(20, 40),  # Temperatura entre 20 e 40 graus
            humidity=random.uniform(30, 70),      # Umidade entre 30% e 70%
            luminosity=random.uniform(0, 100)   # Luminosidade entre 0 e 100 lux
        )

def calculate_average(values):
    if values:
        return round(sum(values) / len(values), 2)
    return 0.0

# Função para configurar o cliente gRPC
def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = sensor_pb2_grpc.SensorServiceStub(channel)
    responses = stub.StreamSensorData(generate_sensor_data())

    temperatures = []
    humidities = []
    luminosities = []

    # Lista para armazenar as linhas da tabela
    sensor_data = []  

    # Configura o Streamlit
    st.set_page_config(layout="wide")
    st.title('Dashboard de Sensores')

    col1, col2 = st.columns([2, 3])
    table_header = ['Sensor ID', 'Temperatura (°C)',  'Umidade (%)', 'Luminosidade (%)', 'Temperatura Média (°C)', 'Status']

    chart_temp_hum = col1.empty()  # Gráfico para o Sensor 1 (Temperatura e Umidade)
    chart_lum = col2.empty()       # Gráfico para o Sensor 2 (Luminosidade)

    for response in responses:
        temperature = round(response.avg_temperature, 2)
        humidity = round(response.avg_humidity, 2)
        luminosity = round(response.avg_luminosity, 2)

        temperatures.append(temperature)
        humidities.append(humidity)
        luminosities.append(luminosity)

        avg_temperature = calculate_average(temperatures)

        sensor_data.append({
            'Sensor ID': response.sensor_id,
            'Temperatura (°C)': f'{temperature} °C' if response.sensor_id == "sensor-01" else 'N/A',
            'Umidade (%)': f'{humidity}%' if response.sensor_id == "sensor-02" else 'N/A',
            'Luminosidade (%)': f'{luminosity} lux' if response.sensor_id == "sensor-02" else 'N/A',
            'Temperatura Média (°C)': f'{avg_temperature} °C' if response.sensor_id == "sensor-01" else 'N/A',
            'Status': response.status
        })

        fig_temp_hum = create_temperature_humidity_chart(temperatures, humidities)
        chart_temp_hum.plotly_chart(fig_temp_hum)

        fig_lum = create_luminosity_chart(luminosities)
        chart_lum.plotly_chart(fig_lum)

    with st.expander("Latest sensor data"):
        df = pd.DataFrame(sensor_data, columns=table_header)
        st.table(df)

if __name__ == "__main__":
    run_client()
