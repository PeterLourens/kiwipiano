from django.contrib import admin
from .models import Booking,  Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'session_name', 'date', 'booked_date')
    list_filter = ('user', 'date')
    search_fields = ['lesson_name', 'user']



    def confirmed_booking(self, queryset):
        queryset.update(confirmed=True)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone_number')
    list_filter = ('user',)
    search_fields = ('user', 'phone_number')



