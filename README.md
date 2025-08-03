# Notebook

Esta es una aplicación de práctica para conceptos de OOP en Python. La aplicación es un cuaderno de notas simple con las siguientes características:

- Agregar una nota con un título, el texto de la nota y la importancia de la nota (HIGH, MEDIUM, LOW). 
El sistema debe asignar un identificador único a cada nota.
- Listar todas las notas.
- Agregar etiquetas a las notas.
- Listar todas las notas importantes (Las que tienen importancia HIGH o MEDIUM).
- Eliminar una nota por su identificador.
- Mostrar notas por etiqueta.
- Mostrar la etiqueta con más notas.

Tu tarea es implementar las clases del modelo en el archivo `src/notebook.py` y las
clases de la interfaz de usuario en el archivo `src/console.py`. 

Considera los siguientes aspectos para la implementación:

## 1. Clase `Note`

- La clase debe tener las siguientes constantes:

  - `HIGH` de tipo `str` con valor `'HIGH'`.
  - `MEDIUM` de tipo `str` con valor `'MEDIUM'`.
  - `LOW` de tipo `str` con valor `'LOW'`.

  Puedes consultar el documento de estudio **Conceptos de POO** para más información sobre constantes en clases.
  O tambiénn puedes consultar en Internet sobre constantes en clases en Python.


- La clase debe tener los siguientes atributos:

  - `code` de tipo `str` inicializado con un parámetro en el constructor.
  - `title` de tipo `str` inicializado con un parámetro en el constructor.
  - `text` de tipo `str` inicializado con un parámetro en el constructor.
  - `importance` de tipo `str` inicializado con un parámetro en el constructor.
  - `creation_date` de tipo `datetime`. Este atributo **no** se inicializa con parámetro en el constructor y 
  tiene como valor por defecto la fecha y hora actual.
      > **Consejo**: Puedes usar la función `datetime.now()` del módulo `datetime` para obtener la fecha y hora actual.
  - `tags` de tipo `list[str]`. Este atributo **no** se inicializa en el constructor y tiene como valor por defecto una lista vacía.


- La clase debe tener un método de instancia `add_tag` que recibe un parámetro `tag` de tipo `str` y agrega la etiqueta al atributo `tags`. 
El método no debe agregar la etiqueta si ya está en el atributo `tags`.


- La clase debe tener un método de instancia `__str__` que devuelve un `str` con el siguiente formato:

    ```python
    Date: {creation_date}
    {title}: {text}
    ```

    Donde `{creation_date}` debe ser reemplazado con la fecha de creación de la nota y `{title}` y `{text}` deben ser 
    reemplazados con el título y texto de la nota.

## 2. Clase `Notebook`

- La clase debe tener un atributo `notes` de tipo `list[Note]`. No debe ser inicializado con un parámetro en el 
constructor y debe tener como valor por defecto una lista vacía.


- La clase debe tener un método de instancia `add_note` que recibe los parámetros `title` de tipo `str`, `text` de tipo 
`str` e `importance` de tipo `str` y devuelve un `int` con el código de la nota. El método debe hacer lo siguiente:

  - Generar un nuevo código para la nota. El código debe ser un entero único mayor que 0. Puedes usar la función `len` 
  para obtener el número de notas y agregar 1 para obtener el nuevo código. **Debes tener cuidado de no agregar un código
  repetido**.
  - Crear un nuevo objeto `Note` con los parámetros recibidos y el código generado.
  - Agregar la nueva nota al atributo `notes`.
  - Devolver el código de la nota.

- La clase debe tener un método de instancia `delete_note` que recibe el parámetro `code` de tipo `int`. 
  El método debe eliminar la nota con el código recibido como parámetro del atributo `notes`.
- La clase debe tener un método de instancia `important_notes` que devuelve una `list[Note]` con las notas que tienen 
  la importancia `HIGH` o `MEDIUM`.
- La clase debe tener un método de instancia `notes_by_tag` que recibe el parámetro `tag` de tipo `str` y devuelve 
  una `list[Note]` con las notas que tienen la etiqueta recibida como parámetro.
- La clase debe tener un método de instancia `tag_with_most_notes` que devuelve un `str` con la etiqueta que 
  aparece más en las notas. Si hay múltiples etiquetas con el mismo número de notas, devuelve la primera 
  etiqueta en orden alfabético.

## 3. Interfaz de usuario

La interfaz de usuario debe tener un menú con las siguientes opciones:

1. Agregar nota
2. Listar notas
3. Agregar etiqueta a nota
4. Listar notas importantes
5. Eliminar nota
6. Mostrar notas por etiqueta
7. Mostrar etiqueta con más notas
8. Salir

Cada opción se debe implementar como un método de una clase que representa la interfaz por consola.

Además, se debe implementar un método que tenga el ciclo principal de la aplicación. El ciclo debe mostrar el menú y
ejecutar la opción seleccionada por el usuario. El ciclo debe terminar cuando el usuario seleccione la opción de salir.

 > **Consejo**: Puedes utilizar una IA como ChatGPT, Copilot, etc. para ayudarte a generar el código de la interfaz.
 > Para esto, puedes copiar la descripción de la interfaz de usuario y adjuntar el archivo con la implementación que 
 > has hecho de las clases del modelo. Recuerda que es importante que revises y trates de entender el código generado 
 > (puedes preguntarle a la IA si no entiendes algo, para que te lo explique).

## 4. Script principal

Crea un script principal en el archivo `main.py` en el cual definas el código necesario para iniciar la 
ejecución de la aplicación.


