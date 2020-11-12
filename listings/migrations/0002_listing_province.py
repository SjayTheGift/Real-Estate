# Generated by Django 3.1.3 on 2020-11-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='province',
            field=models.CharField(choices=[('EC', 'Eastern Cape'), ('FS', 'Free State'), ('GP', 'Gauteng'), ('KZN', 'KwaZulu-Natal'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'), ('NC', 'Northern Cape'), ('NW', 'North West'), ('WC', 'Western Cape')], default='Eastern Cape', max_length=200),
            preserve_default=False,
        ),
    ]