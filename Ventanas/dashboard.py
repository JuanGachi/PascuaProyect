import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3

def conectar_db():
    conexion = sqlite3.connect("Usuarios.db")
    return conexion

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, correo TEXT, contraseña TEXT)")
    conexion.commit()
    conexion.close()

def agregar_usuario(nombre, apellido, correo, contraseña):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, apellido, correo, contraseña) VALUES (?, ?, ?, ?)", (nombre, apellido, correo, contraseña))
    conexion.commit()
    conexion.close()

def leer_usuarios():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, apellido, correo, contraseña FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def actualizar_usuario(nombre, apellido, correo, contraseña):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre=?, apellido=?, contraseña=? WHERE correo=?", (nombre, apellido, contraseña, correo))
    conexion.commit()
    conexion.close()

def eliminar_usuario(correo):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE correo=?", (correo,))
    conexion.commit()
    conexion.close()

def mostrar_usuarios():
    usuarios = leer_usuarios()
    print("Usuarios:")
    for usuario in usuarios:
        print(usuario)

def crear_dashboard():
    ventana = ThemedTk(theme="plastik")  # Selecciona el tema "arc"
    ventana.title("Dashboard CRUD")

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12), padding=5)

    nombre_label = ttk.Label(ventana, text="Nombre:")
    nombre_label.grid(row=0, column=0, padx=5, pady=5)
    nombre_entry = ttk.Entry(ventana)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)

    apellido_label = ttk.Label(ventana, text="Apellido:")
    apellido_label.grid(row=1, column=0, padx=5, pady=5)
    apellido_entry = ttk.Entry(ventana)
    apellido_entry.grid(row=1, column=1, padx=5, pady=5)

    correo_label = ttk.Label(ventana, text="Correo:")
    correo_label.grid(row=2, column=0, padx=5, pady=5)
    correo_entry = ttk.Entry(ventana)
    correo_entry.grid(row=2, column=1, padx=5, pady=5)

    contraseña_label = ttk.Label(ventana, text="Contraseña:")
    contraseña_label.grid(row=3, column=0, padx=5, pady=5)
    contraseña_entry = ttk.Entry(ventana, show="*")
    contraseña_entry.grid(row=3, column=1, padx=5, pady=5)

    # Crea el Treeview para mostrar los usuarios
    columnas = ("#1", "#2", "#3", "#4", "#5")
    encabezados = ("ID", "Nombre", "Apellido", "Correo", "Contraseña")
    tabla_usuarios = ttk.Treeview(ventana, columns=columnas, show="headings")
    tabla_usuarios.grid(row=5, column=0, columnspan=5, pady=10)

    for col, encabezado in zip(columnas, encabezados):
        tabla_usuarios.heading(col, text=encabezado)
        if col == "#1":
            tabla_usuarios.column(col, minwidth=0, width=25, stretch=False)
        else:
            tabla_usuarios.column(col, minwidth=0, width=len(encabezado) * 25, stretch=False)

    def actualizar_tabla():
        # Elimina los usuarios existentes en la tabla
        for usuario in tabla_usuarios.get_children():
            tabla_usuarios.delete(usuario)

        # Agrega los usuarios de la base de datos a la tabla
        for usuario in leer_usuarios():
            tabla_usuarios.insert("", tk.END, values=usuario)

    # Rellena los campos de entrada al seleccionar una fila en la tabla
    def on_seleccionar(event):
        item = tabla_usuarios.item(tabla_usuarios.focus())
        valores = item["values"]
        if valores:
            id_, nombre, apellido, correo, contraseña = valores
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, nombre)
            apellido_entry.delete(0, tk.END)
            apellido_entry.insert(0, apellido)
            correo_entry.delete(0, tk.END)
            correo_entry.insert(0, correo)
            contraseña_entry.delete(0, tk.END)
            contraseña_entry.insert(0, contraseña)

    tabla_usuarios.bind("<<TreeviewSelect>>", on_seleccionar)


    # Modifica las funciones agregar, actualizar y eliminar para actualizar la tabla
    def agregar():
        agregar_usuario(nombre_entry.get(), apellido_entry.get(), correo_entry.get(), contraseña_entry.get())
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        correo_entry.delete(0, tk.END)
        contraseña_entry.delete(0, tk.END)
        actualizar_tabla()

    def actualizar():
        id_ = tabla_usuarios.item(tabla_usuarios.focus())["values"]
        if id_:
            id_ = id_[0]
            actualizar_usuario(id_, nombre_entry.get(), apellido_entry.get(), correo_entry.get(), contraseña_entry.get())
            actualizar_tabla()

    def eliminar():
        id_ = tabla_usuarios.item(tabla_usuarios.focus())["values"]
        if id_:
            id_ = id_[0]
            eliminar_usuario(id_)
            actualizar_tabla()
    def actualizar_usuario(id_, nombre, apellido, correo, contraseña):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET nombre=?, apellido=?, correo=?, contraseña=? WHERE id=?", (nombre, apellido, correo, contraseña, id_))
        conexion.commit()
        conexion.close()
    def eliminar_usuario(id_):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=?", (id_,))
        conexion.commit()
        conexion.close()

    agregar_btn = ttk.Button(ventana, text="Agregar", command=agregar)
    agregar_btn.grid(row=4, column=0, padx=5, pady=5)
    actualizar_btn = ttk.Button(ventana, text="Actualizar", command=actualizar)
    actualizar_btn.grid(row=4, column=1, padx=5, pady=5)

    eliminar_btn = ttk.Button(ventana, text="Eliminar", command=eliminar)
    eliminar_btn.grid(row=4, column=2, padx=5, pady=5)

    mostrar_btn = ttk.Button(ventana, text="Mostrar", command=actualizar_tabla)
    mostrar_btn.grid(row=4, column=3, padx=5, pady=5)

    actualizar_tabla()  # Llama a la función para cargar los usuarios iniciales en la tabla

    ventana.mainloop()

def main():
    crear_tabla()
    crear_dashboard()

if __name__ == "__main__":
    main()
