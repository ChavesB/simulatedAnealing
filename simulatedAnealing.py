# =============================================================================
# INICIO DO PROGRAMA - Autor: Bruno Cesar Alves Costa
# =============================================================================

#Digitar no console do spyder ou IPython %matplotlib auto
import matplotlib.pyplot as plt
import numpy as np

def Direcao(pi, pj, pk):
    x1 = pk[0] - pj[0]
    y1 = pk[1] - pj[1]
    x2 = pj[0] - pi[0]
    y2 = pj[1] - pi[1]
    
    return (x1*y2 - x2*y1)

def onSegment(pi, pj, pk):
    if (min(pi[0],pj[0]) <= pk[0] <= max(pi[0],pj[0])):
        return True
    else: return False

def Intersect(p1, p2, p3, p4):
    d1 = Direcao(p3, p4, p1)
    d2 = Direcao(p3, p4, p2)
    d3 = Direcao(p1, p2, p3)    
    d4 = Direcao(p1, p2, p4)
    
    if (((d1>0 and d2>0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0))):
        return True
    elif (d1==0 and onSegment(p3, p4, p1)):
        return True
    elif (d2==0 and onSegment(p3, p4, p2)):
        return True
    elif (d3==0 and onSegment(p1, p2, p3)):
        return True
    elif (d4==0 and onSegment(p1, p2, p4)):
        return True
    else:
        return False

def Energia(psx, psy):
    ax = np.array(psx)
    ay = np.array(psy)
    dx = ax[1:-1] - ax[:-2]
    dy = ay[1:-1] - ax[:-2]
    return np.sqrt(np.sum(dx**2) + np.sum(dy**2))

def Perturba(x, y, p):
    
    # Inversão #
    
    i,j = np.random.randint(0, len(x) - 1, size=2)
    
    if i>j:
        i,j = j,i
    
    p[i:j+1] = p[j:i-p.size-1:-1]
    x[i:j+1] = x[j:i-x.size-1:-1]
    y[i:j+1] = y[j:i-y.size-1:-1]
    
    # Translação #
    
    i,j = np.random.randint(0, len(x) - 1,size=2)    

    if i>j:
        i,j = j,i
        
    k = np.random.randint(0, len(x) - 1)
    
    xtemp = x.copy()
    ytemp = y.copy()
    ptemp = p.copy()
    
    if k<i:
        p[k:k+j-i+1] = ptemp[i:j+1]
        p[k+j-i+1:j+1] = ptemp[k:i]
        x[k:k+j-i+1] = xtemp[i:j+1]
        x[k+j-i+1:j+1] = xtemp[k:i]
        y[k:k+j-i+1] = ytemp[i:j+1]
        y[k+j-i+1:j+1] = ytemp[k:i]
    elif k>j:
        p[i:i+k-j]= ptemp[j+1:k+1]
        p[i+k-j:k+1] = ptemp[i:j+1]
        x[i:i+k-j]= xtemp[j+1:k+1]
        x[i+k-j:k+1] = xtemp[i:j+1]
        y[i:i+k-j]= ytemp[j+1:k+1]
        y[i+k-j:k+1] = ytemp[i:j+1]
    else:
        p[k:] = ptemp[i:i+ptemp.size-k]
        p[:k-i] = ptemp[i+ptemp.size-k:]
        p[k-i:k] = ptemp[:i]
        
        x[k:] = xtemp[i:i+xtemp.size-k]
        x[:k-i] = xtemp[i+xtemp.size-k:]
        x[k-i:k] = xtemp[:i]
        
        y[k:] = ytemp[i:i+ytemp.size-k]
        y[:k-i] = ytemp[i+ytemp.size-k:]
        y[k-i:k] = ytemp[:i]


    # Troca #
    
    i,j = np.random.randint(0, len(x) - 1, size=2)
    
    if i>j:
        i,j = j,i
    
    p[i],p[j] = p[j],p[i]
    x[i],x[j] = x[j],x[i]
    y[i],y[j] = y[j],y[i]
    
    ####### Cruzamento de segmentos ########   
    arestas = list(zip(x, y))
    
    i = np.random.randint(0,len(arestas),dtype=int)

    if(i+3<len(arestas)):
        if(Intersect(arestas[i],arestas[i+1],arestas[i+2], arestas[i+3])):
            p[i],p[i+3] = p[i+3],p[i]
            x[i],x[i+3] = x[i+3],x[i]
            y[i],y[i+3] = y[i+3],y[i]
    elif(i+2<len(arestas)):
        if(Intersect(arestas[i],arestas[i+1],arestas[i+2], arestas[0])):
            p[i],p[0] = p[0],p[i]
            x[i],x[0] = x[0],x[i]
            y[i],y[0] = y[0],y[i]
    elif(i+1<len(arestas)):
        if(Intersect(arestas[i],arestas[i+1],arestas[0], arestas[1])):
            p[i],p[1] = p[1],p[i]
            x[i],x[1] = x[1],x[i]
            y[i],y[1] = y[1],y[i]
    else:
        if(Intersect(arestas[i],arestas[0],arestas[1], arestas[2])):
            p[i],p[2] = p[2],p[i]
            x[i],x[2] = x[2],x[i]
            y[i],y[2] = y[2],y[i]
    
    ####### Arestas Concorrentes ########


