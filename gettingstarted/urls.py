from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.home, name="Home"),
    path("about/", hello.views.about, name="About"),
    path("admission/", hello.views.admission, name="Admission"),
    path("admission_hid/", hello.views.admission_hid, name="Admission"),
    path("campus/", hello.views.campus, name="Campus"),
    path("contact/", hello.views.contact, name="Contact Us"),
    path("facility/", hello.views.facility, name="Facilities"),
    path("faculty/", hello.views.faculty, name="Faculty"),
    path("placement/", hello.views.placement, name="Placement"),
    path("table/", hello.views.table, name="Table"),
    path("delete/", hello.views.delete, name="Table"),
    path("base/", hello.views.base, name="base"),
    path("lc/", hello.views.lc, name="lc"),
    path("logout/", hello.views.logout, name="logout"),
    path("enquiry/", hello.views.enquiry, name="enquiry"),
    path("navbar/", hello.views.navbar, name="navbar"),
    path("student/", hello.views.student, name="student"),
    
    

    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
