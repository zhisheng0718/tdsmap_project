# Generated by Django 3.1 on 2020-09-23 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TdsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50, verbose_name='区市町')),
                ('facility', models.CharField(max_length=100, verbose_name='施設名称')),
                ('address', models.CharField(max_length=100, verbose_name='所在地')),
                ('spot', models.CharField(max_length=100, verbose_name='水飲み栓設置場所')),
                ('entry', models.CharField(max_length=100, verbose_name='入場料等')),
                ('type', models.CharField(max_length=50, verbose_name='タイプ')),
                ('jis', models.IntegerField(verbose_name='市区町村コード')),
            ],
        ),
    ]
