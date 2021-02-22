import java.util.Date;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Main {

    public static void main(String[] args) {

        ReentrantLock lock = new ReentrantLock();
        CyclicBarrier barrier = new CyclicBarrier(1);
    }
}
