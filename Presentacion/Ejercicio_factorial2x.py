def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

def combinatoria(valor_n,valor_m):
    nf=factorial(valor_n)
    mf=factorial(valor_m)
    nmf=factorial(valor_n-valor_m)
    combinaciones=nf/(mf*nmf)
    return combinaciones

valor_n=int(input("ingrese valor-n: "))
valor_m=int(input("ingrese valor-m: "))
valor_p=int(input("ingrese valor-p: "))
valor_q=int(input("ingrese valor-q: "))

imaginario0=(combinatoria(valor_n,valor_m)*combinatoria(valor_p,valor_q))/ (combinatoria(valor_n,valor_p)+ combinatoria(valor_m,valor_q))

print(imaginario0)