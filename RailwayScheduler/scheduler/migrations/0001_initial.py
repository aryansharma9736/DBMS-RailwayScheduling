# Generated by Django 3.1.3 on 2020-11-21 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_km', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100)),
                ('platform_count', models.PositiveIntegerField()),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.staffmember')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.category')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.station')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.route')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.staffmember')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='end_station_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end', to='scheduler.station'),
        ),
        migrations.AddField(
            model_name='route',
            name='start_station_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start', to='scheduler.station'),
        ),
        migrations.CreateModel(
            name='SeatChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('first_class', models.PositiveIntegerField()),
                ('second_class', models.PositiveIntegerField()),
                ('ac', models.PositiveIntegerField()),
                ('sleeper', models.PositiveIntegerField()),
                ('general', models.PositiveIntegerField()),
                ('train_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduler.train')),
            ],
            options={
                'unique_together': {('date', 'train_id')},
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.station')),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.train')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.staffmember')),
            ],
            options={
                'unique_together': {('station_id', 'date')},
            },
        ),
    ]
