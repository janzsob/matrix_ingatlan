from django.db import models
from . import choices
from datetime import datetime

"""Detail model"""


def image_path(instance, filename):
    return '/'.join([str(instance.reg_date), str(instance.types), str(instance.price), filename])


class Ingatlan(models.Model):

    id = models.AutoField(primary_key=True)
    price = models.IntegerField("Irányár")
    types = models.CharField("Típus", max_length=30,
                             choices=choices.ingatlan_types, help_text="Ingatlan típus")
    city = models.CharField("Település", max_length=35)
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
    cover_photo = models.ImageField(
        "Borítókép", upload_to=image_path)
    photo1 = models.ImageField(
        "Kép1", upload_to=image_path, null=True, blank=True)
    photo2 = models.ImageField(
        "Kép2", upload_to=image_path, null=True, blank=True)
    photo3 = models.ImageField(
        "Kép3", upload_to=image_path, null=True, blank=True)
    photo4 = models.ImageField(
        "Kép4", upload_to=image_path, null=True, blank=True)
    photo5 = models.ImageField(
        "Kép5", upload_to=image_path, null=True, blank=True)
    photo6 = models.ImageField(
        "Kép6", upload_to=image_path, null=True, blank=True)
    photo7 = models.ImageField(
        "Kép7", upload_to=image_path, null=True, blank=True)
    publish = models.BooleanField("Meghirdetés", default=True)
    reg_date = models.DateField(
        "Rögzítés dátuma", default=datetime.now, blank=True)

    def __str__(self):
        return f"MI-{self.id}"
