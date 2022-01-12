from django.urls import path
from HR.view import *

app_name = "HR"
urlpatterns = [
	path('API/APIPersonnel', ApiPersonnel.as_view(), name="APIPersonnel"),
	path('API/ApiLISTPersonnel', ApiLISTPersonnel.as_view(), name="ApiLISTPersonnel"),
	path('API/APIPost', APIPost.as_view(), name="APIPost"),
	path('API/APIGroup', APIGroup.as_view(), name="APIGroup"),
	path('API/APIFieldofStudy', APIFieldofStudy.as_view(), name="APIFieldofStudy"),
	path('API/APIListTopOrganization', APIOrganization.as_view(), name="APIListTopOrganization"),

	path('API/APIPersonnelWithFilterGroup/<int:IdGroup>', ApiPersonnelFilterGroup.as_view(), name="APIPersonnelWithFilterGroup"),
	path('Upload', Upload.as_view(), name="Upload"),
	path('CreatePersonnel', CreatePersonnel.as_view(), name="CreatePersonnel"),
	path('ApiUpdatePersonnel/<int:pk>', ApiUpdatePersonnel.as_view(), name="ApiUpdatePersonnel"),
	path('ListPersonnel', ListPersonnel.as_view(), name="ListPersonnel"),
	path('UpdatePersonnel/<int:pk>', UpdatePersonnel.as_view(), name="UpdatePersonnel"),
	
	#path('H/PersonnelUpload', PersonnelCreate.as_view(), name="list"),
]