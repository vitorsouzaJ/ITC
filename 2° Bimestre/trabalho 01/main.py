
with open("automato.txt","r") as arquivo: #abrir arquivo automato
  estados  = arquivo.readline().split() #armazanar 1 linha na varivavel estados 
  alfabeto = arquivo.readline().split() #armazanar 2 linha na varivavel alfabeto 
  estadoInicial = arquivo.readline().split() #armazanar 3 linha na varivavel estadoInicial
  estadosFinais = arquivo.readline().split() #armazanar 4 linha na varivavel estadosFinais
  matriz = []
  x = arquivo.readline().split()  #armazanar 5 linha na varivavel linh

  while len(x) > 0:
    linha = []
    for i in x:
       
        i = i.split(",")
        linha.append(i)
    matriz.append(linha)
    x = arquivo.readline().split()

with open("entrada.txt","r") as arquivo: #abre arquivo para leitura
  entradas = []              
  linha = arquivo.readline().strip()    #Lê a primeira linha retirando espaços
  
  while len(linha) > 0: #cria loop 
    entradas.append(linha) #add linha na matriz entradas
    linha = arquivo.readline().strip() #le proxima linha e armazenar em linha

saida = open("saida.txt", "w") #cria um novot txt (sse ja existir ele vai reescrever)



saida = open("saida.txt", "w")
contagem=0






#Caminhando Linha entrada
for linhaEntrada in entradas:
    copias = estadoInicial
    
    #Caminhando digito linha entrada
    for digitoLinhaEntrada in linhaEntrada:
    
        #Descobrir valor coluna
        valorColuna = alfabeto.index(digitoLinhaEntrada)
        
        copiasNova = copias.copy()
        #Caminhando copias
        for valorIndexCopia, valorCopia in enumerate(copias):
                      
            #Descobrir valor linha
            valorLinha = estados.index(valorCopia)

          
            atual = matriz[valorLinha][valorColuna]
           

            #Verificar se posição na matriz não é nulo
            if atual.count("*") == 0:
                
                #Verificar se posição na matriz é de apenas um estado
                if len(atual) == 1:
                    copiasNova[valorIndexCopia] = atual[0]
                
                else:
                    for valorIndexAtual, valorAtual in enumerate(atual):
                        if valorIndexAtual == 0:
                            copiasNova[valorIndexCopia] = valorAtual
                        else:
                            copiasNova.append(valorAtual)
                           
      
            if matriz[valorLinha][len(alfabeto)][0] != "*":
                copiasNova.append(matriz[valorLinha][len(alfabeto)][0])         
        copias = []                    
        copias = copiasNova
      
    contagem+=1    
    try:
      
      if copias.index(estadosFinais[0]):
        with open("saida.txt","a") as arquivo:
           arquivo.write("N°"+str(contagem)+" = "+"ACEITO\n") 
    except:
      
      with open("saida.txt","a") as arquivo:
        arquivo.write("N°"+str(contagem)+" = "+"NAO ACEITO\n")
    
                





