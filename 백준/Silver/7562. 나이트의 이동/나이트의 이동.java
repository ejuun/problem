import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int a = 0; a < T; a++) {
			
		StringTokenizer st = new StringTokenizer(br.readLine());
		int I = Integer.parseInt(st.nextToken());
		int [][] visit = new int [I][I];

		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int sx = Integer.parseInt(st1.nextToken());
		int sy = Integer.parseInt(st1.nextToken());
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int ex = Integer.parseInt(st2.nextToken());
		int ey = Integer.parseInt(st2.nextToken());
            
		int ans = 0;
            
		if (sx == ex && sy == ey) {
			System.out.println(ans);
		}
		else {
			visit[sx][sy] = 1;
			
			Queue<int []> queue = new LinkedList<int []>();
			queue.offer(new int[] {sx, sy});
			
			while(!queue.isEmpty()) {
				int[] poll = queue.poll();
				int[] dx = {-1, -2, -2, -1, 1, 2, 2, 1};
				int[] dy = {-2, -1, 1, 2, 2, 1, -1, -2};
								
				for (int k = 0; k < 8; k++) {
					int nx = poll[0] + dx[k];
					int ny = poll[1] + dy[k];
					
					if (nx < 0 || nx >= I || ny < 0 || ny >= I) {
						continue;
					}
				
					if (visit[nx][ny] == 0) {
						visit[nx][ny] = visit[poll[0]][poll[1]]+1;
						queue.offer(new int[] {nx, ny});
						}
					}
				}
			System.out.println(visit[ex][ey]-1);
			}
		}
    }
}