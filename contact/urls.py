from django.urls import path
from . import views

urlpatterns = [
    path('',                          views.portfolio,          name='portfolio'),
    path('api/contact/',              views.contact_api,        name='contact_api'),
    path('messages/',                 views.messages_dashboard, name='messages_dashboard'),
    path('messages/<int:pk>/read/',   views.mark_read,          name='mark_read'),
    path('messages/<int:pk>/delete/', views.delete_message,     name='delete_message'),
]
