# Generated by Django 3.2 on 2023-05-15 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20230512_1447'),
        ('pages', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='new',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.new'),
            preserve_default=False,
        ),
    ]
