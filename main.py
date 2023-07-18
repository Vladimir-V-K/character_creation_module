# Импортируем функцию стандартного модуля random.
from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    DRIEF_DESC_CHAR_BUFF = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name

    #  Объявляем метод атаки.
    def attack(self):
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанес противнику урон, равный '
                f'{value_attack}.')

    #  Объявляем метод защиты.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUF}".')

    #  Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.DRIEF_DESC_CHAR_BUFF}.'


class Warrior(Character):
    DRIEF_DESC_CHAR_BUFF = (' дерзкий воин ближнего боя. '
                            'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    DRIEF_DESC_CHAR_BUFF = (' находчивый воин дальнего боя. '
                            'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    DRIEF_DESC_CHAR_BUFF = (' могущественный заклинатель. '
                            'Черпает силы из природы. веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


warrior = Warrior('Кодослов')
print(warrior)
print(warrior.attack())
