from django.db import models

class Costomer(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    email = models.EmailField(max_length=20, verbose_name='Емайл')
    comments=models.TextField(max_length=255,verbose_name='Комментарий')

    class Meta:
        ordering = ['-id']
        verbose_name='Клиенты'
        verbose_name_plural='Клиенты'

    def __str__(self):
        return self.first_name