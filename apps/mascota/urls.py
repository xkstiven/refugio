from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view,mascota_list
from apps.mascota.views import mascota_edit, mascota_delete

from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar$', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]
