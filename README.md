# fetch_movie
Análisis del funcionamiento del script:

El script movie_fetcher.py se encarga de descargar los detalles de las 250 mejores películas en IMDb, extraer su información y guardarla en un archivo CSV.

Entrada: La entrada del script es una solicitud HTTP a la página web de IMDb para descargar la lista de las 250 mejores películas.

Procesamiento: Después de descargar la página web, se utiliza el módulo Beautiful Soup para analizar la página web y extraer la información relevante de las películas, como título, año, elenco, calificación, votos y enlace. Luego, se almacena esta información en una lista de diccionarios y finalmente se escribe la información en un archivo CSV.

Salida: La salida del script es un archivo CSV que contiene información detallada de las 250 mejores películas de IMDb.

S - Single Responsibility:
Cada método, clase o módulo debe tener una sola responsabilidad y hacer solo una cosa.

O - Open Closed Principle:
El código debe ser abierto para la extensión, pero cerrado para la modificación. Esto significa que se deben agregar nuevas funcionalidades sin cambiar el código existente.

L - Liskov Substitution Principle:
Los objetos de una clase base deben ser reemplazables por objetos de sus subclases sin afectar la funcionalidad del programa.

I - Interface Segregation Principle:
Las interfaces deben ser lo suficientemente específicas para cada cliente y no deben imponer métodos innecesarios a los clientes.

D - Dependency Inversion:
El código debe depender de abstracciones, no de implementaciones concretas.
