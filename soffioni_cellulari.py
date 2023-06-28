"""
Automa cellulare che simula la generazione dei soffioni all'interno di un prato

\legenda
    - = cella libera
    ^ = seme volante
    ° = seme piantato
    * = dente di leone
    @ = soffione


\regole
    \ ovviamente il cambio di stato di ogni cella è sincronizzato
    \ ogni tot i soffioni completamente cresciuti muoiono lasciando lo spazio pulito
    \ ogni volta che vengono generati i semi volanti il soffione che ne genera muore
    \ la direzione dei semi volanti viene decisa dal vento che ha direzione randomica (giù, sù, destra, sinistra)


"""

from random import randint
import time

def stampa_pazi():
    i=0
    while(i<150):
        print()
        i+=1

def stampa_campo(campo):
    for i in range(dim):
        print()
        for j in range(dim):
            print("%2s" % campo[i][j], end=' ')

def genera_campo(campo,start_points):
    random =0
    for i in range(dim):
        print()
        n=0
        for j in range(dim):
            if n<int(dim/3):
                random = randint(0,2)
                if (random==0 and start_points>0) and j>0 and i>int(dim/3):
                    campo[i][j] = "°"
                    start_points-=3
                    n+=1

def crescita_soffioni(campo,f,dim):
    for i in range(dim):
        for j in range(dim):
            if campo[i][j]=="°" and f%4==0:
                campo[i][j] = "*"
            if  campo[i][j]=="*" and f%7==0:
                campo[i][j] = "@"
            if campo[i][j]=="@" and f%10==0:
                campo[i][j]="-"

def diffusione_generazione(campo,dim):

    vento = randint(0,3)
    crescita = randint(0,2)
    sw = ""

    for i in range(dim):
        for j in range(dim):
            if campo[i][j]=="@":
                campo[i][j]=="-"
                volte = randint(0,int(dim/5))
                if crescita>0:
                    d=0
                    if vento==0:
                        d=1
                        if(i+d<dim-1):
                            campo[i+d][j]="^"
                            while(volte>0):
                                try:
                                    if(campo[i+d+1][j]!="-"):
                                        volte=0
                                        campo[i+d][j]="°"
                                    else:
                                        sw = campo[i+d][j]="^"
                                        campo[i+d][j] = "-" 
                                        campo[i+d+1][j] = sw
                                        d+=1
                                    volte-=1
                                except:
                                    volte=0

                    elif vento==1:
                        d=1
                        if(i-d>0):
                            campo[i-d][j]="^"
                            while(volte>0):
                                try:
                                    if(campo[i-d-1][j]!="-"):
                                        volte=0
                                        campo[i-d][j]="°"
                                    else:
                                        sw = campo[i-d][j]="^"
                                        campo[i-d][j] = "-" 
                                        campo[i-d-1][j] = sw
                                        d+=1
                                    volte-=1
                                except:
                                    volte=0
                       
                    elif vento==2:
                        d=1
                        if(j+d<dim-1):
                            campo[i][j+d]="^"
                            while(volte>0):
                                try:
                                    if(campo[i][j+d+1]!="-"):
                                        volte=0
                                        campo[i][j+d]="°"
                                    else:
                                        sw = campo[i][j+d]="^"
                                        campo[i][j+d] = "-" 
                                        campo[i][j+1+d] = sw
                                        d+=1
                                    volte-=1
                                except:
                                    volte=0
                    
                    else:
                        d=1
                        if(j-d>0):
                            campo[i][j-d]="^"
                            while(volte>0):
                                try:
                                    if(campo[i][j-d-1]!="-"):
                                        volte=0
                                        campo[i][j-d]="°"
                                    else:
                                        sw = campo[i][j-d]="^"
                                        campo[i][j-d] = "-" 
                                        campo[i][j-1-d] = sw
                                        d+=1
                                    volte-=1
                                except:
                                    volte=0
                          
                        

def statistiche_campo(campo):

    cl = 0
    semi = 0
    dl = 0
    sf = 0
    semiv = 0

    for i in range(dim):
        for j in range(dim):
            if campo[i][j]=="^":
                semiv+=1
            if campo[i][j]=="°":
                semi+=1
            if  campo[i][j]=="*":
                dl +=1
            if campo[i][j]=="@":
                sf+=1
            if campo[i][j]=="-":
                cl+=1

    print("@@ Statistiche Campo @@")
    print("\nzone libere = ",cl)
    print("\nsemi volanti = ",semiv)
    print("\nsemi = ",semi)
    print("\ndenti di leone = ",dl)
    print("\nsoffioni = ",sf)



#main loop
stampa_pazi()
print("** Generazione Soffioni **")
print()
print()

dim = int(input("Iserisci la dimensione del tuo prato: "))
random = 0
campo = [["-"] * dim for _ in range(dim)]
f=1
start_points = int(input("Inserisci quanti soffioni vuoi che siano generati inizialmente: "))
giorni = int(input("Quanti giorni vuoi far durare la simulazione: "))

genera_campo(campo,start_points)
print()
print()
print()
print("Giorno ",f-1)
stampa_campo(campo)
print()
print()
statistiche_campo(campo)
print()
print()
time.sleep(3)
stampa_pazi()

while(f-1<giorni):    
    crescita_soffioni(campo,f,dim)
    diffusione_generazione(campo,dim)
    print()
    print()
    print()
    print("Giorno ",f)
    stampa_campo(campo)
    print()
    print()
    statistiche_campo(campo)
    print()
    print()


    time.sleep(3)
    stampa_pazi()
    for i in range(dim):
        for j in range(dim):
            if campo[i][j]=="^":
                campo[i][j]="°"

    f+=1
