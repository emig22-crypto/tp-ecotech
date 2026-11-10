
from django.shortcuts import render
from emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    registros = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400},
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_top": metricas["planta_top"],
    }

    return render(request, "sustentabilidad/panel.html", contexto)