# Generated by Django 3.0.4 on 2020-06-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200614_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Returned', 'Returned')], max_length=20),
        ),
    ]