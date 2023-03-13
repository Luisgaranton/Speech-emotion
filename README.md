Este código comienza importando las bibliotecas necesarias, incluyendo Pandas y NumPy para el procesamiento de datos, os y sys para manejar el sistema operativo y la salida del programa, y warnings para filtrar advertencias innecesarias.

El código luego define una variable speech_audio que contiene la ruta de una carpeta que contiene archivos de audio asociados con diferentes emociones.

speech_audio_directory_list es una lista de los archivos en speech_audio. Luego, el código crea tres listas vacías file_emotion, file_statement, y file_path para almacenar la emoción, la declaración y la ruta del archivo de audio.

El código luego recorre cada archivo en cada directorio de la carpeta speech_audio. Extrae información de cada archivo, incluyendo la emoción asociada con el archivo, la declaración y la ruta del archivo. Luego, crea un DataFrame de Pandas llamado speech_audio_df con la información extraída.

A continuación, se reemplazan los números que representan diferentes emociones con sus etiquetas correspondientes para hacer que los datos sean más legibles.

Finalmente, el código muestra las primeras filas del DataFrame y lo guarda en un archivo CSV llamado "speech-audio.csv".




