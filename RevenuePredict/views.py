from django.shortcuts import render, redirect

from .models import TestTaskDB

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    return render(request=request,
                  template_name="registration/register.html",
                  context={"register_form": form})


def home(request):
    if request.method == 'POST':
        author = request.user
        open_date = float(request.POST.get('OpenDate'))
        city_group = float(request.POST.get('CityGroup'))
        p1 = float(request.POST.get('P1'))
        p2 = float(request.POST.get('P2'))
        p6 = float(request.POST.get('P6'))
        p7 = float(request.POST.get('P7'))
        p11 = float(request.POST.get('P11'))
        p17 = float(request.POST.get('P17'))
        p21 = float(request.POST.get('P21'))
        p22 = float(request.POST.get('P22'))
        p28 = float(request.POST.get('P28'))

        elem = TestTaskDB(author=author, OpenDate=open_date,
                          CityGroup=city_group, P1=p1, P2=p2,
                          P6=p6, P7=p7, P11=p11, P17=p17,
                          P21=p21, P22=p22, P28=p28)

        revenue = elem.predict()

        elem.revenue = revenue
        elem.save()

        context = {
            'revenue': revenue
        }

        return render(request, 'RevenuePredict/home.html', context)
    else:
        return render(request, 'RevenuePredict/home.html')


def history(request):
    if request.user.is_authenticated:
        tt_db = TestTaskDB.objects.all()

        context = {
            'items': tt_db
        }
        return render(request, 'RevenuePredict/history.html', context)
    else:
        return redirect('login')
