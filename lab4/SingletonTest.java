import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.List;

public class SingletonTest {
    @Test
    void testSingletonInstance() {
        OrderDatabase db1 = OrderDatabase.getInstance();
        OrderDatabase db2 = OrderDatabase.getInstance();
        assertSame(db1, db2);
    }

    @Test
    void testAddAndRetrieveOrder() {
        OrderDatabase db = OrderDatabase.getInstance();
        Client client = new Client("Sofia");
        List<Dish> items = new ArrayList<>();
        items.add(new Dish("Cake", 80));
        Order order = new RegularOrder(client, items);
        db.addOrder(order);
        assertTrue(db.getOrders().contains(order));
    }
}