window.addEventListener('load', obtenerDatos);

function obtenerDatos() {
    const Nasa_key = '6MXjexvW8M7KAzfDSb7iHttFkmBo35lBCjJv1Aou';
    const ruta = `https://api.nasa.gov/planetary/apod?api_key=${Nasa_key}`;

    fetch(ruta)
        .then(respuesta => respuesta.json())
        .then(resultado => mostrarDatos(resultado))
        .catch(error => console.log('Error al obtener datos:', error));
}

function mostrarDatos({ date, explanation, media_type, title, url }) {
    document.querySelector('#titulo').innerHTML = title;
    document.querySelector('#fecha').innerHTML = date;
    document.querySelector('#descripcion').innerHTML = explanation;
    const multimedia = document.querySelector('#c_multimedia');

    if (media_type === 'video') {
        multimedia.innerHTML = `<iframe class="embed-responsive-item" src="${url}" frameborder="0" allowfullscreen></iframe>`;
    } else {
        multimedia.innerHTML = `<img src="${url}" class="img-fluid" alt="${title}">`;
    }
}
