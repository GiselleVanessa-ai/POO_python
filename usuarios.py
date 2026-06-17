"""
class Usuario:
    id_usuario = 1
    documento = 987654321
    nombre = "Anderson"
    apellido= "Perez"
    correo = "pereza@gmail.com"
    telefono = 123456789
    direccion = "calle 123"

#instancia de la clase usuario
usuario_1 = Usuario()
usuario_2 = Usuario()

usuario_2.nombre = "Juan"

print(usuario_1.correo)
print(usuario_2.nombre)
"""
lista_usuarios = [] #lista global para allmacenar los usuarios creados
class Usuario:
    #crear una funcion para el CONSTRUCTOR 
    def __init__(self, id_usuario : int, documento, nombre : str, apellido : str, correo, telefono, direccion): 
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
    def saludar(self):
        print(f"hola, mi nombre es {self.nombre}")    
    #metodos base CRUD
    #create
    def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"el usuario {self.nombre} ha sido registrado en el sistema")
    #read
    def ver_usuario(self):
        print(f"ID:{self.id_usuario} Nombre:{self.nombre} Apellido:{self.apellido}")
    #update
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"el ususario {self.nombre} ha sido actualixado")
    #delete
    def eliminar_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"el usuario {self.nombre} ha sido eliminado del sistema")
        else:
            print("el usuario no existe")


#crear una instancia de la clase usuario

usuario_1 = Usuario(1, 987654321, "Anderson", "Perez", "pereza@gmail.com", 134568789, "calle 123")
usuario_2 = Usuario(2, 456789123, "Pedro", "Martinez", "martinez@gmail.com", 137894656, "calle 546")

#llamar al metodo saludar
usuario_1.saludar()
usuario_2.saludar()

#mostrar lista de usuarios vacia
print(f"lista de usuarios {lista_usuarios}") #lista vacia

#llamar metodos create
usuario_1.crear_usuario()
print(f"lista de usuarios {lista_usuarios[0].nombre}") #lista con usuario 1

#crear usuario 2
usuario_2.crear_usuario()
print(f"lista de usuarios {lista_usuarios[1].nombre}") 

#llamar los metodos read
usuario_1.ver_usuario()
usuario_2.ver_usuario()

#llamar metodos update
usuario_1.actualizar_usuario("Messi", "Ronaldo")
usuario_1.ver_usuario()

#llamar metodos delete
usuario_2.eliminar_usuario()
usuario_2.ver_usuario()

