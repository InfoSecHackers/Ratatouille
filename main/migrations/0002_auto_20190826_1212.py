# Generated by Django 2.2.1 on 2019-08-26 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='country_id',
        ),
        migrations.AddField(
            model_name='ip',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Country'),
        ),
    ]
