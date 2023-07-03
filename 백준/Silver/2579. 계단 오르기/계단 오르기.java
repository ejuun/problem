import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [] arr = new int[N+1];
	for (int i = 1; i < arr.length; i++) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr[i] = Integer.parseInt(st.nextToken());
	}
	int [] dp = new int [N+1];
	dp[1] = arr[1];
	if (N ==2) {
		dp[2] = Math.max(arr[2], dp[1] + arr[2]);
	}
	else if (N >= 3) {
		dp[2] = Math.max(arr[2], dp[1] + arr[2]);
		for (int i = 3; i < dp.length; i++) {
			dp[i] = Math.max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]);
		}
	}
	System.out.println(dp[N]);
	}
}