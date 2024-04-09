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
		int [][][] visit = new int [N][M][2];
		
		for (int i = 0; i < N; i++) {
			String s = br.readLine();
			for (int j = 0; j < M; j++) {
				int n = Character.getNumericValue(s.charAt(j));
				arr[i][j] = n;
			}
		}

		Queue<int []> queue = new LinkedList<int []>();
		queue.offer(new int [] {0, 0, 0});
		visit[0][0][0] = 1;
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		int idx = -1;
		
        while(!queue.isEmpty()) {
			int[] poll = queue.poll();
			
			if(poll[0] == N-1 && poll[1] == M-1) {
				idx = poll[2];
				break;
			}
							
			for (int k = 0; k < 4; k++) {
				int nx = poll[0] + dx[k];
				int ny = poll[1] + dy[k];
				
				if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
					continue;
				}
			
				if (arr[nx][ny] == 1 && poll[2] == 0) {
					visit[nx][ny][poll[2]+1] = visit[poll[0]][poll[1]][poll[2]] + 1;
					queue.offer(new int[] {nx, ny, poll[2]+1});
					}
				else if(arr[nx][ny] == 0 && visit[nx][ny][poll[2]] == 0) {
					visit[nx][ny][poll[2]] = visit[poll[0]][poll[1]][poll[2]] + 1;
					queue.offer(new int[] {nx, ny, poll[2]});
				}
				}
		}
		int ans = -1;
		if (idx != -1) {
			ans = visit[N-1][M-1][idx];
		}
		System.out.println(ans);
		}
	}