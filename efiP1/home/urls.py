from django.urls import path
from home.views import(
    index_view,
    LogoutView,
    LogginView,
)

urlpatterns = [
    path(route='', view=index_view, name='index'),
    path(route='login', view=LogginView.as_view(), name='login'),
    path(route='logout', view=LogoutView.as_view(), name='logout')

]
