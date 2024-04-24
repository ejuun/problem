import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [][] arr = new int [N][N];
		long [][] dp = new long [N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int n = Integer.parseInt(st.nextToken());
				arr[i][j]= n;
			}
		}
		dp[0][0] = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] > 0) {
					int val = arr[i][j];
				if (i + val < N) {
					dp[i + val][j] += dp[i][j];
				}
				if (j + val < N) {
					dp[i][j + val] += dp[i][j];
				}
				}
			}
		}
		System.out.println(dp[N-1][N-1]);
	}
}