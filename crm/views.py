from rest_framework import generics, serializers
from authentication.permissions import IsBuyerPermission, IsSellerPermission
from crm.services import CRMService
from django.http import JsonResponse
import crm.serializers as CRMSerializers


# Create your views here.


class DepositView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission]

    class InputSerializer(serializers.Serializer):
        deposit_amount = serializers.IntegerField(required=True)

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        deposit_amount = input_serializer.validated_data['deposit_amount']
        CRMService(request.user).deposit(deposit_amount)
        return JsonResponse({'message': 'Amount deposited successfully'}, status=200)


class BalanceView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission]

    def get(self, request):
        balance = CRMService(request.user).get_balance()
        return JsonResponse({'balance': balance}, status=200)


class GetProductView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission | IsSellerPermission]

    def get(self, request):
        available_products = CRMService(request.user).get_available_products()
        output_seralizer = CRMSerializers.ProductSerializer(available_products, many=True)
        return JsonResponse(output_seralizer.data, status=200, safe=False)


class BuyView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission]

    class InputSerializer(serializers.Serializer):
        product_id = serializers.IntegerField()
        amount_of_product = serializers.IntegerField()

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        product_id = input_serializer.validated_data['product_id']
        amount_of_product = input_serializer.validated_data['amount_of_product']
        product_id, cost, balance, transaction_id = CRMService(request.user).buy(product_id, amount_of_product)
        data = {
            'product_id': product_id,
            'cost': cost,
            'remaining_balance': balance,
            'transaction_id': transaction_id
        }
        return JsonResponse(data, status=200)


class ResetView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission]

    def get(self, request):
        CRMService(request.user).reset()
        return JsonResponse({'message': 'Balance was reset successfully'}, status=200)


class ProductView(generics.GenericAPIView):
    permission_classes = [IsSellerPermission]

    def get(self, request):
        seller_products = CRMService(request.user).get_seller_products()
        output_serializer = CRMSerializers.ProductSerializer(seller_products, many=True)
        return JsonResponse(output_serializer.data, status=200, safe=False)

    class PostInputSerializer(serializers.Serializer):
        product_name = serializers.CharField()
        product_cost = serializers.IntegerField()
        product_amount = serializers.IntegerField()

    def post(self, request):
        input_serializer = self.PostInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        product_id = CRMService(request.user).add_product(**input_serializer.validated_data)
        return JsonResponse({'message': 'product added successfully', 'product_id': product_id}, status=200)

    class PutInputSerializer(PostInputSerializer):
        product_id = serializers.IntegerField()

    def put(self, request):
        input_serializer = self.PutInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        CRMService(request.user).update_product(**input_serializer.validated_data)
        return JsonResponse({'message': 'product updated successfully'}, status=200)


class DeleteProductView(generics.GenericAPIView):
    permission_classes = [IsSellerPermission]

    class InputSerializer(serializers.Serializer):
        product_id = serializers.IntegerField()

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        product_id = input_serializer.validated_data['product_id']
        CRMService(request.user).delete_product(product_id)
        return JsonResponse({'message': 'Product deleted successfully', 'product_id': product_id}, status=200)


class TransactionsView(generics.GenericAPIView):
    permission_classes = [IsBuyerPermission]

    def get(self, request):
        transactions = CRMService(request.user).get_transactions()
        output_serializer = CRMSerializers.TransactionSerializer(transactions, many=True)
        return JsonResponse({'transactions': output_serializer.data}, status=200)
