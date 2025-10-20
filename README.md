🐺 Wolfbet Trading Robot APIEste repositorio contiene la documentación y ejemplos de código para interactuar con la API de configuración del Robot de Trading de Wolfbet.Esta API permite a los usuarios enviar y actualizar los parámetros de configuración de su 
robot de trading de forma remota, automatizando estrategias como la Martingala, gestión de Take Profit, Stop Loss y el uso de indicadores técnicos (RSI, MVA).

🚀 Funcionalidad Principal: ConfiguraciónLa API funciona a través de un único endpoint que recibe una solicitud POST con un cuerpo JSON para configurar todos los parámetros del robot de trading en tiempo real.Endpoint|| Método | URL | Descripción || POST | 
https://wolfbetrobot.me/REQUEST_API.php?submit=enviar | Envía la configuración completa del robot.

|AutenticaciónLa autenticación se realiza enviando la clave API (JWT) dentro del cuerpo de la solicitud JSON, utilizando el parámetro APIKEY.

Encabezado Requerido:| Nombre | Valor || Content-Type | application/json |⚙️ Parámetros de la Solicitud (JSON Payload)| Parámetro | Tipo | Descripción | Ejemplo || APIKEY | string | Requerido. Clave de autenticación JWT del usuario. | "TU_CLAVE_JWT_AQUI" || COIN | string | Moneda principal para operar. | "usdt" || COIN_COMAS | string | Lista de monedas separadas por comas (para trading múltiple). | "usdt,ada,eth" || martingala_auto | float | Porcentaje de incremento para la martingala automática. | 0.01 || volumen_entrada | float | Valor base de la apuesta inicial. | 50.0 || TAKE_PROFIT | float | Límite de ganancia objetivo para detener el bot. | 10.0 || bet_value | float | Valor de la apuesta actual/siguiente. | 49.5 || limite_ticks_perdida | integer | Número máximo de pérdidas consecutivas antes de detener el bot (Stop Loss). | 5 || entrada_porcentaje | integer | Porcentaje para la entrada de trading. | 10 || tiempo_limite | integer | Tiempo límite en segundos (e.g., para un indicador o ciclo). | 60 || apuesta_division | integer | Factor de división de la apuesta (para gestión de riesgos). | 1000 || distancia | integer | Parámetro de distancia o desviación para la estrategia. | 100 || mva200_periodos | integer | Periodos del indicador de media móvil simple (MVA). | 50 || indicador | string | Indicador técnico a utilizar (rsi, mva200, etc.). | "rsi" || accion | string | La acción a ejecutar: compra o venta. | "venta" || cerrar_manualmente | string | Envía cierre para detener el bot. | "" || reiniciar_todo | string | Envía reiniciar para borrar la sesión. | "" || submit | string | Valor de envío, debe ser "enviar". | "enviar" |🛠 Ejemplos de ImplementaciónA continuación se presentan ejemplos de cómo realizar esta solicitud en Python y JavaScript.


🐍 Python (usando requests)Este ejemplo utiliza la biblioteca requests y gestiona automáticamente la conversión del diccionario de Python a JSON y el manejo de errores.import requests
import json

def send_wolfbet_config(api_key):
    API_URL = "[https://wolfbetrobot.me/REQUEST_API.php?submit=enviar](https://wolfbetrobot.me/REQUEST_API.php?submit=enviar)"

    config_payload = {
        "APIKEY": api_key,
        "COIN": "usdt",
        "COIN_COMAS": "usdt,ada",
        # ... (otros parámetros)
        "indicador": "rsi",
        "accion": "venta"
    }

    try:
        response = requests.post(
            API_URL, 
            json=config_payload,
            headers={"Content-Type": "application/json"},
            timeout=100
        )
        response.raise_for_status() 
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

☕ JavaScript (usando fetch)Este ejemplo utiliza la API nativa fetch de JavaScript (compatible con navegadores y Node.js), ideal para aplicaciones web.async function sendWolfbetConfig(apiKey) {
    const API_URL = "[https://wolfbetrobot.me/REQUEST_API.php?submit=enviar](https://wolfbetrobot.me/REQUEST_API.php?submit=enviar)";
    
    const configPayload = {
        "APIKEY": apiKey,
        "COIN": "usdt",
        "COIN_COMAS": "usdt,ada",
        // ... (otros parámetros)
        "indicador": "rsi",
        "accion": "venta"
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify(configPayload) 
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Fallo en la solicitud:", error.message);
        return { status: "error", message: error.message };
    }
}
