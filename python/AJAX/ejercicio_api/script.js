let boton = document.getElementById('btnInfo');

async function obtenerUsuarioGithub() {
    let usuario = document.getElementById('username').value;
    let respuesta = await fetch(`https://api.github.com/users/${usuario}`);
    let datos = await respuesta.json();

    console.log(datos);


}

boton.addEventListener('click', obtenerUsuarioGithub);