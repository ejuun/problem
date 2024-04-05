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
        
		int [] visit = new int [N+1];

		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(1);

		while(!queue.isEmpty()) {
			int x = queue.poll();
			
			for (int dot : G.get(x)) {
				if(visit[dot] == 0) {
					queue.offer(dot);
					visit[dot] = visit[x] + 1;
				}
			}
		}
		int idx = 0;
		int dis = 0;
		int cnt = 0;

		for (int i = 2; i < visit.length; i++) {
			if (dis < visit[i]) {
				dis = visit[i];
				idx = i;
				cnt = 1;
			}
			if (dis == visit[i]) {
				cnt += 1;
			}
		}
		cnt -= 1;
		System.out.print(idx+" "+dis+" "+cnt);
	}
	}