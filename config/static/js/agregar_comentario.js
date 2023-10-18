const formularioComentario = document.getElementById('formulario-comentario');
formularioComentario.addEventListener('submit', (event) => {
    event.preventDefault();
    const titulo = document.getElementById('titulo').value;
    const fechaHoraActual = new Date().toISOString().slice(0, 19).replace('T', ' ');
    const contenido = document.getElementById('contenido').value;
    const datos = { id_user: 12, contenido: contenido, titulo: titulo, fecha_hora: fechaHoraActual };
    fetch('/api_comments/savecomments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
});