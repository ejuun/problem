import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	static int [][] arr;
	static int N;
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {-1, 1, 0, 0};
	static int[][] visit;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		int max_val = 0;
		arr = new int [N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int n = Integer.parseInt(st.nextToken());
				arr[i][j] = n;
				max_val = Math.max(max_val, n);
			}
		}
		int ans = 0;
		for (int k = 0; k <= max_val; k++) {	
			visit = new int [N][N];
			int cnt = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] > k && visit[i][j] == 0) {
						bfs(k, i, j);
						cnt += 1;
					}
				}
			}
			if (ans < cnt) {
				ans = cnt;
			}
		}
		System.out.println(ans);
		
		}
	static void bfs(int v, int x, int y) {
		visit[x][y] = 1;
		Queue<int []> queue = new LinkedList<>();
		queue.offer(new int[] {x, y});
		while(!queue.isEmpty()) {
			int[] poll = queue.poll();
			
			for (int i = 0; i < 4; i++) {
				int nx = poll[0] + dx[i];
				int ny = poll[1] + dy[i];
				
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
				continue;
				}
				if (arr[nx][ny] > v && visit[nx][ny] == 0) {
					visit[nx][ny] = 1;
					queue.offer(new int[] {nx, ny});
				}
			}
		}
		return;
	}
}