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
		int [][] arr = new int [N][M];
		int [][] visited = new int [N][M];
        int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		
        for (int i = 0; i < N; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int a = Integer.parseInt(st1.nextToken());
				arr[i][j] = a;
			}
		}
        
		Queue<int []> queue = new LinkedList<int[]>();
		
		int cnt = 0;
		int max_val = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 1 && visited[i][j] == 0) {
					
					int s = 1;
					cnt += 1;
					
					queue.offer(new int[] {i, j});
					visited[i][j] = s;
					
					while (!queue.isEmpty()) {
						int[] poll = queue.poll();
						
						for (int k = 0; k < 4; k++) {
							int nx = poll[0] + dx[k];
							int ny = poll[1] + dy[k];
							
							if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
								continue;
							}
						
							if (visited[nx][ny] == 0 && arr[nx][ny] == 1) {
								s += 1;
								visited[nx][ny] = 1;
								queue.offer(new int[] {nx, ny});
							}
						}
					}			
					if(max_val < s) {
						max_val = s;					
					}
				}
			}
		}
		System.out.println(cnt);
		System.out.println(max_val);
	}
}