from django.urls import path
from main_app.views import MainView

urlpatterns = [
    path('index/', MainView.as_view(), name="form_profile")
]
