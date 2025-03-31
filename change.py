def change():
    expense = 23.75
    money = 100
    change = money-expense
    pesos = int(change)
    centavos = int((change-pesos)*100)
    print(f"Ingresar gasto:")
    print(expense)
    print(f"Dinero recibido")
    print(money)
    print(f"\nVuelto")
    print(f"\nPesos:")
    print(pesos)
    print(f"Centavos:")
    print(centavos)
