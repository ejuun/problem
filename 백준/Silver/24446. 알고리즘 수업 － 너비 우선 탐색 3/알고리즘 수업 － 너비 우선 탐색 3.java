import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		ArrayList<ArrayList<Integer>> G = new ArrayList<>();
		int [] visited = new int[N+1];
		
		for (int i = 0; i < N+1; i++) {
			G.add(new ArrayList<>());
			visited[i] = -1;
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st1.nextToken());
			int v = Integer.parseInt(st1.nextToken());
			G.get(u).add(v);
			G.get(v).add(u);
		}
		
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(R);
		visited[R] = 0;
		while(!queue.isEmpty()) {
				int x = queue.poll();
				
				for (int i = 0; i < G.get(x).size(); i++) {
					int num = G.get(x).get(i);
					if (visited[num] == -1) {
						visited[num] = visited[x] + 1;
						queue.offer(num);
					}
				}
		}
		for (int i = 1; i < visited.length; i++) {
			System.out.println(visited[i]);
		}
		}
}