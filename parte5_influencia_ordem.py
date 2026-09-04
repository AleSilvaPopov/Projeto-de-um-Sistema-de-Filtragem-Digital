"""PARTE 5 - Influencia da ordem do filtro (2, 4 e 8)"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, freqz, filtfilt
from sinal_comum import fs, t, x, x_util, mask20, retorna_db, fc, wn

ripple_db = 1
ordens = [2, 4, 8]
cores = {2: '#2ca02c', 4: '#1f77b4', 8: '#d62728'}

fig, axs = plt.subplots(2, 2, figsize=(13, 8), num='Parte 5 - Influencia da ordem')

print(f"{'Ordem':<6}{'Butter@1000':>14}{'Butter@3000':>14}{'Cheby@1000':>13}{'Cheby@3000':>13}")
for ordem in ordens:
    b_b, a_b = butter(ordem, wn, btype='low')
    b_c, a_c = cheby1(ordem, ripple_db, wn, btype='low')
    w_b, h_b = freqz(b_b, a_b, worN=8000, fs=fs)
    w_c, h_c = freqz(b_c, a_c, worN=8000, fs=fs)
    db_b, db_c = retorna_db(h_b), retorna_db(h_c)

    axs[0,0].plot(w_b, db_b, color=cores[ordem], label=f'ordem {ordem}')
    axs[0,1].plot(w_c, db_c, color=cores[ordem], label=f'ordem {ordem}')

    a_b1000 = db_b[np.argmin(np.abs(w_b-1000))]; a_b3000 = db_b[np.argmin(np.abs(w_b-3000))]
    a_c1000 = db_c[np.argmin(np.abs(w_c-1000))]; a_c3000 = db_c[np.argmin(np.abs(w_c-3000))]
    print(f"{ordem:<6}{a_b1000:>13.1f}dB{a_b3000:>13.1f}dB{a_c1000:>12.1f}dB{a_c3000:>12.1f}dB")

    y_b = filtfilt(b_b, a_b, x)
    y_c = filtfilt(b_c, a_c, x)
    axs[1,0].plot(t[mask20]*1000, y_b[mask20], color=cores[ordem], label=f'ordem {ordem}')
    axs[1,1].plot(t[mask20]*1000, y_c[mask20], color=cores[ordem], label=f'ordem {ordem}')

for ax, titulo in [(axs[0,0], 'Butterworth por ordem'), (axs[0,1], 'Chebyshev I por ordem')]:
    for f in [100, 1000, 3000]:
        ax.axvline(f, color='gray', ls=':', alpha=0.5)
    ax.set_xlim(0, 4000); ax.set_ylim(-140, 5)
    ax.set_title(titulo); ax.set_xlabel('Frequencia (Hz)'); ax.set_ylabel('Magnitude (dB)')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

for ax, titulo in [(axs[1,0], 'Sinal filtrado - Butterworth'), (axs[1,1], 'Sinal filtrado - Chebyshev I')]:
    ax.plot(t[mask20]*1000, x_util[mask20], '--', color='black', alpha=0.4, label='100 Hz ideal')
    ax.set_title(titulo); ax.set_xlabel('Tempo (ms)'); ax.set_ylabel('Amplitude')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

fig.tight_layout()
plt.show()
