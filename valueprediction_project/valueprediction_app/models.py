from django.db import models

class HouseData(models.Model):
    overall_quality = models.IntegerField()
    gr_liv_area = models.IntegerField()
    garage_cars = models.IntegerField()
    garage_area = models.IntegerField()
    total_bsmt_sf = models.IntegerField()
    first_flr_sf = models.IntegerField()
    full_bath = models.IntegerField()
    tot_rms_abv_grd = models.IntegerField()
    year_built = models.IntegerField()
    year_remod_add = models.IntegerField()

    def __str__(self):
        return f"{self.overall_quality}, {self.gr_liv_area}, {self.garage_cars}, {self.garage_area}, {self.total_bsmt_sf}, {self.first_flr_sf}, {self.full_bath}, {self.tot_rms_abv_grd}, {self.year_built}, {self.year_remod_add}"