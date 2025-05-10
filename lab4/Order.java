// === Order.java ===
import java.util.List;

public abstract class Order {
    protected Client client;
    protected List<Dish> items;

    public Order(Client client, List<Dish> items) {
        this.client = client;
        this.items = items;
    }

    public Client getClient() {
        return client;
    }

    public List<Dish> getItems() {
        return items;
    }
}