// === OrderManager.java ===
import java.util.ArrayList;
import java.util.List;

public class OrderManager {
    private List<OrderNotifier> notifiers = new ArrayList<>();

    public void addNotifier(OrderNotifier notifier) {
        notifiers.add(notifier);
    }

    public void placeOrder(Order order) {
        OrderDatabase.getInstance().addOrder(order);
        for (OrderNotifier notifier : notifiers) {
            notifier.notifyKitchen(order);
        }
    }
}