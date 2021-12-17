from django.urls import path
from HR.view import *

app_name = "HR"
urlpatterns = [
	path('API/APIPersonnel', ApiPersonnel.as_view(), name="APIPersonnel"),
	path('API/APIPost', APIPost.as_view(), name="APIPost"),
	path('API/APIGroup', APIGroup.as_view(), name="APIGroup"),
	path('API/APIFieldofStudy', APIFieldofStudy.as_view(), name="APIFieldofStudy"),

	path('API/APIPersonnelWithFilterGroup/<int:IdGroup>', ApiPersonnelFilterGroup.as_view(), name="APIPersonnelWithFilterGroup"),
]