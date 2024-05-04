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
		int [] dp = new int [K+1];
		int [] coins = new int [N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st1.nextToken());
			coins[i] = n;
		}
		for (int i = 1; i < K+1; i++) {
			dp[i] = 100000001;
		}
		for (int coin : coins) {
			for (int i = coin; i < K+1; i++) {
				dp[i] = Math.min(dp[i], dp[i-coin]+1);
			}
		}
		if (dp[K] == 100000001) {
			dp[K] = -1;
		}
		System.out.println(dp[K]);
	}
}