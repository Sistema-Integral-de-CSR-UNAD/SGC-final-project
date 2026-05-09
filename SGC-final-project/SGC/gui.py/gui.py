import tkinter as tk
from tkinter import messagebox, ttk
from SGC.modelos.cliente import Cliente
from SGC.utilidades.logger import registrar_log

class VentanaSGC:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ - Sistema Integral de Gestión")
        self.root.geometry("500x450")
        
        # Título decorativo
        tk.Label(root, text="Panel de Gestión Software FJ", font=("Arial", 14, "bold")).pack(pady=10)

        # Formulario
        self.marco = tk.LabelFrame(root, text=" Registro de Clientes ", padx=15, pady=15)
        self.marco.pack(padx=20, pady=10, fill="both")

        tk.Label(self.marco, text="ID Cliente:").grid(row=0, column=0, sticky="w")
        self.ent_id = tk.Entry(self.marco)
        self.ent_id.grid(row=0, column=1, pady=5)

        tk.Label(self.marco, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.ent_nombre = tk.Entry(self.marco)
        self.ent_nombre.grid(row=1, column=1, pady=5)

        tk.Label(self.marco, text="Email:").grid(row=2, column=0, sticky="w")
        self.ent_email = tk.Entry(self.marco)
        self.ent_email.grid(row=2, column=1, pady=5)

        # Botón de acción
        self.btn_guardar = ttk.Button(self.marco, text="Registrar Cliente", command=self.procesar_cliente)
        self.btn_guardar.grid(row=3, columnspan=2, pady=15)

    def procesar_cliente(self):
        try:
            # Captura de datos
            id_val = self.ent_id.get()
            nombre = self.ent_nombre.get()
            email = self.ent_email.get()

            if not id_val or not nombre or not email:
                raise ValueError("Todos los campos deben estar llenos.")

            # Instanciación con Herencia
            nuevo_cliente = Cliente(id_val, nombre, email)
            
            # Feedback al usuario
            messagebox.showinfo("Éxito", f"Cliente registrado correctamente:\n{nuevo_cliente.mostrar_detalle()}")
            registrar_log(f"GUI: Registro exitoso - ID {id_val}")

        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
            registrar_log(f"GUI: Intento fallido - {e}", es_error=True)
        except Exception as e:
            messagebox.showerror("Error Crítico", f"Ocurrió un fallo: {e}")
            registrar_log(f"FALLO GUI: {e}", es_error=True)

def iniciar_aplicacion():
    root = tk.Tk()
    app = VentanaSGC(root)
    root.mainloop()