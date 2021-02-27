import random
import matplotlib.pyplot as plt
import scipy.stats as stats
#Lembre-se sempre de definir o polígono seguindo a ordem dos vértices (tanto faz ser sentido horário ou anti-horário).

def parouimpar(x):
    '''Assume que x é um número inteiro. Retorna se é par ou ímpar'''
    if x%2==0:
        return 'Par'
    else:
        return 'Ímpar'


def yc(x1,y1,x2,y2,xa):
    '''Calcula onde o raio vertical de xa encontra com a reta (x1,y1)->(x2,y2)'''
    try:
        return y1+((y2-y1)/(x2-x1))*(xa-x1)
    except ZeroDivisionError:
        return True


def local(xa,ya,x1,y1,x2,y2):
    '''Retorna se o ponto(xa,ya) está a esquerda, direita, acima, abaixo ou
entre a reta(x1,y1)->(x2,y2)'''
    if x1<xa and x2<xa:
        return 'Esquerda'
    elif x1>xa and x2>xa:
        return 'Direita'
    elif y1<ya and y2<ya:
        return 'Abaixo'
    elif y1>ya and y2>ya:
        return 'Acima'
    else:
        return 'Entre'


def testar(x,y,vertices):
    '''(x,y) é um ponto qualquer. Testa-se se o ponto está dentro do polígono.
Retorna uma variável booleana. Dentro => True. Fora => False.'''
    cruzamentos=0
    for i in range(len(vertices)):
        try:
            x1,y1=vertices[i][0],vertices[i][1]
            x2,y2=vertices[i+1][0],vertices[i+1][1]
            if local(x,y,x1,y1,x2,y2)=='Esquerda' or local(x,y,x1,y1,x2,y2)=='Direita' or local(x,y,x1,y1,x2,y2)=='Abaixo':
                continue
            elif local(x,y,x1,y1,x2,y2)=='Acima':
                cruzamentos +=1
            else:
                if yc(x1,y1,x2,y2,x)>=y:
                    cruzamentos+=1
                else:
                    continue
        except IndexError:
            continue
    if parouimpar(cruzamentos)=='Par':
        return False
    else:
        return True
  

def limites(v):
    '''Retorna o xmin,xmax,ymin e ymax do vetor.'''
    xmin,xmax,ymin,ymax=v[0][0],0,v[0][1],0
    for i in v:
        if i[0]<xmin: #pegando o xmin e xmax
            xmin=i[0]
        if i[0]>xmax:
            xmax=i[0]
            
        if i[1]<ymin: #pegando o ymin e ymax
            ymin=i[1]
        if i[1]>ymax:
            ymax=i[1]       
    return xmin-0.1*xmin,xmax+0.1*xmax,ymin-0.1*xmin,ymax+0.1*ymax
    
    
def jogar(poligono,n=5000,grafico=True):
    '''Joga n agulhas do método de Monte Carlo sobre o polígono definido. Retorna a área encontrada.
\nSe grafico=True, plota um gráfico (recomendável caso queira saber se definiu o polígono corretamente).'''
    v=poligono.copy()
    v.append(v[0]) #polígono=[[x1,y1],[x2,y2],...,[xn,yn],[x1,y1]]
    xmin,xmax,ymin,ymax=limites(v) 
    n=int(n)
    dentro=0
    dentrox,dentroy=[],[]
    forax,foray=[],[]
    for agulhas in range(n):
        x=random.uniform(xmin,xmax)
        y=random.uniform(ymin,ymax)
        if testar(x,y,v):
            dentro+=1
            if grafico:
                dentrox.append(x)
                dentroy.append(y)
        else:
            if grafico:
                forax.append(x)
                foray.append(y)
    area=((xmax-xmin)*(ymax-ymin))*dentro/n

    if grafico==True:
        fig, ax = plt.subplots(1)
        ax.scatter(dentrox, dentroy, c='black', alpha=0.8, edgecolor=None,marker='.')
        ax.scatter(forax, foray, c='silver', alpha=0.6, edgecolor=None,marker='.')
        ax.set_aspect('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.annotate('Área='+str(round(area,4)),xycoords='axes fraction',xy = (1.05, 0.8))
        plt.show()
    return area


def ts(alpha,gl):
    '''Retorna o valor de t-student para tal alpha e tal g.l..'''
    return stats.t.ppf(1-(alpha/2), gl)


def estimativa(v,n,series,printar=True): 
    '''Joga n agulhas do método de Monte Carlo sobre o polígono definido pelo vetor de vérices v series vezes. Retorna a área encontrada com o desvio-padrão e intervalo de confiança.'''
    est=[]
    for i in range(series):
        est.append(jogar(v,n,False))
    desvio=stats.tstd(est)
    est_atual=sum(est)/series
    IC= ts(0.05,series-1)*(desvio/(series**0.5))
    if printar==True:
        print('Estimativa=',str(round(est_atual,5))+'+/-'+str(round(IC,5))+'\nDev. padrão='+str(round(desvio,5))+'\nAgulhas='+str(n)+'\n-----------------------------')
    return(est_atual,desvio,IC)


def area(v,precisao=1,series=20,printar=True):
    '''Joga n agulhas do método de Monte Carlo sobre o polígono definido pelo vetor de vérices v _series_ vezes. Retorna a área encontrada com o desvio-padrão e intervalo de confiança. 
\nSe printar=True mostra os dados de forma mais agradável.  '''
    n=1000
    Incerteza=precisao
    while Incerteza>=precisao:
        est,desvio,IC=estimativa(v,n,series,printar)
        Incerteza=100*(IC/est) 
        n*=2
    return est,IC
