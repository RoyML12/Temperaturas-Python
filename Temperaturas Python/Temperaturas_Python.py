import tkinter as tk
from tkinter import messagebox

def radioButton_Selected():
    sel = rbSeleccion.get()

    if sel == "Celsius":
        tbCelsius.config(state="normal")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="disabled")

    elif sel == "Kelvin":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="normal")

    elif sel == "Fahrenheit":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="normal")
        tbKelvin.config(state="disabled")

def btnCalcular_Click():
    try:
        if rbSeleccion.get() == "Celsius":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")

            celsius = float(tbCelsius.get())
            print(celsius)

            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)

            tbFahrenheit.insert(0, str(round(farenheintt, 2)))

            kelvin = celsius + 273.0
            print(kelvin)

            tbKelvin.insert(0, str(round(kelvin, 2)))

        elif rbSeleccion.get() == "Kelvin":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")

            kelvin = float(tbKelvin.get())
            print(kelvin)

            celsius = kelvin - 273.0
            tbCelsius.insert(0, str(round(celsius, 2)))
            print(celsius)

            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)

            tbFahrenheit.insert(0, str(round(farenheintt, 2)))

        elif rbSeleccion.get() == "Fahrenheit":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")

            farenheinth = float(tbFahrenheit.get())
            print(farenheinth)

            celsius = (farenheinth - 32.0) * 5.0 / 9.0
            print(celsius)

            kelvin = celsius + 273.0
            print(kelvin)

            tbCelsius.insert(0, str(round(celsius, 2)))
            tbKelvin.insert(0, str(round(kelvin, 2)))

        else:
            messagebox.showwarning(
                "Temperatura Seleccionada",
                "Seleccione una temperatura de entrada (Kelvin/Fahrenheit/Celsius)."
            )

    except ValueError:
        messagebox.showerror("Error", "Ingrese un numero valido en el campo habilitado.")

def btnLimpiar_Click():
    tbKelvin.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)

    tbCelsius.config(state="normal")
    tbFahrenheit.config(state="normal")
    tbKelvin.config(state="normal")
    rbSeleccion.set("")

ventana = tk.Tk()
ventana.title("Actividad 03 - Conversor Temperatura")
ventana.geometry("380x430")
ventana.configure(bg="Pink")

rbSeleccion = tk.StringVar(value="")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

main = tk.Frame(ventana, bg="Pink")
main.grid(row=0, column=0, sticky="nsew", padx=16, pady=14)
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)

tk.Label(
    main,
    text="Conversor de Temperatura",
    font=("Segoe UI", 14, "bold"),
    bg="Pink"
).grid(row=0, column=0, columnspan=2, pady=(0, 10))

tk.Frame(main, height=2, bg="#000000").grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 14))

def fila_label_entry(r, texto, entry):
    tk.Label(main, text=texto, font=("Segoe UI", 10, "bold"), bg="Pink").grid(
        row=r, column=0, sticky="e", padx=(0, 10), pady=6
    )
    entry.grid(row=r, column=1, sticky="ew", pady=6)

tbCelsius = tk.Entry(main, justify="center")
tbFahrenheit = tk.Entry(main, justify="center")
tbKelvin = tk.Entry(main, justify="center")

fila_label_entry(2, "Temp. en Celsius:", tbCelsius)
fila_label_entry(3, "Temp. en Fahrenheit:", tbFahrenheit)
fila_label_entry(4, "Temp. en Kelvin:", tbKelvin)

tk.Frame(main, height=2, bg="#000000").grid(row=5, column=0, columnspan=2, sticky="ew", pady=(10, 12))

gb = tk.LabelFrame(
    main,
    text="Seleccione Temperatura de Entrada:",
    padx=12,
    pady=10,
    bg="Pink",
    font=("Segoe UI", 9, "bold")
)
gb.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, 12))
gb.grid_columnconfigure(0, weight=1)

rbKelvin = tk.Radiobutton(gb, text="Kelvin", value="Kelvin",
                          variable=rbSeleccion, command=radioButton_Selected, bg="Pink")
rbKelvin.grid(row=0, column=0, sticky="w", pady=3)

rbFahrenheit = tk.Radiobutton(gb, text="Fahrenheit", value="Fahrenheit",
                              variable=rbSeleccion, command=radioButton_Selected, bg="Pink")
rbFahrenheit.grid(row=1, column=0, sticky="w", pady=3)

rbCelsius = tk.Radiobutton(gb, text="Celsius", value="Celsius",
                           variable=rbSeleccion, command=radioButton_Selected, bg="Pink")
rbCelsius.grid(row=2, column=0, sticky="w", pady=3)

btnCalcular = tk.Button(main, text="Calcular", width=12,
                        bg="#7CFC00", command=btnCalcular_Click, padx=6, pady=6)
btnCalcular.grid(row=7, column=0, sticky="e", padx=(0, 8), pady=10)

btnLimpiar = tk.Button(main, text="Limpiar", width=12,
                       bg="#FF3030", fg="white",
                       command=btnLimpiar_Click, padx=6, pady=6)
btnLimpiar.grid(row=7, column=1, sticky="w", padx=(8, 0), pady=10)

tbCelsius.config(state="normal")
tbFahrenheit.config(state="normal")
tbKelvin.config(state="normal")

ventana.mainloop()
