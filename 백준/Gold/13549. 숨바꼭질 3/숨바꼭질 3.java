import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int [] visited = new int[100001];
		visited[N] = 1;
		
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(N);
		
		int ans = 0;
		int find = 0;
		int [] move = new int [3];
		int new_num = 0;
		if (N!=K) {
			while(!queue.isEmpty()) {
				int x = queue.poll();
				
				for (int i = 0; i < move.length; i++) {
					if (i == 0) {
						new_num = x * 2;
						if (0 <= new_num && new_num <= 100000) {
							
						if (visited[new_num] == 0) {
							visited[new_num] = visited[x];
							queue.offer(new_num);
						}
						}
					}
					else if(i == 1) {
						new_num = x -1;
						if (new_num >= 0) {
							if (visited[new_num] == 0) {
								visited[new_num] = visited[x] + 1;
								queue.offer(new_num);
							}
						}
					}
					else {
						new_num = x + 1;
						if (new_num <= 100000) {
							if (visited[new_num] == 0) {
								visited[new_num] = visited[x] + 1;
								queue.offer(new_num);
							}
						}
					}
					if (new_num == K) {
						find = 1;
						break;
					}
				}
				if (find == 1) {
					break;
				}
			}
			ans = visited[K] - 1;
		}
		System.out.println(ans);
	}
}