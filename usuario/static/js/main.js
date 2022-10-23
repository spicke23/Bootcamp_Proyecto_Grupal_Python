
var fechaLarga = new Date();

let dia = fechaLarga.getDate()
let mes = fechaLarga.getMonth()+1
let ano = fechaLarga.getFullYear()

let hora = fechaLarga.getHours()
let minutos = fechaLarga.getMinutes()

var fechaCorta = "Fecha actual: " + dia + "/"+ mes +"/" + ano + "- Hora actual: " + hora+":"+minutos


var contenedor = document.getElementById("contenedor").innerHTML;
contenedor ="<p>"+  contenedor + fechaCorta +"</p>";
document.getElementById("contenedor").innerHTML = contenedor;
 
console.log(fechaCorta)


let btnEnviar= document.getElementById('btnEnviar')

if (btnEnviar){
    btnEnviar.addEventListener('click', validar)
}

function validar(e){
    e.preventDefault()
    let nombre=document.getElementById('nombre').value
    let correo=document.getElementById('correo').value
    let mensaje=document.getElementById('mensaje').value
    let mensajeError = document.getElementById("mensajeError")

    if ((nombre=='' || nombre==' ') || (correo=='' || correo==' ') || (mensaje=='' || mensaje==' ')    ) {
        console.log("Faltan campos por completar")
        mensajeError.textContent="Faltan campos por completar"
        mensajeError.className+='text-center alert alert-danger'
    }
    else{
        console.log("Mensaje enviado correctamente")
        mensajeError.className+='text-center alert alert-success'
        mensajeError.textContent="Mensaje enviado correctamente"
    }

  

}