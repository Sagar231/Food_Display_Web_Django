# Generated by Django 4.2.2 on 2023-07-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://i0.wp.com/servedcatering.com/wp-content/uploads/2021/05/menu-item-placeholder.png?ssl=1', max_length=500),
        ),
    ]
