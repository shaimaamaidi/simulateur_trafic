from simulateur_trafic.tests.conftest import feu_rouge, route_simple


def test_cycle_du_feu(feu_rouge):
    assert feu_rouge.etat == "vert"

    feu_rouge.avancer_temps(4)
    assert feu_rouge.etat == "vert"

    feu_rouge.avancer_temps(1)
    assert feu_rouge.etat == "orange"

    feu_rouge.avancer_temps(1)
    assert feu_rouge.etat == "rouge"

    feu_rouge.avancer_temps(6)
    assert feu_rouge.etat == "vert"


def test_arret_au_feu_rouge(feu_rouge, route_simple):
    route_simple.ajouter_feu_rouge(feu_rouge, 500)
    route_simple.update(61)
    assert route_simple.feuRouge.etat == "rouge"

    for v in route_simple.vehicules:
        assert v.position <= route_simple.position_feu - 0.1
