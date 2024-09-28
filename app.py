'''Crie uma lista com 15 nomes de cidades e exiba na tela em ordem alfabética. 
 '''

cidades = ["Nova York (EUA)","Tóquio (Japão)","Paris (França)","Londres (Reino Unido)", "Sydney (Austrália)","Berlim (Alemanha)","Roma (Itália)","Cidade do Cabo (África do Sul)","Mumbai (Índia)","São Paulo (Brasil)","Xangai (China)","Toronto (Canadá)","Moscovo (Rússia)","Buenos Aires (Argentina)","Seul (Coreia do Sul)"]

print("\n")

cidades.sort()

# exibindo em ordem alfabética
print("Lista em ordem alfabética: \n")
for cidade in cidades:
    print(cidade)