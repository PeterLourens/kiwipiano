from django.contrib import admin
from .models import Booking, Session, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'date')
    list_filter = ('user', 'date')
    search_fields = ['lesson_name', 'user']



    def confirmed_booking(self, queryset):
        queryset.update(confirmed=True)



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_name', 'session_date', 'start_time', 'session_status')
    list_filter = ('session_date', 'session_name')
    search_fields = ('session_status', 'session_name')



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user','phone_number')
    list_filter = ('user',)
    search_fields = ('user', 'phone_number')



