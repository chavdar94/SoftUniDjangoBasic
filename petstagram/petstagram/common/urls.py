from django.urls import path

from .views import home_page, like_func, copy_link_to_clipboard, add_comment

urlpatterns = [
    path('', home_page, name='home_page'),
    path('like/<int:photo_id>/', like_func, name='photo_like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='photo_share'),
    path('comment/<int:photo_id>/', add_comment, name='add_comment'),
]
