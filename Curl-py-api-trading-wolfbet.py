import requests
import json
import logging

# Configuración de logging para ver información de la solicitud (opcional)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def send_wolfbet_config():
    """
    Envía la configuración del Robot de Trading Wolfbet mediante una solicitud HTTP POST.
    
    Utiliza la biblioteca 'requests' de Python para replicar la funcionalidad cURL.
    """
    # 1. URL del Endpoint
    API_URL = "https://wolfbetrobot.me/REQUEST_API.php?submit=enviar"

    # 2. Clave de Autenticación (¡REEMPLAZAR con tu clave JWT real!)
    API_KEY = "TU_CLAVE_JWT_AQUI" 

    # 3. Cuerpo de la Solicitud (Payload)
    # Se define como un diccionario de Python. 'requests' lo convertirá a JSON automáticamente.
    config_payload = {
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
    }

    # 4. Cabeceras
    # Es crucial especificar Content-Type: application/json
    headers = {
        "Content-Type": "application/json"
    }

    print("--- Iniciando Solicitud POST a Wolfbet API ---")
    print("JSON a enviar (Dict):", config_payload)

    try:
        # La función requests.post gestiona la serialización del diccionario a JSON 
        # y aplica las cabeceras.
        response = requests.post(
            API_URL, 
            json=config_payload, # Usamos el parámetro 'json' en lugar de 'data'
            headers=headers,
            timeout=100 # Tiempo límite en segundos, similar a CURLOPT_TIMEOUT
        )
        
        # 5. Manejo de la Respuesta
        
        # Lanza una excepción si el estado HTTP es un error (4xx o 5xx)
        response.raise_for_status() 

        # Intenta obtener el cuerpo de la respuesta como JSON
        # La respuesta es un diccionario de Python
        data = response.json()
        
        print("\n--- Respuesta Exitosa del Servidor (JSON) ---")
        # Imprime el diccionario de Python en formato JSON legible
        print(json.dumps(data, indent=2)) 
        print("----------------------------------------------")

        return data

    except requests.exceptions.HTTPError as err_h:
        # Error HTTP (ej. 404, 500)
        print(f"\n--- Error HTTP ---")
        print(f"Código: {response.status_code}")
        print(f"Mensaje: {err_h}")
        print("--------------------")
    except requests.exceptions.ConnectionError as err_c:
        # Error de conexión (ej. DNS fallido, rechazo de conexión)
        print(f"\n--- Error de Conexión ---")
        print(f"Mensaje: {err_c}")
        print("---------------------------")
    except requests.exceptions.Timeout as err_t:
        # Solicitud agotó el tiempo de espera
        print(f"\n--- Error de Tiempo de Espera (Timeout) ---")
        print(f"Mensaje: {err_t}")
        print("--------------------------------------------")
    except requests.exceptions.RequestException as err:
        # Cualquier otro error de requests (error base)
        print(f"\n--- Error Desconocido de Solicitud ---")
        print(f"Mensaje: {err}")
        print("--------------------------------------")
    except json.JSONDecodeError:
        # El servidor respondió con algo que no es JSON (como texto o HTML)
        print("\n--- Error de Decodificación JSON ---")
        print("La respuesta del servidor no es un JSON válido.")
        print(f"Respuesta de texto recibida:\n{response.text}")
        print("------------------------------------")
    
    return {"status": "error", "message": "Fallo en la solicitud a la API."}

# Asegúrate de tener la biblioteca 'requests' instalada: pip install requests
if __name__ == "__main__":
    send_wolfbet_config()
