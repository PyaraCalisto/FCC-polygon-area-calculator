#Cria a classe Rectangle e 9 funções a ela,
# duas de uso interno e 7 externas. Usamos
# __init__ é padrão para atribuir os valores
# iniciais à classe e __str__, também padrão
# para modificar a saida de print() da classe.
# outra opção seria usar __repr__()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

#Cria as funções set_width para atribuir o valor
# de width e set_height com o mesmo propósito.

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# Cria a função get_area para calcular a área.

    def get_area(self):
        return self.width * self.height
# Cria a função get_perimeter para calcular o perimetro.

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
# Cria a função get_diagonal para calcular a diagonal.

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)
# Cria a função get_picture para desenhar o retangulo
# com base nos valores de width e height. Também usa a
# condicional if para verificar se um dos lados do
# retangulo é maior do que 50 e retorna uma mensagem
# de erro caso seja.

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        return (("*" * self.width) + "\n") * self.height
# Cria a função get_amount_inside para calcular
# quantos de retangulos menores cabem no retangulo.

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


# Cria a subclasse Square herdando os parametros
# da classe Rectangle, mas usando side para width
# e height.
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
