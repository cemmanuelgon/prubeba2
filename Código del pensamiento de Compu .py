totaldesayuno=0
totalalmuerzo=0
totalcena=0
cantdesayuno = 0
cantalmuerzo=0
cantcena=0
resultado=0
print("Escoge algún menú")
resultado = 0
while True:
    menu = int(input("""
Menú de comida
(1) Desayuno
(2) Almuerzo
(3) Cena
(4) salir
"""))
    if menu == 1:
        print("El menu consta de un plato de hotcakes, bañadas en azúcar glass, nutella, fresas y crema. Q.20.00") 
        print("Cuantos desayunos desea agregar?")
        calculodesayuno = int(input(cantdesayuno))
        totaldesayuno = calculodesayuno * 20
        print("Total de desayuno: Q.",totaldesayuno)
    elif menu == 2:
        print("El plato consta de carne azada, sazonada con cebolla, orégano y con cebolla caramelizada, con acompañamiento de aguacate y papas.Q50.00")    
        print("Cuantos almuerzos desea agregar?")
        calculoalmuerzo = int(input(cantalmuerzo))
        totalalmuerzo = calculoalmuerzo * 20
        print("Total de almuezo: Q.",totalalmuerzo)
    elif menu == 3:
        print("El plato consta de huevos con frijoles acompañados de un embutido a tu elección, café o jugo de naranja.Q25.00")
        print("Cuantas cenas desea agregar?")
        calculocena = int(input(cantcena))
        totalcena = calculocena * 20
        print("Total de cena: Q.",totalcena)
        
    elif menu ==4:
        break    
resultado= totaldesayuno+totalalmuerzo+totalcena
print("el precio a pagar es de: Q", resultado)