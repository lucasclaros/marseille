import plotly.graph_objects as go

# Função para criar o gráfico de luminosidade como pizza
def create_luminosity_chart(luminosities):
    # Faixas de luminosidade ajustadas para a escala de 0 a 1000 lux
    luminosity_ranges = ['0-25 lux (Baixa)', '26-50 lux (Média-Baixa)', '51-75 lux (Média-Alta)', '76-100 lux (Alta)']
    luminosity_counts = [0, 0, 0, 0]

    for lum in luminosities:
        # Ajusta a luminosidade para as faixas definidas
        if lum <= 25:
            luminosity_counts[0] += 1
        elif lum <= 50:
            luminosity_counts[1] += 1
        elif lum <= 75:
            luminosity_counts[2] += 1
        else:
            luminosity_counts[3] += 1

    # Definir as cores para cada faixa de luminosidade (do mais escuro para o mais claro)
    luminosity_colors = ['#ffff99', '#ffcc00', '#ff9900', '#ff6600']
    luminosity_colors.reverse()  # Inverte a ordem para começar do mais claro

    # Criar o gráfico de pizza
    fig = go.Figure(go.Pie(
        labels=luminosity_ranges,
        values=luminosity_counts,
        title="Distribuição de Luminosidade",
        sort=False,  # Impede a ordenação automática
        marker=dict(colors=luminosity_colors),  # Define as cores fixas
        textinfo='percent+label',  # Exibe a porcentagem e o nome da faixa
        textposition='outside',  # Garante que o texto sempre fique fora do gráfico
    ))

    # Melhorando o layout, personalizando título e outros elementos
    fig.update_layout(
        title="Distribuição de Luminosidade",
        title_font=dict(size=18, family='Arial', color='black'),  # Ajusta o estilo do título
        title_pad=dict(t=50),  # Aumenta o espaço entre o título e o gráfico
        showlegend=True,  # Exibe a legenda
        plot_bgcolor="white",  # Altera o fundo para branco
        paper_bgcolor="white",  # Altera o fundo da área de impressão
        margin=dict(t=100, b=50, l=50, r=50),  # Aumenta a margem superior para afastar as labels do título
        autosize=True
    )

    return fig
