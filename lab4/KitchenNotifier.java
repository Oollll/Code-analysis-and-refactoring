// === KitchenNotifier.java ===
public class KitchenNotifier implements OrderNotifier {
    @Override
    public void notifyKitchen(Order order) {
        System.out.println("[Kitchen] New order from client: " + order.getClient().getName());
    }
}