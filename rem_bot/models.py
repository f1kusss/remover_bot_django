from django.db import models

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name='Имя пользователя'
    )
    username = models.TextField(
        verbose_name='Никнейм'
    )

    def __str__(self):
        return f'#{self.external_id} {self.name} {self.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'