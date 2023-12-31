const formularioComentario = document.getElementById('formulario-comentario');
formularioComentario.addEventListener('submit', (event) => {
    
    event.preventDefault();
    alert("si")
    const titulo = document.getElementById('titulo').value;
    const id_user= document.getElementById('id_user').value;
    const fechaHoraActual = new Date().toISOString().slice(0, 19).replace('T', ' ');
    const contenido = document.getElementById('contenido').value;
    const datos = { id_user: id_user, contenido: contenido, titulo: titulo, fecha_hora: fechaHoraActual };
    fetch('/api_comments/savecomments', {
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
const botonNuevoComentario = document.querySelector('.btn.btn-primary.has-icon.btn-block');

// Agrega un manejador de eventos para el evento "mouseover"
botonNuevoComentario.addEventListener('mouseover', () => {
  botonNuevoComentario.style.backgroundColor = '#333'; // Cambia el color de fondo al color deseado
});

// Agrega un manejador de eventos para el evento "mouseout" (cuando el mouse se aleja)
botonNuevoComentario.addEventListener('mouseout', () => {
  botonNuevoComentario.style.backgroundColor = '#62ac18c3'; // Restablece el color de fondo al original
});