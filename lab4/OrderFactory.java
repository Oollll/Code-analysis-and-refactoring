// === OrderFactory.java ===

import java.util.List;

public class OrderFactory {
    public static Order createOrder(String type, Client client, List<Dish> items) {
        switch (type.toLowerCase()) {
            case "regular":
                return new RegularOrder(client, items);
            case "bulk":
                return new BulkOrder(client, items);
            default:
                throw new IllegalArgumentException("Invalid order type: " + type);
        }
    }
}