document.querySelector('form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const client = document.querySelector('#client').value;
  const mail = document.querySelector('#mail').value;
  const description = document.querySelector('#description').value;
  const service = document.querySelector('#service').value;

  if(!client || !mail || !description || !service) {
    alert('Por favor, rellene todos los campos');
    return;
  }

  const response = await fetch('/api/cotization', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      client,
      mail,
      description,
      service,
    }),
  });

  if (response.ok) {
    alert('Cotización enviada con éxito');
  } else {
    alert('Ha ocurrido un error al enviar la cotización');
  }

  load_cotization(await response.json());
});

function load_cotization(cotization) {
  document.querySelector('#cotization').style.display = 'block';
  document.querySelector('form').style.display = 'none';
  document.querySelector('#cotization-number').innerText = cotization.cotizationNumber;
  document.querySelector('#client-cotization').innerText = cotization.client;
  document.querySelector('#mail-cotization').innerText = cotization.mail;
  document.querySelector('#description-cotization').innerText = cotization.description;
  document.querySelector('#service-cotization').innerText = cotization.service;
  document.querySelector('#price-cotization').innerText = cotization.price;
  document.querySelector('#date-cotization').innerText = cotization.date;
}

document.querySelector('#back-button').addEventListener('click', () => {
  document.querySelector('#cotization').style.display = 'none';
  document.querySelector('form').style.display = 'flex';
  document.querySelector('form').reset();
});