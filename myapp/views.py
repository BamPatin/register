from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db.models import Q



# Create your views here.
def index(request) :
    all_person = Person.objects.all()
    # all_person = Person.objects.filter(email__contains='a')  
    # all_person = Person.objects.filter(email__istartswith='b')  
    # all_person = Person.objects.filter(email__endswith='n')
    # all_person = Person.objects.filter(Q(email__istartswith='b') & Q(email__endswith ='m'))  
    # all_person = Person.objects.filter(age =22)  
    # all_person = Person.objects.filter(email__contains='@gmail')
    # Loop through the objects and update the email field
    for obj in all_person:
        obj.email = obj.email.replace('@gmail', '@actuarialbiz')
        obj.save()

    return render(request,"index.html",{"all_person":all_person})

def loginform(request) :
    return render(request,"login.html")

def form(request) :
    if request.method == "POST" :
        #รับข้อมูล
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        image = request.POST["image"]

        #บันทึกข้อมูล
        person = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender = gender,
            username = username,
            email = email,
            image = image
            # password = password
        )
        person.set_password(password)  #แปลงpasswordเป็นการเข้ารหัส
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
        person.first_name = request.POST["first_name"]           #แก้ไขข้อมูลใหม่ตามที่ส่งมาจากแบบฟอร์ม
        person.last_name = request.POST["last_name"]           #แก้ไขข้อมูลใหม่ตามที่ส่งมาจากแบบฟอร์ม
        person.age = request.POST["age"]
        person.gender = request.POST["gender"]
        person.username = request.POST["username"]
        person.email = request.POST["email"]
        person.password = request.POST["password"]
        person.image = request.POST["image"]
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

def login(request) :
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        #ระบบ login ปลอมๆ
        # try:
        #     user = Person.objects.get(username=username , password=password)
        # except:
        #     user = None
        user = auth.authenticate(username=username , password=password)
        if user is not None :
            auth.login(request, user)
            messages.success(request,"เข้าสู่ระบบสำเร็จ")
            return redirect('/')
        else :
            messages.success(request,"ไม่สามารถเข้าสู่ระบบได้")
            return redirect('/login')
    #else:
    #   form = LoginForm()
    return render(request, 'login.html', {'form': form})


