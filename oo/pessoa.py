# classe é o que define como os objetos se comportam
class Pessoa:
    def cumprimentar(self): # definir um método. O método pertence a uma classe, atralado a um objeto
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
# método é uma função que pertence à classe