https://replit.com/join/vytpgmiduw-luz-valeriaval4

animalitos= input("¿Hay animales para registrar? (si o no): ").lower()

menos2años = 0
entre2y5años = 0
entre5y10años = 0
igualomayor10= 0
si= 0

while animalitos == "si":
    edad= int(input("¿cuantos años tiene el animal?: "))

    if edad < 2:
        menor2años += 1
    elif 2 <= edad < 5:
        entre2y5años += 1
    elif 5 <= edad < 10:
        entre5y10años += 1
    elif edad >= 10:
        igualomayor10 += 1

    si += 1
    animalitos = input("¿Hay más animales para registrar? (si o no): ").lower()

if si > 0:
    p_menor_a_2 = (menora2 / ta) * 100
    p_entre_2_y_5 = (entre2y5años / ta) * 100
    p_entre_5_y_10 = (entre5y10años / ta) * 100
    p_mayor_o_igual_a_10 = (igualomayor10 / ta) * 100

    print(f"Número de animales registrados: {ta}")  
    print(f"Menor a 2 años: {menor2años} ({p_menor_a_2}% del total)")
    print(f"Entre 2 y 5 años: {entre2y5años} ({p_entre_2_y_5}% del total)")
    print(f"Entre 5 y 10 años: {entre5y10años} ({p_entre_5_y_10}% del total)")
    print(f"Mayor o igual a 10 años: {igualomayor10} ({p_mayor_o_igual_a_10}% del total)")
