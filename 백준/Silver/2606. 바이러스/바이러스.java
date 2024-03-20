import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		int L = Integer.parseInt(br.readLine());
		
		int [][] com = new int [T+1][T+1];
		
		for (int a = 0; a < L; a++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int S = Integer.parseInt(st.nextToken());
				int E = Integer.parseInt(st.nextToken());
				com[S][E] = com[E][S] = 1;
			}
		int [] visited = new int[T+1];
		int ans = 0;
        
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(1);
        visited[1] = 1;
		
        while(!queue.isEmpty()) {
        	int x = queue.poll();
        	for (int i = 0; i < com.length; i++) {
				if (com[x][i] == 1 && visited[i] == 0) {
					visited[i] = 1;
					queue.offer(i);
					ans += 1;
				}
        	}
    	}
        System.out.println(ans);
	}
}