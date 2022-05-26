from django.db import models

class Costomer(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Name')
    email = models.EmailField(max_length=20, verbose_name='email')
    comments=models.TextField(max_length=255,verbose_name='comments')

    class Meta:
        ordering = ['-id']
        verbose_name='Клиенты'
        verbose_name_plural='Клиенты'

    def __str__(self):
        return self.first_name