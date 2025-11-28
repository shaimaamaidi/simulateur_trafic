from simulateur_trafic.exceptions.exceptions import CycleInvalidError,TempsAvancementInvalidError


class FeuRouge:
    """
    un feu rouge simple avec un cycle :
        -vert : cycles secondes
        -organge : 1 seconde
        -rouge : cycles secondes
    """

    def __init__(self, cycle=5):
        if cycle < 0:
            raise CycleInvalidError("Le cycle doit etre un nombre positif!")
        self.temps = 0
        self.duree_vert = cycle
        self.duree_rouge = cycle
        self.duree_orange = 1
        self.cycle_total = self.duree_rouge + self.duree_vert + self.duree_orange

    @property
    def etat(self):
        """
        Cette fonction permet de retourner etat du feu
        Exemple : sachant que cycle=5
            vert  : 5 s   (0 → 4)
            orange: 1 s   (5)
            rouge : 5 s   (6 → 10)
        retourne :
            string : etat du feu (vert ou rouge ou orange)
        """
        if self.temps < self.duree_vert:
            return "vert"
        elif self.temps < self.duree_orange + self.duree_vert:
            return "orange"
        else:
            return "rouge"

    def avancer_temps(self, dt):
        """
        Cette fonction permet d'avncer le temps passé du FeuRouge
        paramètres :
            dt: le temps passé en secondes
        """
        if dt < 0:
            raise TempsAvancementInvalidError("Le temps passé doit etre un nombre positif!")
        self.temps = (self.temps + dt) % self.cycle_total