from rest_framework import generics
from rest_framework import viewsets, response, decorators, serializers, permissions, status

from apps.accounts.models import UserProxy

BaseSerializer = serializers.ModelSerializer


class UserSerializer(BaseSerializer):

    class Meta:
        model = UserProxy
        fields = ['username', 'is_active']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProxy.objects.none()  # only self
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch']

    def get_queryset(self):
        # by default, only return current user information
        return UserProxy.objects.filter(id=self.request.user.id)

    @decorators.list_route(methods=['get'])
    def me(self, request):
        """Owner only and ReadOnly"""
        user = UserProxy.objects.get(id=request.user.id)
        user_serializer = self.serializer_class(user, context={'request': request})
        user_data = user_serializer.data
        # insert extra data:
        # user_data['preferences'] = user.dump_preferences()
        return response.Response(user_data)
