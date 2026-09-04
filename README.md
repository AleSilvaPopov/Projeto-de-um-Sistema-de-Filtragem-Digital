# Projeto de um Sistema de Filtragem Digital

Sinal simulado de um sensor industrial, contaminado por interferências, e
recuperado por filtragem digital:

```
x(t) = sen(2π·100t) + 0,5·sen(2π·1000t) + 0,3·sen(2π·3000t)
```

- **100 Hz** — componente útil (informação de interesse do sensor)
- **1000 Hz e 3000 Hz** — interferências/ruído a remover

## Requisitos

Python 3 com `numpy`, `scipy` e `matplotlib`:

```
pip install numpy scipy matplotlib
```

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| `sinal_comum.py` | Geração de x(t), parâmetros de amostragem e funções compartilhadas (FFT, conversão para dB). Não roda sozinho. |
| `parte1_dominio_tempo.py` | Sinal no domínio do tempo. |
| `parte2_analise_fft.py` | Análise espectral via FFT: número de picos, frequências e amplitudes. |
| `parte3_escolha_filtro.py` | Filtro passa-baixas escolhido e frequência de corte (fc = 250 Hz). |
| `parte4_butterworth_vs_chebyshev.py` | Comparação Butterworth vs. Chebyshev I (ordem 4): atenuação, ondulação. |
| `parte5_influencia_ordem.py` | Efeito da ordem do filtro (2, 4 e 8) na rejeição de ruído. |

## Como executar

Cada `parteN_*.py` roda de forma independente (desde que `sinal_comum.py`
esteja na mesma pasta) e abre sua própria janela de gráfico:

```
python parte1_dominio_tempo.py
python parte2_analise_fft.py
python parte3_escolha_filtro.py
python parte4_butterworth_vs_chebyshev.py
python parte5_influencia_ordem.py
```

Cada script imprime no console apenas os resultados numéricos (picos da
FFT, atenuações em dB) e plota os gráficos correspondentes. As discussões
e interpretações técnicas de cada etapa estão descritas abaixo.

## Discussões técnicas

### 1. Domínio do tempo

- 100 Hz = componente útil (maior amplitude).
- 1000 Hz e 3000 Hz = ruído.
- Só olhando o gráfico no tempo não dá pra saber quais frequências estão
  presentes — só que há distorção. Por isso é preciso a FFT.

### 2. FFT

- 3 picos: 100 Hz (1,0), 1000 Hz (0,5), 3000 Hz (0,3).
- Maior amplitude: 100 Hz — confirma que é a componente útil.

### 3. Escolha do filtro

- **Passa-baixas**, pois o útil está abaixo e todo o ruído está acima.
- Passa-altas removeria o útil; passa-faixa e notch seriam mais
  complexos sem necessidade.
- fc = 250 Hz (entre 100 Hz e 1000 Hz).

### 4. Butterworth vs. Chebyshev (ordem 4)

| Filtro | @1000 Hz | @3000 Hz | ondulações |
|---|---|---|---|
| Butterworth | -48,4 dB | -89,0 dB | Não |
| Chebyshev I (1 dB) | -60,1 dB | -101,2 dB | Sim |

Chebyshev rejeita mais, mas tem ondulações na banda passante — indesejável
aqui, já que se quer preservar a amplitude do sinal de 100 Hz.
Butterworth é a escolha mais segura para essa aplicação.

### 5. Influência da ordem (2, 4, 8)

| Ordem | Butter @1000 Hz | Butter @3000 Hz | Cheby @1000 Hz | Cheby @3000 Hz |
|---|---|---|---|---|
| 2 | -24,2 dB | -44,5 dB | -24,1 dB | -44,6 dB |
| 4 | -48,4 dB | -89,0 dB | -60,1 dB | -101,2 dB |
| 8 | -96,9 dB | -178,1 dB | -132,1 dB | -213,8 dB |

Ordem maior = corte mais íngreme e mais rejeição de ruído, mas mais
custo computacional. Ordem 8 deixa o sinal filtrado quase idêntico à
senoide ideal de 100 Hz; ordem 2 ainda tem resíduo perceptível.

## Conclusão

Filtro passa-baixas Butterworth, ordem 4, fc = 250 Hz: boa rejeição do
ruído (-48 dB e -89 dB), sem ondulações, e complexidade razoável.
