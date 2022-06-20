from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
  if request.method == "POST":
    department = request.POST['department']
    name = request.POST['name']
    email = request.POST['email']
    date = request.POST['date']
    time = request.POST['time']
    phone = request.POST['phone']
    
    
    
    return render(request, 'home.html', {'department':department,'name':name,'email':email,'date':date,'time':time,'phone':phone})
  else: 
    return render(request, 'home.html', {})


def about(request):
  return render(request, 'about.html', {})

def contact(request):
  if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    send_mail(
      name,
      message,
      email,
      ["kr.mishra.3534@gmail.com"],
    )
    return render(request, 'contact.html', {'name':name,'email':email,'subject':subject,'message':message})
  else: 
    return render(request, 'contact.html', {})

def services(request):
  return render(request, 'services.html', {})

def appointment(request):
  if request.method == 'POST':
    department = request.POST['department']
    name = request.POST['name']
    email = request.POST['email']
    date = request.POST['date']
    time = request.POST['time']
    phone = request.POST['phone']
    App_message = 'Name: ' + name + ' ' + '\nPhone: ' + phone + ' ' + '\nDate: ' + date + ' ' + '\nTime: ' + time + '\nDepartment: ' + department + '\nEmail: ' + email
    send_mail(
      'Appointment Request',
      App_message,
      email,
      ["kr.mishra.3534@gmail.com"],
    )
    return render(request, 'appointment.html', {'department':department,'name':name,'email':email,'date':date,'time':time,'phone':phone})
  else: 
    return render(request, 'home.html', {})

