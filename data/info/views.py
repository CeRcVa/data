from django.utils import timezone
from django.db.models import Sum
from rest_framework import generics
from .models import FinancialEntry, ExpenseEntry
from .serializers import FinancialEntrySerializer, ExpenseEntrySerializer


class BaseEntryTotalView(generics.ListAPIView):
    serializer_class = None
    queryset = None

    def get_queryset(self):
        period = self.kwargs['period']
        today = timezone.now().date()

        if period == 'week':
            start_date = today - timezone.timedelta(days=today.weekday())
            end_date = start_date + timezone.timedelta(days=6)
        elif period == 'month':
            start_date = today.replace(day=1)
            end_date = (start_date + timezone.timedelta(days=32)).replace(day=1) - timezone.timedelta(days=1)
        elif period == 'year':
            start_date = today.replace(month=1, day=1)
            end_date = today.replace(month=12, day=31)
        else:
            return self.queryset.none()

        queryset = self.queryset.filter(entry_date__range=(start_date, end_date)).aggregate(
            total_salary=Sum('salary'),
            total_business_income=Sum('business_income'),
            total_rent_income=Sum('rent_income'),
            total_remittances=Sum('remittances'),
            total_other_financial=Sum('other'),
            total_utilities=Sum('utilities'),
            total_groceries_shopping=Sum('groceries_shopping'),
            total_transportation=Sum('transportation'),
            total_cafe_restaurant=Sum('cafe_restaurant'),
            total_health=Sum('health'),
            total_other_expense=Sum('other'),
        )

        return [queryset]


class FinancialEntryListCreateView(generics.ListCreateAPIView):
    queryset = FinancialEntry.objects.all()
    serializer_class = FinancialEntrySerializer


class FinancialEntryTotalView(BaseEntryTotalView):
    queryset = FinancialEntry.objects.all()
    serializer_class = FinancialEntrySerializer


class ExpenseEntryListCreateView(generics.ListCreateAPIView):
    queryset = ExpenseEntry.objects.all()
    serializer_class = ExpenseEntrySerializer


class ExpenseEntryTotalView(BaseEntryTotalView):
    queryset = ExpenseEntry.objects.all()
    serializer_class = ExpenseEntrySerializer
