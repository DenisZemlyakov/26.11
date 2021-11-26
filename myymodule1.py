from random import *
inimised=["Markus", "Arno", "Elizabet", "Konor", "batman"]
palgad=[1200,2500,750,395,1200]

def sisesta_andmed(i,p): #Добавить в список новых три фамилии
    N=3
    for n in range(N):
        a=input("Введите фамилию нового работника: ")
        i.append(a)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p): #выводим на экран список имен и зарплат
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #удаляем человека из списка
    nimi=input("Введите имя для удаления из списка: ")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,". ",i[e],"-", p[e])
        jaar=int(input("Порядковый номер: "))
        i.pop(abi_list[jaar-1])
        p.pop(abi_list[jaar-1])
        andmed_ekranile(i,p)

    return i,p
        
def keskmine_kustutamine(i,p): #удаление всех зарплат ниже средней
    summa=0
    new_list5=[]
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Средняя зарплата составляет - ", summa, " все зарплаты ниже этой цифры будут удалены!")
    w=0
    while w<len(p):
        if p[w]<summa:
            del p[w]
        else:
            w+=1
    print("В списке зарплат остались зарплаты выше средней: ",p)

def otsing_nimi_jargi(inimesed:list,palgad:list):
    """Tagastame järjend või tekst
    :rtype var: tulemas
    """
    nimi=input("keda otsime?")
    for inimene in inimesed:
        if inimene.upper()==nimi.upper():
            n=inimesed.count(nimi)
            peint("Inimene on olemas, selline kohtume ",n,"korda")
            b=1
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palgad[k]
                b+=k+1
                t.append(nimi+str(palk))
            else:
                t="Ei ole nimekirjas"
        return t
       

