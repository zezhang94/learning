package problems;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;

public class ThreadOrder {

    public static void main(String[] args) {
        CyclicBarrier barrier = new CyclicBarrier(3, new Runnable() {
            @Override
            public void run() {
                System.out.print("|");
            }
        });

        Thread printA = new Thread(new CyclicWorker(barrier, "A"));
        printA.start();
        Thread printB = new Thread(new CyclicWorker(barrier, "B"));
        printB.start();
        Thread printC = new Thread(new CyclicWorker(barrier,"C"));
        printC.start();

    }

}

class CyclicWorker implements Runnable {

    private static List<CountDownLatch> latchA;
    private static List<CountDownLatch> latchB;

    private static final int N = 7;
    static {
        latchA = new ArrayList<>();
        latchB = new ArrayList<>();
        for (int i = 0; i < N; ++i) {
            latchA.add(new CountDownLatch(1));
            latchB.add(new CountDownLatch(1));
        }
    }
    private CyclicBarrier barrier;
    private String option;

    CyclicWorker(CyclicBarrier barrier, String option) {
        this.barrier = barrier;
        this.option = option;
    }

    @Override
    public void run() {
        try {
            int i = 0;
            Thread t = null;
            while (i < N) {
                switch (option) {
                    case "A":
                        t = new Thread(new PrintA(latchA.get(i)));
                        break;
                    case "B":
                        t = new Thread(new PrintB(latchA.get(i), latchB.get(i)));
                        break;
                    case "C":
                        t = new Thread(new PrintC(latchB.get(i)));
                        break;
                    default:
                        break;
                }
                if (t != null) {
                    t.start();
                    t.join();
                }
                barrier.await();
                ++i;
            }
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }
    }
}

class PrintA implements Runnable {

    private CountDownLatch latchA;

    PrintA(CountDownLatch latch) {
        latchA = latch;
    }

    @Override
    public void run() {
        System.out.print("A");
        latchA.countDown();
    }
}

class PrintB implements Runnable {

    private CountDownLatch latchA;
    private CountDownLatch latchB;

    PrintB(CountDownLatch latch1, CountDownLatch latch2) {
        latchA = latch1;
        latchB = latch2;
    }
    @Override
    public void run() {
        try {
            latchA.await();
            System.out.print("B");
            latchB.countDown();
        } catch (InterruptedException e) {
            // empty
        }
    }
}

class PrintC implements Runnable {

    private CountDownLatch latchB;

    PrintC(CountDownLatch latch) {
        latchB = latch;
    }

    @Override
    public void run() {
        try {
            latchB.await();
            System.out.print("C");
        } catch (InterruptedException e) {
            // empty
        }

    }
}

