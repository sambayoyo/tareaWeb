const formularioAlarma = document.getElementById('formulario-alarma');
formularioAlarma.addEventListener('submit', (event) => {
    event.preventDefault();
    const id_r = document.getElementById('id_r').value;
    const tipo = document.getElementById('tipo').value;
    alert("pasa")
    const datos = { id_r: id_r, tipo: tipo };
    fetch('/api_Alarmas/savealarma', {
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
const botonNuevoComentario = document.getElementById('save-alarm');

// Agrega un manejador de eventos para el evento "mouseover"
botonNuevoComentario.addEventListener('mouseover', () => {
  botonNuevoComentario.style.backgroundColor = '#333'; // Cambia el color de fondo al color deseado
});

// Agrega un manejador de eventos para el evento "mouseout" (cuando el mouse se aleja)
botonNuevoComentario.addEventListener('mouseout', () => {
  botonNuevoComentario.style.backgroundColor = '#62ac18c3'; // Restablece el color de fondo al original
});