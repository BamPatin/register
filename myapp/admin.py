from django.contrib import admin
from myapp.models import Person ,Author
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ('display_image',)
    
    # # def display_image(self, obj):
    # #     return obj.image_tag()

    # # display_image.short_description = 'Image'
    
    list_display = ("first_name", "last_name", "age","gender","show_image",) # field ที่จะแสดง
    # list_per_page = 3              #แสดงข้อมูลหน้าละ3row
    # list_editable = ["age"]           #แก้ไขข้อมูลในหน้าแรก
    # list_filter = ['email']                     # filter
    # search_fields = ['first_name']    # ให้ไปค้นหาที่ field ไหน
    # prepopulated_fields = {'name' : ['first_name']}   # เพิ่ม field ใหม่จาก field ที่มีอยู่
    # field = ["a","b","c"]  #เรียงฟิลด์ใหม่สำหรับรับข้อมูล
    fieldsets = (
        (None,{'fields':['first_name','last_name','age','username','email','password','gender','image']}),
        ('category',{'fields':['last_login'], 'classes':['collapse']}),
        ) #รวมกลุ่มfieldที่ใช้ด้วยกันไว้ด้วยกัน

admin.site.register(Person, UserAdmin)   #เรียกใช้ตาราง person บนหน้า admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')

admin.site.register(Author, AuthorAdmin)

