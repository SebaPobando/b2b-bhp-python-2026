let likes1 = 0;
let likes2 = 0;
let likes3 = 0;

function darLike1() {
    likes1++;
    document.getElementById("span1").innerText = likes1;
}

function darLike2() {
    likes2++;
    document.getElementById("span2").innerText = likes2;
}

function darLike3() {
    likes3++;
    document.getElementById("span3").innerText = likes3;
}


// let buttons = document.querySelectorAll("button");
// // Para cada botón un listener y aumentar la cantidad de likes:
// buttons.forEach(function (btn) {
//     btn.addEventListener("click", function () {
//         //aumentamos el contador:
//         this.parentElement.querySelector('span').innerText++;
//     });
// });

