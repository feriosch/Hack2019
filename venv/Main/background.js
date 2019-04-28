

var vered = "";
    $(document).ready(function(){
        $(document).ready(function(){
            console.log("Hola");
            var url = window.location.href;
            console.log(url);
          
            req = $.ajax({
                url: 'http://127.0.0.1:5000/validacion',
                type: 'POST',
                data: {url: url}

            });
           console.log(req);
            req.done(function(data){
               vered = data.vered;
               console.log(vered);
            });

       });
    });