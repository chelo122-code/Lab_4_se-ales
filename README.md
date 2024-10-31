# Laboratorio 4 de señales - Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet

## Introducción.

En el presente laboratorio, se aborda la variabilidad de la frecuencia cardíaca (HRV) como un indicador crucial de la salud cardiovascular y la respuesta del sistema nervioso autónomo ante diferentes estímulos, como el ejercicio y el reposo. A través de un análisis estadístico detallado de los datos obtenidos durante un periodo de actividad física moderada, se explora cómo la actividad simpática y parasimpática del organismo influye en la frecuencia y fuerza de los latidos cardíacos. Este estudio no solo proporciona una comprensión de la dinámica del ritmo cardíaco, sino que también pone de manifiesto la importancia de la HRV como herramienta diagnóstica en contextos clínicos.

Además, se emplea la transformada wavelet, una técnica avanzada de análisis de señales, para descomponer la señal electrocardiográfica en sus componentes de frecuencia y tiempo. A través de este enfoque, se identifican patrones en la variabilidad de la frecuencia cardíaca que reflejan las fluctuaciones inherentes al funcionamiento del sistema nervioso autónomo. La elección de la wavelet madre, específicamente la wavelet Morlet, permite un análisis preciso de las bandas de baja y alta frecuencia, proporcionando información valiosa sobre el estado fisiológico del individuo durante la adquisición de la señal. Este enfoque integral combina conceptos teóricos y prácticos para entender mejor la relación entre el ejercicio y la respuesta cardiovascular.

## Conceptos principales para tener en cuenta.

### Actividad simpática y parasimpática del sistema nervioso autónomo (SNA).

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

