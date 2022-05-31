
import django_filters
from django_filters import DateFilter, CharFilter
from usuarios.models import *
from ..daw.models import*

class orderFilter(django_filters.filterset):
    start_date = DateFilter(field_name="date_created",lookup_expr='gte')
    end_date= DateFilter(field_name="date_created",lookup_expr='lte')
    note=CharFilter(field_name='note',lookup_expr='incontains')

    class meta:
        models=Order
        fields='_all_'
        exclude={'custome','date_created'}