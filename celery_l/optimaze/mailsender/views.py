from django.shortcuts import render, redirect, reverse
from .forms import EmailForm
from django.conf import settings
from django.core.mail import send_mail


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            to_send = [
                form.cleaned_data['sender'],
            ]
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email, to_send)
            request.session['recipient_list'] = to_send
            return redirect(reverse('mailsender:answer_page'))
    else:
        form = EmailForm()

    return render(request, 'mailsender/email.html', {'form': form})


def answer_page_view(request):
    return render(request, 'mailsender/answer/success.html', {
        'recipient_list': request.session.get('recipient_list', []),
    })
