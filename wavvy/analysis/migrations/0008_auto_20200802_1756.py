# Generated by Django 2.1.5 on 2020-08-02 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_auto_20200802_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_name', models.CharField(max_length=100)),
                ('lat', models.FloatField(max_length=100)),
                ('lng', models.FloatField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='airTemperature',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='gust',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='precipitation',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='spot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spot', to='analysis.Spot'),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='waterTemperature',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='waveDirection',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='waveHeight',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='wavePeriod',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forcastdata',
            name='windDirection',
            field=models.FloatField(max_length=100),
        ),
    ]
