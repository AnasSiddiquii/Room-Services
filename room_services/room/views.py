from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from .models import *


# main
def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def room_view(request):
    data = Room.objects.all()
    d = {'data':data}   
    return render(request,'main/room_view.html',d)

def contact(request):
    return render(request,'main/contact.html')

def register(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        dob = request.POST['dob']
        p = request.POST['pwd']
        g = request.POST['gender']
        i = request.FILES['profile_pic']
        try:
            user= User.objects.create_user(first_name=fn,last_name=ln,username=e,password=p)
            Signup.objects.create(user=user,mobile=c,image=i,gender=g,dob=dob)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'main/register.html',d)

def login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pswd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                auth.login(request,user)
                error="not"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'main/login.html',d)


# admin
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'admin/admin_home.html')

def view_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Signup.objects.all()
    d= {'data':data}
    return render(request,'admin/view_user.html',d)

def delete_user(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('view_user')

def view_room_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Room.objects.all()
    d = {'data':data}
    return render(request,'admin/view_room_admin.html',d)

def edit_room(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    data = Room.objects.get(id=id)
    if request.method == 'POST':
        rno = request.POST['roomno']
        p = request.POST['price']
        rt = request.POST['rtype']
        s = request.POST['status']
        data.room_no=rno
        data.type=rt
        data.status=s
        data.price=p
        try:
            data.save()
            error="no"
        except:
            error="yes"
        try:
            i = request.FILES['room_img']
            data.image = i
            data.save()
        except:
            pass

    d = {'data':data,'error':error}
    return render(request,'admin/edit_room.html',d)

def delete_room(request,id):
    data = Room.objects.get(id=id)
    data.delete()
    return redirect('view_room_admin')

def add_room(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        n = request.POST['roomno']
        p = request.POST['price']
        rt = request.POST['rtype']
        s = request.POST['status']
        i = request.FILES['image']
        try:
            Room.objects.create(room_no=n,image=i,type=rt,status=s,price=p)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'admin/add_room.html',d)

def view_booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'admin/view_booking.html',d)

def change_status(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    data = Booking.objects.get(id=id)
    if request.method == 'POST':
        s = request.POST['rstatus']
        data.status = s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'admin/change_status.html',d)

def delete_booking(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('view_booking')

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Feedback.objects.all()
    d={"data":data}
    return render(request,'admin/view_feedback.html',d)

def delete_feedback(request,id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')

def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method =='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'admin/change_password_admin.html',d)

def logout(request):
    auth.logout(request)
    return redirect('/')


# user
def edit_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    data = User.objects.get(id=request.user.id)
    data2 = Signup.objects.get(user=request.user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        g = request.POST['gender']
        dob = request.POST['dob']
        try:
            i = request.FILES['image']
            data2.image=i
        except:
            pass
        data.first_name=f
        data.last_name=l
        data.username=e
        data.mobile=c
        data.gender=g
        data.dob=dob
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'data2':data2,'error':error}
    return render(request,'user/edit_user.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'user/user_home.html')

def view_room_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Room.objects.all()
    d = {'data':data}
    return render(request,'user/view_room_user.html',d)

def book_room(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    data3 = Room.objects.get(id=id)
    data2 = Signup.objects.get(user=request.user)
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        f = f+" "+l
        e = request.POST['email']
        c1 = request.POST['contact']
        c2 = request.POST['contact2']
        bd = request.POST['booking_date']
        day = request.POST['select_days']
        g = request.POST['gender']
        p = request.POST['price']
        dob = request.POST['dob']
        rn = request.POST['roomno']
        p = int(p) * int(day)
        try:
            Booking.objects.create(room_no=rn,name=f,email=e,dob=dob,gender=g,contact1=c1,contact2=c2,booking_date=bd,total_days=day,price=p,status="Pending")
            error="no"
        except:
            error="yes"
    d = {'data3':data3,'data2':data2,'error':error}
    return render(request,'user/book_room.html',d)

def view_booking_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Booking.objects.all()
    d={"data":data}
    return render(request,'user/view_booking_user.html',d)

def cancel_booking(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('view_booking_user')

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    data = Signup.objects.get(user=request.user)
    if request.method == 'POST':
            n = request.POST['fname']
            e = request.POST['email']
            c = request.POST['mobile']
            f = request.POST['purpose']
            try:
                Feedback.objects.create(name=n,email=e,contact=c,comment=f)
                error="no"
            except:
                error="yes"
    d = {'error':error,'data':data}
    return render(request,'user/feedback.html',d)

def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method =='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'user/change_password_user.html',d)