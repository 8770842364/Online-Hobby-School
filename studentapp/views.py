from django.shortcuts import render,redirect
#for import table from admin app

from adminapp.models import course1
from datetime import date


from . import models as studentmodel


from django.contrib.auth import logout
# Create your views here.



def sessioncheckadmin_middleware(get_response):
   def middleware(request):
      if request.path=='/studenthome/' or request.path=='/studenthome/courselist3/' or request.path=='/studenthome/batchlist1/' or request.path=='/studenthome/admission/': 
         #if request.session["emailid"]==None or request.session["role"]!="student":
         if 'emailid' not in request.session:
            response=redirect('/login/')
         else:
            response=get_response(request)
      else:
         response=get_response(request)
         return response
   return middleware



def studenthome(request):
    #print("welcome admin")
    #for fetch session data ---------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #--------------------------------------------
    return render(request,"studenthome.html",{"emailid":emailid,"role":role})

def courselist3(request):
    res=course1.objects.all()
    return render(request,"courselist3.html",{'res':res})

def batchlist1(request):
    s="""select b.courseid,a.batchid,b.name,b.duration,b.fees,a.startdate,a.batchtime,a.facultyname
    from adminapp_batch1 as a 
    inner join adminapp_course1 as b on 
    a.courseid_id=b.courseid
    where a.batchstatus=1"""
    res=course1.objects.raw(s)
    return render(request,"batchlist1.html",{'res':res})

def admission(request):
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        s="""select b.courseid,a.batchid,b.name,b.duration,b.fees,a.startdate,a.batchtime,a.facultyname
        from adminapp_batch1 as a 
        inner join adminapp_course1 as b on 
        a.courseid_id=b.courseid
        where a.batchid="""+batchid
        res=course1.objects.raw(s)
        return render(request,"admission.html",{'res':res})
    else:
        batchid=request.POST.get("batchid")
        emailid=request.session.get("emailid")
        today = date.today()
        admissiondate = today.strftime("%Y-%m-%d")
        obj=studentmodel.admission(batchid=batchid,emailid=emailid,admissiondate=admissiondate)
        obj.save()
        return render(request,"success.html",{'res':''})
    
def success(request):
    return render(request,"success.html")

def logout1(request):
    logout(request)
    return redirect("http://localhost:8000/")