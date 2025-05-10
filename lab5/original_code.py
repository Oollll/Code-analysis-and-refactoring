class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
        self.status = "created"

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def save_to_database(self):
        print("Saving to database...")

    def send_email_confirmation(self):
        print("Sending email to", self.customer_name)