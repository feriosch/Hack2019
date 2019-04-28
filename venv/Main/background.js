console.log("Hola");
var pathname = window.location.href;
console.log(pathname);

 req = $.ajax({
          url: '/validacion',
          type: 'POST',
          data: {url: pathname}
 });
console.log(req);
            req.done(function(data){
               vered = data.vered;
               alert(vered);
            });

