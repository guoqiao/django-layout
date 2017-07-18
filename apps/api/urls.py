from rest_framework import routers
from . import views as v

router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet)

urlpatterns = router.urls
