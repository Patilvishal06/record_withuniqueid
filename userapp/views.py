from django.shortcuts import render
from .models import User

def submit_form(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            aadhar_number = request.POST['aadhar_number']
            unique_id = first_name[:2] + last_name[:2] + aadhar_number[-4:]

            user = User(first_name=first_name, last_name=last_name, email=email, aadhar_number=aadhar_number, unique_id=unique_id)
            user.save()
            users = User.objects.all()

            return render(request, 'confirmation.html', {'users': users})

        except Exception as e:
            print(e)
    return render(request, 'form.html')