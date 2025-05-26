from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

cotizations = []
services = [
  {"name": "constitución de empresa", "price": 1500}, 
  {"name": "defensa laboral", "price": 2000},
  {"name": "consultoría tributaria", "price": 800},
]

@app.route('/')
def index():
  return jsonify(cotizations)

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

  final_cotization = {
    'cotizationNumber': cotizationNumber,
    'price': price,
    'date': date,
    'client': client,
    'mail': mail,
    'service': service,
    'description': description
  }

  cotizations.append(final_cotization)
  return jsonify(final_cotization)

if __name__ == '__main__':
  app.run(debug=True)
