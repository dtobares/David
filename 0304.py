
#ESTA ES LA MANERA RECURSIVA
def collatz (n):
    if n==1:
        return 0
    else:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        respuesta=collatz(n)
        return 1+respuesta
collatz(4)
print(collatz(4))




