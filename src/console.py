# Importamos el cuaderno y la nota
# para poder usarlos desde la consola
from notebook import Notebook, Note


class ConsoleUI:
    def __init__(self):
        # Se crea el cuaderno que manejará las notas
        self.notebook = Notebook()

    def show_menu(self):
        # Muestra las opciones disponibles al usuario
        print("\n--- NOTEBOOK ---")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")

    def add_note(self):
        # Pide datos al usuario y crea una nota
        title = input("Título: ")
        text = input("Texto: ")
        importance = input("Importancia (HIGH, MEDIUM, LOW): ")
        code = self.notebook.add_note(title, text, importance)
        print(f"Nota agregada con código {code}")

    def list_notes(self):
        # Muestra todas las notas existentes
        for note in self.notebook.notes:
            print(note)

    def add_tag_to_note(self):
        # Agrega una etiqueta a una nota específica
        code = int(input("Código de la nota: "))
        tag = input("Etiqueta: ")

        for note in self.notebook.notes:
            if note.code == code:
                note.add_tag(tag)
                print("Etiqueta agregada")
                return

        print("Nota no encontrada")

    def list_important_notes(self):
        # Muestra solo las notas importantes
        for note in self.notebook.important_notes():
            print(note)

    def delete_note(self):
        # Elimina una nota usando su código
        code = int(input("Código de la nota a eliminar: "))
        self.notebook.delete_note(code)
        print("Nota eliminada")

    def show_notes_by_tag(self):
        # Muestra las notas que tengan cierta etiqueta
        tag = input("Etiqueta: ")
        notes = self.notebook.notes_by_tag(tag)

        if not notes:
            print("No hay notas con esa etiqueta")
        for note in notes:
            print(note)

    def show_tag_with_most_notes(self):
        # Muestra la etiqueta más usada
        tag = self.notebook.tag_with_most_notes()
        if tag:
            print(f"Etiqueta con más notas: {tag}")
        else:
            print("No hay etiquetas")

    def run(self):
        # Ciclo principal del programa
        # Se repite hasta que el usuario decida salir
        while True:
            self.show_menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                self.add_note()
            elif option == "2":
                self.list_notes()
            elif option == "3":
                self.add_tag_to_note()
            elif option == "4":
                self.list_important_notes()
            elif option == "5":
                self.delete_note()
            elif option == "6":
                self.show_notes_by_tag()
            elif option == "7":
                self.show_tag_with_most_notes()
            elif option == "8":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
