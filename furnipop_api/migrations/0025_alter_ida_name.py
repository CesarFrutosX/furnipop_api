# Generated by Django 4.1.4 on 2023-02-01 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0024_alter_itemspedidos_ida_alter_itemspedidos_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemspedidos',
            name='idA',
            field=models.IntegerField(db_column='idA', primary_key=True, serialize=False),
        ),
        migrations.RenameField(
            model_name='itemspedidos',
            old_name='idA',
            new_name='id',
        ),

    ]
