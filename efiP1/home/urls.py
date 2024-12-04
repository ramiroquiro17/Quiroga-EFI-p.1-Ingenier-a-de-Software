from django.urls import path
from home.views import(
    index_view,
    LogoutView,
    LogginView,
    UpdateLang,
)

urlpatterns = [
    path(route='', view=index_view, name='index'),
    path(route='login', view=LogginView.as_view(), name='login'),
    path(route='update_lang/', view=UpdateLang.as_view(), name='update_lang'),
    path(route='logout', view=LogoutView.as_view(), name='logout')

]
