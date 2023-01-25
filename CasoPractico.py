import tkinter as tk
import mysql.connector
class CRUD:
    def __init__(self, root):
        self.root = root
        self.crearElementos()

    def crearElementos(self):
        # Crear etiquetas
        self.label1 = tk.Label(self.root, text="Nombre")
        self.label1.pack()
        self.label2 = tk.Label(self.root, text="Primer apellido")
        self.label2.pack()
        self.label3 = tk.Label(self.root, text="Segundo apellido")
        self.label3.pack()
        self.label4 = tk.Label(self.root, text="DNI")
        self.label4.pack()
        self.label5 = tk.Label(self.root, text="Fecha de nacimiento")
        self.label5.pack()
        self.label6 = tk.Label(self.root, text="Puesto de trabajo")
        self.label6.pack()
        self.label7 = tk.Label(self.root, text="Sueldo")
        self.label7.pack()
        self.label8 = tk.Label(self.root, text="Años de antigüedad")
        self.label8.pack()

        # Crear campos de entrada
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()
        self.entry4 = tk.Entry(self.root)
        self.entry4.pack()
        self.entry5 = tk.Entry(self.root)
        self.entry5.pack()
        self.entry6 = tk.Entry(self.root)
        self.entry6.pack()
        self.entry7 = tk.Entry(self.root)
        self.entry7.pack()
        self.entry8 = tk.Entry(self.root)
        self.entry8.pack()

        # Crear botones
        self.button1 = tk.Button(self.root, text="Insertar", command=self.insertarDatos)
        self.button1.pack()
        self.button2 = tk.Button(self.root, text="Borrar", command=self.borrarDatos)
        self.button2.pack()
        self.button3 = tk.Button(self.root, text="Modificar", command=self.actualizarDatos)
        self.button3.pack()
        self.button4 = tk.Button(self.root, text="Mostrar", command=self.buscarDatos)
        self.button4.pack()
    def insertarDatos(self):
            # Obtener los valores de los campos de entrada
            nombre = self.entry1.get()
            primerApellido = self.entry2.get()
            segundoApellido = self.entry3.get()
            dni = self.entry4.get()
            fechaNacimiento = self.entry5.get()
            puestoTrabajo = self.entry6.get()
            salario = self.entry7.get()
            aniosExp = self.entry8.get()

            # Crear una conexión a la base de datos
            conn=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="empresa")
            cursor = conn.cursor()

            # Insertar los datos en la tabla "empleados"
            cursor.execute("INSERT INTO empleados VALUES ('" + nombre + "','" +  primerApellido + "','" + segundoApellido + "','" + dni  + "','" + fechaNacimiento
                            + "','" + puestoTrabajo  + "','" + salario  + "','" + aniosExp + "')")
            cursor.execute("commit")
            conn.close()

    def borrarDatos(self):
            # Obtener el valor del campo de entrada
            dni = self.entry4.get()

            # Crear una conexión a la base de datos
            conn=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="empresa")
            cursor = conn.cursor()

            # Borrar el registro con el DNI especificado
            cursor.execute("DELETE FROM empleados WHERE dni= " + "'" + dni + "'")
            cursor.execute("commit")
            conn.close()

    def actualizarDatos(self):
            # Obtener los valores de los campos de entrada
            nombre = self.entry1.get()
            primerApellido = self.entry2.get()
            segundoApellido = self.entry3.get()
            dni = self.entry4.get()
            fechaNacimiento = self.entry5.get()
            puestoTrabajo = self.entry6.get()
            salario = self.entry7.get()
            aniosExp = self.entry8.get()

            # Crear una conexión a la base de datos
            conn=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="empresa")
            cursor = conn.cursor()

            # Modificar el registro con el DNI especificado
            sql = "UPDATE empleados SET Nombre =%s, Primer_apellido=%s, Segundo_apellido=%s, Fecha_nacimiento=%s, Puesto_trabajo=%s, sueldo=%s, años_antiguedad=%s WHERE DNI =%s"
            valores = (nombre, primerApellido, segundoApellido, fechaNacimiento, puestoTrabajo, salario, aniosExp, dni)
            cursor.execute(sql, valores)
            cursor.execute("commit")
            conn.close()
            
    def buscarDatos(self):
        # Crear un diccionario para almacenar los campos y datos a utilizar en la consulta
        filtros = {}

        # Obtener los valores de las entradas
        nombre = self.entry1.get()
        primerApellido = self.entry2.get()
        segundoApellido = self.entry3.get()
        dni = self.entry4.get()
        fechaNacimiento = self.entry5.get()
        puestoTrabajo = self.entry6.get()
        salario = self.entry7.get()
        aniosExp = self.entry8.get()

        # Añadir cualquier campo y dato no vacío al diccionario de filtros
        if nombre:
            filtros['Nombre'] = nombre
        if primerApellido:
            filtros['Primer_apellido'] = primerApellido
        if segundoApellido:
            filtros['Segundo_apellido'] = segundoApellido
        if dni:
            filtros['DNI'] = dni
        if fechaNacimiento:
            filtros['Fecha_nacimiento'] = fechaNacimiento
        if puestoTrabajo:
            filtros['Puesto_trabajo'] = puestoTrabajo
        if salario:
            filtros['sueldo'] = salario
        if aniosExp:
            filtros['años_antiguedad'] = aniosExp

        # Crear una conexión a la base de datos
        conn=mysql.connector.connect(host="localhost", 
                              user="root", 
                              passwd="", 
                              database="empresa")
        cursor = conn.cursor()

        # Crear la consulta select a partir de los filtros
        consulta = "SELECT * FROM empleados"
        if filtros:
            consulta += " WHERE"
            for i, (campo, dato) in enumerate(filtros.items()):
                if i > 0:
                    consulta += " AND"
                consulta += " {} = '{}'".format(campo, dato)

        # Ejecutar la consulta
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        # Mostrar los resultados en la consola
        print(resultados)
root = tk.Tk()
crud = CRUD(root)
root.mainloop()
