# Generated by Django 4.1.5 on 2023-01-27 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ord_no',
        ),
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='주문'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='comment',
            table='shinhan_comment',
        ),
    ]
