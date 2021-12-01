// Se indica que la función cargará después de que el DOM este listo
$(document).ready(function () {
    // Se atrapa el envío del formulario
    $('#preguntaForm').submit(function (e) {
        // Se evita que el formulario se envie
        e.preventDefault();
        // Se crea llamada a AJAX
        $.ajax({
            // Obtiene datos del formulario y los vuelve JSON
            data: $(this).serialize(),
            // Obtiene el método usado en el formulario
            type: $(this).attr('method'),
            // Usa la URL indicada en el formulario
            url:  $(this).attr('action'),
            // Acción en caso de respuesta exitosa
            success: function (response) {
                // Crea un mensaje emergente
                alert("Se registró correctamente la pregunta " + response.titulo);
                // Limpia el formulario
                document.getElementById("preguntaForm").reset();
            },
            // Acción para respuesta con error
            error: function (response) {
                // Imprime error en mensaje emergente y consola
                alert(response.responseJSON.errors);
                console.log(response);
            }
        });
        return false;
    });
})
