from django.urls import path
from .views import send_email, answer_page_view


app_name = 'mailsender'

urlpatterns = [
    path('', send_email, name='send_email'),
    path('answer/', answer_page_view, name='answer_page'),
]
