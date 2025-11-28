import csv
import json
import os

from simulateur_trafic.tests.conftest import export_exemple, historique_exemple


def test_parse_vehicule_info(export_exemple):
    s = "(ID:5, Pos:20, Vit:10)"
    result = export_exemple.parse_vehicule_info(s)
    assert result == {"id": 5, "position": 20.0, "vitesse": 10.0}


def test_exporter_resultats_csv(tmp_path, export_exemple, historique_exemple):
    export_exemple.exporter_resultats_csv(historique_exemple)

    assert os.path.exists("resultats.csv")

    with open("resultats.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["Tour", "Route", "ID_Vehicule", "Position", "Vitesse"]

    assert rows[1] == ["1", "A1", "1", "10.0", "5.0"]


def test_exporter_resultats_json(tmp_path, export_exemple, historique_exemple):
    export_exemple.exporter_resultats_json(historique_exemple)

    assert os.path.exists("historique.json")

    with open("historique.json", encoding="utf-8") as f:
        data = json.load(f)

    assert "Tour 1" in data
    assert "Tour 2" in data
    assert data["Tour 1"]["A1"][0] == "(ID:1, Pos:10, Vit:5)"
