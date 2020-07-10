# Generated by Django 2.2.14 on 2020-07-06 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('nearest_station', models.CharField(max_length=100)),
                ('rent', models.IntegerField()),
                ('security_deposit', models.IntegerField()),
                ('rent_type', models.CharField(choices=[('RENT', 'Rent'), ('SUB RENT', 'Sub Rent')], default='RENT', max_length=10)),
                ('share_type', models.CharField(choices=[('Full apartment', 'Full apartment'), ('Sharing apartnent', 'Sharing apartnent'), ('Room sharing', 'Room sharing'), ('Studio', 'Studio')], default='Full apartment', max_length=100)),
                ('size_of_full_apartment', models.IntegerField()),
                ('available_from', models.DateTimeField()),
                ('description', models.CharField(max_length=1024)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
