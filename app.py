import scipy.stats
import streamlit as st
import time

st.header('Jogando uma moeda')

# Inicializa o gráfico de linhas com um valor inicial
chart = st.line_chart([0.5])

def toss_coin(n):
    # Simula n lançamentos de moeda (0 = coroa, 1 = cara)
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Itera sobre os resultados, calcula a média e atualiza o gráfico
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        # Adiciona uma nova linha de dados ao gráfico
        chart.add_rows([mean])
        # Pequeno atraso para visualizar o progresso
        time.sleep(0.05)

    return mean

# Widget de controle deslizante para o número de tentativas
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
# Botão para iniciar a simulação
start_button = st.button('Executar')

# Lógica executada quando o botão é clicado
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
    # Chama a função de lançamento da moeda
    mean = toss_coin(number_of_trials)
    # Opcional: Você pode adicionar aqui um st.write(f'Média final: {mean}') se quiser mostrar o resultado final.