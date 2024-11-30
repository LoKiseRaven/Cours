# Q1.  Dire si deux listes données en entrée ont au moins un élément en commun. Et on cherche tous les éléments commun.


```python
def element_commun(liste1, liste2):
    for i in liste1:
        for j in liste2:
            if i == j:
                return True
    return False
```


```python
def element_commun(liste1, liste2)
	tab2.sort()
	for elt in tab1
		if dicho2(elt, tab2)
			return True
	return False
```

Si on cherche tous les éléments, je append dans une liste au lieu de return True, et au lieu de return False je return ma liste

# Q2. Vous avez une liste d'un million d'identifiant (int) dans lequelle vous devez effectuer un certain nombre de recherches. Avez-vous intérêt à trier la liste auparavant ?

Oui il vaut mieux trier la liste avant.

# Q3. Etant données une liste et une cible, trouver deux entiers dans la liste dont la somme vaut la cible.

```python
def somme_cible(liste, cible)
	liste.sort()
	
	i = 0
	j = len(liste)-1
	
	min = liste[i]
	max = liste[j]
	
	for _ in liste:
		if min + max == cible:
			return min, max
		if min + max > cible:
			j--
			max = liste[j]
		if min + max < cible:
			i++
			min = liste[i]
	return None
```

# Q4. Trouver la 7ème plus grande valeur d'une liste. (et si on remplace 7 par une valeur donnée en entrée dont on pense qu'elle n'est pas trop grande ?)

```python
def recherche_n_eme_val(liste, n)
	maxVal[]
	max = liste[0]
	for i in range(n):
		for j in liste:
			if j > max:
				if j in maxVal:
					break
				
				
	return liste[n-1]
```

# Q5. Dans un tableau d'entiers tab, trouvez le morceau tab[a:b] avec la somme maximale.

```python
def morceau(liste, a, b):
	return "oula c'est complexe comme question"
```

