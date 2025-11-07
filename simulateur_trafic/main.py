from core.simulateur import Simulateur

simu = Simulateur(fichier_config="data/scratch.json")
simu.lancer_simulation(n_tours=5, delta_t=60)
