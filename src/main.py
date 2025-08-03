# Importamos la interfaz por consola
from console import ConsoleUI


def main():
    # Se crea la aplicación
    app = ConsoleUI()

    # Se inicia el programa
    app.run()


# Este bloque asegura que el programa
# solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()

