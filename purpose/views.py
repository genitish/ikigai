from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def section(request):
    u=User.objects.all()
    s=Section.objects.all()
    t=None
    if request.method == 'POST':
        x=request.POST.get('list')
        y = request.POST
        l=None
        for key,value in y.items():
                if value== 'Add':
                    l=key

        t= Section.objects.get(name=l)
        m=list.objects.create(name=x,user=request.user,section=t)
    p=[]
    q=[]
    r=[]
    w=[]
    passion=set()
    mission=set()
    profession=set()
    vocation=set()

    for i in list.objects.filter(user=request.user,section=s[0]):
        p.append(i.name)

    for i in list.objects.filter(user=request.user,section=s[1]):
        q.append(i.name)
    for i in list.objects.filter(user=request.user,section=s[2]):
        r.append(i.name)
    for i in list.objects.filter(user=request.user,section=s[3]):
        w.append(i.name)
   
      
    passion=set(p).intersection(set(q))
    mission=set(p).intersection(set(w))
    profession=set(r).intersection(set(q))
    vocation=set(w).intersection(set(r))

    print(passion)
    print(mission)
    print(profession)
    print(vocation)
    purpose = []
    for i in passion:
        purpose.append(i)
    for i in mission:
        purpose.append(i)
    for i in profession:
        purpose.append(i)
    for i in vocation:
        purpose.append(i)

    t=list.objects.all().filter(user=request.user).order_by('-id')
    return render(request,'purpose/section.html',{'s':s,'t':t,'u':u,'purpose':purpose})
@login_required
def edit(request,pk):

    l=list.objects.get(pk=pk)
    form=UpdateList(instance=l)
    if request.method=="POST":
        form=UpdateList(request.POST,instance=l)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user

            instance.save()
            return redirect('purpose:home')
        else:
            form=UpdateList(instance=pk)
    return render(request,'purpose/update.html',{'form':form})
@login_required
def users(request):
    u=User.objects.exclude(email=request.user.email)
    return render(request,'purpose/users.html',{'u':u})
@login_required
def retrive_by_user(request,pk):



    l=list.objects.all().filter(user=request.user)

    return render(request,'purpose/retrive.html',{'l':l,'k':k})
@login_required
def retrieve_user_list(request,pk):

    s=Section.objects.all()
   
    u=User.objects.get(pk=pk)
    t=list.objects.filter(user=u)
    return render(request,'purpose/retrive.html',{'s':s,'t':t})

@login_required
def delete(request,pk):
    l=list.objects.get(pk=pk).delete()
    return redirect('purpose:home')

