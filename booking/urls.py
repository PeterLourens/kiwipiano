from django.urls import path
from . import views
from booking.views import(
    BookingDetailView, 
    BookingUpdateView,
) 


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('booking_login/', views.booking_login, name='booking_login'),
    path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_detail/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking_update/<int:pk>/', views.BookingUpdateView.as_view(), name='booking_update'),
    #path('booking_update_success/<int:pk>/', views.BookingUpdateSuccessView.as_view(), name='booking_update_success'),
    #path('booking_delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),
    path('booking_delete/<int:pk>/', views.booking_delete, name='booking_delete'),
   
    
   
   
]