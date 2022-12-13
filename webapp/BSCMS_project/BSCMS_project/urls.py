"""BSCMS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from App.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('about/',aboutPage, name="about"),
    path('babysitter/', babysitters,name='babysitter'),
    path('enroll',enrollmentForm, name="enroll"),
    path('services/',services,name="services"),
    path('babysitter_details/<int:id>',babysitter_detail_page,name="babysitte-detail"),
    path('contact_us',contact_us, name="contactUs"),
    path("admin_login",admin_login,name="admin_login"),
    path("dashboard/",dashboard, name="dashboard"),
    path("dashboard/manage_babysitter/",manage_babysitter,name="manage_babysitters"),
    path("dashboard/edit_babysitter/<int:id>",edit_babysitter,name="edit_babysitter"), 
    path("delete/<str:object_type>/<int:id>",delete_object,name="delete_object"),
    path("dashboard/add_babysitter",add_babysiiter,name="add_babysitter"),
    path("dashboard/subscriber",subscriber,name= "subscriber"),
    path("dashboard/all_enroll",all_enrollment,name="all_enroll"),
    path("dashboard/enroll_detail/<int:id>",enrollment_details,name="enroll_detail"),
    path("logout",log_out,name="logout"),
    path("dashboard/diffrent_enroll/<str:request_type>",diffrent_enrollment,name="diff_enroll"),
    path("dashboard/report",reports,name="report"),
    path("dashboard/about_us_edit/<str:request_type>",about_us_edit,name="about_us_edit"),
    path("dashboard/enquiry/<str:request_type>",enqury_deatils,name="enquiry"),
    path("dashboard/update_enquri/<int:id>",enqury_read,name="read_enquiry"),
    path("dashboard/add_service",add_services,name="add_service"),
    path("dashboard/manage_service",manage_service,name="manage_service"),
    path("dashboard/filter_enrollment/<str:enroll_id>",filter_enrollments),
    path("dashboard/edit_service/<int:s_id>",edit_service,name="edit_service"),
    path("dashboard/reset_password",reset_password,name="reset_pass")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)