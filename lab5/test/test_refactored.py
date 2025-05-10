from refactored_code import Order, OrderRepository, EmailService

def test_order_total_calculation():
    order = Order("Oleg", [{"price": 10, "quantity": 2}, {"price": 5, "quantity": 4}])
    assert order.calculate_total() == 40

def test_order_repository_saving(capfd):
    repo = OrderRepository()
    order = Order("Anna", [])
    repo.save(order)
    out, _ = capfd.readouterr()
    assert "Anna" in out

def test_email_service(capfd):
    email = EmailService()
    email.send_confirmation("Ivan")
    out, _ = capfd.readouterr()
    assert "Ivan" in out