
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    
    if not registros:
        return {"total_emisiones": 0.0, "planta_top": None}

    
    total_emisiones = sum(calcular_emisiones_carbono(r["consumo_kwh"]) for r in registros)

    
    consumo_por_planta = {}
    for r in registros:
        planta = r["planta"]
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + r["consumo_kwh"]

    
    planta_top = max(consumo_por_planta, key=consumo_por_planta.get)

    return {
        "total_emisiones": total_emisiones,
        "planta_top": planta_top,
    }


if __name__ == "__main__":
    registros = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400},
    ]
    print(obtener_metricas_consumo(registros))