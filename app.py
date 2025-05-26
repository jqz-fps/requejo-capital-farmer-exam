import os, json
from flask import Flask, request, jsonify, render_template
from datetime import datetime
from google import genai
from dotenv import load_dotenv

app = Flask(__name__)

# Aqui cargamos las variables de entorno
load_dotenv()
# Y creamos el cliente de gemini (AI de Google)
gemini_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

cotizations = []
services = [
  {"name": "constitución de empresa", "price": 1500}, 
  {"name": "defensa laboral", "price": 2000},
  {"name": "consultoría tributaria", "price": 800},
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/cotization', methods=['POST'])
def new_cotization():
  cotization_data = request.get_json()
  try:
    # Aquí se validan los datos de entrada
    client = cotization_data['client']
    mail = cotization_data['mail']
    description = cotization_data['description']
    service = cotization_data['service']

    # Este objeto se utiliza para buscar el servicio
    service_obj = next(
      (s for s in services if s["name"].lower() == service.lower()),
      None
    )
    # En el caso de que no se encuentre el servicio, se lanza una excepción
    if service_obj is None:
      raise KeyError("Servicio no encontrado")
    # Se obtiene el precio del servicio
    price = service_obj['price']
  except KeyError:
    return jsonify({'error': 'Missing data'}), 400
  
  cotizationNumber = "COT-2025-" + f"{len(cotizations) + 1:04}"
  date = datetime.now().strftime("%d/%m/%Y")

  ai_response = analyze_description(description, service)

  final_cotization = {
    'cotizationNumber': cotizationNumber,
    'price': price,
    'date': date,
    'client': client,
    'mail': mail,
    'service': service.capitalize(),
    'description': description,
    "ai_response": ai_response
  }

  cotizations.append(final_cotization)
  return jsonify(final_cotization), 201

def analyze_description(description, service):
  prompt = f"""
    Eres de una empresa de abogados y estás haciendo cotizaciones legales.
    Analiza este caso legal: {description}
    Tipo de servicio: {service}
    
    Evalúa:
    1. Complejidad (Baja/Media/Alta)
    2. Ajuste de precio recomendado (0%, 25%, 50%)
    3. Servicios adicionales necesarios
    4. Genera propuesta profesional para cliente

    No me respondas como si fuera a mí, responde como si fuese al cliente que te está solicitando esta información. Response de 2 a 3 parrafos profesionales y que no pasen de las 400 palabras cada una, pero teniendo en cuenta lo que se evalúa (que se solicita anteriormente).
  """

  response = gemini_client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
  )

  return response.text

if __name__ == '__main__':
  app.run(debug=True)