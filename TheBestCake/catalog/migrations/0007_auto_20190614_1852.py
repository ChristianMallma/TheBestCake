# Generated by Django 2.0.2 on 2019-06-14 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190614_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritocompras',
            name='comprado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='pendiente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carritocompras',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_carrito', to='catalog.Design'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_comentarios', to='catalog.Design'),
        ),
    ]
