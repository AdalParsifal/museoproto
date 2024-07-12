# Generated by Django 5.0.6 on 2024-07-04 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museodataproto', '0002_remove_artpiece_genre_remove_artpiece_style_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='GalleryArtPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curator_notes', models.TextField(blank=True)),
                ('art_piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museodataproto.artpiece')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museodataproto.gallery')),
            ],
            options={
                'unique_together': {('gallery', 'art_piece')},
            },
        ),
        migrations.AlterField(
            model_name='gallery',
            name='art_pieces',
            field=models.ManyToManyField(blank=True, related_name='galleries', through='museodataproto.GalleryArtPiece', to='museodataproto.artpiece'),
        ),
    ]
