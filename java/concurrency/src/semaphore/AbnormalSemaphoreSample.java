package semaphore;

import java.util.concurrent.Semaphore;

/**
 * Run 5 threads at a time.
 */
public class AbnormalSemaphoreSample {

    public static void main(String[] args) throws InterruptedException {
        Semaphore semaphore = new Semaphore(0);
        for (int i = 0; i < 10; i++) {
            Thread t = new Thread(new MyWorker(semaphore));
            t.start();
        }
        semaphore.release(5);
        while (semaphore.availablePermits() != 0) {
            Thread.sleep(100L);
        }
        semaphore.release(5);
    }

}

class MyWorker implements Runnable {
    private Semaphore semaphore;

    public MyWorker(Semaphore semaphore) {
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        try {
            semaphore.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
