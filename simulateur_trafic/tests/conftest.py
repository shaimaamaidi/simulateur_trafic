import pytest
from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from simulateur_trafic.models.reseau import ReseauRoutier
from simulateur_trafic.models.feu_rouge import FeuRouge


@pytest.fixture
def vehicule_exemple():
    return Vehicule(1, position=0, vitesse=10)


@pytest.fixture
def route_simple(vehicule_exemple):
    return Route("A1", longueur=1000, limite_vitesse=30, vehicules=[vehicule_exemple])


@pytest.fixture
def reseau_simple(route_simple):
    reseau = ReseauRoutier()
    reseau.ajouter_route(route_simple)
    return reseau


@pytest.fixture
def feu_rouge():
    return FeuRouge(5)
