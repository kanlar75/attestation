from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from electronics_network.models import Company, Contact, Product
from users.permissions import IsActive, IsSuperuser
from electronics_network.serializers import CompanyDetailSerializer, \
    CompanySerializer, ProductSerializer, ContactSerializer


class ContactViewSet(ModelViewSet):
    """Контакты. """

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class ProductViewSet(ModelViewSet):
    """Продукты. """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class CompanyDetailAPIView(generics.RetrieveAPIView):
    """Детально компания. """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class CompanyDeleteAPIView(generics.DestroyAPIView):
    """Удалить компанию. """

    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class CompanyListAPIView(generics.ListAPIView):
    """Список компаний. """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [AllowAny]


class CompanyCreateAPIView(generics.CreateAPIView):
    """Добавить компанию. """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """Обновить компанию. """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]
