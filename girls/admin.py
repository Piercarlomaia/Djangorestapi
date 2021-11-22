from django.contrib import admin
from django.contrib.auth.models import User
from .models import cursos, aulas, User2

# Register your models here.
admin.site.register(User2)

admin.site.register(cursos)
admin.site.register(aulas)