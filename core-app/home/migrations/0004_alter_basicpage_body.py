# Generated by Django 5.1.4 on 2024-12-11 10:50

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_basicpage_eventpage_gallerypage_news_newspage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', 0), ('paragraph', 1), ('image', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title'}), 1: ('wagtail.blocks.RichTextBlock', (), {}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {})}, null=True),
        ),
    ]
