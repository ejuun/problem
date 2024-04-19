import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
    static int[] dx = {0, 0, -1, 1, -1, -1, 1, 1};
	static int[] dy = {-1, 1, 0, 0, -1, 1, 1, -1};	
    
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			if(w== 0 && h == 0) {
				break;
			}
			int [][] arr = new int [h][w];
			int [][] visit = new int [h][w];
            
			for (int i = 0; i < h; i++) {
				StringTokenizer st1 = new StringTokenizer(br.readLine());
				for (int j = 0; j < w; j++) {
					int n = Integer.parseInt(st1.nextToken());
					arr[i][j] = n;
				}
			}
			int ans = 0;

			Queue<int []> queue = new LinkedList<>();
			
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					if (arr[i][j] == 1 && visit[i][j] == 0) {
						ans += 1;
						queue.offer(new int[] {i,j});
						visit[i][j] = 1;

						while (!queue.isEmpty()) {
							int [] poll = queue.poll();
							for (int k = 0; k < 8; k++) {
								int nx = poll[0] + dx[k];
								int ny = poll[1] + dy[k];
								
								if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
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
}