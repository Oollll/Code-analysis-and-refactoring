// === Menu.java ===
import java.util.ArrayList;
import java.util.List;

public class Menu {
    private List<Dish> dishes = new ArrayList<>();

    public void addDish(Dish dish) {
        dishes.add(dish);
    }

    public boolean containsDish(Dish dish) {
        return dishes.contains(dish);
    }

    public List<Dish> getDishes() {
        return dishes;
    }
}