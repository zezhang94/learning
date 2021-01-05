package semaphore;

import java.util.concurrent.Semaphore;

/**
 * At most 5 threads.
 */
public class UsualSemaphoreSample {

    public static void main(String[] args) throws InterruptedException {
        Semaphore semaphore = new Semaphore(5);
        for (int i = 0; i < 30; i++) {
            Thread t = new Thread(new SemaphoreWorker(semaphore));
            t.start();
        }
    }

}

class SemaphoreWorker implements Runnable {

    private Semaphore semaphore;

    public SemaphoreWorker(Semaphore semaphore) {
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        try {
            semaphore.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            semaphore.release();
        }
    }

}