import json   
import os


CARPETA_DESTINO = r"C:\Users\Emiliano\Desktop\clase 1\trabajo practico final\tp_ecotech\ejercicio 2"

class StockInvalidoError(Exception):
    """Se lanza cuando el stock viola las reglas de negocio."""
    pass

class DispositivoEcológico:
    def __init__(self, modelo, precio, stock):
        self.modelo = modelo
        self.precio = precio
        self.set_stock(stock)   # usa el setter, así también valida al crear el objeto

    def get_stock(self):
        return self.__stock

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise StockInvalidoError("El stock debe ser un número entero no negativo.")
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self):
        return f"Modelo: {self.modelo} | Precio: ${self.precio} | Stock: {self.get_stock()}"

    def a_diccionario(self):
        return {
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock(),
        }
    
class PanelSolar(DispositivoEcológico):
    def __init__(self, modelo, precio, stock, potencia_watts):
        super().__init__(modelo, precio, stock)
        self.potencia_watts = potencia_watts

    def obtener_ficha_tecnica(self):
        ficha_base = super().obtener_ficha_tecnica()
        return f"{ficha_base} | Potencia: {self.potencia_watts} W"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["potencia_watts"] = self.potencia_watts
        return datos
    
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        datos = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False) 

if __name__ == "__main__":
    catalogo = []

    # Productos válidos
    catalogo.append(DispositivoEcológico("Termostato-Smart", 350.0, 10))
    catalogo.append(PanelSolar("SolarMax-500", 1200.0, 8, 500))

    # Intento inválido, capturado
    try:
        catalogo.append(PanelSolar("Panel-Defectuoso", 900.0, -3, 400))
    except StockInvalidoError as error:
        print(f"[ERROR CONTROLADO] {error}")

        # Exportación
    gestor = GestorInventario()
    os.makedirs(CARPETA_DESTINO, exist_ok=True)   # crea la carpeta si no existe
    ruta = os.path.join(CARPETA_DESTINO, "catalogo_ecotech.json")
    gestor.guardar_catalogo_json(catalogo, ruta)
    print(f"Catálogo exportado correctamente en: {ruta}")