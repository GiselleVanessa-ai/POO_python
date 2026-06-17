
lista_zapatos = []
class Zapatos:
    def __init__(self, id_zapato, marca, talla, color, material, precio):
        self.id_zapato = id_zapato
        self.marca = marca
        self.talla = talla
        self.color = color
        self.material = material
        self.precio = precio

    def crear_zapato(self):
        lista_zapatos.append(self)
        print(f"el zapato  de la marca {self.marca} ha sido registrado en el sistema")

    def ver_zapato(self):
        print(f"ID:{self.id_zapato} Marca:{self.marca} Talla:{self.talla} Color:{self.color} Material:{self.material} Precio:{self.precio}")

    def actualizar_zapato(self, nueva_talla, nuevo_color, nuevo_material, nuevo_precio, marca):
        self.talla = nueva_talla 
        self.color = nuevo_color
        self.material = nuevo_material
        self.precio = nuevo_precio
        self.marca = marca
        print(f"el zapato de la marca {self.marca} ha sido actualizado")
    
    def eliminar_zapato(self):
        if self in lista_zapatos:
            lista_zapatos.remove(self)
            print(f"el zapato de la marca {self.marca} con el id {self.id_zapato} ha sido eliminado del sistema")

        else:
            print("el zapato no existe")

    def vender_zapato(self):
        print(f"el zapato de la marca {self.marca} con el id {self.id_zapato} ha sido vendido por {self.precio} pesos")

#instancia

zapato_1 = Zapatos(1, "Bata", 35, "negro", "cuero", 100000)
zapato_2 = Zapatos(2, "Mussi", 41, "azul", "sintetico", 285000)

#crear zapato

zapato_1.crear_zapato()
print(f"lista de zapatos: id {lista_zapatos[0].id_zapato} de la marca {lista_zapatos[0].marca}")

zapato_2.crear_zapato()
print(f"lista de zapatos: id {lista_zapatos[1].id_zapato} de la marca {lista_zapatos[1].marca}")

#ver zapato
zapato_1.ver_zapato()
zapato_2.ver_zapato()

#actualizar zapato

zapato_1.actualizar_zapato(40, "rojo", "lona", 257000, "clarks")
zapato_1.ver_zapato()

#delete

zapato_2.eliminar_zapato()

#vender zapato
zapato_1.vender_zapato()
zapato_2.vender_zapato() 
