from django.db import models

# Create your models here.


class Pipe(models.Model):

    PIPE_UNIT = (
        ('1', 'IN'),
        ('2', 'lb/ft3')
    )

    pipe_od = models.FloatField(blank=False)
    pipe_od_unit = models.CharField(max_length=1,choices=PIPE_UNIT, default=1, blank=True)
    pipe_wt = models.FloatField(blank=False)
    pipe_wt_unit = models.CharField(max_length=1,choices=PIPE_UNIT, default=1, blank=True)
    pipe_density = models.FloatField(blank=False)
    pipe_density_unit = models.CharField(max_length=1,choices=PIPE_UNIT, default=1, blank=True)
    corrosion_allowance = models.FloatField(blank=False)
    corrosion_allowance_unit = models.CharField(max_length=1,choices=PIPE_UNIT, default=1, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)


# class Pipe(models.Model):

#     PIPE_STATUS = (
#         ('1', 'Pipe Outside Diameter (OD)'),
#         ('2', 'Pipe Wall Thickness (t)'),
#         ('3', 'Pipe Density'),
#         ('4', 'Corrosion Allowance'),
#     )

#     description = models.IntegerField(blank=False)
#     value = models.IntegerField(blank=False)
#     unit = models.IntegerField(blank=False)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __init__(self):
#         return self.pipe_od



class Coating(models.Model):
    pipe    = models.OneToOneField(Pipe, on_delete=models.CASCADE)
    coating_no = models.IntegerField(blank=False)
    description = models.CharField(max_length=1000, blank=True)
    thickness = models.FloatField(blank=False)
    density = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Contents(models.Model):
    CONTENT = (
        ('1', 'Air'),
        ('2', 'Water'),
        ('3', 'Sea Water')
    )

    coating = models.OneToOneField(Coating, on_delete=models.CASCADE)
    pipe    = models.OneToOneField(Pipe, on_delete=models.CASCADE)
    installation_empty = models.FloatField(blank=False)
    installation_empty_content = models.CharField(max_length=1,choices=CONTENT, default=1, blank=True)
    flooded = models.FloatField(blank=False)
    flooded_content = models.CharField(max_length=1,choices=CONTENT, default=1, blank=True)
    hydrotest = models.FloatField(blank=False)
    hydrotest_content = models.CharField(max_length=1,choices=CONTENT, default=1, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)