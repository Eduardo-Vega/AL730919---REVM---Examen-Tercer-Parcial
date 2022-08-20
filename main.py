
import math
    
##  ---------------------------------------- BUSQEDA BINARIA --------------------------------------------------- ##

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)
      
def option_1():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    key = int(text_prompt('Ingrese el número a buscar: '))
    position = binary_search(key, arr)
    if position == -1:
      print(''.join([str(x) for x in ['El valor buscado ', int(key), ' no fue encontrado en el arreglo de 12 posiciones.']]))
    else:
      print(''.join([str(x) for x in ['El valor buscado ', int(key), ' se enceuntra en la posición del índice ', position]]))


def binary_search(key, arr):
  i = 0
  j = 12-1
  while i <= j:
    mid = math.floor((i + j) / 2)
    if arr[int(mid)] == key:
      return mid
    elif arr[int(mid)] < key:
      i = mid + 1
    else:
      j = mid - 1
  return -1   
    
print("Seleccione una opción: \n 1. Binary Serch \n 2. Ternary Search \n 3. Jump Searh \n 4. Salir")
selec = int(text_prompt("Opción: "))
if selec == 1:
    option_1()
elif selec == 2:
    option_2()
elif selec == 4:
    quit()