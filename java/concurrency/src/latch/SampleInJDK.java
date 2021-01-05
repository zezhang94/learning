package latch;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executor;

public class SampleInJDK {
}

/*
 * A start signal that prevents any worker from proceeding until
 * the driver is ready for them to proceed;
 */
class Driver {
    void main() throws InterruptedException {
        int N = 10;

        CountDownLatch startSignal = new CountDownLatch(1);
        CountDownLatch doneSignal = new CountDownLatch(N);

        for (int i = 0; i < N; ++i) // create and start threads
            new Thread(new Worker(startSignal, doneSignal)).start();

        doSomethingElse();            // don't let run yet
        startSignal.countDown();      // let all threads proceed
        doSomethingElse();
        doneSignal.await();           // wait for all to finish
    }

    void doSomethingElse() {
    }
}

class Worker implements Runnable {
    private final CountDownLatch startSignal;
    private final CountDownLatch doneSignal;

    Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
        this.startSignal = startSignal;
        this.doneSignal = doneSignal;
    }

    public void run() {
        try {
            startSignal.await();
            doWork();
            doneSignal.countDown();
        } catch (InterruptedException ex) {
        } // return;
    }

    void doWork() {
    }
}


/*
 * A completion signal that allows the driver to wait until all workers have completed.
 */
class Driver2 {

    void main() throws InterruptedException {
        int N = 10;

        CountDownLatch doneSignal = new CountDownLatch(N);
        Executor e = new Executor() {
            @Override
            public void execute(Runnable command) {
                System.out.println("");
            }
        };

        for (int i = 0; i < N; ++i) // create and start threads
            e.execute(new WorkerRunnable(doneSignal, i));

        doneSignal.await();           // wait for all to finish
    }
}

class WorkerRunnable implements Runnable {
    private final CountDownLatch doneSignal;
    private final int i;

    WorkerRunnable(CountDownLatch doneSignal, int i) {
        this.doneSignal = doneSignal;
        this.i = i;
    }

    public void run() {
        try {
            doWork(i);
            doneSignal.countDown();
        } catch (InterruptedException ex) {
        } // return;
    }

    void doWork(int i) throws InterruptedException {
    }
}