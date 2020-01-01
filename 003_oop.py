

class MyFirstClass:
    def __init__(self):
        pass


class Cup:
    # Class object attribute - same for any instance of this class
    # Note that 'category' is not prefixed by 'self' because attribute applies to ALL instances
    category = 'liquid holder'

    def __init__(self, material, state):
        self.material = material
        self.state = state

    def empty(self):
        self.state = 'empty'

    def fill(self):
        self.state = 'full'

    def print_current_state(self):
        print("This cup is made of {} and is currently {}. Like all cups, it is a {}."
              .format(self.material, self.state, Cup.category))


class Animal:
    def __init__(self, name):
        self.name = name
        # print("Animal CREATED")

    def what_am_i(self):
        raise NotImplementedError("Subclass must implement this method")

    def eat(self):
        print("{} is eating like an animal.".format(self.name))


class Dog(Animal):
    # NOTE: Notice that Dog does not need to supply an __init__ method unless we want to change behaviour from Animal
    # def __init__(self, name):
    #     Animal.__init__(self, name)
    #     print("Dog CREATED")

    def what_am_i(self):
        print("I am a dog and my name is {}. WOOF!".format(self.name))

    # return string representation of this class instance
    def __str__(self):
        return "{} the Dog".format(self.name)

    # return 'length' representation of this class instance
    def __len__(self):
        return len(self.name)

    # Python has destructors
    def __del__(self):
        print("{} has been put down... YOU MONSTER!".format(self.name))


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        # print("Cat CREATED")

    def what_am_i(self):
        print("I am a cat and my name is {}. MEOW!".format(self.name))

    # return string representation of this class instance
    def __str__(self):
        return "{} the Cat".format(self.name)

    # return 'length' representation of this class instance
    def __len__(self):
        return len(self.name)

    # Python has destructors
    def __del__(self):
        print("{} has been sent away to live on a farm.".format(self.name))


my_first_instance = MyFirstClass()
print(type(my_first_instance))
my_cup_a = Cup('glass', 'empty')
my_cup_b = Cup('stainless steel', 'full')
my_cup_c = Cup('plastic', 'half-full')
print(type(my_cup_a))
print('My cups are made of | a: {} | b: {} | c: {}'.format(my_cup_a.material, my_cup_b.material, my_cup_c.material))
print('Cup category: {}'.format(Cup.category))
print('Cup A is made of {} and is currently {}'.format(my_cup_a.material, my_cup_a.state))
my_cup_a.fill()
print('Cup A is now currently {}'.format(my_cup_a.state))
my_cup_a.empty()
print('Cup A is now currently {}'.format(my_cup_a.state))
for cup in (my_cup_a, my_cup_b, my_cup_c):
    cup.print_current_state()
my_dog = Dog('Otto')
my_cat = Cat('Sparkles')
my_dog.eat()
my_dog.what_am_i()
my_cat.eat()
my_cat.what_am_i()
print(my_dog)
print(my_cat)
print(len(my_dog))
print(len(my_cat))
# This is how to remove an object reference from memory
del my_dog
del my_cat
