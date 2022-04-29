with open("automato.txt","r") as arquivo: #abrir arquivo automato
  alfabeto = arquivo.readline().split() #armazanar 1 linha na varivavel alfabeto
  estados = arquivo.readline().split() #armazanar 2 linha na varivavel estado
  estadoInicial = arquivo.readline().split() #armazanar 3 linha na varivavel estadoInicial
  estadosFinais = arquivo.readline().split() #armazanar 4 linha na varivavel estadosFinais
  matriz = []
  
  linha = arquivo.readline().split()  #armazanar 5 linha na varivavel linha
  import sys
  if len(linha) == 0:
       with open("saida.txt","w") as arquivo:
        arquivo.write("Matriz Vazia")
        sys.exit()
  
  while len(linha) > 0:  # cria loop adicionando linhas na matriz
     
        matriz.append(linha) # add a linha na matriz
        linha = arquivo.readline().split() #ler proxima linha e armazenar em linha
     

with open("entrada.txt","r") as arquivo: #abre arquivo para leitura
  entradas = []              
  linha = arquivo.readline().strip()    #Lê a primeira linha retirando espaços
  
  while len(linha) > 0: #cria loop 
    entradas.append(linha) #add linha na matriz entradas
    linha = arquivo.readline().strip() #le proxima linha e armazenar em linha

saida = open("saida.txt", "w") #cria um novot txt (sse ja existir ele vai reescrever)
contagem=0
  
for entr in entradas: #cria um loop para percorrer todas as possiveis entradas
  atual = estadoInicial[0]
  conta=0
  teste=0
    
  for y in entr: #cria loop para percorrer cada elemente de cada entrada
    conta = conta + 1
    nao_aceita= True

  
    for x in range(0,len(estados),1):# Para descobrir a linha da matriz
      if atual == str(estados[x]):
        entr = x   
        
    for x in range(0,len(alfabeto),1): # Para descobrir a coluna da matriz
      if y == alfabeto[x]:
        coluna = x
        
    for j in alfabeto: #para percorrer o alfabeto, e testar se nao tem alguma entrada incorreta
      if y == j :
        teste= teste + 1
        
    if(teste < conta):       
      nao_aceita= False
      atual = False #localizar dentro da matriz o proximo estado
      #print("erro")
      break

    if nao_aceita == True:
      atual = matriz[entr][coluna] #localizar dentro da matriz o proximo estado
    
  for i in estadosFinais:  #comparar estado atual com o final, e ver se aceita
    
    if i == atual:
      contagem+=1
      with open("saida.txt","a") as arquivo:
        arquivo.write(str(contagem)+" = "+"ACEITO\n")
        
    else:
      contagem+=1
      with open("saida.txt","a") as arquivo:
        arquivo.write(str(contagem)+" = "+"NAO ACEITO\n")
    
 
