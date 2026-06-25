from django.urls import path
from . import views

urlpatterns = [

    path("", views.paper_list, name="paper_list"),

    path("add/", views.add_paper, name="add_paper"),

    path("edit/<int:id>/", views.edit_paper, name="edit_paper"),

    path("delete/<int:id>/", views.delete_paper, name="delete_paper"),

    path("search/", views.public_search, name="public_search"),

]