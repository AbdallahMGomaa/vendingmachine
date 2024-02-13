from crm.models import Product, Transaction
from authentication.models import User
import crm.validators as Validators


class CRMService:
    def __init__(self, user: User):
        self.user = user

    def deposit(self, amount: int):
        Validators.validate_deposit_amount(amount)
        self.user.deposit += amount
        self.user.save()

    def get_available_products(self):
        products = Product.objects.filter(amount_available__gt=0).values('name', 'cost')
        return products

    def create_transaction(self, buyer, product, amount):
        transaction = Transaction.objects.create(user=buyer, product=product, amount=amount)
        return transaction
    def buy(self, product_id: int, amount_of_product: int) -> (int, int, int):
        product_to_buy = Product.objects.get(id=product_id)
        amount_available = product_to_buy.amount_available
        Validators.validate_buy_transaction(self.user.deposit, product_to_buy.cost, amount_of_product, amount_available)
        self.user.deposit -= product_to_buy.cost
        product_to_buy.amount_available -= amount_of_product
        self.user.save()
        product_to_buy.save()
        transaction = self.create_transaction(self.user, product_to_buy, amount_of_product)
        return product_id, product_to_buy.cost, self.user.deposit, transaction.id

    def reset(self):
        self.user.deposit = 0
        self.user.save()

    def get_seller_products(self):
        seller = self.user
        seller_products = Product.objects.filter(seller=seller)
        return seller_products

    def add_product(self, product_name, product_cost, product_amount):
        Validators.validate_product_data(product_cost, product_amount)
        seller = self.user
        product = Product.objects.create(name=product_name, cost=product_cost, amount_available=product_amount,
                                            seller=seller)
        return product.id

    def update_product(self, product_id, product_name, product_cost, product_amount):
        Validators.validate_product_data(product_cost, product_amount)
        seller = self.user
        product = Product.objects.get(id=product_id, seller=seller)
        product.name = product_name
        product.cost = product_cost
        product.amount_available = product_amount
        product.save()

    def delete_product(self, product_id):
        seller = self.user
        product = Product.objects.get(id=product_id, seller=seller)
        product.delete()

    def get_balance(self):
        return self.user.deposit

    def get_transactions(self):
        transactions = Transaction.objects.filter(user=self.user)
        return transactions
