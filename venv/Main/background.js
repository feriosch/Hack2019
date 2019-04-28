console.log("Hola");
var pathname = window.location.href;
console.log(pathname);

 req = $.ajax({
     url: '/validar',
     type: 'POST',
     data: {url: pathname}
     
 });
console.log(req);
 req.done(function(data){
    console.log(data.phish); 
 });