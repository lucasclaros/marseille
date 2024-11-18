# marseille
Marseille is a gRPC application for real-time monitoring of temperature data. It leverages bidirectional streaming to provide continuous and efficient updates of temperature readings, making it ideal for scenarios where low latency and scalability are critical.

Este é um **dashboard interativo** projetado para monitorar e exibir dados de sensores em tempo real. A comunicação entre o cliente e o servidor é realizada usando o protocolo **gRPC**, permitindo que os dados de **temperatura**, **umidade** e **luminosidade** sejam transmitidos em tempo real e visualizados por meio de gráficos interativos e uma tabela.

## Funcionalidades Principais

1. **Comunicação gRPC Bidirecional**:
   - O cliente e o servidor se comunicam via **gRPC** com **streaming bidirecional**. O servidor envia dados contínuos para o cliente sem a necessidade de requisições repetidas.
   - O cliente pode gerar dados simulados para testes ou utilizar dados reais de sensores.

2. **Simulação de Dados**:
   - Para desenvolvimento e teste, o cliente gera **dados simulados** de sensores (temperatura, umidade e luminosidade) e os envia ao servidor a cada intervalo de tempo.
   - Esses dados são processados e exibidos em tempo real.

3. **Exibição de Dados**:
   - **Gráficos Interativos**:
     - **Gráfico de Temperatura e Umidade**: Exibe a variação de temperatura e umidade ao longo do tempo, utilizando linhas para cada grandeza.
     - **Gráfico de Luminosidade**: Exibe a distribuição de luminosidade em faixas específicas utilizando um gráfico de pizza.
   - **Tabela de Dados**: Exibe as leituras mais recentes dos sensores, incluindo **temperatura**, **umidade** e **status**.

4. **Atualização em Tempo Real**:
   - Gráficos e a tabela são atualizados automaticamente conforme o servidor envia novos dados.
   - O layout da aplicação é projetado para exibir dados em tempo real de forma clara e interativa.

## Tecnologias Utilizadas

- **gRPC**: Comunicação eficiente e de baixa latência entre o cliente e o servidor.
- **Streamlit**: Interface gráfica interativa para exibição dos gráficos e tabelas.
- **Plotly**: Biblioteca para a criação de gráficos interativos.
- **Python**: Linguagem utilizada para a implementação da lógica do servidor e cliente.

## Fluxo da Aplicação

1. O **servidor** gera e envia dados de sensores para o cliente por meio de gRPC, utilizando dados reais ou simulados.
2. O **cliente** recebe esses dados em tempo real, processa e atualiza os gráficos e a tabela.
3. A aplicação é capaz de exibir **temperatura**, **umidade** e **luminosidade** de maneira interativa e em tempo real.

## Objetivo da Aplicação

O objetivo principal da aplicação é fornecer uma maneira prática e visual de monitorar dados de sensores em tempo real, ideal para ambientes que requerem monitoramento contínuo de condições, como **salas de servidores**, **laboratórios**, **hospitais** e **instalações industriais**.

---

## Setup

### Requisitos

- Python 3.7+
- Dependências do projeto: `grpcio`, `plotly`, `streamlit`, `pandas`

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/lucasclaros/marseille.git
   cd dashboard-sensores
