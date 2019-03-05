# Generated by Django 2.1.7 on 2019-03-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price_ebook',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_ebook',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_new',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_used',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('S', 'Sell'), ('D', 'New Shipment'), ('R', 'Rent'), ('G', 'Got back book from rent')], default='S', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Genre name'),
        ),
    ]