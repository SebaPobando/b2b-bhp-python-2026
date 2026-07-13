let btn_sesion = document.getElementById("btn_sesion");
console.log(btn_sesion);
let btn_definicion = document.getElementById("btn_definicion");
console.log(btn_definicion);
let btn_gato = document.getElementById("btn_gato");
console.log(btn_gato);
let btn_golden = document.getElementById("btn_golden");
console.log(btn_golden);

btn_sesion.addEventListener("click", function(){
    btn_sesion.innerText = "Cerrar sesión";
})

btn_definicion.addEventListener("click", function(){
    btn_definicion.remove();
})

btn_gato.addEventListener("click", function(){
    alert("Te ha gustado el Gato Atrigrado");// mostrar alerta

    let texto_boton = btn_gato.innerText; // '22 me gusta'
    let numero_boton = parseInt(texto_boton); // 22
    console.log(numero_boton); // mostrar el 22

    numero_boton = numero_boton + 1; // 22 lo aumentamos en 1.
    console.log(numero_boton); // 23

    //reemplazar el texto actual del boton por el texto nuevo con el 
    //numero aumentado en 1.
    btn_gato.innerText = numero_boton + " me gusta"; 
})

