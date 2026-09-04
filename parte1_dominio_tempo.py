"""PARTE 1 - Geração do sinal e analise no dominio do tempo"""

import matplotlib.pyplot as plt
from sinal_comum import t, x, x_util, mask20

print("Amplitude pico do sinal somado (medida):", round(max(abs(x)), 3))

fig, axs = plt.subplots(2, 1, figsize=(10, 7), num='Parte 1 - Dominio do tempo')

axs[0].plot(t*1000, x, color='#1f77b4', linewidth=0.8)
axs[0].set_title('Sinal x(t) completo (0 a 200 ms)')
axs[0].set_xlabel('Tempo (ms)'); axs[0].set_ylabel('Amplitude'); axs[0].grid(alpha=0.3)

axs[1].plot(t[mask20]*1000, x[mask20], color='#d62728', label='x(t) = sinal composto')
axs[1].plot(t[mask20]*1000, x_util[mask20], '--', color='#2ca02c', alpha=0.7, label='componente 100 Hz (util)')
axs[1].set_title('Zoom (0 a 20 ms) - sinal composto vs. componente util isolada')
axs[1].set_xlabel('Tempo (ms)'); axs[1].set_ylabel('Amplitude')
axs[1].legend(loc='upper right', fontsize=8); axs[1].grid(alpha=0.3)

fig.tight_layout()
plt.show()
