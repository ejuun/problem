import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	static int [][] arr;
	static int [] visit;
	static int [] dfs_visit;
	static int N;
	static ArrayList<ArrayList<Integer>> G;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());
		
		G = new ArrayList<>();
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
		for (int i = 1; i < N+1; i++) {
			Collections.sort(G.get(i));
		}
		dfs_visit = new int [N+1];
		dfs(V);
		System.out.println();
		bfs(V);

	}
	static void dfs(int v) {
		dfs_visit[v] = 1;
		System.out.print(v + " ");
		for (int dot : G.get(v)) {
			if(dfs_visit[dot] == 0) {
				dfs(dot);
			}
		}	
	}
    
	static void bfs(int v) {
	
		visit = new int [N+1];
		visit[v] = 1;
		System.out.print(v + " ");
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(v);
		while(!queue.isEmpty()) {
			int x = queue.poll();
			
			for(int dot : G.get(x)) {
				if(visit[dot] == 0) {
					System.out.print(dot + " ");
					visit[dot] = 1;
					queue.offer(dot);
				}
			}
		}
		return;
	}
}