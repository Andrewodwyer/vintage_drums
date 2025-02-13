# Generated by Django 5.1.3 on 2024-12-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_stickdetail_material_alter_stickdetail_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickdetail',
            name='material',
            field=models.CharField(blank=True, choices=[('maple', 'Maple'), ('hickory', 'Hickory'), ('oak', 'Oak'), ('carbon_fiber', 'Carbon Fiber')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stickdetail',
            name='size',
            field=models.CharField(blank=True, choices=[('7A', '7A'), ('5A', '5A'), ('5B', '5B'), ('2B', '2B')], max_length=50, null=True),
        ),
    ]
