package problems.fork.and.join;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class Join {
    public static void main(String[] args) {
        int sum = 0;
        int n = 5;
        ExecutorService executorService = Executors.newFixedThreadPool(3);
        List<Future<Integer>> futures = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            futures.add(executorService.submit(new SimpleWorker(i)));
        }

        try {
            for (Future<Integer> future : futures) {
                sum += future.get();
            }
            System.out.println(sum);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
