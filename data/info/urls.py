from django.urls import path
from .views import FinancialEntryListCreateView, FinancialEntryTotalView, ExpenseEntryListCreateView, \
    ExpenseEntryTotalView

urlpatterns = [
    path('financial-entries/', FinancialEntryListCreateView.as_view(), name='financial-entry-list-create'),
    path('financial-entries/total/<str:period>/', FinancialEntryTotalView.as_view(), name='financial-entry-total'),

    path('expense-entries/', ExpenseEntryListCreateView.as_view(), name='expense-entry-list-create'),
    path('expense-entries/total/<str:period>/', ExpenseEntryTotalView.as_view(), name='expense-entry-total'),
]
