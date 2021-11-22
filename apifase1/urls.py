"""apifase1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from girls.views import  CursosAdminView, CursosaAdminViewDetail, AulasAdminView, AulasaAdminViewDetail, UserAdminView, UseraAdminViewDetail
from girls.views import ProfessorCursoView, ProfessorCursoViewDetail, ProfessorAulasView, AlunoCursoView, ProfessorAulasDetailView, AlunoCursoDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path("api/admin/cursos", CursosAdminView.as_view(), name="CursosAdmin"),
    path("api/admin/user", UserAdminView.as_view(), name="UserAdmin"),
    path("api/admin/aulas", AulasAdminView.as_view(), name="AulasAdmin"),
    path("api/professor/cursos", ProfessorCursoView.as_view(), name="Professorcursosview"),
    path("api/professor/aulas", ProfessorAulasView.as_view(), name="Professoraulasview"),
    path("api/professor/cursos/<int:pk>", ProfessorCursoViewDetail.as_view(), name="Professorcursosdetail"),
    path("api/professor/aulas/<int:pk>", ProfessorAulasDetailView.as_view(), name="Professoraulasdetailview"),
    path("api/alunos/cursos", AlunoCursoView.as_view(), name="Alunoscursosview"),
    path("api/alunos/cursos/<int:pk>", AlunoCursoDetailView.as_view(), name="Alunocursodetailview"),
    path("api/admin/cursos/<int:pk>", CursosaAdminViewDetail.as_view(), name="CursosAdmindetail"),
    path("api/admin/user/<int:pk>", UseraAdminViewDetail.as_view(), name="UserAdmindetail"),
    path("api/admin/aulas/<int:pk>", AulasaAdminViewDetail.as_view(), name="AulasAdmindetail"),

]
