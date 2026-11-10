def limpiar_registro_sensor(registro_raw):
    
    sensor_id = registro_raw["sensor_id"].strip()

    
    temperatura_texto = registro_raw["temperatura"].strip()
    temperatura = float(temperatura_texto.rstrip("°C").strip())

    
    ubicacion = (registro_raw.get("ubicacion") or "").strip()
    if not ubicacion:
        ubicacion = "Ubicación no especificada"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    
    lista_sensores_alerta = [sensor["sensor_id"] for sensor in lista_sensores_limpios if sensor["temperatura"] > umbral_temperatura]

    
    if lista_sensores_limpios:
        promedio_temperatura = sum(sensor["temperatura"] for sensor in lista_sensores_limpios) / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0.0

    return (lista_sensores_alerta, promedio_temperatura)

if __name__ == "__main__": 
  
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 31.2 C", "ubicacion": "   "},
        {"sensor_id": " SENSOR-003", "temperatura": "28.0°C"},
        {"sensor_id": "SENSOR-004", "temperatura": "29.5°C", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR-005 ", "temperatura": " 32.1 °C", "ubicacion": None},
    ]

    umbral = 30.0

    
    registros_limpios = [limpiar_registro_sensor(registro) for registro in registros_crudos]

    
    alertas, promedio = generar_resumen_sensores(registros_limpios, umbral)

    
    print("=== REPORTE DE SENSORES ECOTECH ===")
    print(f"Sensores en alerta ({umbral}°C): {', '.join(alertas)}")
    print(f"Promedio de temperatura: {promedio:.2f}°C")