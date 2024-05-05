import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [] dp = new int [10000001];
		dp[1] = 1;
		dp[2] = 2;
		for (int i = 3; i < N+1; i++) {
			dp[i] = (dp[i-2] %10) + (dp[i-1] % 10);
		}
		System.out.println(dp[N] % 10);
	}
}