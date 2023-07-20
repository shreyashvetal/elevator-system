# Generated by Django 4.2.3 on 2023-07-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Operational'), (2, 'Maintenance')], default=1)),
                ('direction', models.SmallIntegerField(choices=[(1, 'Up'), (2, 'Down'), (3, 'Stop')], default=3)),
                ('current_floor', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
