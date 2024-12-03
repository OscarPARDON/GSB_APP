import os
from datetime import datetime

from django.db.models import Max
from django.shortcuts import render, redirect

from DjangoProject1.settings import STATICFILES_DIRS
from candidate.models import Application
from visitor.forms import ApplicationForm
from visitor.models import Publication


def visitorpage(request): # Default Page
    posts = Publication.objects.all() # Get all the Publications in the Database
    error = request.GET.get('error', '') # If an error is sent, get the error
    return render(request, 'visitor_page.html', {'posts': posts, 'error': error}) # Call the template and pass the variables


def application(request): # Application Page : Displays the application form & manage the data submition

    postID = request.GET.get('postID', '') # Get the job offer linked to the application
    if not (postID and Publication.objects.filter(id=int(postID)).exists()): # If the job offer doesn't exists ...
        return redirect('/') # Redirection to the homepage

    if request.method == 'POST': # If a form is submitted

        if Application.objects.filter(candidate_firstname=request.POST['firstname'],candidate_lastname=request.POST['name'],post_id=postID).exists(): #If there is already an application from the person on this job offer ...
            return redirect('/?error=Vous avez déja candidaté pour cette offre') # Redirection to the homepage and inform the user that he already applied to this offer

        form = ApplicationForm(request.POST, request.FILES) # Collect the submited form's data

        # Application Number Generation
        today = datetime.now().strftime('%Y%m%d')# Get the current date in format YYYYMMDD
        max_application = Application.objects.aggregate(Max('application_number'))['application_number__max'] # Get the most recent application number
        if max_application and max_application[:8] == today: # If this is not the first application today ...
            max_num = int(max_application[-3:]) + 1 # Incrementation of the biggest number
        else: # If this is the first application of the day ...
            max_num = 0 # set to 0

        max_num_str = f"{max_num:03}" # Formate the 3 digits number
        number = f"{today}{max_num_str}" # Build the application number (Current date + incrementing 3 digits number)

        if form.is_valid(): # If the submitted data match with expected (see clean() function in Application/forms.py) ...
            insertion = Application( # Prepare the insertion in the database
                application_number=number,
                candidate_firstname=form.cleaned_data['firstname'],
                candidate_lastname=form.cleaned_data['name'],
                candidate_mail=form.cleaned_data['email'],
                candidate_phone=form.cleaned_data['phone'],
                candidate_password=hash(form.cleaned_data['password']), #hash the password
                post_id=int(postID),
            )
            insertion.save() # Save the application in the database

            #Files management
            path = os.path.join('', str(STATICFILES_DIRS[0]) + '/files/' + number ) # Get the path of the file storage repository
            os.mkdir(path) # Create a repository named with the application number
            cv_extension = os.path.splitext(str(request.FILES['cv']))[1] # Get the extension of the file
            cover_letter_extension = os.path.splitext(str(request.FILES['cover_letter']))[1] # Get the extension of the file
            storage_path_cv = os.path.join('', str(path), 'cv' + cv_extension) # Create a path to the new repository and name the file "CV.extension"
            storage_path_coverletter = os.path.join('', str(path), 'coverletter' + cover_letter_extension) # Create a path to the new repository and name the file "coverletter.extension"
            cv_file = request.FILES['cv'] # Get the uploaded CV file
            cover_letter_file = request.FILES['cover_letter'] # Get the uploaded cover letter file

            with open(storage_path_cv, 'wb+') as destination: # Open the uploaded cv file
                for chunk in cv_file.chunks():
                    destination.write(chunk) # Copy the downloaded file in the new repository

            with open(storage_path_coverletter, 'wb+') as destination: # Open the uploaded cover_letter file
                for chunk in cover_letter_file.chunks():
                    destination.write(chunk) # Copy the downloaded file in the new repository

            return redirect('/application_success?application_number=' + number) # If every step is done successfully, redirect to the success page

    else: # If no form is submitted ...
        form = ApplicationForm() # Get the form from forms.py

    return render(request, 'application_form.html', {'form': form, 'postID': postID}) # Call the application form and pass the variables


def application_success(request): # Successful Application Page : inform the user that the application was sucessfully sent and display the application number needed to connect
    application_number = request.GET.get('application_number', '') # Get the newly created application number
    return render(request,'application_success.html',{'application_number': application_number}) # Call the successful application template and pass the variable