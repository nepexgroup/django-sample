from django.contrib import admin
from django.urls import path


from django.conf.urls import include
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
# from src.sample import Event


# class EventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'
#
# # ViewSets define the view behavior.
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#
#
# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'events', EventViewSet)
#
#
urlpatterns = [
    path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/v1/', include(router.urls))
]
