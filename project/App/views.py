from django.shortcuts import render,redirect
from App.forms import RegForm,CraftsForm
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def register(request):
	if request.method=="POST":
		q=RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lg')
	q=RegForm()
	return render(request,'html/register.html',{'u':q})

def contact(request):
	return render(request,'html/contact.html')


def hc(request):
	if request.method=="POST":
		j=CraftsForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
			return redirect('/')
	j=CraftsForm()
	return render(request,'html/handcrafts.html',{'u':j})

def profile(request):
	return render(request,'html/profile.html')