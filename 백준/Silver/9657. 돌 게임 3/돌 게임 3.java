import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int [] dp = new int [1001];
			dp[0] = 1;
			dp[1] = 1;
			dp[2] = 0;
			dp[3] = 1;
			dp[4] = 1;			
			int n = Integer.parseInt(br.readLine());
			for (int i = 5; i < n+1; i++) {
				if (dp[i-1] + dp[i-3] + dp[i-4] == 3) {
					dp[i] = 0;
				}else {
					dp[i] = 1;
				}
			}
			if (dp[n] == 1) {
				System.out.println("SK");
			}else {
				System.out.println("CY");
			}
    }
}