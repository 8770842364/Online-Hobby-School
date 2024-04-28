from django.shortcuts import render,redirect
from . import models as adminmodel
from django.core.files.storage import FileSystemStorage

#for display image
from django.conf import settings
media_url=settings.MEDIA_URL

from myapp2.models import mstuser


from django.contrib.auth import logout


# Create your views here.
def sessioncheckadmin_middleware(get_response):
   def middleware(request):
      if request.path=='/adminhome/' or request.path=='/adminhome/addcourse1/' or request.path=='/adminhome/courselist1/' or request.path=='/adminhome/addbatch/' or request.path=='/adminhome/studentlist/' :
         if request.session["emailid"]==None or request.session["role"]!="admin":
          if 'emailid' not in request.session:
            response=redirect('/login/')
          else:
            response=get_response(request)
      else:
         response=get_response(request)
         return response
   return middleware



def adminhome(request):
    #print("welcome admin")
    #for fetch session data ---------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #--------------------------------------------
    return render(request,"adminhome.html",{"emailid":emailid,"role":role})


    
def courselist1(request):
    res=adminmodel.course1.objects.all()
    return render(request,"courselist1.html",{'res':res})

def editcourse(request):
    if request.method=="GET":
     courseid=request.GET.get("courseid")
     rs=adminmodel.course1.objects.filter(courseid=courseid)
     return render(request,"editcourse.html",{'rs':rs})
    else:
       courseid=request.POST.get("courseid")
       duration=request.POST.get("duration")
       fees=request.POST.get("fees")
       detail=request.POST.get("detail")
       adminmodel.course1.objects.filter(courseid=courseid).update(duration=duration,fees=fees,detail=detail)
       return redirect("/adminhome/courselist1/")
    
def addbatch1(request):
   if request.method=="GET":
      res=adminmodel.course1.objects.all()
      return render(request,"addbatch1.html",{'res':res,'msg':''})
   else:
      courseid=request.POST.get("courseid")
      print("course id=",courseid)
      startdate=request.POST.get("startdate")
      batchtime=request.POST.get("batchtime")
      facultyname=request.POST.get("facultyname")
      batchstatus=1 #1 for new batch
      obj=adminmodel.batch1(courseid_id=courseid,startdate=startdate,batchtime=batchtime,
                           facultyname=facultyname,batchstatus=batchstatus)
      obj.save()
      return render(request,"addbatch1.html",{'res':'','msg':'record saved'})
   
def addcourse1(request):
   if request.method=="GET":
      return render(request,"addcourse1.html",{'msg':''})
   else:
      name=request.POST.get("name")
      duration=request.POST.get("duration")
      fees=request.POST.get("fees")
      detail=request.POST.get("detail")
      #1 for file uploading
      courseicon=request.FILES["courseicon"]
      fs=FileSystemStorage()
      courseimg=fs.save(courseicon.name,courseicon)
      obj1=adminmodel.course1(name=name,duration=duration,fees=fees,detail=detail,courseicon=courseicon)
      obj1.save()
      return render(request,"addcourse1.html",{'msg':'record saved'})


def studentlist(request):
    res=mstuser.objects.filter(role="student")
    return render(request,"studentlist.html",{'res':res})

def logout2(request):
   logout(request)
   return redirect("http://localhost:8000/")