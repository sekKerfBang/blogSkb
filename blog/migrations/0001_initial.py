# Generated by Django 5.1.7 on 2025-03-31 15:01

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('img_article', models.ImageField(blank=True, null=True, upload_to='article_img/')),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('auteur', models.CharField(max_length=100)),
            ],
        ),
    ]
