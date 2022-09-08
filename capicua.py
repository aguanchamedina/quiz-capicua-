from tkinter import mainloop

print("---------------------------------------------")
print("---------------NUMERO-CAPÍCUA----------------")
print("---------------------------------------------")

 #INPUT
num = input("Digite un número de 5 cifras: ") 

#PROCESS
if num == num[::-1]: 
    print("El número si es capícua. ") 
else: 
    print("El número no es capícua. ")

#OUTPUT

mainloop

