"""
Ce module contient la définition de la classe Route pour le simulateur de trafic.
"""
from simulateur_trafic.exceptions.exceptions import VehiculePresentsError, PositionInvalideError, VehiculeInvalideError, \
    TempsAvancementInvalidError
from simulateur_trafic.models.vehicule import Vehicule


class Route:
    """
    Représente une rue dans le simulateur.

    Attributes:
        nom (str): le nom de la rue.
        longueur (int): la longueur de la rue.
        start (list[int]): coordonnées [x, y] du début de la rue dans le graphique.
        end (list[int]): coordonnées [x, y] de la fin de la rue dans le graphique.
        limite_vitesse (float): vitesse maximale autorisée sur la rue.
        vehicules (list[Vehicule]): liste des véhicules présents sur la rue.
    """

    def __init__(self, nom: str, longueur: int, start: list[int] = None, end: list[int] = None,
                 limite_vitesse: float = 0, vehicules: list = None):
        """
        Initialise une nouvelle route dans le simulateur.

        Args:
            nom (str): nom de la rue.
            longueur (int): longueur de la rue.
            start (list[int]): coordonnées [x, y] du début de la rue.
            end (list[int]): coordonnées [x, y] de la fin de la rue.
            limite_vitesse (float): vitesse maximale autorisée sur la rue.
            vehicules (list[dict], optional): liste de dictionnaires contenant les informations
                des véhicules à initialiser sur la rue. Chaque dictionnaire doit contenir
                les clés "id", "position" et "vitesse".
        """
        self.nom = nom
        self.start = start
        self.end = end
        self.longueur = longueur
        self.limite_vitesse = limite_vitesse
        self.feuRouge = None
        self.position_feu = None
        self.vehicules: list[Vehicule] = []
        if vehicules:
            for v in vehicules:
                if isinstance(v, dict):
                    vehicule = Vehicule(identifiant=v["id"], position=v["position"], vitesse=v["vitesse"])
                elif isinstance(v, Vehicule):
                    vehicule = v
                else:
                    raise VehiculeInvalideError(
                        f"Erreur sur la route '{self.nom}' lors de la création :Chaque élément de 'vehicules' doit être un dict ou un objet Vehicule.")
                self.ajouter_vehicule(vehicule)

    def ajouter_vehicule(self, vehicule: Vehicule):
        """
        Ajoute un véhicule sur la route.

        Args:
            vehicule (Vehicule): objet Vehicule à ajouter.
        """
        if vehicule in self.vehicules:
            raise VehiculePresentsError("Le véhicule est déjà présent sur la route.")
        if vehicule.position > self.longueur:
            raise PositionInvalideError("La position du véhicule est invalide.")
        vehicule.route_actuelle = self
        self.vehicules.append(vehicule)

    def mettre_a_jour_vehicules(self, temps: float):
        """
        Met à jour la position des véhicules sur la route.

        Args:
            temps (float): durée écoulée pendant laquelle les véhicules avancent.
        """
        if temps < 0:
            raise TempsAvancementInvalidError("Temps d'avancement des vehicules doit etre un nombre positif!")
        for vehicule in list(self.vehicules):
            if vehicule.vitesse > self.limite_vitesse:
                vehicule.vitesse = self.limite_vitesse

            vehicule.avancer(temps)

            if vehicule.position > self.longueur:
                vehicule.position = self.longueur
                self.vehicules.remove(vehicule)

    def ajouter_feu_rouge(self, feu, position=None):
        """
        Cette méthode permet de déplacer un feu dans un position donné en paramètre

        paramètres:
            feu: (FeuRouge) le feu à ajouter dans la route
            position: (int, int) position du feu à ajouter
        """
        if position > self.longueur or position<0:
            raise PositionInvalideError(
                f"la position du feu dans la route est incorrecte :doit etre un nombre positif inférieur de {self.longueur}")
        self.feuRouge = feu
        self.position_feu = position

    def update(self, dt=1.0):
        """
        Cette méthode permet de mettre à jour le feu et déplacer les véhicules

        paramètres :
            dt: (float) temps d'avancement
        """
        try:
            if self.feuRouge:
                self.feuRouge.avancer_temps(dt)

            if self.feuRouge and self.feuRouge.etat == "rouge":
                for vehicule in list(self.vehicules):
                    if vehicule.position < self.position_feu:
                        vitesse = max(vehicule.vitesse, self.limite_vitesse)
                        nouvelle_position = min(vehicule.position + vitesse * dt, self.position_feu - 0.1)
                        vehicule.position = nouvelle_position
            else:
                self.mettre_a_jour_vehicules(dt)
        except TempsAvancementInvalidError as e:
            print(f"Erreur dans l'avancement du temps du FeuRouge :{e}")
