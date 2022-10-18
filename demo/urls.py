from django.urls import path
from . import views
from demo.views import *

urlpatterns = [
    path('export_data_to_excel/',export_data_to_excel),
    path('import_data_to_db/',import_data_to_db),
]