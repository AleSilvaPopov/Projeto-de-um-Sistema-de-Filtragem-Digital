"""
=====================================================================
 MODULO COMUM - Geracao do sinal e utilitarios compartilhados
 Analise de Sinais e Sistemas - UFGD
=====================================================================
 Este modulo e importado por parte1..parte5. Nao gera graficos
 sozinho - apenas define o sinal x(t) e funcoes auxiliares usadas
 em varias partes do projeto (evita repetir o mesmo codigo 5 vezes).
=====================================================================
"""
import numpy as np

# Parametros de amostragem
fs = 20000           # Hz
T = 0.2              # duracao do sinal
N = int(fs * T)
t = np.arange(N) / fs

# x(t) = sen(2*pi*100*t) + 0,5*sen(2*pi*1000*t) + 0,3*sen(2*pi*3000*t)
f_util, f_ruido1, f_ruido2 = 100, 1000, 3000
x_util   = np.sin(2*np.pi*f_util*t)
x_ruido1 = 0.5*np.sin(2*np.pi*f_ruido1*t)
x_ruido2 = 0.3*np.sin(2*np.pi*f_ruido2*t)
x = x_util + x_ruido1 + x_ruido2

mask20 = t <= 0.02

# FFT
janela = np.hanning(N)
freqs = np.fft.rfftfreq(N, d=1/fs)

def espectro(sig):
    Xf = np.fft.rfft(sig * janela)
    mag = (2/np.sum(janela)) * np.abs(Xf)
    return freqs, mag

def retorna_db(h):
    return 20*np.log10(np.abs(h) + 1e-12)


# filtro passa-baixas
fc = 250             # Hz
nyq = fs / 2
wn = fc / nyq         # Usar no butter/cheby1
