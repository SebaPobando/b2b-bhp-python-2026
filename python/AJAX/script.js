const boton = document.getElementById('btnConsultar');

async function obtenerUsuarioGitHub() {
  const usuario = document.getElementById('usuarioInput').value;
  const respuesta = await fetch(`https://api.github.com/users/${usuario}`);
  const datos = await respuesta.json();

  console.log(datos);

  document.getElementById('perfil').innerHTML = `
    <img src="${datos.avatar_url}" width="150">
    <h2>${datos.name} tiene ${datos.followers} seguidores</h2>`;
}

boton.addEventListener('click', obtenerUsuarioGitHub);