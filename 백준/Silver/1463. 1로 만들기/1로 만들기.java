import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [] visit = new int [N+1];
		visit[N] = 1;
        
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(N);
		while (!queue.isEmpty()) {
			int x = queue.poll();
			
			if(x == 1) {
				System.out.println(visit[x] - 1);
				break;
			}
			
			if (x % 3 == 0) {
				int new_x = x/3;
				if (visit[new_x] == 0) {
					visit[new_x] = visit[x] + 1;
					queue.offer(new_x);
				}
			}
			if (x % 2 == 0) {
				int new_x = x/2;
				if (visit[new_x] == 0) {
					visit[new_x] = visit[x] + 1;
					queue.offer(new_x);
				}
			}
			if (x > 1) {
				int new_x = x - 1;
				if (visit[new_x] == 0) {
					visit[new_x] = visit[x] + 1;
					queue.offer(new_x);
				}
			}
		}
	}
}