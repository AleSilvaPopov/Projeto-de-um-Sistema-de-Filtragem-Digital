"""PARTE 2 - Analise espectral via FFT"""

import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sinal_comum import x, espectro

freqs, mag = espectro(x)

peaks, _ = find_peaks(mag, height=0.05*max(mag), distance=20)
peak_freqs, peak_mags = freqs[peaks], mag[peaks]

print(f"Numero de picos espectrais detectados: {len(peak_freqs)}")
print("\nPicos espectrais (ordenados por amplitude, do maior para o menor):")
for f, m in sorted(zip(peak_freqs, peak_mags), key=lambda p: -p[1]):
    print(f"  f = {f:8.1f} Hz   |   amplitude = {m:.4f}")

maior = max(zip(peak_freqs, peak_mags), key=lambda p: p[1])
print(f"\nComponente de maior amplitude: {maior[0]:.0f} Hz (amplitude {maior[1]:.3f})")

fig, ax = plt.subplots(figsize=(10, 5), num='Parte 2 - Espectro FFT')
ax.plot(freqs, mag, color="#b41f1f", linewidth=0.9)
ax.plot(peak_freqs, peak_mags, 'rx', markersize=9)
for f, m in zip(peak_freqs, peak_mags):
    ax.annotate(f'{f:.0f} Hz\n({m:.2f})', (f, m), textcoords="offset points",
                xytext=(0, 8), ha='center', fontsize=8)
    
ax.set_xlim(0, 4000)
ax.set_title('Espectro (FFT com janela de Hanning) - picos identificados')
ax.set_xlabel('Frequencia (Hz)'); ax.set_ylabel('Amplitude'); ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
