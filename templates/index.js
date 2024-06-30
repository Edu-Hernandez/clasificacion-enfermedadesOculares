
const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastTrigger.addEventListener('click', () => {
        toastBootstrap.show()
    })
}

function limpiarDatos() {
    // Limpia la imagen mostrada y el campo de clasificación
    document.getElementById("imgPreview").src = "./thumbnail.svg"; // Cambia a tu imagen placeholder
    document.getElementById("classification").value = ""; // Limpia el campo de clasificación
    document.getElementById("btnLimpiar").style.display = "none"; // Oculta el botón de limpiar
}