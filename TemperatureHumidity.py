# TemperatureHumidity.py
import streamlit as st
import plotly.graph_objs as go

def create_temperature_humidity_chart(temperatures, humidities):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(range(len(temperatures))),
        y=temperatures,
        mode='lines',
        name='Temperatura (°C)',
        line=dict(color='#FF6347', width=3)  # Cor laranja suave
    ))

    # Adiciona o gráfico de umidade com cor azul
    fig.add_trace(go.Scatter(
        x=list(range(len(humidities))),
        y=humidities,
        mode='lines',
        name='Umidade (%)',
        line=dict(color='#1E90FF', width=3)  # Cor azul
    ))

    fig.update_layout(
        title='Temperatura e Umidade',
        title_font=dict(size=18, family='Arial', color='black'),
        title_pad=dict(t=50),
        xaxis_title='Leituras',
        yaxis_title='Valor',
        dragmode=False,  # Desabilita o arrasto (pan)
        hovermode=False,  # Desabilita o hover
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        autosize=True,
        showlegend=True
    )

    return fig
