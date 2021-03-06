from django.shortcuts import render
from .models import Question, Applicant, Message
from django.core.mail import send_mail
from django.conf import settings


def index(request): 
    context = {
        'questions': Question.objects.all(),
        'applicants':  Applicant.objects.filter(status=1),
        'empty_cards': range(4 - Applicant.objects.filter(status=1).count())
    }
    if request.method == "POST":
        applicant_email = request.POST.get('email')
        applicant_name = request.POST.get('name')
        applicant_surname = request.POST.get('surname')
        subject = 'Müraciətin qəbul olundu'
        message = 'Salam, dəyərli ' + str(applicant_name) + ' ' + str(applicant_surname) + ', \nChallengers Club-a müraciətin etdiyin üçün təşəkkür edirəm.  1 Yanvar tarixindən etibarən müraciətin dəyərləndiriləcək və sənə ətraflı məlumat göndəriləcək. \nHəvəsin və istəyin daimi olsun.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [applicant_email]
        send_mail(subject, message, from_email, recipient_list)
        if request.POST.get('motivation_letter'):
            Applicant.objects.create(
                name = request.POST.get('name'),
                surname = request.POST.get('surname'),
                birth_date = request.POST.get('birth_date'),
                phone = request.POST.get('phone'),
                email = request.POST.get('email'),
                motivation_letter = request.POST.get('motivation_letter'))
        
        if request.POST.get('message_text'):
            sender_email = request.POST.get('sender_email')
            sender_name = request.POST.get('sender_name')
            subject = 'Mesajını aldım'
            message = 'Salam, dəyərli ' + str(sender_name) + '. \nMesajını aldım. Ən qısa zamanda cavablandıracam. \nTəşəkkür edirəm.'
            from_email = settings.SERVER_EMAIL
            recipient_list = [sender_email]
            send_mail(subject, message, from_email, recipient_list)
            Message.objects.create(
                sender_name = request.POST.get('sender_name'),
                sender_email = request.POST.get('sender_email'),
                message_text = request.POST.get('message_text'))

        

    return render(request, 'index.html', context)
