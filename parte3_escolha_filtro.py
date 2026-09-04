"""PARTE 3 - Escolha e justificativa do tipo de filtro digital"""

import numpy as np
import matplotlib.pyplot as plt
from sinal_comum import x, espectro, fc

freqs, mag = espectro(x)

print(f"Filtro escolhido: passa-baixas, fc = {fc} Hz.")

fig, axs = plt.subplots(1, 2, figsize=(13, 5), num='Parte 3 - Escolha do filtro')

ax = axs[0]
ax.plot(freqs, mag, color='#1f77b4', linewidth=0.9)
ax.axvspan(0, fc, color='green', alpha=0.12, label='banda passante')
ax.axvspan(fc, 4000, color='red', alpha=0.08, label='banda rejeitada')
ax.axvline(fc, color='black', ls='--', linewidth=1.2, label=f'fc = {fc} Hz')
ax.set_xlim(0, 4000)
ax.set_title('Espectro do sinal e corte escolhido')
ax.set_xlabel('Frequencia (Hz)'); ax.set_ylabel('Amplitude')
ax.legend(fontsize=8); ax.grid(alpha=0.3)

ax2 = axs[1]
f_axis = np.linspace(0, 4000, 2000)
lpf  = (f_axis <= fc).astype(float)
hpf  = (f_axis >  fc).astype(float)
bpf  = ((f_axis > 400) & (f_axis < 2000)).astype(float)
notch = 1 - (((f_axis > 900) & (f_axis < 1100)) | ((f_axis > 2900) & (f_axis < 3100))).astype(float)

ax2.plot(f_axis, lpf, label='Passa-baixas (ESCOLHIDO)', color='#2ca02c', linewidth=2)
ax2.plot(f_axis, hpf - 0.02, label='Passa-altas (descartado)', color='#d62728', linestyle='--')
ax2.plot(f_axis, bpf - 0.04, label='Passa-faixa (descartado)', color='#9467bd', linestyle='--')
ax2.plot(f_axis, notch - 0.06, label='Rejeita-faixa/notch duplo (desnecessario)', color='#ff7f0e', linestyle='--')
for f0 in [100, 1000, 3000]:
    ax2.axvline(f0, color='gray', alpha=0.3, linewidth=0.8)
ax2.set_ylim(-0.15, 1.15)
ax2.set_title('Mascaras ideais - comparação de tipos de filtro')
ax2.set_xlabel('Frequencia (Hz)'); ax2.set_ylabel('Ganho ideal (1 = passa, 0 = corta)')
ax2.legend(fontsize=7, loc='center right'); ax2.grid(alpha=0.3)

fig.tight_layout()
plt.show()
