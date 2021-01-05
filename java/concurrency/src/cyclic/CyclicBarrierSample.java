package cyclic;

import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

/**
 * Run 5 threads at a time.
 */
public class CyclicBarrierSample {

    public static void main(String[] args) throws InterruptedException {

        CyclicBarrier barrier = new CyclicBarrier(5, new Runnable() {
            @Override
            public void run() {
                System.out.println("Action...GO again!");
            }
        });

        for (int i = 0; i < 5; i++) {
            Thread t = new Thread(new CyclicWorker(barrier));
            t.start();
        }

    }

    static class CyclicWorker implements Runnable {

        private CyclicBarrier barrier;

        public CyclicWorker(CyclicBarrier barrier) {
            this.barrier = barrier;
        }

        @Override
        public void run() {
            try {
                for (int i = 0; i < 7; i++) {
                    System.out.println((i + 1) + " - " + Thread.currentThread().getName());
                    barrier.await();
                }
            } catch (BrokenBarrierException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}