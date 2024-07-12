from django.contrib import admin
from .models import (
    Profile,
    Medium,
    Style,
    Genre,
    Author,
    CulturePeriod,
    ArtPiece,
    ArchaeoPiece,
    Gallery,
    GalleryArtPiece,
    GalleryArchaeoPiece,
    Favorite,
    Comment,
    Like,
)

admin.site.register(Profile)
admin.site.register(Medium)
admin.site.register(Style)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(CulturePeriod)
admin.site.register(ArtPiece)
admin.site.register(ArchaeoPiece)
admin.site.register(Gallery)
admin.site.register(GalleryArtPiece)
admin.site.register(GalleryArchaeoPiece)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Like)
