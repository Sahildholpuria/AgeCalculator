TGREEN = '\033[94m' #Colour For The Text

print(TGREEN + "Developed By Sahil Dholpuria")

BirthYear = int(input("Enter Your Birth Year : ")) #get input from the user and convert into Integer
CurrentYear = int(input("Enter Current Year : "))

Age = CurrentYear - BirthYear

print("Your Age is " + str(Age))
