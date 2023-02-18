from django.urls import path
from .views import HomepageView,Homepage2

urlpatterns = [
    path('top-headlines/', HomepageView.as_view(), name='homepage'),
    path('top-headlines/page/2/',  Homepage2.as_view(), name='homepage'),

]
