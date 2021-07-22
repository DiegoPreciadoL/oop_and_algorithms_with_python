
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Estoy caminando")


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Estoy moviendome en bicicleta")


def main():
    persona = Persona('Diego')
    persona.avanza()

    ciclista = Ciclista('Diego Ciclista')
    ciclista.avanza()


if __name__ == '__main__':
    main()

