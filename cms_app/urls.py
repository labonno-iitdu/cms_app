from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('add_contact/',views.add_contact,name='add_contact'),
    path('update_contact/',views.update_contact,name='update_contact'),
    path('delete_contact/',views.delete_contact,name='delete_contact'),
    path('others/',views.others,name='others'),
]