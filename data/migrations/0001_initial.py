# Generated by Django 3.2.13 on 2022-06-29 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuName',
            fields=[
                ('gubn', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SewerPipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idn', models.CharField(max_length=10)),
                ('gubn_nam', models.CharField(max_length=5)),
                ('mea_ynd', models.DateTimeField()),
                ('mea_wal', models.FloatField()),
                ('sig_sta', models.CharField(max_length=10)),
                ('gubn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.guname')),
            ],
        ),
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raingauge_code', models.CharField(max_length=5)),
                ('raingauge_name', models.CharField(max_length=10)),
                ('gu_code', models.IntegerField()),
                ('gu_name', models.CharField(max_length=5)),
                ('rainfall10', models.FloatField()),
                ('receive_time', models.DateTimeField()),
                ('gubn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.guname')),
            ],
        ),
    ]