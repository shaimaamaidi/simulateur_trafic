from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule

def test_ajouter_route(reseau_simple):
    route2 = Route("A2", longueur=1000, limite_vitesse=30)
    # Avant l'ajout
    nombre_routes_avant = len(reseau_simple.routes)
    reseau_simple.ajouter_route(route2)
    # Après l'ajout
    assert len(reseau_simple.routes) == nombre_routes_avant + 1
    assert route2 in reseau_simple.routes

def test_simuler(reseau_simple, route_simple,vehicule_exemple):
    # Avant la simulation

    position_initiale = vehicule_exemple.position

    reseau_simple.simuler(5)
    # Après la simulation
    assert vehicule_exemple.position > position_initiale
    assert vehicule_exemple.position <= route_simple.longueur