'''
Inicio do Códigos
'''
plt.close()
plt.ion()
x=np.random.randint(0,30,size=30,dtype=int)
y=np.random.randint(0,30,size=30,dtype=int)
p=np.arange(0,30,1)
xl=list(x)
yl=list(y)
xl.append(xl[0])
yl.append(yl[0])
plt.suptitle("Tempera Simulada Para Problema do Caixeiro Viajante - Processando...\n\n")
plt.subplot(1,2,1)
plt.plot(xl,yl,'c-',xl,yl,'ro') 
plt.title("Configuração Inicial")
Perturba(x,y,p)    
plt.axis([-1,31,-1,31])
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

xl=list(x)
yl=list(y)
xl.append(xl[0])
yl.append(yl[0])
plt.subplot(1,2,2)
plt.plot(xl,yl,xl,yl,'ro')

total = 0

KB=8.61*10**(-5)       #constante de Boltzman
escala=0.1             #escala de redução da temperatura
suc = False
t = 300

e1 = Energia(xl,yl)
plt.title("Energia: "+str(e1))
plt.draw() 
plt.pause(0.00005) 
    
sucesso = 0
fracasso = 0

while total < 10:
    sucesso = 0
    fracasso = 0
    while ( (not(sucesso<=100))|(fracasso<=1000)) and ((sucesso<=100)|(not(fracasso<=1000)) ):
        xcopy = x.copy()
        ycopy = y.copy()
        pcopy = p.copy()                
        Perturba(x, y, p)
        xl=list(x)
        yl=list(y)
        xl.append(xl[0])
        yl.append(yl[0])
        plt.subplot(1,2,2)
        plt.cla()
        plt.plot(xl,yl,xl,yl,'ro')
        e2 = Energia(xl, yl)

        probabilidade = np.exp((e1-e2)/(KB*t))
        probNovoEst = np.random.rand()

        if ((e1-e2)>0 or (probNovoEst < probabilidade)):
            if suc:
                sucesso += 1
            else:
                sucesso = 1
                suc = True

            e1 = e2
            xl=list(x)
            yl=list(y)
            xl.append(xl[0])
            yl.append(yl[0])
            plt.subplot(1,2,2)
            plt.cla()
            plt.plot(xl,yl,xl,yl,'ro')
            plt.title("Energia: "+str(e2))
            plt.draw()

            plt.pause(0.0000005)
        else:
            x = xcopy
            y = ycopy
            p = pcopy
            if suc==False:
                fracasso += 1
            else:
                fracasso = 1
                suc = False
    #fim 1º while
    t = t*(1-escala)
    total += 1
    print(total)
#fim 2º while

plt.suptitle("Tempera Simulada Para Problema do Caixeiro Viajante - Terminou\n\n")
plt.title("Energia: "+str(e1))
plt.draw()

'''
Fim Código
'''
