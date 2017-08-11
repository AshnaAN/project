from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #courier
    url(r'^courier','front.views.courier_request', name='courier_request'),
    url(r'^cou','front.views.courier_res',name='courier_res'),
    #
    url(r'^user','front.views.user_login',name='user_login'),
    url(r'^response','front.views.user_response', name='user_response'),
    url(r'^edata','front.views.hello'),
    url(r'^adminu','front.views.adminuser'),
    
    url(r'^about','front.views.abt'),
    url(r'^depots','front.views.depot'),
    url(r'^fares','front.views.fare'),

    url(r'^bushire$','front.views.ebushire'),
    url(r'^bushire-submit','front.views.ebushiresubmit'),
    #homepage
    url(r'^home','front.views.home'),
    url(r'^bhome','front.views.homepbus'),
    url(r'^chome','front.views.homepcourier'),
    #
    url(r'^search','front.views.search'),
    url(r'^xyz', 'front.views.adhome'),
    url(r'^details', 'front.views.adminuser'),
    url(r'^cdetails', 'front.views.hello'),
    url(r'^admin', 'front.views.login'), #admin-login
    url(r'^wqr', 'front.views.my'),
    url(r'^book', 'front.views.seat'),
    url(r'^dbusreq', 'front.views.bush'),
    url(r'^admin/', include(admin.site.urls)),
]
