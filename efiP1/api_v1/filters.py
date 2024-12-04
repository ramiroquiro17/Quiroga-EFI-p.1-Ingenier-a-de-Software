import django_filters

from concesionaria.models import Auto

class AutoFilter(django_filters.FilterSet):
    categoria = django_filters.CharFilter(
        field_name='categoria__nombre',
        lookup_expr='icontains'
    )
    marca = django_filters.CharFilter(
        field_name='marca__nombre',
        lookup_expr='icontains'
    )
    modelo = django_filters.CharFilter(
        field_name='modelo__nombre',
        lookup_expr='icontains'
    )
    pais = django_filters.CharFilter(
        field_name='pais__nombre',
        lookup_expr='icontains'
    )
    color = django_filters.CharFilter(
        field_name='color__nombre',
        lookup_expr='icontains'
    )
    precio = django_filters.RangeFilter(
        field_name='precio'
    )
    
    class Meta:
        model = Auto
        fields = ['categoria', 'marca', 'modelo', 'pais', 'color', 'precio']
