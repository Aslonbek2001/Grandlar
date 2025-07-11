# Generated by Django 5.2 on 2025-05-26 06:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_status', models.CharField(choices=[('new', 'Yangi'), ('approved', 'Tasdiqlandi'), ('rejected', 'Rad etildi')], default='new', max_length=10, verbose_name='Ariza holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BallApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SpiritualityBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Kitobxonlik madaniyati (0-20)')),
                ('field2', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name=' "5 muxim tashabbus" doirasidagi to\'garaklarda faol ishtiroki (0-20)')),
                ('field3', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Talabaning akademik o'zlashtirishi (0-10)")),
                ('field4', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va odob-axloq kodeksiga rioya etishi (0-5)")),
                ('field5', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari (0-10)")),
                ('field6', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)")),
                ('field7', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=' Talabalarning "Ma\'rifat darslari" dagi faol ishtiroki (0-10)')),
                ('field8', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Volontyorlik va jamoat ishlaridagi faolligi (0-5)')),
                ('field9', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar (0-5)')),
                ('field10', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi (0-5)')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, verbose_name="Talabaning o'zlshtirish ko'rsatkichi")),
            ],
        ),
    ]
