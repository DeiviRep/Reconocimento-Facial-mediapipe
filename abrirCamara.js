function getCameraStream() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            // Establecer el flujo de la cámara como fuente de video
            const videoElement = document.getElementById('videoElement');
            videoElement.srcObject = stream;

            // Inicializar el elemento canvas
            const canvasOutput = document.getElementById('canvasOutput');
            const context = canvasOutput.getContext('2d');

            // Establecer la frecuencia de fotogramas para capturar y procesar imágenes
            const FPS = 30;

            // Función para capturar y procesar imágenes de la cámara
            function processCameraFrame() {
                // Capturar una imagen del elemento de video y dibujarla en el canvas
                context.drawImage(videoElement, 0, 0, canvasOutput.width, canvasOutput.height);

                // Convertir la imagen del canvas a un objeto Mat de OpenCV
                const imageData = context.getImageData(0, 0, canvasOutput.width, canvasOutput.height);
                const src = cv.matFromImageData(imageData);

                // Aplicar operaciones de procesamiento de imágenes aquí
                // Por ejemplo, convertir la imagen a escala de grises
                cv.cvtColor(src, src, cv.COLOR_RGBA2GRAY);

                // Mostrar la imagen procesada en el canvas
                cv.imshow('canvasOutput', src);

                // Liberar memoria
                src.delete();

                // Solicitar la próxima actualización de fotograma
                requestAnimationFrame(processCameraFrame);
            }

            // Iniciar el procesamiento de imágenes de la cámara
            processCameraFrame();
        })
        .catch(function(error) {
            console.error('Error al acceder a la cámara:', error);
        });
}

getCameraStream()