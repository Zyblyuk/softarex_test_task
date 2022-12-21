from django.shortcuts import render
from django.shortcuts import redirect

from .models import TestTaskDB

from .forms import NewUserForm
from .forms import ProfileForm
from .forms import PredictTableForm

from django.contrib.auth import login
from django.contrib import messages

from django.urls import reverse_lazy

from django.http import HttpResponse
import json

list_atr = ['OpenDate', 'CityGroup', 'P1',
            'P2', 'P6', 'P7', 'P11', 'P17',
            'P21', 'P22', 'P28']


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
    form = PredictTableForm()
    if request.method == 'POST':
        author = request.user

        atr_dict = {}
        for i in list_atr:
            atr_dict[i] = request.POST.get(i)

        if 'submit' in request.POST:
            form = PredictTableForm(atr_dict)

            elem = TestTaskDB(author=author, OpenDate=atr_dict['OpenDate'],
                              CityGroup=atr_dict['CityGroup'], P1=atr_dict['P1'],
                              P2=atr_dict['P2'], P6=atr_dict['P6'], P7=atr_dict['P7'],
                              P11=atr_dict['P11'], P17=atr_dict['P17'], P21=atr_dict['P21'],
                              P22=atr_dict['P22'], P28=atr_dict['P28'])

            revenue = elem.predict()


            elem.revenue = revenue
            elem.save()

            context = {
                'attribute_dict': atr_dict,
                'revenue': revenue,
                'predict_table_form': form
            }
            return render(request, 'RevenuePredict/home.html', context)

        elif 'save_json' in request.POST:
            atr_dict['revenue'] = request.POST.get('revenue')
            response =  HttpResponse(json.dumps(atr_dict), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = f'inline; filename={request.user}_result.json'
            return response

    else:
        context = {
            'list_atr': list_atr,
            'predict_table_form': form
        }
        return render(request, 'RevenuePredict/home.html', context)


def history(request):
    if request.user.is_authenticated:
        tt_db = TestTaskDB.objects.all().filter(author=request.user)

        context = {
            'db_list': tt_db
        }
        if request.method == 'POST':
            if 'clear_history' in request.POST:
                tt_db.delete()
                return render(request, 'RevenuePredict/history.html', context)
            if 'save_json' in request.POST:
                response = HttpResponse(json.dumps([i.get_dict() for i in tt_db]),
                                        content_type="application/vnd.ms-excel")

                response['Content-Disposition'] = f'inline; filename={request.user}_history.json'
                return response

        else:
            return render(request, 'RevenuePredict/history.html', context)
    else:
        return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.username = request.POST.get('new_username')
            request.user.email = request.POST.get('new_email')
            request.user.save()

            login(request, request.user)

            messages.success(request, "Edit successful.")

            return redirect('/profile')

        username = request.user.username
        email = request.user.email


        profile_form = ProfileForm(default_username=username, default_email=email)


        context = {
            'username': username,
            'profile_form': profile_form

        }
        return render(request, 'RevenuePredict/profile.html', context)
    else:
        return redirect('login')
