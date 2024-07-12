from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Medium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name    

class CulturePeriod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ArtPiece(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.CharField(max_length=255, blank=True)
    medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True)
    styles = models.ManyToManyField(Style, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    image = models.ImageField(upload_to='artwork/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class ArchaeoPiece(models.Model):
    title = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    culture_period = models.ForeignKey(CulturePeriod, on_delete=models.SET_NULL, null=True, blank=True)
    production_date = models.CharField(max_length=255, blank=True)
    material = models.CharField(max_length=255)
    technique = models.CharField(max_length=255, blank=True)
    dimensions = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='archaeo/')
    findspot = models.CharField(max_length=255, blank=True)
    current_location = models.CharField(max_length=255, blank=True)

class Gallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='galleries')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    art_pieces = models.ManyToManyField(ArtPiece, through='GalleryArtPiece', related_name='galleries', blank=True)
    archaeological_pieces = models.ManyToManyField(ArchaeoPiece, through='GalleryArchaeoPiece', related_name='galleries', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryArtPiece(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    note = models.TextField(blank=True)

    class Meta:
        unique_together = ('gallery', 'art_piece')

class GalleryArchaeoPiece(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    archaeo_piece = models.ForeignKey(ArchaeoPiece, on_delete=models.CASCADE)
    note = models.TextField(blank=True)

    class Meta:
        unique_together = ('gallery', 'archaeo_piece')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE, null=True, blank=True)
    archaeological_piece = models.ForeignKey(ArchaeoPiece, on_delete=models.CASCADE, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user.username}'
