import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static int white = 0;
	public static int blue = 0;
	public static int[][] arr;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
			
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				StringTokenizer st1 = new StringTokenizer(st.nextToken());
					int n = Integer.parseInt(st1.nextToken());
					arr[i][j] = n;
				}
			}
		recur(N, 0, 0);
		System.out.println(white);
		System.out.println(blue);
		
			}
	
	public static void recur(int N, int s, int e) {
		int check = arr[s][e];
		for (int i = s; i < N+s; i++) {
			for (int j = e; j < N+e; j++) {
				if (check != arr[i][j]) {
					check = -1;
					break;
				}
			}
			if (check == -1) {
				break;
		}
	}
		if (check == -1) {
			recur(N/2, s, e);
			recur(N/2, s, e+N/2);
			recur(N/2, s+N/2, e);
			recur(N/2, s+N/2, e+N/2);
		}
		else {
			if (check == 1) {
				blue += 1;
			}else {
				white += 1;
			}
		}
		}
}