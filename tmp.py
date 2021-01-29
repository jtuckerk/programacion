class Board:
  def __init__(self):
    self.datos = []
    # B.)
    self.crear_datos()

  def crear_datos(self):
    self.datos.append(2)
    self.datos.append(3)


def main():
  board = Board()

  print("los datos son:", board.datos)


  while True:

    # accion de jugadores
    board.datos[0] += 1

    print("los datos son:", board.datos)
  # que va a pasar si hago:
  # A.)

  # print("los datos son:", board.datos)

main()
