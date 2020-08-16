from django.contrib import admin
from django.urls import path
from . import views

app_name = "warranty"
urlpatterns = [
    path('', views.index, name = "index"),
    path('notes', views.NoteListView.as_view(), name = 'notes'),
    path('items', views.ItemListView.as_view(), name = 'items'),
]

#NOTES URLS:
urlpatterns += [  
    path('note/create/', views.NoteCreate.as_view(), name='note_create'),
    path('notes/add/', views.AddNote, name='add_note'),
    path('notes/detail/<int:pk>', views.NoteDetail, name='add_note'),
    # path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
#ITEMS URLS:
urlpatterns += [  
    path('items/edit/<int:pk>', views.ItemUpdate.as_view(), name = 'item_edit'),
    path('items/add/', views.AddItem, name = 'item_add'),
]