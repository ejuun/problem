import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [][] arr = new int [N][N];
		int [][] visit = new int [N][N];
		
		for (int i = 0; i < N; i++) {
			String s = br.readLine();
			for (int j = 0; j < N; j++) {
				int n = Character.getNumericValue(s.charAt(j));
				arr[i][j] = n;
			}
		}
        
		Queue<int []> queue = new LinkedList<int []>();
		ArrayList<Integer> val = new ArrayList<Integer>();
        
		int house = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == 1 && visit[i][j] == 0) {
					int cnt = 1;
					house += 1;
					queue.offer(new int[] {i,j});
					visit[i][j] = 1;
					while(!queue.isEmpty()) {
						int[] poll = queue.poll();
						int[] dx = {0, 0, -1, 1};
						int[] dy = {-1, 1, 0, 0};										
						for (int k = 0; k < 4; k++) {
							int nx = poll[0] + dx[k];
							int ny = poll[1] + dy[k];
							
							if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
								continue;
							}
						
							if (visit[nx][ny] == 0 && arr[nx][ny] == 1) {
								visit[nx][ny] = 1;
								cnt += 1;
								queue.offer(new int[] {nx, ny});
								}
							}
						}
					val.add(cnt);
				    }
			    }
	        }
		System.out.println(house);
        Collections.sort(val);
		for (int i = 0; i < val.size(); i++) {
			System.out.println(val.get(i));
		    }
		}
    }