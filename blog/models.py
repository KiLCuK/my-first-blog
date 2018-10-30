from django.db import models
from django.utils import timezone

class Post(models.Model): #bu satır modelimizi tanımlıyor (bir nesne).
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE) #models.ForeignKey - başka bir modele referans tanımlar.
    title=models.CharField(max_length=120) #models.CharField - belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
    text=models.TextField() #models.TextField - bu da uzun metinleri tanımlar. Blog gönderileri için biçilmiş kaftan
    created_date=models.DateTimeField(
        default=timezone.now) #models.DateTimeField - bu da gün ve saati tanımlamada kullanılır.
    published_date=models.DateTimeField(
        blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title