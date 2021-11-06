from django.shortcuts import render
from .forms import ImageForms, SendMail
from .modeldeep import search
from PIL import Image 
from .models import Images
from django.core.mail import send_mail

# Create your views here.

def getImage(request):


	context = {'description':'', 'obj':None,}
	


	if request.method == 'POST':

		form = ImageForms(request.POST,request.FILES)
		if form.is_valid():

			img = form.cleaned_data['img']


			image = Image.open(img).convert('RGB')
			description = search(image)
			context['description'] = description
			obj = Images( img = img)
			obj.save()
			context['obj'] = obj
			
	else: 

		form = ImageForms()

	context['form'] = form
	return render(request, 'imagedescription/index.html',context)

def contact(request):
	if request.method == 'POST':
		form = SendMail(request.POST)
		if form.is_valid():
			subject = "Hi, i am Dat" 
			body = {'first_name': form.cleaned_data['first_name'], 'last_name': form.cleaned_data['last_name'],'message':form.cleaned_data['message'], 'to_email':form.cleaned_data['to_email']}
			message = body['first_name'] + " " + body['last_name'] + ': '+body['message']

			endpoint= [i.strip() for i in body['to_email'].split(',')]

			send_mail(subject, message, 'caodat12345@gmail.com', endpoint) 
			# except BadHeaderError: #add this
			# 	return HttpResponse('Invalid header found.') #add this
			     
	form = SendMail()
	return render(request, "imagedescription/contact.html", {'form':form})