# Generated by Django 2.2.7 on 2019-12-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_banner_smallofferreplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='smallOffer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Первый заголовок на баннере (чтобы выделить цветом слово или фразу используйте выражение : @@текст## )'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='smallOfferReplaced',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
