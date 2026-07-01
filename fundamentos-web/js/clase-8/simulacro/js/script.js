const btn_pregunta = document.getElementById("pregunta");
console.log(btn_pregunta);

btn_pregunta.addEventListener("click", function(){
    alert("Mundo Muñecas, encuentra muñecas internacionales");
});

const lista_botones = document.querySelectorAll(".btn-agregar");
console.log(lista_botones);


lista_botones.forEach(function(boton){
    boton.addEventListener("click",function(){
        const valor_carrito = document.getElementById("cantidad");

        let valor_actual = valor_carrito.innerText;

        let nuevo_valor = parseInt(valor_actual) + 1;

        valor_carrito.innerText = nuevo_valor;
    })
})


const lista_opciones = document.querySelectorAll("option");
console.log(lista_opciones);


lista_opciones.forEach(function(op){
    this.addEventListener("click", function(){
        const valor_orden = document.getElementById("orden");
        console.log(valor_orden);
        let opcion_seleccionada = op.innerText;
        valor_orden.innerText = opcion_seleccionada;
    })
})