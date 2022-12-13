from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from datetime import datetime, timedelta
# Create your views here.


def home(request):
    subscribe_fun(request)
    babysitter = BabySitters.objects.all().order_by('-regDate')[:6]

    return render(request, "index.html", context={"babysitters": babysitter})


def services(request):
    subscribe_fun(request)
    services = Service.objects.all()
    return render(request, "services.html",{"services":services})


def babysitters(request):
    subscribe_fun(request)

    babysiter = BabySitters.objects.all()

    return render(request, "babySitter.html", context={"babysitters": babysiter})


def babysitter_detail_page(request, id):
    babysiter = BabySitters.objects.get(id=id)

    return render(request, "babysiter_detail.html", context={"babysitter": babysiter})


def enrollmentForm(request):
    sub = subscribe_fun(request)
    if request.method == "POST" and not sub:
        name = request.POST.get("name", "")
        mobile = request.POST.get("mobile", 0)
        altMobile = request.POST.get("alt-mobile", 0)
        email = request.POST.get("email", "")
        childName = request.POST.get("childName", "")
        childGen = request.POST.get("childGen", "")
        program = request.POST.get("program", "")
        address = request.POST.get("add", "")
        landmark = request.POST.get("landmark", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zipcode = request.POST.get("zipcode", "")
        dob = request.POST.get("dob", "")

        enroll_obj = Enrollment.objects.create(yourName=name,
                                               phoneNumber=mobile,
                                               alternateNumber=altMobile,
                                               email=email,
                                               childName=childName,
                                               childGender=childGen,
                                               dob=dob,
                                               programName=program,
                                               address=address,
                                               state=state,
                                               zipcode=zipcode,
                                               city=city,
                                               landmark=landmark,
                                               )
        enroll_obj.enrollMent_number()
        enroll_obj.save()
        return redirect('home')
    return render(request, "enrollForm.html")


def aboutPage(request):
    subscribe_fun(request)
    about_us = AboutUs.objects.filter().first()
    return render(request, "about.html", context={"a": about_us})


def contact_us(request):
    subscribe_fun(request)
    contact = Contact_us.objects.filter().first()
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        mobile = request.POST.get("mobile", 0)
        email = request.POST.get("email", "")
        msg = request.POST.get("msg", "")
        
        Contact.objects.create(
            first_name=first_name, last_name=last_name, email=email, mobile=mobile, massege=msg)
        return redirect("home")
    return render(request, "contactUs.html", context={"c": contact})


def admin_login(request):
    subscribe_fun(request)
    sub = subscribe_fun(request)
    error = False
    if request.method == "POST" and not sub:
        userId = request.POST.get("email")
        pas = request.POST.get("password", "")

        user = User.objects.filter(
            Q(email=userId) | Q(username=userId)).first()
        if user:
            u = authenticate(username=user.username, password=pas)
            if u:
                login(request, u)
                return redirect("dashboard")
            else:
                error = True
        else:
            error = True
    d = {"error": error}
    return render(request, "admin.html", d)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')


def subscribe_fun(request):
    subscriber_post = False
    if request.method == "POST":
        sub = request.POST.get("subscriber", 0)
        if sub:
            email = request.POST.get('Email', "")
            Subscriber.objects.get_or_create(email=email)
            subscriber_post = True
    return subscriber_post


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    total_baby = BabySitters.objects.all().count()
    totalEnroll = Enrollment.objects.all().count()
    totalSub = Subscriber.objects.all().count()
    newEnrroll = Enrollment.objects.filter(status=None)
    onHoldEnroll = Enrollment.objects.filter(status="onhold")
    acceptedEnroll = Enrollment.objects.filter(status="accept")
    rejectedEnroll = Enrollment.objects.filter(status="rejected")

    d = {"totalbabysitter": total_baby,
         "totalEnroll": totalEnroll, "totalsub": totalSub, "newenrroll": newEnrroll, "onhold": onHoldEnroll, "accepted": acceptedEnroll, "rejected": rejectedEnroll}
    return render(request, "dashboard.html", context=d)


def add_babysiiter(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", 0)
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("satate", "")
        languageKnown = request.POST.get("languageknown", "")
        profile_pic = request.FILES.get("profile-pic", "")
        cert = request.POST.get("certificate", "")
        experiece = request.POST.get("experience", "")
        desc = request.POST.get("discription", "")

        BabySitters.objects.get_or_create(name=name, email=email, mobileNo=mobile, address=address, city=city,
                                          languagesKnown=languageKnown, babySittersExp=experiece, profilePic=profile_pic, certificate=cert, descreption=desc)

        return redirect("dashboard")
    return render(request, "add_babysitter.html")


def manage_babysitter(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    babysitters = BabySitters.objects.all()
    return render(request, "manage_babysitter.html", context={"babysitters": babysitters})


def edit_babysitter(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    babysitter = BabySitters.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", 0)
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")

        languageKnown = request.POST.get("languageknown", "")
        profile_pic = request.FILES.get("profile-pic")
        if not profile_pic:
            profile_pic = babysitter.profilePic

        cert = request.POST.get("certificate", "")
        experiece = request.POST.get("experience", "")
        desc = request.POST.get("discription", "")
        
        babysitter.name = name
        babysitter.email = email
        babysitter.mobileNo = mobile
        babysitter.address = address
        babysitter.city = city
        babysitter.languagesKnown = languageKnown
        babysitter.profilePic = profile_pic
        babysitter.certificate = cert
        babysitter.babySittersExp = experiece
        babysitter.descreption = desc
        babysitter.save()
        return redirect("manage_babysitters")
    return render(request, 'edit_babysitter.html', context={"babysitter": babysitter})


def delete_object(request, object_type, id):
    if object_type == "babysitter":
        babysitter = BabySitters.objects.get(id=id)
        babysitter.delete()
        return redirect("manage_babysitters")
    if object_type == "service":
        service = Service.objects.get(id=id)
        service.delete()
        return redirect("manage_service")
    return redirect("dashboard")


def subscriber(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    subscriber = Subscriber.objects.all()
    return render(request, "subscriber.html", context={"subscriber": subscriber})


def all_enrollment(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enrollments = Enrollment.objects.all()
    return render(request, "all_enrollments.html", context={"enrollments": enrollments})


def enrollment_details(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enrollment = Enrollment.objects.get(id=id)
    if request.method == "POST":
        remark = request.POST.get("remark", "")
        status = request.POST.get("status", "")
        enrollment.remark = remark
        enrollment.status = status
        enrollment.save()
    return render(request, "details_enroll.html", context={"e": enrollment})


def diffrent_enrollment(request, request_type):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request_type == "new_enrollment":
        enrollments = Enrollment.objects.filter(status=None)
    else:
        enrollments = Enrollment.objects.filter(status=request_type)

    return render(request, "enroll_diffrent.html", context={"enrollments": enrollments})


def reports(request):

    show = False
    enrollments, babysitters = "", ""
    if request.method == "POST":
        start_date = request.POST.get('start_date', "")
        end_date = request.POST.get("end_date", "")
        enrollments = Enrollment.objects.filter(
            enrollmentDate__gte=start_date).filter(enrollmentDate__lte=end_date)
        babysitters = BabySitters.objects.filter(
            regDate__gte=start_date).filter(regDate__lte=end_date)

        show = True

    d = {"show": show, "enrollments": enrollments, "babysitters": babysitters}
    return render(request, "report.html", d)


def about_us_edit(request, request_type):
    about_bool, contact_bool = False, False
    about_us, contact_us_d = "", ""
    if request_type == "about_us":
        about_us = AboutUs.objects.filter().first()
        about_bool = True
        if request.method == "POST":
            heading = request.POST.get("heading", "")
            content = request.POST.get("Content", "")
            about_us.heading = heading
            about_us.details = content
            about_us.save()
            return redirect("dashboard")
    else:
        contact_bool = True
        contact_us_d = Contact_us.objects.filter().first()
        if request.method == "POST":
            mobile = request.POST.get("mobile", "")
            address = request.POST.get("address", "")
            email = request.POST.get("email", "")
            contact_us_d.address = address
            contact_us_d.phone = mobile
            contact_us_d.email = email
            contact_us_d.save()

            return redirect("dashboard")
    d = {"a_bool": about_bool, "c_bool": contact_bool,
         "a": about_us, "c": contact_us_d}
    return render(request, "about_us_edit.html", context=d)

def enqury_deatils(request,request_type):
    enquiry = ""
    if request_type == "is_read":
        enquiry = Contact.objects.filter(isRead=True)
    else:
        enquiry = Contact.objects.filter(isRead=False)
    d= {"enquiry":enquiry}
    return render(request,"enqiry.html",d)

def enqury_read(request,id):
    en = Contact.objects.get(id=id)
    en.isRead = True
    en.save()
    return redirect("dashboard")

def add_services(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        service_detail = request.POST.get("service_detail", "")
        service_img = request.FILES.get("service_img")
        
        Service.objects.create(service=name,serviceDetail=service_detail,service_img=service_img)
        return redirect("dashboard")
    return render(request,"add_services.html")

def manage_service(request):
    services = Service.objects.all()
    return render(request,"manage_services.html",context={"services":services})

def edit_service(request,s_id):
    service = Service.objects.get(id = s_id)
    if request.method == "POST":
        name = request.POST.get("name","")
        service_detail = request.POST.get("service_detail", "")
        service_img = request.FILES.get("service_img")
        service.service = name
        service.serviceDetail = service_detail
        if not service_img:
            service_img = service.service_img
        service.service_img = service_img

        service.save()
        return redirect("manage_service")

    return render(request,"edit_service.html",context={"service":service})

def filter_enrollments(request,enroll_id):
    enrollments = Enrollment.objects.filter(enrollNumber__icontains= enroll_id)
    return render(request,"enrollment_filter.html",context={"enrollments":enrollments})

def reset_password(request):
    error = False
    if request.method =="POST":
        o_pass = request.POST.get("c_password","")
        n_pass = request.POST.get("n_password","")
        u = authenticate(username = request.user,password=o_pass)
        if u:
            u.set_password(n_pass)
            u.save()
            login(request,u)
            return redirect("dashboard")
        else:
            error = True
    
            

    return  render(request,"reset_password.html",context={"error":error})