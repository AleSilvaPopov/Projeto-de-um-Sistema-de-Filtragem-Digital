"""PARTE 4 - Butterworth vs Chebyshev (ordem 4)"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, freqz, filtfilt
from sinal_comum import fs, t, x, x_util, mask20, espectro, retorna_db, fc, wn

ordem = 4
ondulacao_db = 1 

b_butter, a_butter = butter(ordem, wn, btype='low')
b_cheby, a_cheby = cheby1(ordem, ondulacao_db, wn, btype='low')

y_butter = filtfilt(b_butter, a_butter, x)
y_cheby = filtfilt(b_cheby, a_cheby, x)

w_butter, h_butter = freqz(b_butter, a_butter, worN=8000, fs=fs)
w_cheby, h_cheby = freqz(b_cheby, a_cheby, worN=8000, fs=fs)

def atenuacao(w, h, f_alvo):
    return retorna_db(h)[np.argmin(abs(w - f_alvo))]

att_b_1000 = atenuacao(w_butter, h_butter, 1000)
att_b_3000 = atenuacao(w_butter, h_butter, 3000)
att_c_1000 = atenuacao(w_cheby, h_cheby, 1000)
att_c_3000 = atenuacao(w_cheby, h_cheby, 3000)

print(f"--- Atenuacao (ordem {ordem}, fc={fc} Hz) ---")
print(f"Butterworth  @1000Hz: {att_b_1000:.1f} dB   @3000Hz: {att_b_3000:.1f} dB")
print(f"Chebyshev I  @1000Hz: {att_c_1000:.1f} dB   @3000Hz: {att_c_3000:.1f} dB")

fig, axs = plt.subplots(2, 2, figsize=(13, 8), num='Parte 4 - Butterworth vs Chebyshev')

axs[0,0].plot(w_butter, retorna_db(h_butter), label='Butterworth', color='#1f77b4')
axs[0,0].plot(w_cheby, retorna_db(h_cheby), label='Chebyshev I', color='#d62728')
axs[0,0].axhline(-3, color='green', ls='--', alpha=0.5, label='-3 dB')
axs[0,0].set_xlim(0, 4000); axs[0,0].set_ylim(-100, 5)
axs[0,0].set_title(f'Resposta em frequencia (ordem {ordem}, fc={fc} Hz)')
axs[0,0].set_xlabel('Frequencia (Hz)'); axs[0,0].set_ylabel('Magnitude (dB)')
axs[0,0].legend(fontsize=8); axs[0,0].grid(alpha=0.3)

axs[0,1].plot(w_butter, retorna_db(h_butter), label='Butterworth', color='#1f77b4')
axs[0,1].plot(w_cheby, retorna_db(h_cheby), label='Chebyshev I', color='#d62728')
axs[0,1].set_xlim(0, fc); axs[0,1].set_ylim(-3, 0.5)
axs[0,1].axvline(100, color='gray', ls=':', alpha=0.6, label='100 Hz (util)')
axs[0,1].set_title('Zoom na banda passante - ondulação')
axs[0,1].set_xlabel('Frequencia (Hz)'); axs[0,1].set_ylabel('Magnitude (dB)')
axs[0,1].legend(fontsize=8); axs[0,1].grid(alpha=0.3)

axs[1,0].plot(t[mask20]*1000, x[mask20], color='lightgray', label='original')
axs[1,0].plot(t[mask20]*1000, x_util[mask20], '--', color='black', alpha=0.5, label='100 Hz ideal')
axs[1,0].plot(t[mask20]*1000, y_butter[mask20], color='#1f77b4', label='Butterworth')
axs[1,0].plot(t[mask20]*1000, y_cheby[mask20], color='#d62728', label='Chebyshev I')
axs[1,0].set_title('Sinal filtrado no tempo (zoom 0-20 ms)')
axs[1,0].set_xlabel('Tempo (ms)'); axs[1,0].set_ylabel('Amplitude')
axs[1,0].legend(fontsize=7); axs[1,0].grid(alpha=0.3)

f_b, m_b = espectro(y_butter)
f_c, m_c = espectro(y_cheby)
axs[1,1].semilogy(f_b, m_b, color='#1f77b4', label='Butterworth')
axs[1,1].semilogy(f_c, m_c, color='#d62728', label='Chebyshev I')
axs[1,1].set_xlim(0, 4000); axs[1,1].set_ylim(1e-5, 2)
axs[1,1].set_title('Espectro do sinal filtrado')
axs[1,1].set_xlabel('Frequencia (Hz)'); axs[1,1].set_ylabel('Amplitude')
axs[1,1].legend(fontsize=8); axs[1,1].grid(alpha=0.3, which='both')

fig.tight_layout()
plt.show()
