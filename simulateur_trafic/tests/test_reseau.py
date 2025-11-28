import pytest

from models.reseau import ReseauRoutier
from simulateur_trafic.models.route import Route
from simulateur_trafic.tests.conftest import reseau_simple, route_simple, vehicule_exemple


def test_ajouter_route(reseau_simple):
    route2 = Route("A2", longueur=1000, limite_vitesse=30)
    # Avant l'ajout
    nombre_routes_avant = len(reseau_simple.routes)
    reseau_simple.ajouter_route(route2)
    # Après l'ajout
    assert len(reseau_simple.routes) == nombre_routes_avant + 1
    assert route2 in reseau_simple.routes


def test_simuler(reseau_simple, route_simple, vehicule_exemple):
    # Avant la simulation
    position_initiale = vehicule_exemple.position
    reseau_simple.simuler(5)
    # Après la simulation
    assert vehicule_exemple.position > position_initiale
    assert vehicule_exemple.position <= route_simple.longueur


def test_etat_reseau(reseau_simple, vehicule_exemple, route_simple):
    etat = reseau_simple.etat_reseau()
    assert isinstance(etat, dict)
    assert route_simple.nom in etat
    assert vehicule_exemple.identifiant in etat[route_simple.nom]


def test_ajouter_intersection(reseau_simple, route_simple):
    reseau_simple.ajouter_intersection("I1", [route_simple])
    assert "I1" in reseau_simple.intersections
    assert reseau_simple.intersections["I1"] == [route_simple]


def test_from_json_valide(vehicule_exemple):
    config = {
        "routes": [
            {"nom": "R1", "longueur": 100, "start": None, "end": None,
             "limite_vitesse": 50,
             "vehicules": [{"id": vehicule_exemple.identifiant, "position": 0, "vitesse": 10}]}
        ],
        "intersections": [{"nom": "I1", "connecte": ["R1"]}]
    }
    reseau = ReseauRoutier.from_json(config)
    assert "R1" in [r.nom for r in reseau.routes]
    assert "I1" in reseau.intersections
    assert len(reseau.intersections["I1"]) == 1
