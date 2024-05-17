from datetime import datetime, date


class Human(object):  # Toda classe herda object.
    planet = 'Earth'  # Será usado por todos os objetos da classe.

    # Self: Permite referenciar coisas da própria classe.
    # Método Construtor: Quando você cria uma variável daquela classe o método contributor é ativo.

    def __init__(self, name=None, birth_date=None):  # Construtor da classe.
        self.name = name
        self.birth_date = birth_date
        # Atributo privado __age.

    @property  # Decorator - Permite usar a função como propriedade.
    def age(self):
        today = datetime.now().date()
        difference = today - self.birth_date
        return int(difference.days / 365)

    @staticmethod  # Decorator - Permite usar a função sem o self.
    def human_lives_in():
        return Human.planet


h1 = Human('Antônio', date(2005, 1, 17))
print(h1.name, h1.birth_date, h1.age, h1.human_lives_in(), Human.human_lives_in())
