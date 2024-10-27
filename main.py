class BigClass:
    PER = 'Тут прописываются переменные класса'
    dict_mess = {}

    # вызывается перед инициализаией класса, используется обычно для проверки, есть уже соединие с чем-то или нет и подобное
    # должен возвращать то, что вернёт класс супер, метод new с переданным имененм класса
    # за место cls можно передавать другой класс
    def __new__(cls, *args, **kwargs):
        # проверки
        return super().__new__(cls)

    # Инициализатор, присваиваются все нужные переменные, вызывается после __new__ при объявление класса
    def __init__(self, name):
        self.name = name
        self.__word1 = 'asdasd'
        self.__word2 = 'asdasd'

    # Вызывает при удаление сборщиком мусора данного класса
    # Лучше не использовать, потому что неизвестно, когда сборщик до него доберётся
    def __del__(self):
        if hasattr(self, 'file'):
            self.file.close()
            print("Файл закрыт")

    # ________________________________ classmethod and staticmethod
    # Используются исходя из названий, первый внутри класса, второй из любого места, вызывается через имя класса,
    # можно не передавать экземпляр класса
    @classmethod
    def add_message(cls, msg):
        cls.dict_mess[id(msg)] = msg

    @staticmethod
    def check_card_number(number):
        number = number.replace("-", "")
        if len(number) != 16 or not number.isdigit():
            return False
        else:
            return True

    # Три типа переменных, публичные - self.name
    # приватные self._name и защищённые, к последним из вне класса по имени доступа нет
    # Для получения доступа к ним используют: Функции геттеры и сеттеры, свойства property, а также дескрипторы(дата и нон-дата)

    # геттер, сеттер
    def get_word(self):
        # Можно добавить условия
        return self.__word1

    def set_word(self, value):
        # Тут можно проверки прописать
        self.__word1 = value

    # property
    # Два варианта использованя: 1 через перечисление, второй через декораторы(на самом деле оба через декораторы)
    #1
    @property
    def word(self):
        return self.__word1

    @word.setter
    def word(self, value):
        self.__word1 = value

    @word.deleter
    def word(self):
        del self.__word1

    # Третий вариант дескриптор
    # В начале основного класса прописывается, что переменная является таким-то классом name = StringValue()

    #class StringValue:
    #    def __init__(self, min_length=2, max_length=50):
    #        self.min_length = min_length
    #        self.max_length = max_length

    #    def __set_name__(self, owner, name):
    #        self.name = "_" + name

    #    def __set__(self, instance, value):
    #        if type(value) == str:
    #            if self.min_length <= len(value) <= self.max_length:
    #                instance.__dict__[self.name] = value

    #    def __get__(self, instance, owner):
    #        return instance.__dict__[self.name]


    def __getattribute__(self, item):
        # метод вызывается при обращение к атрибуту класса pt.name
        return super().__getattribute__(self, item)

    def __getattr__(self, item):
        # метод вызывается, когда вызываемый объект не существует
        return False

    def __setattr__(self, key, value):
        # перед определением переменной, можно реализовать проверку на корректность данных
        super().__setattr__(self, key, value)

    def __delattr__(self, item):
        # Вызывается перед удалением атрибута, можно реализовывать проверки
        super().__delattr__(self, item)

    def __call__(self, *args, **kwargs):
        # Данный магический метод вызывается, когда объекту ставятся скобки, то есть объект класса вызывается
        # как функция пример obj()
        return self.name * 3

    def __str__(self):
        # пользовательское отображение названия класса в методах print() and str()
        return self.name

    def __repr__(self):
        # отображение для разработчиков
        return self.__class__

    def __len__(self):
        # что объект класса возвращает на вызов функции len()
        return len(self.name)

    def __abs__(self):
        # Логика поведения при вызове функции abs для объекта класса
        return abs(len(self.name))


    # математические методы, у всегх есть вариант с i или r в начале, определяющий с какой стороны находится основной объект
    def __add__(self, other):
        # логика сложения
        return len(self.name) + other

    def __sub__(self, other):
        # логика сложения
        return len(self.name) - other


    def __mul__(self, other):
        # Логика умножения
        return len(self.name) * other

    def __truediv__(self, other):
        # Логика деления
        return len(self.name) / other

    def __floordiv__(self, other):
        # Логика целочисленного деления
        return len(self.name) // other

    def __mod__(self, other):
        # Логика остатка от деления
        return len(self.name) % other


    # Операторы сравнения, если ne не определён, то вызывается eq и определяется not
    def __eq__(self, other):
        # вызывается при равенстве
        return self.name == other

    def __ne__(self, other):
        # вызывается при знаке неравенства !=
        return self.name != other

    def __lt__(self, other):
        # Вызывается при знаке меньше
        return self.name < other

    def __le__(self, other):
        # Вызывается при знаке меньше или равно
        return self.name <= other

    def __gt__(self, other):
        # вызывается при знаке больше
        return self.name > other

    def __ge__(self, other):
        # для операторов больше или равно
        return self.name >= other

    # Если не определён метод hash, То определяется по методу Equety, сравнения
    def __hash__(self):
        # возвращает хеш класса
        return hash(self.name)



