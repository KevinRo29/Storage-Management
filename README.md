# Aplicación Python con Firebase

Esta aplicación Python utiliza Firebase para almacenamiento de datos en la nube. Sigue los pasos a continuación para instalar y utilizar la aplicación.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Navega al directorio del repositorio:

    ```bash
    cd tu-repositorio
    ```

3. Instala las dependencias necesarias utilizando pip:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Obtén el archivo `firebase.json` desde la consola de Firebase y colócalo en el directorio raíz de la aplicación.

2. Crea un archivo `.env` en el directorio raíz de la aplicación y define la variable `STORAGEBUCKET` con la URL de tu almacenamiento en Firebase:

    ```plaintext
    STORAGEBUCKET=tu-url-de-storage-en-firebase
    ```

## Uso

1. Ejecuta la aplicación Python:

    ```bash
    python main.py
    ```
