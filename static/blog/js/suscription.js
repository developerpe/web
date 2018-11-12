'use strict';
$(document).ready(function(){
  $('#Suscripcion').addClass("is-active");
});
$(".delete").click(function() {
   $("#Suscripcion").removeClass("is-active");
});
$("#cerrar").click(function() {
   $("#Suscripcion").removeClass("is-active");
});
$('#subscribe').click(function(){
    $('#message').fadeIn(5000,function(){
        document.getElementById('message').innerHTML = 'Enviando...';
    });
});
$('#mc-form').submit(function(event){
    event.preventDefault();
    $.ajax({
        url: '/',
        type: 'POST',
        data: $('#mc-form').serialize(),
        success: function(response){
          console.log(response);
            $('#message').fadeIn(5000,function(){
                document.getElementById('message').innerHTML = 'Su registro fué completado correctamente!\nRecuerda revisar en tu bandeja de No deseados! :D';
                document.getElementById('mc-email').value = '';
            });
            setTimeout(function(){
              $("#Suscripcion").removeClass("is-active");
            },1000);
          }
    });
});
