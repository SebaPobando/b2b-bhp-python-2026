let boton = document.getElementById('btnInfo');

async function obtenerUsuarioGithub() {
    let usuario = document.getElementById('username').value;

    let respuesta = await fetch(`https://api.github.com/users/${usuario}`);
    let datos = await respuesta.json();

    console.log(datos);

    document.getElementById('perfil').innerHTML = `
        <img src="${datos.avatar_url}" width="150">
        <h2>${datos.name} tiene ${datos.followers} seguidores</h2>`;

}

boton.addEventListener('click', obtenerUsuarioGithub);