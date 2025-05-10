class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
        self.status = "created"

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)


class OrderRepository:
    def save(self, order: Order):
        print(f"Order for {order.customer_name} saved to database.")


class EmailService:
    def send_confirmation(self, customer_name):
        print(f"Confirmation email sent to {customer_name}")