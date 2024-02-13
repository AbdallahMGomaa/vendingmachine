from django.urls import path

from crm import views

urlpatterns = [
    path('deposit/', views.DepositView.as_view(), name='deposit'),
    path('balance/', views.BalanceView.as_view(), name='balance'),
    path('buy/', views.BuyView.as_view(), name='buy'),
    path('transactions/', views.TransactionsView.as_view(), name='transactions'),
    path('all_products/', views.GetProductView.as_view(), name='all_products'),
    path('reset/', views.ResetView.as_view(), name='reset'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('product/delete/', views.DeleteProductView.as_view(), name='delete_product'),
]
