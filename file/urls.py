from django.urls import path
from . import views

urlpatterns = [
    path(
        "file/",
        views.FileView.as_view(),
        name="file-upload",
    ),
    # path("home/", views.FormView.as_view(), name="file"),
    # path("home/upload/", views.ProcessaFileView.as_view(), name="upload"),
]
