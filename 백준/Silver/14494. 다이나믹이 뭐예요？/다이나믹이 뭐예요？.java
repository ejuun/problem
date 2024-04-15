import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int m = 1000000007;

		int [][] dp = new int [1001][1001];
		dp[0][0] = 1;
		for (int i = 1; i < 1001; i++) {
			for (int j = 1; j < 1001; j++) {
				dp[i][j] = ((dp[i-1][j] + dp[i][j-1]) % m + dp[i-1][j-1]) % m; 
			}
		}
		System.out.println(dp[N][K]);
	}
}
