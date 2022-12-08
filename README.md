# INTRODUCCIÓN
A continuación veras un repositorio al cual le asigné el nombre de Refinando código correspondiente a la tarea PP5 del cuso introducción a la programación. En esta ocasión estamos trabajando con la calidad de los códigos por lo que nuestro objetivo principal es limpiar el código usando una herramienta que aprendimos en clase que es pylint y pytest y a la vez vamos a crear un nuevo repositorio en GitHub que luego clonaremos. 

# REFACTORIZACIÓM
Después que ya habíamos hecho los pasos anteriores lo que prosiguio fue en crear varias funciones, de las cuales la primera consistió en una función que debía de recibir la ruta de archivo de costos como entrada y debía de devolver una lista con los costos en formato númerico. Después había que crear otra que recibía la lista de los costos como entraada y devolvía el precio total y por último había que crear otra que llamaba a las anteriores para luego imprimir el precio de los regalos en pantalla. Después que teníamos esa parte, debímos de incluir un entry point desde donde sed debía llamar a la función principal. 

# LIMPIEZA
En esta ocasión debimos de usar pylint para poder limpiar nuestro código y a base de esto poder editarlo y conseguir una buena puntuación, con respecto a esta parte casi la mayoría de las cosas que no estaban correctas era porque había que agregar docstrings a las funciones y agregar datos, para poder cumplir con esta parte había que buscar los estándares PEP8 para poder comenzar a arreglar.

# GESTIÓN DE ERRORES 
* CONTROL DE ERRORES *
En esta parte los errores que más me ocuparon  que salieron fue porque tenía errores con la identación pero eso se resolvió analizando el código y en la creación de la que se suponía que debía de ser mi función principal en donde no me estaba imprimiendo la respuesta correcta pero esto después se arregló ya que la segunda función entonces tomo como parámetro la primera función. También otro error fue que al usar with open () para poder abrir el archivo que teníamos con los precios pero para solucionar esto solo debíamos de cambiar el formato de la función.

* PRUEBAS UNITARIAS *
Para esto utilicé pylest, en donde una era para ver si el costo total era correcto, había otra que era para ver si la lista de los precios era correcta y para reconfirmar que la función nos devolvía al resultado de las otras dos que ya había hecho. 

  # CONTROL DE VERSIONES
  * Enlace permanente al respitorio de GitHub:

https://github.com/peralttanicole/gift_costs.txt 


  
  * Captura de pantalla