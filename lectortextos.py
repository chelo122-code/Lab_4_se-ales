import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pywt

# Cargar los datos del archivo
data = np.loadtxt("ubicacion del archivo .txt", delimiter=',')

# Separar tiempo y amplitud
tiempo = data[:, 0]
amplitud = data[:, 1]

# Atenuar los valores de amplitud entre -40 y 40
fclasismo = np.array([0 if -40 <= x <= 2060 else x for x in amplitud])

# Aplicar la wavelet Morlet
scales = np.arange(1, 40)  # Define un rango de escalas 100

# Especificar parámetros de la wavelet Morlet
wavelet = 'cmor1.5-1.0'  # Aquí 1.5 es el ancho de banda y 1.0 la frecuencia central

# Aplicar la transformada continua de wavelet (CWT) con los parámetros especificados
coeficientes, frecuencias = pywt.cwt(amplitud, scales, wavelet)

# Visualizar el espectrograma de la transformada wavelet
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(coeficientes), extent=[tiempo.min(), tiempo.max(), scales.min(), scales.max()],
           cmap='jet', aspect='auto', interpolation='bilinear')
plt.colorbar(label='Magnitud')
plt.xlabel("Tiempo (s)")
plt.ylabel("Escala")
plt.title("Transformada Wavelet Continua usando Morlet")
plt.show()

# Detectar picos en la señal atenuada
picos, _ = find_peaks(fclasismo, height=0)
numero_picos = len(picos)
LPM = numero_picos/5 #5 por ser de cinco minutos de toma de datos

# Calcular intervalos entre picos y su desviación estándar
intervalos_picos = np.diff(tiempo[picos])
desviacion_estandar = round(np.std(intervalos_picos), 5)

# Ventana alrededor de cada pico
ventana = 0.1  # Ventana de 0.1 segundos, ajústala si es necesario
ventanas_picos = []

for pico in picos:
    # Identificar el índice inicial y final de la ventana
    idx_ini = np.where(tiempo >= (tiempo[pico] - ventana))[0][0]
    idx_fin = np.where(tiempo <= (tiempo[pico] + ventana))[0][-1]
    ventanas_picos.append((tiempo[idx_ini:idx_fin], fclasismo[idx_ini:idx_fin]))

# Visualización de la señal completa y los picos detectados
plt.figure(figsize=(10, 6))
#plt.plot(tiempo, amplitud, label="Original")
plt.plot(tiempo, fclasismo, label='Señal Atenuada')
plt.plot(tiempo[picos], fclasismo[picos], 'rx', label='Picos Detectados')

# detallito de sombreado bajo la curva
for ventana_tiempo, ventana_amplitud in ventanas_picos:
    plt.fill_between(ventana_tiempo, ventana_amplitud, color='gray', alpha=0.3)

print(f"Número de picos detectados: {numero_picos}")
print(f"Latidos por minutos: {LPM}")
print(f"Desviación estándar entre intervalos de picos: {desviacion_estandar} segundos")
#verificando los datos de tiempo de los datos
print(f"Rango de tiempo de los datos: {tiempo.min()} a {tiempo.max()}")

# Configurar límites del eje x

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend()
plt.show()
