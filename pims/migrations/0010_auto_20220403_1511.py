# Generated by Django 3.2.11 on 2022-04-03 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pims', '0009_auto_20210829_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='items',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.CreateModel(
            name='item_container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pims.container')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pims.item')),
            ],
        ),
    ]