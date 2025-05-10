// === OrderDatabase.java ===
import java.util.ArrayList;
import java.util.List;

public class OrderDatabase {
    private static OrderDatabase instance;
    private List<Order> orders;

    private OrderDatabase() {
        orders = new ArrayList<>();
    }

    public static synchronized OrderDatabase getInstance() {
        if (instance == null) {
            instance = new OrderDatabase();
        }
        return instance;
    }

    public void addOrder(Order order) {
        orders.add(order);
    }

    public List<Order> getOrders() {
        return orders;
    }
}
