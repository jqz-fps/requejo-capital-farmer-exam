# Sistema de Cotizaciones - Capital & Farmer

## Instalación
1. Clone el repositorio
2. pip install -r requirements.txt
3. python app.py
> [!IMPORTANT]
> Este proyecto utiliza la API de Gemini para realizar el analisis de la descripción de la cotización. Para poder utilizar esta funcionalidad, es necesario tener una cuenta de Google Cloud Platform y crear una API Key de la plataforma.

## Uso
- Acceder a http://localhost:5000
- Completar formulario de cotización
- Se mostrará la información enviada y la cotización recibida, además de un analisis realizado por Inteligencia Artificial.
- En el caso de que se desee volver a enviar una cotización, podrá volver a hacerlo mediante el botón "Volver" o recargando la página.

## APIs utilizadas
Se usó la API de Gemini para realizar el analisis de la descripción de la cotización.

## Funcionalidades bonus
- Se agregó una simple validación de datos para evitar errores en la entrada de datos.
