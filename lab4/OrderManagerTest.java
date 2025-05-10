// === OrderManagerTest.java ===
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;

public class OrderManagerTest {
    @Test
    void testOrderNotification() {
        OrderManager manager = new OrderManager();
        TestNotifier notifier = new TestNotifier();
        manager.addNotifier(notifier);

        Client client = new Client("Petro");
        Order order = new RegularOrder(client, List.of(new Dish("Fish", 120)));
        manager.placeOrder(order);

        assertTrue(notifier.wasNotified);
    }

    static class TestNotifier implements OrderNotifier {
        boolean wasNotified = false;
        public void notifyKitchen(Order order) {
            wasNotified = true;
        }
    }
}