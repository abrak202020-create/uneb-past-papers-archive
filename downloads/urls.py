from django.urls import path
from . import views

urlpatterns = [

    path("", views.download_list, name="download_list"),

    path("<int:id>/", views.download_paper, name="download_paper"),

]