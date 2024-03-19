import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for (int a = 0; a < T; a++) {
		int cnt = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int [][] arr = new int[M][N];
		int [][] visited = new int[M][N];
		
		for (int i = 0; i < K; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st1.nextToken());
				int y = Integer.parseInt(st1.nextToken());
				arr[x][y] = 1;
			}
        
		int[] X = {0, 0, -1, +1};
        int[] Y = {-1, +1, 0, 0};
        
        Queue<int[]> queue = new LinkedList<int[]>();
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (visited[i][j] == 0 && arr[i][j] != 0) {
					cnt += 1;
					queue.offer(new int[] {i, j});
					visited[i][j] = 1;
					while (!queue.isEmpty()) {
						int[] poll = queue.poll();
						
						for (int l = 0; l < 4; l++) {
							int nx = poll[0] + X[l];
							int ny = poll[1] + Y[l];
						
						if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
							continue;
						}
						if (arr[nx][ny] == 1 && visited[nx][ny] == 0) {
							queue.offer(new int[] {nx, ny});
							visited[nx][ny] = 1;
							}
							}
						
						}
						
					}
				}
			}
		System.out.println(cnt);
		}
	}
	}