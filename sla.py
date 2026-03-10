x= int(input("Digite um numero de 1 a 10 para ver a tabuada")) 
for cont in range(1, 11):
    tabu = x * cont
    print (f"{x} X {cont} = {tabu}")