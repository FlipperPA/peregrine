# Generated by Django 2.0.5 on 2018-05-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peregrine', '0007_auto_20180523_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='peregrinesettings',
            name='revisions_to_keep',
            field=models.IntegerField(blank=True, default=None, help_text='The number of revisions to keep. If None, keeps all revisions.', null=True),
        ),
    ]
