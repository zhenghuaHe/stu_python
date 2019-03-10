#!/esr/bin/python3
#-*- coding:utf-8 -*-


#子類可以繼承多個父類的屬性和方法
class Animai(object):
    pass

#哺乳類
class Mammal(Animai):
    pass

class Runnable(object):
    def run(self):
        print("Running...")

class  Flyable(object):
    def fly(self):
        print("Flying...")
#鳥類
class Bird(Animai):
    pass


class  Dog(Mammal,Runnable):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird):
    pass


