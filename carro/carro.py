class Carro:
    def __init__(self, request):
        # Almacenar la petición actual para usarla más adelante
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")  # Construir carro de la compra para esta sesión
        # Carro va a ser un diccionario
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, autos):
        if str(autos.id_auto) not in self.carro.keys():
            self.carro[str(autos.id_auto)] = {
                "id_auto": autos.id_auto,
                "nombre": autos.marca,
                "precio": str(autos.precio),
                "cantidad": 1,
                "imagen": autos.imagen
            }
        else:
            for key, value in self.carro.items():
                if key == str(autos.id_auto):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + autos.precio
                    break  # Ya no recorras más
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, autos):
        # primero ver si existe para poder eliminar
        if str(autos.id_auto) in self.carro:
            del self.carro[str(autos.id_auto)]
            self.guardar_carro()

    def restar_auto(self, autos):
        for key, value in self.carro.items():
            if key == str(autos.id_auto):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - autos.precio
                if value["cantidad"] < 1:
                    self.eliminar(autos)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True