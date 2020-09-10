from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'testapp/Javaexams.html')

@login_required
def python_exam_view(request):
    return render(request,'testapp/Pythonexam.html')

@login_required
def aptitude_exam_view(request):
    return render(request,'testapp/Aptitude.html')


def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        #if form.is_valid():
        #    form.save()
        user=form.save()
        user.set_password(user.password)    #When you sing in your page, you will be able to login
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
