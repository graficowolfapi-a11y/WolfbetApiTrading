<?php
// Este script ejecuta una llamada cURL POST a la API de Wolfbet para enviar la configuración del robot.
// Los resultados se imprimirán directamente en la salida (pantalla).


$curl = curl_init();

$api_key_largo = "{YOUR_API_KEY_WOLFBET}";



$json_payload = "{
    \"APIKEY\": \"{$api_key_largo}\",
    \"COIN\": \"usdt\",
    \"COIN_COMAS\": \"usdt,ada\",
    \"martingala_auto\": 0.01,
    \"volumen_entrada\": 50,
    \"TAKE_PROFIT\": 10.0,
    \"bet_value\": 49.5,
    \"limite_ticks_perdida\": 5,
    \"entrada_porcentaje\": 10,
    \"tiempo_limite\": 60,
    \"apuesta_division\": 1000,
    \"distancia\": 100,
    \"mva200_periodos\": 50,
    \"cerrar_manualmente\": \"\", 
    \"reiniciar_todo\": \"\",
    \"submit\": \"enviar\",
    \"indicador\": \"rsi\",
    \"accion\": \"venta\"
}";

//var_dump(json_decode($json_payload,true));

// Configuración de cURL
curl_setopt_array($curl, array(
  CURLOPT_URL => "https://wolfbetrobot.me/REQUEST_API.php?submit=enviar",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 100,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => $json_payload, // Se usa la variable JSON
  CURLOPT_HTTPHEADER => array(
    "Content-Type: application/json" // Añadir la cabecera Content-Type para el JSON
  ),
  // *** SOLUCIÓN AL ERROR SSL ***
  CURLOPT_SSL_VERIFYPEER => false,
  // *****************************
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);


header('Content-Type: text/plain'); // Establecer cabecera de texto plano para mostrar la salida de cURL
echo "--- Resultado de la consulta cURL ---\n";

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo "Respuesta del Servidor (JSON/Texto):\n";
  // Mostrar la respuesta en formato legible (si es JSON, lo decodifica)
  $decoded_response = json_decode($response, true);
  if (json_last_error() === JSON_ERROR_NONE) {
    echo json_encode($decoded_response, JSON_PRETTY_PRINT);
  } else {
    echo $response; // Mostrar como texto si no es JSON
  }
}
echo "\n-------------------------------------\n";

// Muestra el JSON que fue enviado
//echo "JSON Enviado:\n";
//echo $json_payload;

?>
