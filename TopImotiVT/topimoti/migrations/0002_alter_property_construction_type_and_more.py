# Generated by Django 4.2.18 on 2025-03-10 17:46

import TopImotiVT.topimoti.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topimoti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='construction_type',
            field=models.CharField(choices=[('Тухла', 'Тухла'), ('Панел', 'Панел'), ('Монолит', 'Монолит')], max_length=50, verbose_name='Вид строителство'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена в евро'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[TopImotiVT.topimoti.validators.validate_file_size]),
        ),
    ]
