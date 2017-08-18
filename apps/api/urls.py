from rest_framework import routers
from . import views as v

router = routers.DefaultRouter()
# register your APIs here
router.register(r'users', v.UserViewSet)
# add more...

urlpatterns = router.urls
