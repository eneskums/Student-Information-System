# Generated by Django 2.2.12 on 2020-05-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_bolumsekreteri_gorulentranskript'),
    ]

    operations = [
        migrations.AddField(
            model_name='mezun',
            name='calismaDurumu',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='idariGorev',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='il',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='isAdresi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='iseBaslamaTarihi',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='maas',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='mezuniyetYili',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='sektor',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='sirketKurumAdi',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='ulke',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mezun',
            name='unvanMeslek',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bolumsekreteri',
            name='oncekiGirisTranskriptMezun',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bolumsekreteri',
            name='oncekiGirisTranskriptOgrenci',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisIs',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisStaj',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisTranskript',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisIs',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisStaj',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisTranskript',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ogretimgorevlisi',
            name='oncekiGirisDersIcerik',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]