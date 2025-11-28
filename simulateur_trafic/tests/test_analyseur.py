from simulateur_trafic.tests.conftest import analyseur_exemple, route_simple


def test_update_stats(analyseur_exemple):
    analyseur_exemple.update_stats(1)
    assert 1 in analyseur_exemple.vitesse_moyenne
    assert "A1" in analyseur_exemple.vitesse_moyenne[1]
    assert "A1" in analyseur_exemple.temps_parcours[1]


def test_calculer_zones_congestion(analyseur_exemple):
    zones = analyseur_exemple._calculer_zones_congestion()
    assert zones == {}


def test_calculer_temps_parcours(analyseur_exemple, route_simple):
    temps = analyseur_exemple._calculer_temps_parcours()
    for v in route_simple.vehicules:
        assert temps["A1"][v.identifiant] == route_simple.longueur / v.vitesse
