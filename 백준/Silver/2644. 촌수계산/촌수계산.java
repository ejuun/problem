import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<ArrayList<Integer>> G = new ArrayList<>();
		for (int i = 0; i < n+1; i++) {
			G.add(new ArrayList<>());
		}
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int s = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());

		int m = Integer.parseInt(br.readLine());
		for (int i = 0; i < m; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st1.nextToken());
			int y = Integer.parseInt(st1.nextToken());
			G.get(x).add(y);
			G.get(y).add(x);
		}
		
		int[] visit = new int [n+1];
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(s);
		visit[s] = 1;
		while(!queue.isEmpty()) {
			int x = queue.poll();
			for (int dot: G.get(x)) {
				if (visit[dot] == 0) {
					queue.offer(dot);
					visit[dot] = visit[x] + 1;
				}
			}
		}
		if (visit[e] == 0) {
			System.out.println(-1);
		}else {
			System.out.println(visit[e]-1);
		}
	}
}