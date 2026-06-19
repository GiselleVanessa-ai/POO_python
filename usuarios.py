""" class Usuario:
    id_usuario = 1
    documento = 1052312321
    nombre = "Pepito"
    apellido = "Perez"
    correo = "pepitoperez@gmail.com"
    telefono = "321123123"
    direccion = "Calle 123"

#Creando una Instancia de la Clase Usuario
usuario_1 = Usuario()
usuario_2 = Usuario()

usuario_2.nombre = "Felipe"

print(usuario_1.nombre)
print(usuario_2.nombre) """

lista_usuarios = [] # Lista global para almacenar los usuarios creados

class Usuario:
    # Crear una funcion para el CONSTRUCTOR
    def __init__(self, id_usuario: int, documento, nombre: str, apellido, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}")
        
    def encriptar_contraseña(self, contraseña):
          print(f"Contraseña encriptada: {contraseña}")
        
    # Metodos Base CRUD
    
    #CREATE
    def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"✅ Éxito: El usuario {self.nombre} ha sido registrado en el sistema.")
    
    #READ
    def ver_usuario(self):
        print(f"ID: {self.id_usuario} Nombre: {self.nombre} {self.apellido}")
        
    #UPDATE
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"✅ Éxito: El usuario ha sido actualizado a {self.nombre} {self.apellido}.")
        
    #DELETE
    def eliminar_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"✅ Éxito: El usuario {self.nombre} ha sido eliminado del sistema.")
        else:
            print(f"⚠️ Advertencia: El usuario {self.nombre} no se encuentra en el sistema.")
    #POLIMORFISMO
    def consultar_certificado(self):
        pass
        
#Creando una Instancia de la Clase Usuario
usuario_1 = Usuario(1,10532457,"Falcao", "Garcia","fgarcia@gmail.com","321321312","Calle 123")

usuario_2 = Usuario(2,10532458,"James", "Rodriguez","jrodriguez@gmail.com","321321313","Calle 456")

#Llame a lo Metodos de la clase Usuario
usuario_1.saludar()
usuario_2.saludar()

# Llamar los Metodos CREATE
print(f"Lista de usuarios: {lista_usuarios}") # Lista vacia
usuario_1.crear_usuario()
usuario_2.crear_usuario()

# Llamar los Metodos READ
print(f"Lista de usuarios: {lista_usuarios[0].nombre}")# Falcao
print(f"Lista de usuarios: {lista_usuarios[1].nombre}")# James
usuario_1.ver_usuario()
usuario_2.ver_usuario()

#Llamar los Metodos UPDATE
usuario_1.actualizar_usuario("Messi","Ronaldo")
usuario_1.ver_usuario()

#Llamar los Metodos DELETE
usuario_2.eliminar_usuario()


# ----------------------------------------------------------------------------------
# APLICANDO LOS 4 PILARES DE LA POO
#-----------------------------------------------------------------------------------

# HERENCIA y ENCAPSULAMIENTO APRENDIZ

class Aprendiz(Usuario):
    def __init__(self, id_usuario: int, documento, nombre: str, apellido, correo, telefono, direccion, programa, ficha=None, resultados=[]):
        
        # Usamos super() para llamar al constructor de la clase padre (Usuario)
        super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)

        # Atributos propios del Aprendiz
        self.programa = programa
        self.ficha = ficha
        
        # ENCAPSULAMIENTO: Usamos un atributo privado para almacenar los resultados académicos del aprendiz
        self.__resultados = resultados #Privado
        
    #GET >Consultar o Ver el Atributo
    def get_resultados(self):
        return self.__resultados
        
    #SET > Modificar o Actualizar el Atributo
    def set_resultados(self, notas):
        self.__resultados.append(notas)
        print(f"📝 Resultado guardado para el aprendiz {self.nombre}. Total notas: {len(self.__resultados)}")
  


    # 4. POLIMORFISMO
    # Sobrescribimos el método de la clase padre para darle un comportamiento específico
    def consultar_certificado(self):
        print(f"🎓 [CERTIFICADO DE APRENDIZ] Generando certificado de notas del programa {self.programa} para {self.nombre}.")
        
aprendiz_1 = Aprendiz(3,10532459,"Sofia", "Lopez","sofia.lopez@gmail.com","321321314","Calle 789", "Analisis y Desarrollo de Sistemas", "Ficha 123", ["Programación", "Base de Datos"], ["Aprobado", "Aprobado"])

print(f"Imprimir atributo privado {aprendiz_1.get_resultados()}") 
print(f"Imprimir atributo publico {aprendiz_1.nombre}")










        

class Instructor(Usuario):
    def __init__(self, id_usuario: int, documento, nombre: str, apellido, correo, telefono, direccion,perfil_profesional,anios_experiencia):
        
        super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)
        
        self.perfil_profesional = perfil_profesional
        self.anios_experiencia = anios_experiencia
        
    # 4. POLIMORFISMO
    # El instructor tiene una forma diferente de generar su certificado
    def consultar_certificado(self):
        print(f"💼 [CERTIFICADO DE INSTRUCTOR] Generando constancia laboral para {self.nombre}, Perfil: {self.perfil_profesional}.")
        
instructor_1 = Instructor(4,10532460,"Carlos", "Martinez","carlos.martinez@gmail.com","321321315","Calle 101", "Profesor de Programación", 10)

aprendiz_1.consultar_certificado() # Llamamos al método polimórfico del Aprendiz
instructor_1.consultar_certificado() # Llamamos al método polimórfico del Instructor