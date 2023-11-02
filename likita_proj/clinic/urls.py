from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import AppointmentSitemap, UserPannelSitemap, StaffPannelSitemap


sitemaps = {
    'booking':AppointmentSitemap,
    'userPanel': UserPannelSitemap,
    'staffPanel' : StaffPannelSitemap
    #add DynamicSitemap to the dictionary
    
    # 'static':StaticSitemap, #add StaticSitemap to the dictionary
    
}
urlpatterns = [
    
    path('booking_sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('booking/', views.book_an_appointment, name='booking'),
    path('booking-submit/', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel/', views.userPanel, name='userPanel'),
    path('user-update/<str:pk>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<str:pk>/', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel/', views.staffPanel, name='staffPanel'),
    
]
