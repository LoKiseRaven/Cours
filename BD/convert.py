import re
import csv

def convert_point(point_str):
    # Utilisation d'une expression régulière pour extraire les coordonnées, y compris les négatives
    match = re.match(r"Point\((-?\d+\.\d+)\s+(-?\d+\.\d+)\)", point_str)
    
    if match:
        # Récupère les deux coordonnées et les retourne sous forme de chaîne avec une virgule en les inversants
        return f"{match.group(2)},{match.group(1)}"
    else:
        raise ValueError("Format de point invalide")

# Exemple d'utilisation
point = "Point(43.0 33.0)"
resultat = convert_point(point)
print(resultat)  # Affiche: 43.0,33.0

def lire_csv_et_convertir(fichier_csv):
    points_convertis = []
    with open(fichier_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            point_str = row[0]  # Supposons que le point est dans la première colonne
            try:
                point_converti = convert_point(point_str)
                points_convertis.append(point_converti)
            except ValueError as e:
                print(f"Erreur de conversion pour le point {point_str}: {e}")
    return points_convertis

def exporter_liste_vers_txt(liste, fichier_txt):
    with open(fichier_txt, 'w') as txtfile:
        for item in liste:
            txtfile.write(f"{item}\n")

# Exemple d'utilisation
fichier_csv = 'points.csv'
fichier_txt = 'points_convertis.txt'
points_convertis = lire_csv_et_convertir(fichier_csv)
exporter_liste_vers_txt(points_convertis, fichier_txt)

