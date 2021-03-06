# Generated by Django 3.2.4 on 2021-07-21 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=20)),
                ('Employee_Code', models.CharField(max_length=10)),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.position')),
            ],
        ),
    ]
