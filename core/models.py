from django.db import models


class TopPost(models.Model):
    name = models.CharField("ism" , max_length=256)
    abo = models.TextField()
    date = models.DateTimeField("soat", auto_now_add=True)


    def __str__(self):
        return self.name
