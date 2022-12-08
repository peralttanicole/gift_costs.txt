#Nicole A. Peralta
#22-0262
# Refinando codigos
# En este programa lo que hicimos fue refinar un codigo con los estandares establecidos en la clase


# Cree una funcion que me recibia la ruta del archivo de costos como entrada y me devolvia una lista con los costos en formato numérico.

#Nicole A. Peralta
#22-0262
# Refinando codigos
# En este programa lo que hicimos fue refinar un codigo con los estandares establecidos en la clase

# Cree una funcion que me recibia la ruta del archivo de costos como entrada y me devolvia una lista con los costos en formato numérico.

def costs_list():
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archivo:
        gift_costs = list(archivo)
    gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
    archivo.close()  # cerrar el archivo después de usarlo y no ser necesario
    return gift_costs

# Cree una funcion que me recibio la lista de los costos como entrada y devuelva el precio total.

def total(gift_costs):
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  # los costos menores a 1000 no se le agrega impuesto

    return total_price

# Cree una funcion que me llamo a las anteriores para luego imprimir el precio de los regalos en pantalla.
  
def main():
    print(total(costs_list()))