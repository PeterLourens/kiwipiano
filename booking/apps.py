from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'


    # to connect the receivers in the ready method
    def ready(self):
        import booking.signals
