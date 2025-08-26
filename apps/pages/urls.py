from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('coming-soon/',views.coming_soon_view,name='coming'),
    path('contact/',views.contact_view,name='contact'),
    path('faq/',views.faq_view,name='faq'),
]