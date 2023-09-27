def ageverifier(current_year):
    name = str(input("What's your name? "))
    birth_year = int((input("Type your birth year (e.g. 1999)? ")))
    age = current_year - birth_year

    if age >= 18:
        print("Nice, " + name + "! You can acess our platafform")

    else:
        wait_period =  18 - age
        print ("Sorry, " + name + " you have to wait " + str(wait_period) + " more years to have the acess to our platafform.")



ageverifier(2023)