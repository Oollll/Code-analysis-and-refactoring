import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class DishTest {
    @Test
    void testDishCreation() {
        Dish dish = new Dish("Pizza", 150.0);
        assertEquals("Pizza", dish.getName());
        assertEquals(150.0, dish.getPrice());
    }
}