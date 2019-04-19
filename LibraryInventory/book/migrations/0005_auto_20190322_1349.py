# Generated by Django 2.1.7 on 2019-03-22 18:49

import book.utils.ModelValidators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20190305_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='book_state',
            field=models.CharField(choices=[('N', 'New'), ('U', 'Used'), ('E', 'Ebook')], max_length=1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(help_text='Quantity must be greater than zero', validators=[
                book.utils.ModelValidators.validate_nonzero]),
        ),
    ]