![image](https://github.com/user-attachments/assets/8b83bbfd-c55d-40ce-98a4-5641ab76f710)


### Adquisición de la señal.

Para la adquisición de la señal, se utilizó una placa STM32 conectada a un módulo AD8232, junto con tres electrodos ubicados estratégicamente para registrar el electrocardiograma (ECG).

![image](https://github.com/user-attachments/assets/20eb4eaf-da66-40b0-93eb-27f8ff25bdc3)

La señal se registró mientras el individuo permanecía sentado en una silla, con la espalda recta y en una posición relajada. Durante los 5 minutos de adquisición de datos, se sostuvo una conversación casual para ayudar a mantener un ambiente relajado, sin llegar a alterar el ritmo cardíaco y asegurando así una captura representativa del ECG en reposo.

Una vez completada la adquisición, los datos se guardaron en un archivo de texto (.txt) para su posterior procesamiento. Los análisis estadísticos y espectrales se realizaron utilizando la transformada wavelet en Python, lo que permitió obtener una visión detallada de las variaciones de la señal en diferentes escalas de tiempo y frecuencia.

### Wavelet utilizada.

El tipo de wavelet madre utilizada para nuestra señal ECG fue **morlet**.

![image](https://github.com/user-attachments/assets/6ef9120b-f2cc-4fc8-8e27-1318e5b6a2a5)

Es una buena opción para analizar señales electrocardiográficas debido a su capacidad de descomponer una señal en distintas frecuencias de forma precisa y de adaptarse bien a la estructura de las señales biológicas. Esta wavelet combina una onda sinusoidal modulada por una envolvente gaussiana, lo cual permite analizar tanto la variabilidad temporal como frecuencial de la señal. Esta nos va a servir especialmente para estudiar componentes específicos como las bandas de baja frecuencia (LF) y alta frecuencia (HF), las cuales están asociadas con la actividad del sistema nervioso autónomo.

Por lo tanto,  puede detectar cambios en la frecuencia de la señal con suficiente precisión y localizar eventos transitorios en el tiempo, donde se presentan complejos QRS y variaciones de la frecuencia cardíaca. Además, como puede ser una señal multiescala esta puede adaptarse para analizar detalles finos o características más globales de la señal, también permite aislar y examinar las variaciones en la frecuencia cardíaca que ocurren a distintos niveles de la señal.

### Señal original.

![image](https://github.com/user-attachments/assets/480ff758-4138-47a4-8be3-bd2e475748dc)

El tiempo de muestreo utilizado fue de 5 minutos, lo que permitió obtener un intervalo extenso de la señal ECG. Como resultado, los latidos aparecieron muy juntos, formando una señal continua con poco espacio entre ellos. Aunque se logró identificar adecuadamente los picos R, no se observaron con claridad los demás complejos y segmentos que conforman la señal.

Durante el análisis, se notó que la magnitud de la señal varió en función de la actividad del corazón. Esta variabilidad podría atribuirse a la ligera agitación que experimentó el individuo durante la charla, lo que impactó el comportamiento de los latidos.

La frecuencia de muestreo utilizada fue de 165 Hz. De acuerdo con el teorema de Nyquist, para reconstruir la señal original sin pérdida de información, la frecuencia de muestreo debe ser al menos el doble de la frecuencia máxima presente en la señal. Al dividir los 99 latidos por minuto (lpm) entre 60 segundos, obtenemos una frecuencia de 1.65 Hz para la señal. Por lo tanto, se decidió multiplicar esta frecuencia por 100, resultando en una frecuencia de muestreo de 165 Hz.

### Filtro utilizado.

Se utilizo un filtro pasabanda Butterworth es un tipo de filtro diseñado para permitir el paso de señales dentro de un rango de frecuencias específicas, mientras atenúa las señales fuera de ese rango.

#### ¿Por qué este filtro?

En el caso de las señales ECG, este filtro que opera entre 20 Hz y 450 Hz es útil debido a que las componentes de la señal ECG que son relevantes para el análisis clínico se encuentran dentro de este rango. Con la frecuencia mínima (20 Hz) se elimina el ruido de baja frecuencia que puede ser causado por movimientos corporales, interferencias electromagnéticas o la actividad muscular. Mientras que con la frecuencia máxima (450 Hz) se establece para descartar las frecuencias más altas que pueden introducir ruido y no están relacionadas con la actividad cardíaca, como las interferencias producidas por fuentes eléctricas o artefactos.

#### Parámetros:

**Orden del Filtro (4):** Un filtro de cuarto orden implica que la pendiente de atenuación es más pronunciada en comparación con filtros de menor orden. Esto significa que el filtro puede proporcionar una mejor atenuación fuera de la banda de paso, lo que es esencial para minimizar el ruido y mejorar la calidad de la señal filtrada, a medida que aumenta el orden del filtro la transición entre la banda pasante y la banda de atenuación se vuelve más abrupta, lo que ayuda a preservar las características importantes de la señal ECG.

**Respuesta en Frecuencia:** Los filtros Butterworth son conocidos por su respuesta plana en la banda de paso, lo que significa que en lo posible no introducen distorsiones en las frecuencias permitidas.

## Análisis en el dominio del tiempo y aplicación de transformada Wavelet.

### Estadísticos principales.

#### Picos R e intervalos, media y desviación estándar de la señal.

![image](https://github.com/user-attachments/assets/1a4f68e1-9ff5-431f-bd2a-801491117251)

### Señal con la wavelet escogida.

#### Frecuencias bajas.

![image](https://github.com/user-attachments/assets/fa64bfb3-3fd2-424a-b219-0ab4764f7b2a)

#### Frecuencias altas.

![image](https://github.com/user-attachments/assets/86e1ce6c-56a1-42af-8807-5d3f99db4e22)


### Análisis en la banda de baja frecuencia y en la banda de alta frecuencia.

#### Frecuencias bajas.

En la banda de frecuencias bajas se observa una mayor magnitud en los latidos, ya que en este rango de frecuencias denominado bajo y medio, se presentan las mayoeres caracteristicas del ECG como el complejo QRS, onda P y T, y al no tener cambios bruscos en las magnitudes sugiere estabilidad en la respuesta simpática del individuo. Las frecuencias bajas están asociadas con la actividad del sistema nervioso simpático, lo cual podría indicar que el individuo estaba en un estado de alerta o actividad moderada. Este tipo de actividad puede estar relacionado con acciones como hablar de forma animada, reír o responder con cierta rapidez, reflejando una ligera respuesta simpática.

#### frecuencias altas.

En la banda de frecuencias altas la magnitud de la señal es baja en la mayoría de las escalas (50 a 200)  con valores de magnitud baja, ya que en este rango de frecuencia, los datos abstraibles seran principalmente del ruido y/o organos del cuerpo, mostrando leves precencias de de  manchas claras, dadas posiblemente por procesos digestivos y respiratorios, aunque cuenta con una interferencia que se registra con gran magnitud en la mayor escala, que deducimos que es por saturacion de frecuencias fantasmas o por pequeñas fracciones de la señal que se toma como no continuidad de la suavidad de la funcion.
Las frecuencias altas están relacionadas con la actividad del sistema nervioso parasimpático, que regula la respuesta de "descanso y digestión". Dado que la magnitud en estas frecuencias, son bajas y los cambios en la potencia son mínimos, es probable que el sistema parasimpático no haya tenido una intervención significativa en este período de análisis.

#### Conclusión general.

- La estabilidad de la potencia en las frecuencias bajas sugiere una actividad simpática moderada y constante, posiblemente debido a la interacción social o la actividad física ligera.
- La baja magnitud y la mínima variabilidad en las frecuencias altas sugieren una limitada activación del sistema parasimpático, lo que indica que el individuo no se encontraba en un estado de relajación profunda.

