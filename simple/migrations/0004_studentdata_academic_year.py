# Generated by Django 4.1.2 on 2023-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0003_studentdata_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='Academic_year',
            field=models.CharField(default='2023', max_length=255),
        ),
    ]
