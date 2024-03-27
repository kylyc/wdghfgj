from django.shortcuts import render
from apps.base.models import InfoUser, Skills, MyService, Education, PersentShow, Blogs
from apps.secondary.models import Secondary, Backend, Desinger, Frontend, Android, Colleagues 

# Create your views here.
def index(request):
    blogs = Blogs.objects.all()
    backend = Backend.objects.latest("id")
    frontend = Frontend.objects.latest("id")
    desinger = Desinger.objects.latest("id")
    android = Android.objects.latest("id")
    colleagues = Colleagues.objects.all()
    persent = PersentShow.objects.all()
    skills = Skills.objects.all()
    myservice = MyService.objects.all()
    education = Education.objects.all()
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    return render(request, "index.html", locals())

def blog_details(request, id):
    blogs = Blogs.objects.get(id=id)
    infouser = InfoUser.objects.latest("id")
    return render(request, "blog-details.html", locals())

