# Generated by Django 5.2 on 2025-04-17 12:29

import datetime
import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.AlterModelOptions(
            name='adminuser',
            options={'verbose_name': 'Admin', 'verbose_name_plural': 'Admins'},
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('r_id', models.IntegerField(db_index=True)),
                ('number', models.CharField(db_index=True, max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='FavouriteRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications_enabled', models.BooleanField(default=False)),
                (
                    'route',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='favourited_by', to='app.route'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Favourite route',
                'verbose_name_plural': 'Favourite routes',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_id', models.IntegerField(db_index=True)),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.city')),
            ],
            options={
                'verbose_name': 'Stop',
                'verbose_name_plural': 'Stops',
            },
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(db_index=True, default='', max_length=1)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.route')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stop')),
            ],
            options={
                'verbose_name': 'RouteStop',
                'verbose_name_plural': 'RouteStops',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(through='app.RouteStop', to='app.stop'),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('garage_number', models.CharField(db_index=True, max_length=128)),
                (
                    'type',
                    models.IntegerField(choices=[(1, 'Автобус'), (2, 'Троллейбус'), (3, 'Трамвай')], db_index=True),
                ),
                ('state_number', models.CharField(db_index=True, max_length=128)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.city')),
                (
                    'route',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name='transports', to='app.route'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Transport',
                'verbose_name_plural': 'Transports',
            },
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_tag_id', models.BigIntegerField(db_index=True)),
                ('is_actual', models.BooleanField(db_index=True, default=True)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transport')),
            ],
            options={
                'verbose_name': 'QR code',
                'verbose_name_plural': 'QR codes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=32, unique=True)),
                ('chat_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.city')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='PastRide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'verbose_name': 'Past ride',
                'verbose_name_plural': 'Past rides',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                (
                    'days',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ('mon', 'ПН'),
                                ('tue', 'ВТ'),
                                ('wed', 'СР'),
                                ('thu', 'ЧТ'),
                                ('fri', 'ПТ'),
                                ('sat', 'СБ'),
                                ('sun', 'ВС'),
                            ],
                            max_length=15,
                        ),
                        size=None,
                    ),
                ),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                (
                    'interval',
                    models.DurationField(
                        choices=[
                            (datetime.timedelta(seconds=300), '5'),
                            (datetime.timedelta(seconds=600), '10'),
                            (datetime.timedelta(seconds=900), '15'),
                            (datetime.timedelta(seconds=1200), '20'),
                        ]
                    ),
                ),
                (
                    'favourite_route',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.favouriteroute'),
                ),
                (
                    'stop',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='notifications_stops', to='app.stop'
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='app.user'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.AddField(
            model_name='favouriteroute',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='favourite_routes', to='app.user'
            ),
        ),
    ]
