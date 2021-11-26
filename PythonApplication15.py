from myymodule1 import*      
while 1:
    print("a - ввод данных: \ne - вывод на экран: \nk - удаление: ие зарплат ниже средней.\nz - топ три. \nl - удаление зарплат ниже средней. \nu - поиск зарплат по имени.")
    valik=input()
    if valik.lower()=="a":
        inimised,palgad=sisesta_andmed(inimised,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimised, palgad)
    elif valik.lower()=="k":
        inimised,palgad=kustutamine(inimised, palgad)
    elif valik.lower()=="z":
        top3(inimised,palgad, int(input("1 - топ трех самых богатых, 2 - топ трех самых бедных.")))
    elif valik.lower()=="l":
        keskmine_kustutamine(inimised,palgad)
    elif valik.lower()=="u":
        name_search1(inimised, palgad)
    else:
        break

