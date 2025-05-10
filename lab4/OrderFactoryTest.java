// === OrderFactoryTest.java ===
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
import java.util.ArrayList;

public class OrderFactoryTest {
    @Test
    void testCreateRegularOrder() {
        Client client = new Client("Ivan");
        List<Dish> dishes = List.of(new Dish("Soup", 50));
        Order order = OrderFactory.createOrder("regular", client, dishes);
        assertTrue(order instanceof RegularOrder);
    }

    @Test
    void testCreateBulkOrder() {
        Client client = new Client("Olena");
        List<Dish> dishes = List.of(new Dish("Steak", 200));
        Order order = OrderFactory.createOrder("bulk", client, dishes);
        assertTrue(order instanceof BulkOrder);
    }

    @Test
    void testInvalidOrderType() {
        Client client = new Client("Test");
        List<Dish> dishes = new ArrayList<>();
        assertThrows(IllegalArgumentException.class, () -> {
            OrderFactory.createOrder("unknown", client, dishes);
        });
    }
}