from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .models import Course, Department, Instructor
from controlescolar.forms import CustomUserCreationForm

# Vistas de paginas
def dashboard(request):
    return render(request, "dashboard.html")

def homepage(request):
    return  render(request, 'homepage.html')

# Vista para el registro de usuarios administradores nuevos

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("homepage"))

# Vistas de paginas que acceden a la DB
class CourseList(ListView):
    model = Course
    context_object_name = ('courses')
    template_name = 'course_list.html'

class DepartmentList(ListView):
    model = Department
    context_object_name = ('departments')
    template_name = 'department_list.html'

class TeachesList(ListView):
    model = Instructor
    context_object_name = ('teachers')
    template_name = 'teaches_list.html'

# Paginas de detalles

class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'details/course_detail.html'

class DeptDetail(DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'details/dept_detail.html'

class TeachesDetail(DetailView):
    model = Instructor
    context_object_name = 'teacher'
    template_name = 'details/teaches_detail.html'

#formularios de creacion

class CourseCreateView(CreateView):
    model = Course
    template_name = 'form/course_form.html'
    fields = ['course_id', 'title', 'dept_name', 'credits']

    def form_valid(self, form):
        messages.success(self.request, "El curso fue creado correctamente.")
        return super(CourseCreateView, self).form_valid(form)

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'form/department_form.html'
    fields = ['dept_name', 'building', 'budget']

    def form_valid(self, form):
        messages.success(self.request, "El departamento fue creado correctamente.")
        return super(DepartmentCreateView, self).form_valid(form)


class InstructorCreateView(CreateView):
    model = Instructor
    template_name = 'form/instructor_form.html'
    fields = ['id', 'name', 'dept_name', 'salary']

    def form_valid(self, form):
        messages.success(self.request, "El instructor fue creado correctamente.")
        return super(InstructorCreateView, self).form_valid(form)

#formularios de Update

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'form/department_form.html'
    fields = ['dept_name', 'building', 'budget']
    success_url = reverse_lazy('departments')

    def form_valid(self, form):
        messages.success(self.request, "El departamento fue actualizado correctamente.")
        return super(DepartmentUpdateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'form/course_form.html'
    fields = ['title', 'dept_name', 'credits']
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        messages.success(self.request, "El curso fue actualizado correctamente.")
        return super(CourseUpdateView, self).form_valid(form)

class InstructorUpdateView(UpdateView):
    model = Instructor
    template_name = 'form/instructor_form.html'
    fields = ['name', 'dept_name', 'salary']
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        messages.success(self.request, "El profesor fue actualizado correctamente.")
        return super(InstructorUpdateView, self).form_valid(form)