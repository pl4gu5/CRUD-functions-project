# Generated by Django 5.0.6 on 2024-06-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='project_start_date',
            field=models.DateTimeField(),
        ),
    ]
