const formularioPuntoE = document.getElementById('formulario-puntoE');
formularioPuntoE.addEventListener('submit', (event) => {
    event.preventDefault();
    const id_ruta = document.getElementById('id_ruta').value;
    const longitud = document.getElementById('latitud').value;
    const latitud = document.getElementById('latitud').value;
    const tipo_punto = document.getElementById('tipo_punto').value;
    alert("pasa")
    const datos = { id_ruta: id_ruta, longitud:longitud, latitud:latitud, tipo_punto: tipo_punto };
    fetch('/api_Puntos_E/savepunto', {
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
const botonNuevoComentario = document.getElementById('save-puntoE');

// Agrega un manejador de eventos para el evento "mouseover"
botonNuevoComentario.addEventListener('mouseover', () => {
  botonNuevoComentario.style.backgroundColor = '#333'; // Cambia el color de fondo al color deseado
});

// Agrega un manejador de eventos para el evento "mouseout" (cuando el mouse se aleja)
botonNuevoComentario.addEventListener('mouseout', () => {
  botonNuevoComentario.style.backgroundColor = '#62ac18c3'; // Restablece el color de fondo al original
});