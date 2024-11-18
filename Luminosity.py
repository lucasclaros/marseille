import plotly.graph_objects as go

def create_luminosity_chart(luminosities):
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

    luminosity_colors = ['#ffff99', '#ffcc00', '#ff9900', '#ff6600']
    luminosity_colors.reverse()

    fig = go.Figure(go.Pie(
        labels=luminosity_ranges,
        values=luminosity_counts,
        sort=False,
        marker=dict(colors=luminosity_colors),
        textinfo='percent+label',
        textposition='outside',
    ))

    fig.update_layout(
        title="Distribuição de Luminosidade",
        title_font=dict(size=18, family='Arial', color='black'),
        title_pad=dict(t=50),
        showlegend=True,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(t=100, b=50, l=50, r=50),
        autosize=True
    )

    return fig
