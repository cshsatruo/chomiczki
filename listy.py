'''
Lista to zbiór elementów zapisanych pod jedną nazwą zmiennej, w [],
jej elem są oddzielone przecinkami. Elementy wewnątrz listy mogą być róznego typu
i mogą się powtarzać.
Aby odwołać sie do konkretnego elem, z listy, korzystamy
z możliwości indeksowania elem. (pierwszy elementy ma zerowy indeks!!!!)
'''
#indeksy 0     1       2        3      4     5
lista =["Ala","Kasia","Szymon","Pola","Iga","Ula"]

#odwoł do pierwszego elementy - podaj numer indeksu
print(lista[0])

# zwraca dane z zakresu [nr:nr]
print(lista[0:3])
# zwraca wszystkie elem
print(lista[0:6])

#zwraca wszystkie
print(lista)

# długość listy
print(len(lista))

# nadpisanie elem na wskazanym indeksie
lista[2]="Kasia"
print(lista)

#METODY STOS. NA LISTACH

# + nowego elem (na końcu)
lista.append(11.73)
print(lista)

# + nowego elem na określona pozycję
lista.insert(1,"Adam")
print(lista)

# - elem
lista.remove("Kasia")
print(lista)

# - elem ze wskazanego indeksu
lista.pop(5)
print(lista)

# - ostatni elem
lista.pop()
print(lista)

# sortowanie listy
lista.sort()
print(lista)

# odwracanie listy
lista.reverse()
print(lista)

#spr, czy elem jest na liście (pokaże nr indekstu)
print(lista.index("Kasia"))

#zlicza ilość wystąpień danego elementu

print(lista.count("Ewa"))

# łącznie dwóch list ver1
lista2=[12,15,0, True]
lista.extend(lista2)
print(lista)

# łącznie dwóch list bez użycia metody ver2
razem = lista + lista2
print(razem)

# czyszczenie zawartości listy
lista2.clear()
print(lista2)
