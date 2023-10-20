const formularioRuta = document.getElementById('formulario-Ruta');
formularioRuta.addEventListener('submit', (event) => {
    event.preventDefault();
    const id_u = document.getElementById('id_u').value;
    const longitud1 = document.getElementById('longitud1').value;
    const latitud1 = document.getElementById('latitud1').value;
    const longitud2 = document.getElementById('longitud2').value;
    const latitud2 = document.getElementById('latitud2').value;
    alert("pasa")
    const datos = { id_u: id_u, longitud1: longitud1, latitud1: latitud1, longitud2: longitud2, latitud2: latitud2 };
    fetch('/api_Rutas/saveruta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
        window.onload()
});

// Selecciona el botón por su ID
const botonNuevoComentario = document.getElementById('save-route');

// Agrega un manejador de eventos para el evento "mouseover"
botonNuevoComentario.addEventListener('mouseover', () => {
  botonNuevoComentario.style.backgroundColor = '#333'; // Cambia el color de fondo al color deseado
});

// Agrega un manejador de eventos para el evento "mouseout" (cuando el mouse se aleja)
botonNuevoComentario.addEventListener('mouseout', () => {
  botonNuevoComentario.style.backgroundColor = '#62ac18c3'; // Restablece el color de fondo al original
});





