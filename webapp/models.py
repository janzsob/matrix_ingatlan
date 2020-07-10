from django.db import models
from . import choices
from datetime import datetime

"""Detail model"""


class Ingatlan(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField("Irányár")
    types = models.CharField("Típus", max_length=30,
                             choices=choices.ingatlan_types, help_text="Ingatlan típus")
    size = models.IntegerField("Alapterület(m²)", blank=True, null=True)
    rooms = models.DecimalField(
        "Szobák száma", max_digits=5, decimal_places=1, blank=True, null=True)
    condition = models.CharField("Állapot", max_length=30,
                                 choices=choices.ingatlan_condition, blank=True)
    build_date = models.DecimalField(
        "Építés éve", max_digits=4, decimal_places=0, null=True, blank=True)
    komfort = models.CharField(
        "Komfort", max_length=30, choices=choices.ingatlan_komfort, blank=True)
    energy = models.CharField("Energiatanúsítvány", max_length=30, blank=True)
    emelet = models.IntegerField("Emelet", null=True, blank=True)
    bulding_floor = models.IntegerField(
        "Épület szintjei", null=True, blank=True)
    elevator = models.CharField(
        "Lift", max_length=30, choices=choices.ingatlan_elevator, blank=True)
    inner_height = models.IntegerField("Belmagasság(m)", null=True, blank=True)
    heating = models.CharField(
        "Fűtés", max_length=40, choices=choices.ingatlan_heating, blank=True)
    air_con = models.CharField(
        "Légkondicionáló", max_length=30, choices=choices.ingatlan_air_con, blank=True)
    over_head = models.DecimalField(
        "Rezsiköltség(Ft/hó)", max_digits=5, decimal_places=0, null=True, blank=True)
    garage = models.CharField(
        "Garázs", max_length=30, choices=choices.ingatlan_garage, blank=True)
    garden = models.CharField(
        "Kert", max_length=30, choices=choices.ingatlan_garden, blank=True)
    bathroom_toilet = models.CharField(
        "Fürdő és WC", max_length=40, choices=choices.ingatlan_bathroom_wc, blank=True)
    orientation = models.CharField(
        "Tájolás", max_length=30, choices=choices.ingatlan_orientation, blank=True)
    reg_date = models.DateField(
        "Rögzítés dátuma", default=datetime.now, blank=True)

    def __str__(self):
        return f"MI-{self.id}"
