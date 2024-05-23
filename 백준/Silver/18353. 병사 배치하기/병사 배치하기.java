import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int [] dp = new int [n];
		int [] arr = new int [n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i] = num;
			dp[i] = 1;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if(arr[j] > arr[i]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
				}
			}
		}
		int max_val = 0;
		for (int i = 0; i < dp.length; i++) {
			if(max_val < dp[i]) {
				max_val = dp[i];
			}
		}
		int ans = n - max_val;
		System.out.println(ans);
	} 
}