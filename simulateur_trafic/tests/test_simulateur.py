from unittest.mock import patch
import pytest
from simulateur_trafic.tests.conftest import simulateur_exemple
from simulateur_trafic.models.reseau import ReseauRoutier


def test_initialisation_simulateur(simulateur_exemple):
    assert isinstance(simulateur_exemple.reseau, ReseauRoutier)
    assert len(simulateur_exemple.reseau.routes) == 1
    assert simulateur_exemple.reseau.routes[0].nom == "RueA"
    assert len(simulateur_exemple.reseau.routes[0].vehicules) == 2


def test_execution_simulation(simulateur_exemple):
    try:
        simulateur_exemple.lancer_simulation(n_tours=3, delta_t=1.0, afficher=False, exporter=False)
    except Exception as e:
        pytest.fail(f"La simulation a levé une exception : {e}")

    # Vérifie que les statistiques ont été mises à jour
    assert simulateur_exemple.stats["tours_effectues"] == 3
    assert len(simulateur_exemple.stats["historique"]) == 3
    for tour, etat in simulateur_exemple.stats["historique"].items():
        assert "RueA" in etat
        assert len(etat["RueA"]) <= 2


def test_affichage_et_export_mock(simulateur_exemple):
    with patch.object(simulateur_exemple.affichage, "afficher_stats") as mock_stats, \
            patch.object(simulateur_exemple.affichage, "visualiser_resultats") as mock_vitesse, \
            patch.object(simulateur_exemple.affichage, "animer_traffic") as mock_anim, \
            patch.object(simulateur_exemple.export, "exporter_resultats_csv") as mock_csv, \
            patch.object(simulateur_exemple.export, "exporter_resultats_json") as mock_json:
        simulateur_exemple.lancer_simulation(n_tours=1, delta_t=1.0, afficher=True, exporter=True)

        mock_stats.assert_called_once()
        mock_vitesse.assert_called_once()
        mock_anim.assert_called_once()
        mock_csv.assert_called_once()
        mock_json.assert_called_once()


def test_simulation_delta_t_negatif(simulateur_exemple):
    with pytest.raises(ValueError):
        simulateur_exemple.lancer_simulation(n_tours=1, delta_t=-1.0, afficher=False, exporter=False)


def test_simulation_sans_vehicules(simulateur_exemple):
    # On vide tous les véhicules
    for route in simulateur_exemple.reseau.routes:
        route.vehicules.clear()

    simulateur_exemple.lancer_simulation(n_tours=2, delta_t=1.0, afficher=False, exporter=False)
    for tour, etat in simulateur_exemple.stats["historique"].items():
        for vehicules in etat.values():
            assert vehicules == []  # pas de véhicules
