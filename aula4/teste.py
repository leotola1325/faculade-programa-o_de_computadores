# ler os 5 numeros e falar qual e o maior

nu1 = int(input("digite o numero 1: "))
nu2 = int(input("digite o numero 2: "))
nu3 = int(input("digite o numero 3: "))
nu4 = int(input("digite o numero 4: "))
nu5 = int(input("digite o numero 5: "))

if nu1>nu2 and nu1>nu3 and nu1>nu4 and nu1>nu5:
    print(f"o numero 1: {nu1} e o maior")
elif nu2>nu1  and nu2>nu3 and nu2>nu4 and nu2>nu5:
    print(f"o numero 2: {nu2} e o maior") 
elif nu3>nu1 and nu3>nu2 and nu3>nu4 and nu3>nu5:
    print(f"o numero 3: {nu3} e o maior") 
elif nu4>nu1 and nu4>nu2 and nu4>nu3 and nu4>nu5:
    print(f"o numero 4: {nu4} e o maior") 
else: 
    print(f"o numero 5: {nu5} e o maior")





