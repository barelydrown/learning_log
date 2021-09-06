from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по конкретной теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text}'
