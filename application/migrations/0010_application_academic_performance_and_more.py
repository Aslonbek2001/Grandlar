# Generated by Django 5.2 on 2025-06-26 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_alter_spiritualityball_field1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='academic_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name="Akademik o'zlashtirish ko'rsatkichi (GPA*2)"),
        ),
        migrations.AddField(
            model_name='application',
            name='attendance',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name="Talabaning darslarga to'liq va kechikmasdan kelishi (0-5)"),
        ),
        migrations.AddField(
            model_name='application',
            name='cultural_visits',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Teatr va muzey, xiyobon, kino, tarixiy qadamjolarga tashriflar'),
        ),
        migrations.AddField(
            model_name='application',
            name='enlightenment_classes',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Talabaning "Ma\'rifat darslari"dagi faol ishtiroki'),
        ),
        migrations.AddField(
            model_name='application',
            name='five_initiatives',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='"5 muhim tashabbus" doirasidagi to\'garaklarda faol ishtiroki'),
        ),
        migrations.AddField(
            model_name='application',
            name='manners',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name="Talabaning oliy ta'lim tashkilotining ichki tartib qoidalari va Odob-axloq kodeksiga rioya etishi (0-5)"),
        ),
        migrations.AddField(
            model_name='application',
            name='participation_in_events',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name="Xalqaro, respublika, viloyat miqyosidagi ko'rik-tanlov, fan olimpiadalari va sport musobaqalarida erishgan natijalari"),
        ),
        migrations.AddField(
            model_name='application',
            name='reading_culture',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Kitobxonlik madaniyati'),
        ),
        migrations.AddField(
            model_name='application',
            name='spiritual_enlightenment',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name="Ma'naviy-ma'rifiy sohaga oid boshqa yo'nalishlardagi faoliyati"),
        ),
        migrations.AddField(
            model_name='application',
            name='sports_activity',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Talabalarning sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi'),
        ),
        migrations.AddField(
            model_name='application',
            name='volunteer_work',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Volontyorlik va jamoat ishlaridagi faolligi'),
        ),
    ]
