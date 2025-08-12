from ElementoSistema import ElementoSistema

class Archivo(ElementoSistema):
    def __init__(self, nombre: str, tamano: int):
        super().__init__(nombre, tamano)

    def es_directorio(self) -> bool:
        return False

    def get_ficheros(self):
        raise NotImplementedError("Un archivo no contiene ficheros")