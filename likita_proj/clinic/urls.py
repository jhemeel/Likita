from django.urls import path
from . import views

urlpatterns = [
    path('booking', views.book_an_appointment, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<str:pk>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<str:pk>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    
]
