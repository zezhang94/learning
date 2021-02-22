package problems.fork.and.join;

import java.util.concurrent.Callable;

public class SimpleWorker implements Callable<Integer> {

    private int value;

    public SimpleWorker(int arg) {
        this.value = arg;
    }

    @Override
    public Integer call() {
        return value + 1;
    }
}
