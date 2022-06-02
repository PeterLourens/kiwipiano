from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'date', 'start_time', 'lesson_name')
    list_filter = ('user', 'date')
    search_fields = ['lesson_name', 'user']



    def confirmed_booking(self, queryset):
        queryset.update(confirmed=True)





