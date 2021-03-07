"""URL for blogs"""

from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page blog
    path('blog/', views.blog, name='blog'),
    # Page add new post
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:text_id>', views.edit_post, name='edit_post')
]