import pytest

from simulateur_trafic.tests.conftest import affichage_exemple, reseau_simple, analyseur_exemple
import matplotlib

matplotlib.use('Agg')  # pour tests sans GUI


def test_parse_vehicule_info_ok(affichage_exemple):
    s = "(ID:5, Pos:20, Vit:10)"
    result = affichage_exemple.parse_vehicule_info(s)
    assert result == {"id": 5, "position": 20.0, "vitesse": 10.0}


def test_afficher_stats(capsys, affichage_exemple, analyseur_exemple):
    analyseur_exemple.update_stats(1)
    affichage_exemple.afficher_stats(analyseur_exemple)
    captured = capsys.readouterr()
    assert "Statistiques Tour 1" in captured.out


def test_visualiser_resultats(affichage_exemple):
    historique = {1: {"A1": 10}, 2: {"A1": 20}}
    affichage_exemple.visualiser_resultats(historique, False)


def test_animer_traffic(affichage_exemple, reseau_simple):
    historique = {0: {"A1": ["(ID:1, Pos:0, Vit:10)"]}}
    affichage_exemple.animer_traffic(reseau_simple, historique)


def test_affichage_sans_vehicules(affichage_exemple):
    # Historique vide mais au format dict
    vitesse_moyenne_vide = {}  # <-- doit être dict
    historique_vide = {}
    reseau_vide = type("ReseauMock", (), {"routes": []})()

    # Ne doit pas lever d'erreur
    affichage_exemple.visualiser_resultats(vitesse_moyenne_vide)
    affichage_exemple.animer_traffic(reseau_vide, historique_vide)

def test_visualiser_resultats_vide(affichage_exemple):
    # Historique avec des valeurs None
    historique = {1: {"A1": None}, 2: {"A1": 20}}
    # Ne doit pas lever d'erreur
    affichage_exemple.visualiser_resultats(historique, False)


def test_animer_traffic_sans_vehicules(affichage_exemple):
    class RouteMock:
        def __init__(self, nom):
            self.nom = nom
            self.start = (0, 0)
            self.end = (100, 0)
            self.longueur = 100
            self.vehicules = []

    class ReseauMock:
        def __init__(self):
            self.routes = [RouteMock("R1"), RouteMock("R2")]

    reseau = ReseauMock()
    historique = {0: {"R1": [], "R2": []}}

    # Ne doit pas lever d'erreur
    affichage_exemple.animer_traffic(reseau, historique)




