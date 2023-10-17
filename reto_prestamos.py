https://replit.com/join/igfpvnjhca-luz-valeriaval4
def f(x): "calculadora de prestamos"
cantidad=float(input("ingrese la cantidad del prestamo   "))
interes=float(input("ingrese la tasa de interes anual   "))
plazo= float(input("ingrese el plazo en años   "))

if interes <= 5 and plazo <= 5:
    print("esto es un prestamo de bajo riesgo")
elif interes > 5 and plazo > 5:
  print("es un prestamo de riesgo moderado")
else:
  print("es un prestamo de alto riesgo")
