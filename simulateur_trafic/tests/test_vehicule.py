from simulateur_trafic.models.route import Route


def test_avancement_modifie_position(vehicule_exemple):
    position_initiale = vehicule_exemple.position
    vehicule_exemple.avancer(5)
    assert vehicule_exemple.position == position_initiale + 50, \
        "L'avancement ne modifie pas correctement la position du véhicule."


def test_vehicule_ne_depasse_pas_longueur_route(vehicule_exemple, route_simple):
    route_simple.mettre_a_jour_vehicules(200)
    assert vehicule_exemple.position <= route_simple.longueur, \
        "Le véhicule a dépassé la longueur de la route."


def test_changement_de_route_remet_position_a_zero(vehicule_exemple):
    nouvelle_route = Route("B2", longueur=500, limite_vitesse=40)
    vehicule_exemple.changer_de_route(nouvelle_route)

    assert vehicule_exemple.route_actuelle == nouvelle_route, \
        "Le véhicule n’a pas changé de route correctement."
    assert vehicule_exemple.position == 0, \
        "La position n’a pas été réinitialisée à zéro lors du changement de route."
