import numpy as np
import matplotlib.pyplot as plt


def calcule_R(h, n, theta):
    terme1 = 2 / ((n - 1) * h)
    terme2 = (n + 1) / ((n - 1) * h) * np.sum(theta**2)
    return terme1 - terme2


# Normaliser les données avant


# Génération des données
N = 100  # nombre total de points
n = N / 2  # un sous-ensemble de taille N/2 pour le calcul
theta = np.random.randn(N)  # Génération de N valeurs aléatoires pour Theta
print(theta)
h_values = np.linspace(0.1, 2, 100)  # Valeurs possibles pour h

# Calcul de R(h) pour différentes valeurs de h
R_values = [calcule_R(h, n, theta) for h in h_values]


# Enregistrer le graphique
plt.figure(figsize=(8, 6))
plt.bar(h_values, R_values, width=0.05, label="R(h)", color="orange")
plt.title("Évolution de R(h) en fonction de h")
plt.xlabel("h")
plt.ylabel("R(h)")
plt.grid(True)
plt.legend()
plt.savefig("evolution_R_h.png")
