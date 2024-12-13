from django.urls import path

from movie.views import movielist_views, songlist_views, booklist_views

urlpatterns = [
    path('movie/', movielist_views.list, name='movielist'),
    path('movie/upload/', movielist_views.upload, name='upload'),
    path('movie/<int:pk>/', movielist_views.detail, name='movielist'),
    path('movie/<int:pk>/update/', movielist_views.update, name='movielist'),
    path('movie/<int:pk>/delete/', movielist_views.delete, name='movielist'),
    
    path('song/', songlist_views.list, name='songlist'),
    path('song/upload/', songlist_views.upload, name='uploadsong'),
    path('song/<int:pk>/', songlist_views.detail, name='songdetail'),
    path('song/<int:pk>/update/', songlist_views.update, name='updatesong'),
    path('song/<int:pk>/delete/', songlist_views.delete, name='deletesong'),
    
    path('book/', booklist_views.list, name='booklist'),
    path('book/upload/', booklist_views.upload, name='uploadbook'),
    path('book/<int:pk>/', booklist_views.detail, name='bookdetail'),
    path('book/<int:pk>/update/', booklist_views.update, name='updatebook'),
    path('book/<int:pk>/delete/', booklist_views.delete, name='deletebook'),

]


   
