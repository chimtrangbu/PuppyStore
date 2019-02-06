# from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path(
        'api/v1/puppies/<int:pk>',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    path(
        'api/v1/puppies/',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]
