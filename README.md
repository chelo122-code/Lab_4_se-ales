# Laboratorio 4 de señales - Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet

## Introducción.
Para este laboratorio, se revisan algunos aspectos básicos como la actividad que tiene el corazón al realizar ejercicio para la toma de datos. Ademas se hizo un analisis estadistico en la señal al hacer 

## Conceptos principales para tener en cuenta.

### _Actividad simpática y parasimpática del sistema nervioso autónomo (SNA)._

El sistema nervioso autónomo regula diversos procesos fisiológicos del cuerpo de forma involuntaria, es decir, sin control consciente. Este sistema recibe señales (aferencias) de diferentes áreas del sistema nervioso central, las cuales procesan estímulos provenientes tanto del cuerpo como del ambiente externo.

Entre sus funciones, el sistema nervioso autónomo controla la presión arterial, la frecuencia cardíaca, la temperatura corporal, el peso, la digestión, el metabolismo, el balance hidroelectrolítico, la sudoración, la micción, la defecación, la respuesta sexual, y otros procesos vitales. Muchos de estos órganos y sistemas están regulados especialmente por las divisiones simpática o parasimpática del sistema autónomo, y en algunos casos ambos sistemas trabajan juntos de manera recíproca según las necesidades del organismo.

En el **sistema nervioso simpático** se activan las respuestas de "lucha o huida" ante situaciones de estrés o emergencia, preparando al cuerpo para reaccionar. Por ejemplo, en una situación de peligro, el sistema simpático dilata las pupilas para mejorar la visión y permitir una mayor percepción del entorno.

En el **sistema nervioso parasimpático** en cambio, se encarga de conservar y restaurar la energía del cuerpo en momentos de calma, promoviendo la "respuesta de descanso y digestión." Un ejemplo de su acción es la estimulación de la digestión tras una comida: el sistema parasimpático aumenta la producción de enzimas digestivas y la actividad gastrointestinal, permitiendo una digestión y absorción de nutrientes adecuada.


#### Efecto de la actividad simpática y parasimpática en la frecuencia cardiaca.

En el corazón el sistema nervioso autónomo regula la frecuencia y la fuerza de sus latidos según las necesidades del cuerpo. Durante la actividad física el sistema simpático se activa y libera noradrenalina, lo que aumenta la frecuencia cardíaca y la fuerza de contracción para asegurar que la sangre llegue de manera eficiente a los músculos y tejidos que más la requieren. Esto permite que el cuerpo reciba el oxígeno y los nutrientes necesarios para sostener el esfuerzo.

Mientras que en el estado de reposo, el sistema parasimpático entra en acción liberando acetilcolina, el cuál reduce la frecuencia cardíaca y ayuda a conservar energía. Este equilibrio entre ambos sistemas permite que el corazón responda de manera eficaz a las demandas del organismo según el neurotransmisor que se le proporcione, manteniendo una circulación adecuada en diferentes situaciones.

