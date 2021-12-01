// Arreglo con todas las preguntas
const preguntas = document.querySelectorAll('.card');
var colorResaltar;

// Función para cambiar el color
function resaltar(){
    colorResaltar = "#572B6E"
    this.style.borderColor = colorResaltar;
    this.style.margin = "10px 0px 10px 10px";
    this.style.cursor = "pointer";
}

// Función para volver al aspecto original
function original(){
    this.style.borderColor = '';
    this.style.margin = "";
}

function direccionar() {
    var url = this.id;
    window.location.href = url;
}

// Agrega un listener a cada tarjeta encontrada
for (let p of preguntas) {
    p.addEventListener('mouseover', resaltar);
    p.addEventListener('mouseleave', original);
    p.addEventListener('click', direccionar);
}
