# Generated by Django 3.1.7 on 2021-04-02 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210402_0225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='is_whished',
            new_name='is_wished',
        ),
    ]
