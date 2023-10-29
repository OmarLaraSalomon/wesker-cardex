/*   @ Barras de progreso HTML5 animadas con Javascript
     @ author Alejandro Campero */

     function animateprogress (id, val){		


        var getRequestAnimationFrame = function () {  /* <------- Declaro getRequestAnimationFrame intentando obtener la maxima compatibilidad con todos los navegadores */
            return window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||   
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            function ( callback ){
                window.setTimeout(enroute, 1 / 60 * 1000);
            };
            
        };
        
        var fpAnimationFrame = getRequestAnimationFrame();   
        var i = 0;
        var animacion = function () {
                
        if (i<=val) 
            {
                document.querySelector(id).setAttribute("value",i);      /* <----  Incremento el valor de la barra de progreso */
                document.querySelector(id+"+ span").innerHTML = i+"%";     /* <---- Incremento el porcentaje y lo muestro en la etiqueta span */
                i++;
                fpAnimationFrame(animacion);          /* <------------------ Mientras que el contador no llega al porcentaje fijado la funcion vuelve a llamarse con fpAnimationFrame     */
            }
                                            
        }
    
            fpAnimationFrame(animacion);   /*  <---- Llamo la funcion animacion por primera vez usando fpAnimationFrame para que se ejecute a 60fps  */
                    
    }