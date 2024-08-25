from django.db import models
from datetime import datetime 
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Topic(models.Model):
    """Тема,которую изучает пользователь"""
    text = models.CharField(max_length=200) #переменная для хранения небольшого объёма текса в длинну 200 символов(имена,заголовки)
    date_added = models.DateTimeField(default=datetime.now, blank=True)#атрибут автоматического отображения текущей даты и времени
    owner = models.ForeignKey(User,on_delete=models.CASCADE)#инициализация пользователя
    def __str__(self): #функция автоматического отображения темы 
        return self.text


    
class Entry(models.Model):
    """Иформация изученна пользователм по теме"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) #Внешний ключ, который связыва записи одной темы(укаждой темы свой ключ
    text = models.TextField()#произвольный набор текста
    date_added = models.DateTimeField(default=datetime.now, blank=True)#время создания темыы
    user = models.ForeignKey(User,on_delete=models.CASCADE)#инициализация пользователя 
    
    class Meta:#Допольнительная информация по управлению моделью Entry 
        verbose_name_plural = 'entries'#Приказ к Django использования форму множественного числа при обращение  к более чем к одной форме
    def __str__(self):#функция вывода первых 50 символов записи 
        return self.text[:100]+ '...'


# Create your models here.

