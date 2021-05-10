from django.urls import path
from .views import student, add_mark, results
urlpatterns = [
    path('student/', student),
    path('add_mark/', add_mark),
    path('results/', results)

]