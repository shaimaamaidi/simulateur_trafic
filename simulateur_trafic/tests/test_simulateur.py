import pytest
import json
from simulateur_trafic.models.reseau import ReseauRoutier
from simulateur_trafic.core.simulateur import Simulateur

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

def test_initialisation_simulateur(fichier_config_temp):
    sim = Simulateur(fichier_config_temp)
    assert isinstance(sim.reseau, ReseauRoutier)
    assert len(sim.reseau.routes) == 1
    assert sim.reseau.routes[0].nom == "RueA"
    assert len(sim.reseau.routes[0].vehicules) == 2


def test_execution_simulation(fichier_config_temp):
    sim = Simulateur(fichier_config_temp)
    try:
        sim.lancer_simulation(n_tours=3, delta_t=1.0, afficher=False, exporter=False)
    except Exception as e:
        pytest.fail(f"La simulation a levé une exception : {e}")

    # Vérifie que les statistiques ont été mises à jour
    assert sim.stats["tours_effectues"] == 3
    assert len(sim.stats["historique"]) == 3
    for tour, etat in sim.stats["historique"].items():
        assert "RueA" in etat
        assert len(etat["RueA"]) <= 2