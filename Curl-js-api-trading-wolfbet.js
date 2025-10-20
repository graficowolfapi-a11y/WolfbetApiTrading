/**
 * Envía la configuración del Robot de Trading Wolfbet utilizando la API fetch.
 *
 * El método fetch es el estándar en JavaScript para realizar solicitudes de red,
 * y reemplaza la funcionalidad que cURL proporciona en PHP.
 * Se utiliza async/await para manejar la promesa de la solicitud de forma limpia.
 */
async function sendWolfbetConfig() {
    // 1. URL del Endpoint (la misma que en el script PHP)
    const API_URL = "https://wolfbetrobot.me/REQUEST_API.php?submit=enviar";

    // 2. Clave de Autenticación (¡REEMPLAZAR con tu clave JWT real!)
    const API_KEY = "TU_CLAVE_JWT_AQUI"; 

    // 3. Cuerpo de la Solicitud (Payload JSON)
    // Se define como un objeto JavaScript, que luego se convertirá a JSON.
    const configPayload = {
        "APIKEY": API_KEY,
        "COIN": "usdt",
        "COIN_COMAS": "usdt,ada",
        "martingala_auto": 0.01,
        "volumen_entrada": 50,
        "TAKE_PROFIT": 10.0,
        "bet_value": 49.5,
        "limite_ticks_perdida": 5,
        "entrada_porcentaje": 10,
        "tiempo_limite": 60,
        "apuesta_division": 1000,
        "distancia": 100,
        "mva200_periodos": 50,
        "cerrar_manualmente": "", 
        "reiniciar_todo": "",
        "submit": "enviar",
        "indicador": "rsi",
        "accion": "venta"
    };

    console.log("--- Iniciando Solicitud POST a Wolfbet API ---");
    console.log("JSON a enviar:", configPayload);

    try {
        const response = await fetch(API_URL, {
            method: 'POST', // Método de solicitud
            headers: {
                // Cabecera obligatoria para indicar que el cuerpo es JSON
                'Content-Type': 'application/json' 
            },
            // Convertir el objeto JavaScript a una cadena JSON para el cuerpo
            body: JSON.stringify(configPayload) 
        });

        // 4. Manejo de la Respuesta
        
        // Verifica si la respuesta HTTP es exitosa (código 200-299)
        if (!response.ok) {
            // Lanza un error si el estado HTTP indica un problema (ej. 404, 500)
            throw new Error(`Error de red o HTTP: ${response.status} ${response.statusText}`);
        }

        // Intenta obtener el cuerpo de la respuesta como JSON
        const data = await response.json();
        
        console.log("\n--- Respuesta Exitosa del Servidor (JSON) ---");
        console.log(JSON.stringify(data, null, 2)); // Muestra el JSON formateado
        console.log("----------------------------------------------");

        return data;

    } catch (error) {
        // Captura errores de red (ej. URL incorrecta, no hay conexión) o los errores lanzados arriba
        console.error("\n--- Error cURL/Fetch ---");
        console.error("Mensaje de Error:", error.message);
        console.error("------------------------");
        return { status: "error", message: error.message };
    }
}

// Ejecuta la función principal
sendWolfbetConfig();
