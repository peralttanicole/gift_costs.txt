'''Nicole A. Peralta
22-0262
Refinando codigos
En este programa lo que hicimos fue refinar un codigo con los estandares establecidos en la clase'''

import sys

def lista_costo():
    '''Función que trae la lista de costos del archivo gift_costs.txt'''
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archivo:
        gift_costs = list(archivo)
        try:
            gift_costs = [int(c) for c in gift_costs]  # conversion de strings a int
            archivo.close()  # cierra el archivo despues de ser ejecutado
        except ValueError:
            print('La información debe ser numerico.')
            sys.exit()
    return gift_costs

def sum_tot(gift_costs):
    '''Función que suma los precios de la lista de costos'''
    total_price = 0
    for costo in gift_costs:
        if costo > 1000:
            total_price += costo * 1.16  # calcular impuesto
        else:
            total_price += costo  # sin impuesto los costos menores de 1000
    return total_price

def main():
    '''Función principal que invoca las funciones y gebera el costo total'''
    return print(sum_tot(lista_costo()))

if __name__ == '__main__':
    main()
