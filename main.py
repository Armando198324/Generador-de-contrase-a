import random

c = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Dime la longitud de tu contraseña"))
contraseña = ""
for i in range (longitud):
    x = random.choice(c)
    contraseña += x 
print(contraseña)
