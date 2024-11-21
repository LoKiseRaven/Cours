import time
import matplotlib.pyplot as plt

def createList(n):
    liste = []
    for i in range(n):
        liste.append(i)
    return liste



def recherche(n, liste):
    for i in liste:
        if n == liste[i]:
            return i
    return None

def mesure(foo, *args):
    t1 = time.process_time()
    foo(*args)
    return time.process_time() -t1

times = []
# for i in range(10_000_00, 100_000_000, 10_000_000):
#     times.append(mesure(recherche, -1, createList(i)))

print(times)
plt.plot(times)
plt.title('Graphique simple')
plt.xlabel('Nb Elements')
plt.ylabel('Temps')
plt.show()

##########################

def dichotomie(t, v):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            return True
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    return False