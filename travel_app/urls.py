from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

from .views import contact
urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('package/', views.package, name='package'),
    path('destination/', views.destination, name='destination'),
    path('booking/', views.booking, name='booking'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('page/', views.page, name='page'),
    path('contacts/', views.contact, name='contacts'),

    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/reserve/<int:hotel_id>/', views.reserve_hotel, name='reserve_hotel'),

    path('choose/', views.choose_destination, name='choose_destination'),
    
    path('payment/', views.payment, name='payment'),
    path('event/', views.event_list, name='event'),
    path('book-event/<int:event_id>/', views.book_event, name='book_event'),

    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookies-policy/', views.cookies_policy, name='cookies_policy'),
    path('help/', views.help_page, name='help'),
    path('faq/', views.faq_page, name='faq'),
    path('Terms/', views.terms_page, name='Terms'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)