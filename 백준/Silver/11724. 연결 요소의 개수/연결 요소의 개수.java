import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		ArrayList<ArrayList<Integer>> G = new ArrayList<>();

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int [] visited = new int [N+1];

		for (int i = 0; i < N+1; i++) {
			G.add(new ArrayList<>());
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
				int s = Integer.parseInt(st1.nextToken());
				int e = Integer.parseInt(st1.nextToken());
				G.get(s).add(e);
				G.get(e).add(s);
		}
		
		Queue<Integer> queue = new LinkedList<Integer>();
		int ans = 0;
		for (int i = 1; i < N+1; i++) {
			if (visited[i] == 0) {
				ans += 1;
				queue.offer(i);
				visited[i] = 1;
				while(!queue.isEmpty()) {
					int x = queue.poll();
					
					for (int dot : G.get(x)) {
						if(visited[dot] == 0) {
							queue.offer(dot);
							visited[dot] = 1;
						}
					}	
				}
			}
		}
		System.out.println(ans);
	}
	}