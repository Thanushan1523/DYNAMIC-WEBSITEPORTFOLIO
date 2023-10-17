from django.shortcuts import render ,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship
# Create your views here.
def home(request):
    return render(request ,'home.html')


def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request ,'handleblog.html',context)


def about(request):
    return render(request ,'about.html')

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "please login to access this page")
        return redirect('/auth/login/')

    if request.method=="POST": 
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fusn=request.POST.get("usn")
        fcollege=request.POST.get("cname")
        foffer=request.POST.get("offer")
        fstartdate=request.POST.get("startdate")
        fenddate=request.POST.get("enddate")
        fproject=request.POST.get("project")


        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fproject=fproject.upper()
        foffer=foffer.upper()

        query=Internship(fullname=fname,usn=fusn, collage_name=fcollege,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fproject ,email=femail)
        query.save()
        messages.success(request, 'form is submitted')
        return redirect ('/internship')
    return render(request ,'internshipdetails.html')

def contact(request):
    if request.method=="POST": 
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphoneno=request.POST.get("num")
        fdesc=request.POST.get("des")
        query =Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        
        messages.success(request, 'thank you we will get back you soon')
        return redirect ('/contact')
    return render(request ,'contact.html') 