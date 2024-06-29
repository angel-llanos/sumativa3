class Carro:
    def init(self,request):
        #Almacenar la peticion actual para usarla mas adelante
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")#Construir carro de la compra para esta sesion
        #Carro va a ser un diccionario
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self,autos):
        if(str(autos.id) not in self.carro.keys()):
            self.carro[autos.id]={
                "producto_id":autos.id,
                "nombre":autos.marca,
                "precio":str(autos.precio),
                "cantidad":1,
                "imagen":autos.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(autos.id):
                    value["cantidad"]= value["cantidad"]+1
                    value["precio"]=float(value["precio"])+autos.precio
                    break#Ya no recorras mas
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,autos):
        #primer ver si existe para poder eliminar
        autos.id=str(autos.id)
        if autos.id in self.carro:
            del self.carro[autos.id]
            self.guardar_carro()

    def restar_auto(self,autos):
        for key, value in self.carro.items():
            if key==str(autos.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-autos.precio
                if value["cantidad"]<1:
                   self.eliminar(autos) 
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True