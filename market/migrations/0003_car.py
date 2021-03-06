# Generated by Django 2.2.5 on 2019-12-12 04:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0002_auto_20191210_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('carId', models.AutoField(primary_key=True, serialize=False)),
                ('carName', models.CharField(max_length=50)),
                ('carDescription', models.CharField(max_length=1000)),
                ('carPostDate', models.DateField(default=datetime.date.today)),
                ('carPrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('carPicUrl', models.URLField(blank=True)),
                ('carBrand', models.CharField(max_length=500)),
                ('carMillege', models.CharField(max_length=50)),
                ('carYears', models.DateField(default=datetime.date.today)),
                ('carAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
