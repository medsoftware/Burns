# Parkland 
def Parkland():
  peso = float(input("Inserire il peso"))
  sup_ustionata = float(input("inserire la superficie ustionata"))
  return 4*peso*sup_ustionata
def LiquidToFlow(liquid):
  first8 = liquid / 16
  second16 = liquid / 32
  return first8,second16


