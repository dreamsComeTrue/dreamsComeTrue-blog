from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import personal_blog.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", personal_blog.views.index, name="index"),
    path("godot/", personal_blog.views.godot, name="godot"),
    path("db/", personal_blog.views.db, name="db"),
    path("admin/", admin.site.urls),
]
