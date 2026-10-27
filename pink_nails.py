import tkinter as tk
from tkinter import messagebox


class Cliente:
    def __init__(self, nombre, servicio):
        self.nombre = nombre
        self.servicio = servicio


class PinkNailsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pink Nails Studio")
        self.root.geometry("400x430")
        self.root.config(bg="#fff0f5")
        self.root.resizable(False, False)

        self.clientes = []
        self.ingresos = 0

        tk.Label(
            root,
            text="PINK NAILS STUDIO",
            font=("Arial", 16, "bold"),
            bg="#fff0f5",
            fg="#c2185b"
        ).pack(pady=20)

        tk.Label(
            root,
            text="Nombre de la clienta:",
            bg="#fff0f5",
            font=("Arial", 10)
        ).pack()

        self.nombre = tk.Entry(root, width=30)
        self.nombre.pack(pady=8)

        tk.Label(
            root,
            text="Selecciona el servicio:",
            bg="#fff0f5",
            font=("Arial", 10)
        ).pack(pady=5)

        self.servicio = tk.StringVar(root)
        self.servicio.set("Manicure")

        opciones = ["Manicure", "Pedicure", "Uñas acrilicas"]

        tk.OptionMenu(root, self.servicio, *opciones).pack()

        tk.Button(
            root,
            text="Registrar cita",
            command=self.registrar,
            bg="#e75480",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=6
        ).pack(pady=20)

        self.reporte = tk.Label(
            root,
            text="Citas: 0 | Ingresos: $0",
            bg="#fff0f5",
            fg="#880e4f",
            font=("Arial", 10, "bold")
        )
        self.reporte.pack(pady=10)

    def registrar(self):
        nombre = self.nombre.get().strip()
        servicio = self.servicio.get()

        if not nombre:
            messagebox.showwarning(
                "Aviso",
                "Debes ingresar el nombre de la clienta."
            )
            return

        precios = {
            "Manicure": 20000,
            "Pedicure": 30000,
            "Uñas acrilicas": 50000
        }

        nueva_cliente = Cliente(nombre, servicio)
        self.clientes.append(nueva_cliente)
        self.ingresos += precios[servicio]

        self.reporte.config(
            text=f"Citas: {len(self.clientes)} | Ingresos: ${self.ingresos:,}"
        )

        messagebox.showinfo(
            "Cita registrada",
            f"Clienta: {nombre}\n"
            f"Servicio: {servicio}\n"
            f"Precio: ${precios[servicio]:,}"
        )

        self.nombre.delete(0, tk.END)


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = PinkNailsApp(ventana)
    ventana.mainloop()
