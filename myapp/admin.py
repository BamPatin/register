from django.contrib import admin
from myapp.models import Person
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age","gender","show_image",) # field ที่จะแสดง
    # list_filter = ['email']                     # filter
    # search_fields = ('first_name', 'email')    # ให้ไปค้นหาที่ field ไหน
    # prepopulated_fields = {'name' : ['first_name']}   # เพิ่ม field ใหม่จาก field ที่มีอยู่
    fieldsets = (
        (None,{'fields':['first_name','last_name','age','username','email','password','gender','image']}),
        ('category',{'fields':['last_login'], 'classes':['collapse']}),
        ) #รวมกลุ่มfieldที่ใช้ด้วยกันไว้ด้วยกัน

admin.site.register(Person, UserAdmin)   #เรียกใช้ตาราง person บนหน้า admin




