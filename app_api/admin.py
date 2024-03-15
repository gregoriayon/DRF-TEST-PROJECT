from django.contrib import admin
from app_api.models import *

# Register your models here.

admin.site.site_header = "Rest API Test Application"

class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'roll', 'name', 'mark', 'email',)

admin.site.register(StudentsModel, StudentsModelAdmin)


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'salary', 'department',)

admin.site.register(EmployeeModel, EmployeeModelAdmin)

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)

admin.site.register(PersonModel, PersonModelAdmin)


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)

admin.site.register(PlayerModel, PlayerModelAdmin)


class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender',)

admin.site.register(Singer, SingerAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_singer', 'duration',)

    @admin.display(ordering='id', description='Singer')
    def get_singer(self, obj):
        return obj.singer.name

admin.site.register(Song, SongAdmin)