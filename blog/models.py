from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    '''Класс записи блога'''
    
    #Автор
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #Заголовок
    title = models.CharField(max_length=200) # так определяется поле с ограниченой дланной
    #Текст записи
    text = models.TextField() # так определяется поле с неогорониченной длинной
    # Дата и время
    created_date = models.DateTimeField(default=timezone.now) 
    publised_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publised_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    