# Generated by Django 2.0 on 2019-05-18 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190517_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='addresses.DeliveryAddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_before',
            field=models.DateField(default=datetime.datetime(2019, 5, 23, 19, 13, 28, 49613, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
    ]
