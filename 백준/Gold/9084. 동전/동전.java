import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	
	public static void main(String[] args) throws IOException {	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
        for (int j = 0; j < T; j++) {
			int N = Integer.parseInt(br.readLine());
			int [] coins = new int [N];
			StringTokenizer st = new StringTokenizer(br.readLine());
	 		for(int i = 0; i < N; i++) {
				int n = Integer.parseInt(st.nextToken());
				coins[i] = n;
			}
            
	 		int goal = Integer.parseInt(br.readLine());
	 		int [] dp = new int [goal+1];
	 		dp[0] = 1;
	 		
            for (int coin : coins) {
				for (int i = coin; i < dp.length; i++) {
					dp[i] += dp[i-coin]; 
				}
			}
	 		System.out.println(dp[goal]);
			} 
	}
}