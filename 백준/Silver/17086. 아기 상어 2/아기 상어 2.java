import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	static int [][] arr;
	static int[] dx = {0, 0, -1, 1, -1, -1, 1, 1};
	static int[] dy = {-1, 1, 0, 0, -1, 1, 1, -1};
	static int[][] visit;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		arr = new int [N][M];
		for (int i = 0; i < N; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for(int j = 0; j < M; j++) {
				int n = Integer.parseInt(st1.nextToken());
				arr[i][j] = n;
			}
		}
		int ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0) {
					ans = Math.max(ans, bfs(i, j));
				}
			}
		}
		System.out.println(ans);
	}
    
	static int bfs(int i, int j) {
		int N = arr.length;
		int M = arr[0].length;
		Queue<int[]> queue = new LinkedList<int[]>();

		int[][] visit = new int [N][M];
		visit[i][j] = 1;
		queue.offer(new int[] {i,j});
		while(!queue.isEmpty()) {
			int [] poll = queue.poll();
			
			for (int k = 0; k < 8; k++) {
				int ni = poll[0] + dx[k];
				int nj = poll[1] + dy[k];
				if (ni < 0 || ni >= N || nj < 0 || nj >= M) {
					continue;
				}
				if (visit[ni][nj] == 0) {
					visit[ni][nj] = visit[poll[0]][poll[1]] + 1;
					if (arr[ni][nj] == 0) {
						queue.offer(new int[] {ni, nj});					
					}
					else {
						return visit[ni][nj] -1 ;
					}
				}
			}
		}
		return 0;
	}
}