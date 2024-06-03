# Generated by Django 5.0.6 on 2024-06-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=125)),
                ('project', models.CharField(max_length=100)),
                ('project_discription', models.CharField(max_length=300)),
                ('project_cost', models.CharField(max_length=100)),
                ('project_start_date', models.DateTimeField(auto_now_add=True)),
                ('project_deadLine', models.DateTimeField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
