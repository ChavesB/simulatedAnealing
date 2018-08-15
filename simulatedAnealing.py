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

def intersec2d(pi1,pf1,pi2,pf2):
    
    det = (pf2[0]-pi2[0])*(pf1[1]-pi1[1]) - (pf2[1]-pi2[1])*(pf1[0] - pi1[0])
    
    if(det == 0):
        return 0,0
    
    s = ((pf2[0]-pi2[0])*(pi2[1]-pi1[1])-(pf2[1]-pi2[1])*(pi2[0]-pi1[0]))/det
    t = ((pf1[0]-pi1[0])*(pi2[1]-pi1[1])-(pf1[1]-pi1[1])*(pi2[0]-pi1[0]))/det
    
    return s,t

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
    
    ####### Intersecção de retas ########
    for b in range(0,3):
        i = np.random.randint(0,len(arestas),dtype=int)
    
        j=i
        
        while(i==j or j==i-1 or i-1==j+1):
            j = np.random.randint(0,len(arestas),dtype=int)
            if(((i==0 or i==1)  and j==len(arestas)-1) or (i==0 and j==len(arestas)-2) or (j==0 and i==1)):
                j = i
    
        s,t = 0,0
        if(i==0 and j>0):
            s,t = intersec2d(arestas[i],arestas[len(arestas)-1],arestas[j],arestas[j+1])
            k = arestas[i]
            l = arestas[len(arestas)-1]
            m = arestas[j]
            n = arestas[j+1]
        elif(j==(len(arestas)-1)):
            s,t = intersec2d(arestas[i],arestas[i-1],arestas[j],arestas[0])
            k = arestas[i]
            l = arestas[i-1]
            m = arestas[j]
            n = arestas[0]
        else:
            s,t = intersec2d(arestas[i],arestas[i-1],arestas[j],arestas[j+1])
            k = arestas[i]
            l = arestas[i-1]
            m = arestas[j]
            n = arestas[j+1]
        
        if(s != 0 and t != 0):
            px1 = k[0] + (l[0]-k[0])*s
            py1 = k[1] + (l[1]-k[1])*s
            px2 = m[0] + (n[0]-m[0])*t
            py2 = m[1] + (n[1]-m[1])*t
        
            if(px1 == px2 and py1 == py2):
                if(px1<max(k[0],l[0]) and px1>min(k[0],l[0]) and py1<max(k[1],l[1]) and py1>min(k[1],l[1])):
                    p[i],p[j] = p[j],p[i]
                    x[i],x[j] = x[j],x[i]
                    y[i],y[j] = y[j],y[i]





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

KB=8.61*10**(-5)       #constante de Boltzman em eV/K
escala=0.1             #escala de redução da temperatura
suc = False
t = 300

e1 = Energia(xl,yl)
plt.title("Energia: "+str(e1))
plt.draw() 
plt.pause(2) 
    
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

            plt.pause(0.0005)
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
