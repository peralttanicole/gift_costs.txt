# Cree una funcion que me recibia la ruta del archivo de costos como entrada y me devolvia una lista con los costos en formato numérico.

def ruta_archivo(): 
  with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
  gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
  return gift_costs
  
# Cree una funcion que me recibio la lista de los costos como entrada y devuelva el precio total.
  
def devolver_precio(gift_costs):
  gift_costs= ruta_archivo ()
  total_price = 0
  for cost in gift_costs:
    if cost > 1000:
      total_price += cost * 1.16  # agrega impuestos
    else:
       total_price += cost
  return total_price
  
# Cree una funcion que me llamo a las anteriores para luego imprimir el precio de los regalos en pantalla.
  
def principal():
  gift_costs= ruta_archivo ()
  total_price= devolver_precio (gift_costs)
  print(total_price)

if __name__ == '__main__':
  principal()