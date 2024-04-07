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
		int [][] visit = new int [N][M];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int n = Integer.parseInt(st1.nextToken());
				arr[i][j] = n;
			}
		}
        
		int ans = 0;
		Queue<int []> queue = new LinkedList<int []>();
		
        for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 1 && visit[i][j] == 0) {
					ans += 1;
					queue.offer(new int[] {i,j});
					visit[i][j] = 1;
		
                    while(!queue.isEmpty()) {
						int[] poll = queue.poll();
						int[] dx = {0, 0, -1, 1, -1, -1, 1, 1};
						int[] dy = {-1, 1, 0, 0, -1, 1, 1, -1};
										
						for (int k = 0; k < 8; k++) {
							int nx = poll[0] + dx[k];
							int ny = poll[1] + dy[k];
							
							if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
								continue;
							}
						
							if (visit[nx][ny] == 0 && arr[nx][ny] == 1) {
								visit[nx][ny] = 1;
								queue.offer(new int[] {nx, ny});
								}
							}
					}
				}
			}
		}
		System.out.println(ans);
		}
	}