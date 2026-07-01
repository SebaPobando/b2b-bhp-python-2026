document.getElementById('pregunta').addEventListener("click",function(){
    alert("MundoMuñecas, las mejores muñecas internacionales.");
})

var botones_agregar = document.querySelectorAll(".btn-agregar");

//boton1
//boton2
//boton3
//boton4

botones_agregar.forEach(function(boton){
    boton.addEventListener("click",function(){
        let cantidad = document.querySelector("#cantidad");
        cantidad.textContent = parseInt(cantidad.textContent) + 1;
    })
})