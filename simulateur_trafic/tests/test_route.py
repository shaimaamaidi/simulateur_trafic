import pytest
from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from simulateur_trafic.exceptions.exceptions import VehiculeInvalideError, VehiculePresentsError, PositionInvalideError


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

def test_construction_route_vehicule_invalide():
    with pytest.raises(VehiculeInvalideError):
        Route("Test", 100, vehicules=[123])


def test_ajouter_vehicule_erreurs(route_simple):
    v_exist = route_simple.vehicules[0]
    v_hors_route = Vehicule("Vx", position=route_simple.longueur + 1, vitesse=5)

    with pytest.raises(VehiculePresentsError):
        route_simple.ajouter_vehicule(v_exist)

    with pytest.raises(PositionInvalideError):
        route_simple.ajouter_vehicule(v_hors_route)

def test_mettre_a_jour_vehicules_limite_vitesse(route_simple):
    v = Vehicule("Vfast", position=0, vitesse=100)
    route_simple.limite_vitesse = 50
    route_simple.ajouter_vehicule(v)
    route_simple.mettre_a_jour_vehicules(1)
    assert v.vitesse <= route_simple.limite_vitesse
