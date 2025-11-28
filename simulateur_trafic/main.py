import json
from core.simulateur import Simulateur

try:
    simu = Simulateur(fichier_config="data/scratch.json")
    simu.lancer_simulation(n_tours=5, delta_t=60)
except FileNotFoundError:
    print("Erreur : fichier de configuration manquant.")
except json.JSONDecodeError:
    print("Erreur : fichier de configuration invalide.")
except ValueError as e:
    print(f"Erreur de paramètres : {e}")