from .models import Product

CART_SESSION_ID = 'cart'


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:  # if product dont exist in cart
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity  # if product exist in cart just ad quantity
        self.save()

    def __iter__(self):  # for iteration in cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)  # __in because product_ids is list
        cart = self.cart.copy()  # because we want to edit object
        for product in products:  # for add objects name in cart
            cart[str(product.id)]['product'] = product  # use __str__ Product model
        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def save(self):
        self.session.modified = True  # save session after modify

    def remove(self, product):
        p_id = str(product.id)
        if p_id in self.cart:
            del self.cart[p_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

