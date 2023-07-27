import os 
#comando para importar a biblioteca "os"

n = int(input("Digite um numero: "))
#input para receber o numero que sera atribuido a variavel "n"

for kkj in range(1, n+1):
    #for para percorrer a lista de forma crescente 
    if kkj % 3 == 0 and kkj % 5 == 0:
    #if para definir se o numero é divisivel por 3 e 5
        print("SenaiJundiai")
    #print para caso o numero seja divisivel por 3 e 5
    elif kkj % 3 == 0:
    #elif para definir se o numero é divisivel por 3
        print("Senai")
    #print para caso o numero seja divisivel por 3
    elif kkj % 5 == 0:
    #elif para definir se o numero é divisivel por 5
        print("Jundiai")
    #print para caso o numero seja divisivel por 5
    else:
        print(kkj)
    #else para caso o numero não cumpra com nunhum dos requisitos acima
    
os.system("pause")
#comando para pausar o terminal

