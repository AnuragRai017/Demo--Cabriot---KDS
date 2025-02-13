# Generated by Django 5.1.2 on 2024-10-26 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal_period', models.CharField(choices=[('BL', 'Breakfast/Lunch'), ('D', 'Dinner')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='DisplaySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('vegetable', 'Vegetable Section'), ('main', 'Main Section'), ('bread', 'Bread Section')], max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='ingredients/')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='menu_items/')),
            ],
        ),
        migrations.CreateModel(
            name='QuantityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('g', 'Grams'), ('kg', 'Kilograms'), ('num', 'Numbers')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='DisplayItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='displays.dailydisplay')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='displays.displaysection')),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='displays.ingredient')),
                ('menu_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='displays.menuitem')),
                ('quantity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='displays.quantitytype')),
            ],
        ),
    ]
