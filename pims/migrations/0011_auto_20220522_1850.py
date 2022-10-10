# Generated by Django 3.2.11 on 2022-05-23 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pims', '0010_auto_20220403_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='items',
            field=models.ManyToManyField(through='pims.item_container', to='pims.item'),
        ),
        migrations.AlterField(
            model_name='item_container',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pims.container'),
        ),
        migrations.AlterField(
            model_name='item_container',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pims.item'),
        ),
        migrations.AlterUniqueTogether(
            name='item_container',
            unique_together={('item', 'container')},
        ),
    ]