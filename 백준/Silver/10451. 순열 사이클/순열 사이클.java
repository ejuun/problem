import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            ArrayList<Integer> end = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                end.add(Integer.parseInt(st.nextToken()));
            }

            boolean[] visit = new boolean[N];
            int ans = 0;

            for (int i = 0; i < N; i++) {
                if (!visit[i]) {
                    ans++;
                    Queue<Integer> queue = new LinkedList<>();
                    queue.add(i);
                    visit[i] = true;

                    while (!queue.isEmpty()) {
                        int x = queue.poll();
                        int nextIndex = end.get(x) - 1;
                        if (!visit[nextIndex]) {
                            visit[nextIndex] = true;
                            queue.add(nextIndex);
                        }
                    }
                }
            }
            System.out.println(ans);
        }
	}
}