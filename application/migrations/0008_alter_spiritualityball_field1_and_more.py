# Generated by Django 5.2 on 2025-06-26 06:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_spiritualityball_field1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiritualityball',
            name='field1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Kitobxonlik madaniyati (0-20)'),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field10',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi (0-5)'),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field11',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name="Manaviy-ma'rifiy sohaga oid boshqa yo'nalishlardagi faoligi (0-5)"),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name=' "5 muxim tashabbus" doirasidagi to\'garaklarda faol ishtiroki (0-20)'),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Talabaning akademik o'zlashtirishi (0-10)"),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va odob-axloq kodeksiga rioya etishi (0-5)"),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari (0-10)"),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)"),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field7',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=' Talabalarning "Ma\'rifat darslari" dagi faol ishtiroki (0-10)'),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field8',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Volontyorlik va jamoat ishlaridagi faolligi (0-5)'),
        ),
        migrations.AlterField(
            model_name='spiritualityball',
            name='field9',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar (0-5)'),
        ),
    ]
