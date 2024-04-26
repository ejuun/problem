import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	static int [][] arr;
	static int[][][] visit;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int Hx = Integer.parseInt(st1.nextToken());
		int Hy = Integer.parseInt(st1.nextToken());
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int Ex = Integer.parseInt(st2.nextToken());
		int Ey = Integer.parseInt(st2.nextToken());
		
		arr = new int [N][M];
		visit = new int [N][M][2];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st3 = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int n = Integer.parseInt(st3.nextToken());
				arr[i][j] = n;
			}
		}
		
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		int D = -1;
        
		Queue<int []> queue = new LinkedList<>();
		visit[Hx-1][Hy-1][0] = 1;
		queue.offer(new int [] {Hx-1, Hy-1, 0});
		
		while(!queue.isEmpty()) {
			int[] poll = queue.poll();
			
			if (poll[0] == Ex-1 && poll[1] == Ey-1) {
				D = visit[poll[0]][poll[1]][poll[2]]-1;
				break;
			}
			
			for (int i = 0; i < 4; i++) {
				int nx = poll[0] + dx[i];
				int ny = poll[1] + dy[i];
				
				if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
					continue;
				}
				if(arr[nx][ny] ==1 && poll[2] == 0) {
					visit[nx][ny][poll[2]+1] = visit[poll[0]][poll[1]][poll[2]]+1;
					queue.offer(new int [] {nx , ny, poll[2]+1});
				}
				else if (arr[nx][ny] == 0 && visit[nx][ny][poll[2]] == 0) {
					visit[nx][ny][poll[2]] = visit[poll[0]][poll[1]][poll[2]]+1;					
					queue.offer(new int [] {nx , ny, poll[2]});
				}
			}
		}
		System.out.println(D);
	}
}