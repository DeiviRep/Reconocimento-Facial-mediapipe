// Crear un elemento de script
const script = document.createElement('script');

// Establecer el atributo src con la URL de OpenCV.js
script.src = 'https://docs.opencv.org/4.5.4/opencv.js';

// Asignar una función de devolución de llamada para cuando el script se haya cargado
script.onload = function() {
    // OpenCV.js está cargado y listo para usar
    console.log('OpenCV.js cargado correctamente');
    
    // Aquí puedes comenzar a utilizar OpenCV.js
    // Por ejemplo:
    // cv.imread('imagen.jpg');
};

// Agregar el elemento de script al final del cuerpo del documento HTML
document.body.appendChild(script);
