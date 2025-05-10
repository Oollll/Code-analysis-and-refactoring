// === BulkOrder.java ===
import java.util.List;

public class BulkOrder extends Order {
    public BulkOrder(Client client, List<Dish> items) {
        super(client, items);
    }
}