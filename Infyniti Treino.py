#infinite Treino
#Criador: Rodrigo Oliveira

import random

nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))

dezoito = ["Hoje é dia de treinar, então vai PORRA!Billll!", "Calça o tênis com chulé mesmo e vai treinar!Billlll",
       "Aguenta a pressão que hoje é treino de macho!Billll" , "Enche a garrafa de energético do Kratos e fica maromba igual ele!Billll",
       "Se inspira nas gatas que vão pra lá mostrar que são mais esforçadas que tu!Billll"]
menosdezoito = ["Amigo reza a Deus para se inspirar no treino de hoje",
                "Use todos os equipamentos de treino para não se machucar.",
                "Papai do Céu proteja esse atleta que vai treinar hoje,amém!"]

if(idade >= 18):
    kkk = dezoito
elif(idade < 18):
    kkk = menosdezoito

print("Ok", nome, "sua frase de hoje é :\n", random.choice(kkk))

fechar = input()
if(fechar == "fechar"):
    print("FLW BOM TREINO MONSTRO!BILLLL")


    contador = 200
    while(contador > 0 ):
        print(contador, "FLW BOM TREINO MONSTRO!BILLLL")
         
        contador = contador - 1
       
            
