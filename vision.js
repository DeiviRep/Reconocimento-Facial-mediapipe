// Importar MediaPipe
import vision from "@mediapipe/tasks-vision";

// Una vez que OpenCV.js se haya cargado completamente
cv.onRuntimeInitialized = function() {
    // Crear una instancia de FaceMesh
    const faceMesh = new vision.FaceMesh({
        staticImageMode: true,
        maxNumFaces: 1,
        minDetectionConfidence: 0.5,
    });

    // Continuar con el resto del código aquí...
}
