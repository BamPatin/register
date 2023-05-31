from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request) :
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_person})

def about(request) :
    return render(request,"about.html")

def form(request) :
    if request.method == "POST" :
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        #บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/")

    else:
        return render(request,"form.html")
    
def edit(request,person_id) :
    if request.method == "POST" :
    #เมื่อมีการส่งข้อมูลมา
        person = Person.objects.get(id=person_id)     #ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person.name = request.POST["name"]           #แก้ไขข้อมูลใหม่ตามที่ส่งมาจากแบบฟอร์ม
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"อัพเดทข้อมูลเรียบร้อย")
        return redirect("/")
    else :
    #ถ้าไม่มีการส่งข้อมูลมาใช้ข้อมูลเดิม
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def delete(request,person_id) :
    person = Person.objects.get(id=person_id)     #ดึงข้อมูลประชากรที่ต้องการแก้ไข
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")