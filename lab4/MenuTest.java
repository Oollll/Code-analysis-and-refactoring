import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MenuTest {
    @Test
    void testAddAndContainsDish() {
        Menu menu = new Menu();
        Dish dish = new Dish("Burger", 90.0);
        menu.addDish(dish);
        assertTrue(menu.containsDish(dish));
    }

    @Test
    void testMenuIsInitiallyEmpty() {
        Menu menu = new Menu();
        assertTrue(menu.getDishes().isEmpty());
    }
}