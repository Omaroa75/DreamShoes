from rest_framework import generics

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer