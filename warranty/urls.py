from django.contrib import admin
from django.urls import path
from . import views

app_name = "warranty"
urlpatterns = [
    path('', views.ItemListView.as_view(template_name='warranty/index.html'), name = "index"),
    path('notes', views.NoteListView.as_view(), name = 'notes'),    
]

#NOTES URLS:
urlpatterns += [  
    # path('note/create/', views.NoteCreate.as_view(), name='note_create'),
    path('notes/create/', views.CreateNote, name='note_create'),
    path('notes/detail/<int:pk>', views.NoteDetail, name='note_detail'),
    path('notes/update/<int:pk>', views.NoteUpdate.as_view(), name='note_update'),
    path('notes/delete/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),
    # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

#ITEMS URLS:
urlpatterns += [    
    path('items/add/', views.AddItem, name = 'item_add'),
    path('items', views.ItemListView.as_view(), name = 'items'),
    path('items/<int:pk>', views.ItemDetailView.as_view(), name = 'item_detail'),
    path('items/edit/<int:pk>', views.ItemUpdate.as_view(), name = 'item_edit'),
    path('items/delete/<int:pk>', views.ItemDelete.as_view(), name = 'item_delete'),
]

#ITEM LOG URLS:
urlpatterns += [    
    path('log/add/', views.LogCreate, name = 'log_add'),
    path('log/delete/<int:pk>', views.ItemLogDelete.as_view(), name = 'log_delete'),
    
]