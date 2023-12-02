# users/urls.py

from django.urls import path
from controlescolar.views import dashboard, CourseList, DepartmentList, homepage, TeachesList, CourseDetail, TeachesDetail, DeptDetail, register
from controlescolar.views import DepartmentUpdateView, DepartmentCreateView, CourseUpdateView, CourseCreateView, InstructorUpdateView, InstructorCreateView
from django.urls import include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("registro/", register, name='register'),
    path("dashboard/", dashboard, name="dashboard"),
    path('cursos/', CourseList.as_view(), name='courses'),
    path('departamentos/', DepartmentList.as_view(), name='departments'),
    path('', homepage, name ="homepage"),
    path('instructores', TeachesList.as_view(),name="teachers"),
    path('curso/<str:pk>/',CourseDetail.as_view(),name='course'),
    path('departamento/<str:pk>/',DeptDetail.as_view(),name='department'),
    path('profesor/<str:pk>/',TeachesDetail.as_view(),name='teacher'),
    path('curso/create/', CourseCreateView.as_view(), name='course-create'),
    path('curso/update/<str:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('departamento/create/', DepartmentCreateView.as_view(), name='dept-create'),
    path('departamento/update/<str:pk>/', DepartmentUpdateView.as_view(), name='dept-update'),
    path('profesor/create/', InstructorCreateView.as_view(), name='teacher-create'),
    path('profesor/update/<str:pk>/', InstructorUpdateView.as_view(), name='teacher-update'),

]