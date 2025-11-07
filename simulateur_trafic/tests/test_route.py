from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule

def test_ajouter_vehicule(route_simple):
    vehicule2 = Vehicule("V2", position=0, vitesse=15)
    # Avant l'ajout
    nombre_vehicules_avant = len(route_simple.vehicules)
    route_simple.ajouter_vehicule(vehicule2)
    # Après l'ajout
    assert len(route_simple.vehicules) == nombre_vehicules_avant + 1
    assert vehicule2 in route_simple.vehicules

def test_mettre_a_jour_vehicules(route_simple, vehicule_exemple):
    position_initiale = vehicule_exemple.position

    route_simple.mettre_a_jour_vehicules(5)

    assert vehicule_exemple.position > position_initiale
    assert vehicule_exemple.position <= route_simple.longueur
