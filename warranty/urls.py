from django.contrib import admin
from django.urls import path
from . import views

app_name = "warranty"
urlpatterns = [
    path('', views.index, name = "index"),
    path('notes', views.NoteListView.as_view(), name = 'notes'),    
]

#NOTES URLS:
urlpatterns += [  
    path('note/create/', views.NoteCreate.as_view(), name='note_create'),
    path('note/detail/<int:pk>', views.NoteDetail, name='note_detail'),
    path('note/update/<int:pk>', views.NoteUpdate.as_view(), name='note_update'),
    # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
#ITEMS URLS:
urlpatterns += [    
    path('items/add/', views.AddItem, name = 'item_add'),
    path('items', views.ItemListView.as_view(), name = 'items'),
    path('items/edit/<int:pk>', views.ItemUpdate.as_view(), name = 'item_edit'),
]