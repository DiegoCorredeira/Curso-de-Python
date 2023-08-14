"""
CONSTANTE = "Variáveis" que não irão mudar
Muitas condicões no mesmo if (ruim) 
    <- Contagem de complexidade (ruim)
"""

velocidade = 61
local_carro = 101


RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
local_range_pass = (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = local_carro >= local_range_pass

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if velocidade_carro_pass_radar_1:
    print("Velocidade carro passou no radar 1")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if carro_passou_radar_1 and velocidade_carro_pass_radar_1:
    print("Carro multado no radar 1")