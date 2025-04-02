from django.db import models # type: ignore
from django.utils import timezone # type: ignore
import uuid

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    img_article = models.ImageField(upload_to='article_img/' , blank=True, null=True)
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f'nom de l\'article : {self.titre} et son auteur : {self.auteur}'