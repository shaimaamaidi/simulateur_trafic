import json
import pytest
from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from simulateur_trafic.models.reseau import ReseauRoutier
from simulateur_trafic.models.feu_rouge import FeuRouge
from simulateur_trafic.inout.affichage import Affichage
from simulateur_trafic.core.analyseur import Analyseur
from simulateur_trafic.inout.export import Export
from simulateur_trafic.core.simulateur import Simulateur

@pytest.fixture
def vehicule_exemple():
    return Vehicule(1, position=0, vitesse=10)


@pytest.fixture
def route_simple(vehicule_exemple):
    return Route("A1", longueur=1000, limite_vitesse=30, vehicules=[vehicule_exemple], start=[0, 0], end=[100, 0])


@pytest.fixture
def reseau_simple(route_simple):
    reseau = ReseauRoutier()
    reseau.ajouter_route(route_simple)
    return reseau


@pytest.fixture
def affichage_exemple():
    return Affichage()


@pytest.fixture
def analyseur_exemple(reseau_simple):
    return Analyseur(reseau_simple)


@pytest.fixture
def historique_exemple():
    return {
        1: {"A1": ["(ID:1, Pos:10, Vit:5)", "(ID:2, Pos:20, Vit:10)"]},
        2: {"A1": ["(ID:1, Pos:15, Vit:5)", "(ID:2, Pos:25, Vit:10)"]}
    }


@pytest.fixture
def export_exemple():
    return Export()



@pytest.fixture
def fichier_config_temp(tmp_path):
    """
    Crée un fichier JSON temporaire avec une configuration simple de réseau routier.
    """
    config = {
        "routes": [
            {
                "nom": "RueA",
                "longueur": 1000,
                "start": [0, 0],
                "end": [2, 0],
                "limite_vitesse": 60,
                "vehicules": [
                    {"id": 1, "position": 0, "vitesse": 0},
                    {"id": 2, "position": 50, "vitesse": 10}
                ]
            }
        ],
        "intersections": []
    }

    fichier = tmp_path / "config.json"
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    return str(fichier)

@pytest.fixture()
def simulateur_exemple(fichier_config_temp):
    return Simulateur(fichier_config_temp)
@pytest.fixture
def feu_rouge():
    return FeuRouge(5)
