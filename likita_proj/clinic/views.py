from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf.global_settings import EMAIL_HOST_USER
# Create your views here.

def book_an_appointment(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)
    appointment = Appointment.objects.all()
    
    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.info(request, "Please Select A Service!")
            return redirect('booking')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')
    
    
    
    context =  {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'appointment': appointment,
        }
    return render(request, 'clinic/booking.html', context)


def bookingSubmit(request):
    name = request.user
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    
    #Get stored data from django session:
    day = request.session.get('day')
    service = request.session.get('service')
    
    #Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        phone = request.POST['phone']
        message = request.POST['message']
        date = dayToWeekday(day)
        email = request.user.email
        
        
        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                name = name,
                                email = email,
                                service = service,
                                day = day,
                                time = time,
                                phone =phone,
                                message = message
                               
                            )
                            mail = EmailMessage(
                                subject="Appointment with Dokto",
                                body=f" Dear {name}, Your {service} booking is successfull", 
                                from_email=EMAIL_HOST_USER, to=[email])
                            mail.send()
                            messages.success(request, "Appointment Saved!")
                            return redirect('profile', pk=request.user.username)
                        else:
                            messages.info(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.info(request, "The Selected Day Is Full!")
                else:
                    messages.info(request, "The Selected Date Is Incorrect")
            else:
                    messages.info(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.info(request, "Please Select A Service!")


    return render(request, 'clinic/bookingSubmit.html', {'times':hour,})


def userPanel(request):
    name = request.user
    appointments = Appointment.objects.filter(name=name).order_by('day', 'time')
    return render(request, 'clinic/userPanel.html', {
        'name':name,
        'appointments':appointments,
    })
    
    
def userUpdate(request, pk):
    appointment = Appointment.objects.get(id=pk)
    userdatepicked = appointment.day
    #Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    #24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', pk=pk)


    return render(request, 'clinic/userUpdate.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'id': id,
            'appointment': appointment
        })


def userUpdateSubmit(request, pk):
    name = request.user
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    
    email = request.user.email
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, pk)
    appointment = Appointment.objects.get(id=pk)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(id=pk).update(
                                name = name,
                                service = service,
                                day = day,
                                time = time,
                            ) 
                            mail = EmailMessage(
                                subject="Appointment with Dokto Medics Updated",
                                body=f" Dear {name}, Your {service} booking is updated successfull", 
                                from_email=EMAIL_HOST_USER, to=[email])
                            mail.send()
                            messages.success(request, "Appointment Updated!")
                            return redirect('home')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
            
        return redirect('userPanel')


    return render(request, 'clinic/userUpdateSubmit.html', {
        'times':hour,
        'id': pk,
        'appointment': appointment
    })


def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'clinic/staffPanel.html', {
        'items':items,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
 
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, pk):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(id=pk)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x