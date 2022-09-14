from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_data_json
from wishlist.views import show_data_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('json/', show_data_json, name='show_data_json'),
    path('xml/', show_data_xml, name='show_data_xml'),
]