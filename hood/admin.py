from django.contrib import admin
from .models import NeighbourHood,Profile, Business, Post

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)