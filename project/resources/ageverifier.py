import datetime

def ageverifier(birth_year):

    age = datetime.datetime.now().year - birth_year

    if age >= 18:
        return True
    return False


def greetings():
    return "Olá!"