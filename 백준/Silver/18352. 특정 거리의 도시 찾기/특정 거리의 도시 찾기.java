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
		int K = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		ArrayList<ArrayList<Integer>> G = new ArrayList<>();
		for (int i = 0; i < N+1; i++) {
			G.add(new ArrayList<>());
		}
		for (int i = 0; i < M; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st1.nextToken());
			int e = Integer.parseInt(st1.nextToken());
			G.get(s).add(e);
		}
		int [] visit = new int [N+1];
		visit[X] = 1;
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(X);
		
		while(!queue.isEmpty()) {
			int x = queue.poll();
			
			for (int dot : G.get(x)) {
				if(visit[dot] == 0) {
					queue.offer(dot);
					visit[dot] = visit[x] + 1;
				}
			}
		}
		ArrayList<Integer> ans = new ArrayList<Integer>();
		for (int i = 1; i < visit.length; i++) {
			if (visit[i] == K +1) {
				ans.add(i);
			}
		}
		if (ans.size() == 0) {
			System.out.println(-1);
		}else {
			for (int i = 0; i < ans.size(); i++) {
				System.out.println(ans.get(i));
			}
		}
		}
	}