import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int [N];
		int [] dp = new int [N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
			dp[i] = 1;
		}
		for (int i = 0; i < N; i++) {
			for (int j = i; j >= 0; j--) {
				if (arr[i] > arr[j]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
				}
			}	
		}
		int ans = 0;
		for (int i = 0; i < dp.length; i++) {
			if (ans < dp[i]) {
				ans = dp[i];
			}
		}
		System.out.println(ans);
	}
}