import django_filters

from electronics_network.models import Company


class CompanyFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name='contacts__country',
                                      lookup_expr='icontains',
                                      label='Filter company by country.')

    class Meta:
        model = Company
        fields = ('contacts__country',)
