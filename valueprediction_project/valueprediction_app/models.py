from django.db import models

class HouseData(models.Model):
    Overall_Quality = models.IntegerField()
    Ground_Living_Sqft = models.IntegerField()
    Garage_Car_Capacity = models.IntegerField()
    Garage_Sqft = models.IntegerField()
    Basement_Sqft = models.IntegerField()
    First_Floor_Sqft = models.IntegerField()
    Full_Baths = models.IntegerField()
    Bedroom_Count = models.IntegerField()
    Year_Built = models.IntegerField()
    Year_Remodeled = models.IntegerField()

    def __str__(self):
        return f"{self.Overall_Quality}, {self.Ground_Living_Sqft}, {self.Garage_Car_Capacity},{self.Garage_Car_Capacity}, {self.Basement_Sqft}, {self.First_Floor_Sqft}, {self.Full_Baths},{self.Bedroom_Count}, {self.Year_Built}, {self.Year_Remodeled}"