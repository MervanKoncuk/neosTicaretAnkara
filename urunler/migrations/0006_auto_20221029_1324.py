# Generated by Django 3.2.12 on 2022-10-29 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_auto_20221029_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='urun',
            name='tek',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='urunler.tek'),
        ),
    ]
