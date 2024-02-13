def validate_deposit_amount(amount: int):
    try:
        assert amount in [5, 10, 20, 50, 100]
    except:
        raise Exception('Incorrect deposit amount')


def validate_buy_transaction(deposit: int, cost: int, amount_of_product: int, available_amount: int):
    try:
        assert amount_of_product <= available_amount
    except:
        raise Exception('Product available amount is not enough')
    try:
        assert deposit > cost * amount_of_product
    except:
        raise Exception('Insufficient deposit balance')

def validate_product_data(product_cost: int, product_amount):
    try:
        assert product_cost > 0
    except:
        raise Exception('Product cost must be positive')

    try:
        assert product_amount > 0
    except:
        raise Exception('Product amount must be positive')
