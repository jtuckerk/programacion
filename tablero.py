from tkinter import *

def main():
  ventana = Tk()
  ventana.title("Tablero Damas")
  ventana.geometry("800x800")
  ventana.resizable(False, False)
  ventana.configure(background = "black")

  ancho = alto = 8
  cuadro = Button(ventana, width=ancho, height=alto)
  cuadro.grid(row=1, column = 0)

  ventana.mainloop()

if __name__ == "__main__":
  main()

