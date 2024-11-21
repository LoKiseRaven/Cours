import random
import time
import matplotlib.pyplot as plt

def createListRandom(n):
    liste = []
    for _ in range(n):
        liste.append(n)
        liste.shuffle()
    return liste

def measure_time(function):
    def measure_fun(*args):
        t = time.perf_counter()
        function(*args)
        return time.perf_counter() - t
    return measure_fun

@measure_time
def tri_par_insertion(liste):
    if len(liste) == 0 or len(liste) == 1:
        return liste
    listeTrie = []
    listeTrie.append(liste[0])
    for i in range(1, len(liste)):
        for j in range(len(listeTrie)):
            if liste[i] < listeTrie[0]:
                listeTrie.insert(0, liste[i])
                break
            if liste[i] < listeTrie[j]:
                listeTrie.insert(j, liste[i])
                break
            if j == len(listeTrie) - 1:
                listeTrie.append(liste[i])
                break
    return listeTrie



#print("Temps tri par insertion : ", tri_par_insertion(createListRandom(1_000)))

times = []
for i in range(1_000, 10_000, 1_000):
    times.append(tri_par_insertion(createListRandom(i)))

print(times)
plt.plot(times)
plt.title('Graphique simple')
plt.xlabel('Nb Elements')
plt.ylabel('Temps')
plt.show()