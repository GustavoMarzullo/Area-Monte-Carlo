Calcula a área de um polígono por Monte Carlo. 

## Como usar
	
	1. Instale as bibliotecas matplotlib.pyplot e scipy
	2. Rode o código via terminal/cmd com 'python -i MCP.py' ou 'python3 -i MCP.py'
	3. Defina os vértices de seu polígono como polígono=[[x1,y1],[x2,y2],...,[xn,yn]], sempre seguindo a ordem deles (tanto faz ser sentido horário ou anti-horário).
	4. Rode a função que desejar.
	
## Funções disponíveis:

__jogar(poligono,n,grafico=True)__

Joga n agulhas do método de Monte Carlo sobre o polígono definido. Retorna a área encontrada.
Se _grafico=True_, plota um gráfico (recomendável caso queira saber se definiu o polígono corretamente).

__estimativa(v,n,series,printar=True)__

Joga n agulhas do método de Monte Carlo sobre o polígono definido pelo vetor de vérices v _series_ vezes. Retorna a área encontrada com o desvio-padrão e intervalo de confiança. 
Se _printar=True_ mostra os dados de forma mais agradável. 

__area(v,precisao=1,series=20,printar=True)__

Vai aumentando o n da função _estimativa_ até chegar na precisão relativa(%) desejada. 

