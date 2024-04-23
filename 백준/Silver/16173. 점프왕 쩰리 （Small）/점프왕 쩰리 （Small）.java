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
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int n = Integer.parseInt(st.nextToken());
				arr[i][j] = n;
			}
		}
		Queue<int []> queue = new LinkedList<>();
		visit[0][0] = 1;
		queue.offer(new int [] {0, 0, arr[0][0]});
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		while(!queue.isEmpty()) {
			int[] poll = queue.poll();
			
			for (int i = 0; i < 4; i++) {
				int nx = poll[0] + dx[i] * poll[2];
				int ny = poll[1] + dy[i] * poll[2];
				
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
					continue;
				}
				if(visit[nx][ny] == 0) {
					visit[nx][ny] = 1;
					queue.offer(new int [] {nx , ny, arr[nx][ny]});
				}
			}
		}
		if (visit[N-1][N-1] == 0) {
			System.out.println("Hing");
		}else {
			System.out.println("HaruHaru");
		}
	}
}