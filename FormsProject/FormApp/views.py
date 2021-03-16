from django.shortcuts import render
#from django.http import HttpResponse

#*
from django import forms

#**
from FormApp.forms import NewUser

# Create your views here.
def index(call):
    my_dict = {
        'welcome_me' : 'Hey Bud!! Welcome to This Django World',
        'insert_me' : 'Hey Can Enter /Forms To Know More ..... THankYOu'
    }
    return render(call,'index.html',context = my_dict)

#this fnction for jsut for checlong validation and gave vales but in this code validation not worign so please check it for this import for indicate step *
#solution try remove mydict and pass direct forms_details and check validation works or not 11 mar 2021 23:55 tue night
def form_settings(call):
    forms_details = forms.FormField()

    my_dict = {
        'forms' : forms_details
    }
    if call.method == 'POST':

        forms_details  = forms.FormField(call.POST)

        if forms_details.is_valid():

            print("VAlda")
            print("First Name : " +forms_details.cleaned_data['first_name'])
            print("Last Name : " +forms_details.cleaned_data['last_name'])
            print("Email : " +forms_details.cleaned_data['e_mail'])



    return render(call ,'forms.html',context = my_dict)


    # this function is for insert into data base for that you have to import class name from appname.form indicate stwp no by this **
def user_settings(call):

    form = NewUser()

    if call.method == 'POST':

        form = NewUser(call.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(call)

        else:

            print("Nahh invlias formas")

    return render(call,'forms.html',{'form': form})
