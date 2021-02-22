package problems.fork.and.join;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.FutureTask;

public class FutureAndCallable {
    public static void main(String[] args) {
        try {
            int n = 5;

            List<FutureTask<Integer>> tasks = new ArrayList<>();
            List<Thread> threads = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                tasks.add(new FutureTask<>(new SimpleWorker(i)));
                Thread thread = new Thread(tasks.get(i));
                threads.add(thread);
                thread.start();
            }

            int sum = 0;
            for (FutureTask<Integer> task : tasks) {
                sum += task.get();
            }
            System.out.println(sum);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
