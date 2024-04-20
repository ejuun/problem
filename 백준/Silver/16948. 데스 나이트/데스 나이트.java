import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	static int [][] arr;
	static int[][] visit;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		arr = new int [N][N];
		visit = new int [N][N];
		StringTokenizer st = new StringTokenizer(br.readLine());
			int r1 = Integer.parseInt(st.nextToken());
			int c1 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());
			int c2 = Integer.parseInt(st.nextToken());
			visit[r1][c1] = 1;
			int ans = -1;
			int[] dx = {-2, -2, 0, 0, 2, 2};
			int[] dy = {-1, 1, -2, 2, -1, 1};										

			Queue<int []> queue = new LinkedList<>();
			queue.offer(new int [] {r1, c1});
			while(!queue.isEmpty()) {
				int [] poll = queue.poll();
				
				if (poll[0] == r2 && poll[1]== c2) {
					break;
				}
				
				for (int i = 0; i < 6; i++) {
					int nx = poll[0] + dx[i];
					int ny = poll[1] + dy[i];
					
					if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
						continue;
					}
					if(visit[nx][ny] == 0) {
						visit[nx][ny] = visit[poll[0]][poll[1]] + 1;
						queue.offer(new int [] {nx , ny});
					}
				}
			}
			if(visit[r2][c2] != 0) {
				ans = visit[r2][c2] -1 ;
			}
			System.out.println(ans);
	}
}