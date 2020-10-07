from core import views
from django.urls import path


urlpatterns = [
    path('', views.TabletList.as_view(), name='tablets-list'),
    path('tablettes/create', views.TabletCreate.as_view(), name='tablets-create'),
    path('tablettes/<int:pk>', views.TabletDetail.as_view(), name='tablets-detail'),
    path('tablettes/<int:pk>/update', views.TabletUpdate.as_view(), name='tablets-update'),
    path('tablettes/<int:pk>/delete', views.TabletDelete.as_view(), name='tablets-delete'),
    path('marques/create', views.BrandCreate.as_view(), name='brands-create'),

]