# registration_app/views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            registration = form.save()

            # You can also perform additional server-side validation here if needed

            # Redirect to the confirmation page with the registration ID
            return redirect('confirmation', registration_id=registration.id)
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})

def confirmation_page(request, registration_id):
    # Retrieve the registration details from the database
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'confirmation.html', {'registration': registration})