![image](https://github.com/user-attachments/assets/4f136d54-2068-4b7d-823f-2476e2124a01)

### HRV (Variabilidad de la frecuencia cardíaca).

La variabilidad de la frecuencia cardíaca (HRV) es una medida de las diferencias de tiempo entre cada latido del corazón el cuál refleja las variaciones que ocurren entre latidos consecutivos. Aunque idealmente los latidos podrían ocurrir a intervalos de un segundo,en realidad pueden variar ligeramente a veces siendo de 0,99 segundos y otras veces de 1,01 segundos.

Esta variabilidad se evalúa mediante las fluctuaciones en el intervalo R-R, que es el tiempo entre dos picos consecutivos de las ondas R en un electrocardiograma. La onda R representa el punto más alto de la actividad eléctrica en un latido cardíaco, las fluctuaciones en este intervalo indican que el tiempo entre latidos varía, lo cual refleja la capacidad del sistema nervioso autónomo para adaptarse a distintas condiciones fisiológicas.

En el análisis de la HRV, se suelen estudiar diferentes rangos de frecuencia que reflejan varias influencias sobre la variabilidad del ritmo cardíaco. Las frecuencias bajas (LF), por ejemplo, se relacionan más con la actividad simpática que con la parasimpática (aunque se involucra en ambas) por lo que opera en una frecuencia más lenta, respondiendo gradualmente a estímulos de estrés o actividad física. Por otro lado, las frecuencias altas (HF) están más asociadas con la actividad del sistema parasimpático porque actúa más rápidamente y regula funciones en intervalos más cortos, como la respiración. La frecuencia respiratoria puede afectar la variabilidad de la frecuencia cardíaca a través de un fenómeno llamado "arritmia sinusal respiratoria", donde el ritmo cardíaco se acelera durante la inhalación y disminuye durante la exhalación.

![image](https://github.com/user-attachments/assets/f33f9d82-8b56-4e40-a2b2-4360d9a825ae)

### Transformada Wavelet

#### Definición: 
Las wavelets son señales o formas de onda que tienen una duración limitada y un valor promedio de cero. Las wavelets pueden ser irregulares y asimétricas, que son características que les otorgan una mejor adaptación en el análisis de señales en comparación con la transformada de Fourier y con ellas se pueden conocer los valores del dominio del tiempo a partir del dominio de la frecuencia y viceversa.

La elección de una wavelet dependerá del tipo de señal que se quiera analizar, así como la información que se quiera obtener. Podemos seguir dos criterios para la selección de la wavelet. El primero consiste en buscar varias wavelets que tengan una forma parecida a nuestra señal y el segundo se basa en realizar pruebas con diferentes wavelets seleccionando aquella que obtenga los mejores resultados.

Al tipo de wavelet elegida para implementar la transformada wavelet a nuestra señal, se le asigna el nombre de wavelet madre. Se le conoce como wavelet madre ya que será esta la que sufra algunas modificaciones para realizar el análisis: se expandirá o se comprimirá, y se trasladará a lo largo de la señal. Estas modificaciones están a cargo de los parámetros de escalamiento y desplazamiento. En el escalamiento se alarga o se comprime la wavelet, lo que nos permite ver tanto los detalles como los componentes de la señal de forma global. Mientras que el desplazamiento se refiere al recorrido de la wavelet a lo largo de la señal.

![image](https://github.com/user-attachments/assets/c72a817d-7a1a-46c0-9ee0-cce9a8298f1f)


#### Usos:

La transformada wavelet ­descompone una señal mediante el uso de las versiones escaladas y desplazadas de la wavelet madre. Podemos decir que la wavelet actúa como un filtro pasa banda el cual solo permite el paso de ciertos componentes de la señal a una determinada frecuencia. También los parámetros de escalamiento y desplazamiento dan paso a la obtención de los coeficientes wavelet, los cuales nos indican cuánta relación hay entre la señal y la wavelet madre. Esta relación nos permite conocer los componentes frecuenciales de la señal.

Entre sus aplicaciones destacan el análisis de señales biomédicas, como el electrocardiograma (ECG), para detectar anomalías cardíacas; la compresión y mejora de calidad en imágenes y videos; y el diagnóstico de fallas en equipos mecánicos o eléctricos a través de análisis de vibraciones. También se emplea en el procesamiento de señales de audio para reducir ruido y en la restauración de grabaciones antiguas, en el análisis de series de tiempo financieras para identificar patrones y gestionar riesgos, y en sismología para estudiar los movimientos sísmicos y la respuesta de estructuras frente a vibraciones.

#### Tipos de wavelet utilizadas en señales biológicas:

En el análisis de señales biológicas, se utilizan distintos tipos de wavelets cada una adaptada a características específicas de la señal. Los tipos de wavelets más comunes en este campo incluyen:

**Wavelet de Haar:** Es una de las wavelets más simples y rápidas de calcular, normalmente detectar cambios abruptos y discontinuidades en señales. En señales biológicas, se utiliza principalmente para análisis preliminares o cuando se requieren cálculos rápidos, aunque su simplicidad puede limitar su uso en análisis detallados.

**Wavelet Daubechies:** Las wavelets Daubechies son ideales para señales biológicas debido a su capacidad de capturar variaciones suaves y detalles en las señales. La familia de wavelets Daubechies se pueden utilizar en la detección de eventos cardíacos como la onda R en el ECG, ya que representa bien tanto las variaciones en amplitud como los picos específicos, pero algunas son discretas y no lineales.

**Wavelet Coiflet:** Estas wavelets tienen propiedades de simetría y un momento de promedio nulo, lo que permite una mejor representación de la señal sin irse en una dirección. Las wavelets Coiflet se utilizan para análisis de señales EEG, donde la simetría es importante para capturar patrones eléctricos en el cerebro de manera precisa y sin distorsión.

**Wavelet Biorthogonal:** La familia biorthogonal es útil cuando se requiere una buena representación de la señal con mínimo error, permitiendo descomposiciones y reconstrucciones de señal casi perfectas. Es especialmente útil en procesamiento de imágenes médicas y señales ECG donde la precisión es crítica para una interpretación confiable de los datos.

**Wavelet Morlet:** La wavelet Morlet combina una función seno con una envolvente gaussiana, siendo muy útil para análisis en señales como EEG y EMG. Esta wavelet permite analizar variaciones de frecuencia en el tiempo con alta precisión y es excelente para estudios de ritmos cerebrales y análisis de señales musculares.

**Wavelet sombrero mexicano:** Conocida por su forma de sombrero mexicano, esta wavelet es buena para análisis de señales que presentan picos y transiciones rápidas. Se aplica en la detección de eventos específicos dentro de señales biológicas como potenciales evocados en EEG, debido a su capacidad de resaltar eventos aislados y detalles pequeños en una señal.

## Proceso de la señal cardiaca utilizada.

###  Diagrama de flujo.

### Adquisición de la señal.

### Wavelet utilizada.

### Señal cruda.
características, incluyendo frecuencia de muestreo, tiempo de muestreo, niveles de cuantificación, y estadísticos principales.

### Señal con la wavelet escogida.

### Filtro utilizado.

#### ¿Por qué este filtro?
#### Parámetros:


## Análisis en el dominio del tiempo.

### Picos R de la señal.
### Intervalos R-R.
### Media intervalos R-R.
### Desviación estándar.

### Análisis de los parámetros en el dominio del tiempo.

## Aplicación de transformada Wavelet.

### Espectrograma usando la transformada wavelet
### Análisis en la banda de baja frecuencia y en la banda de alta frecuencia.
describe el tipo de wavelet apropiada. Se realiza el análisis tanto en la banda de baja frecuencia como en la banda de alta frecuencia. Se describe críticamente cómo varían las frecuencias a lo largo del tiempo, detallando si hay cambios en la potencia espectral en ambos casos.

Discutir cómo los cambios en la potencia en las bandas de baja y alta frecuencia pueden estar
relacionados con la actividad simpática y parasimpática.



o
t
