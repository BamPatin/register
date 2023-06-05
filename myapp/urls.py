from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index), #(ชื่อpath,กระบวนการทำงาน)
    path('about',views.about),  #login
    path('form',views.form),
    path('edit/<person_id>',views.edit), ##(ชื่อpath/<ชื่อพารามิเตอร์>,กระบวนการทำงาน)
    path('delete/<person_id>',views.delete),
    path('logincheck',views.logincheck)

]