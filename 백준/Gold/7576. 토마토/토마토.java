import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int [][] arr = new int [N][M];
		int [][] visited = new int[N][M];
		Queue<int []> queue = new LinkedList<int []>();
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int n = Integer.parseInt(st1.nextToken());
				arr[i][j] = n;
				visited[i][j] = -1;

				if (n == 1) {
					queue.offer(new int[] {i, j});
					visited[i][j] = 1;
				}
			}
		}
		
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		
		while(!queue.isEmpty()) {
				int[] poll = queue.poll();
				
				for (int i = 0; i < 4; i++) {
					int nx = poll[0] + dx[i];
					int ny = poll[1] + dy[i];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
						continue;
					}
					if (visited[nx][ny] == -1 && arr[nx][ny] == 0) {
						visited[nx][ny] = visited[poll[0]][poll[1]] + 1;
						queue.offer(new int[] {nx, ny});
					}
				}
		}
		int ans = -1;
		int check = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (visited[i][j] == -1 && arr[i][j] == 0) {
					check = 1;
					break;
				}
				else if(visited[i][j] != -1 && arr[i][j] != -1){
					if (ans < visited[i][j]) {
						ans = visited[i][j];
					}
				}
			}
			if (check == 1) {
				ans = -1;
				break;
			}
		}
		if (ans != -1) {
			ans -= 1;
		}
		System.out.println(ans);
	}
	}