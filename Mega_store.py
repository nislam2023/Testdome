from enum import Enum, auto


class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, total_price, discount_type):

    if cart_weight > 0 and discount_type == DiscountType.STANDARD:
        discounted_price = total_price * (1 - 6 / 100)
        print('You got STANDARD discount')
    elif cart_weight > 0 and discount_type == DiscountType.SEASONAL:
        discounted_price = total_price * (1 - 12 / 100)
        print('You got SEASONAL discount')
    elif cart_weight <= 10 and discount_type == DiscountType.WEIGHT:
        discounted_price = total_price * (1 - 6 / 100)
        print('You got WEIGHT-Light discount')
    elif cart_weight > 10 and discount_type == DiscountType.WEIGHT:
        discounted_price = total_price * (1 - 18 / 100)
        print('You got WEIGHT-Prime discount')

    return discounted_price


print(get_discounted_price(12, 100, DiscountType.SEASONAL))
