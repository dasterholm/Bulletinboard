# Generated by Django 4.2.3 on 2023-07-18 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theWowAdv', '0002_response_title_alter_advertisement_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='responseAdvertisement',
            new_name='advert',
        ),
    ]
