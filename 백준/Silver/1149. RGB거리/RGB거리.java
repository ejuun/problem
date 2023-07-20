import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(br.readLine());
	int [][] arr = new int [n][3];
	for (int i = 0; i < arr.length; i++) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int j = 0; j < 3; j++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i][j] = num;
		}
	}
	int [][] dp = new int [n][3];
	for (int i = 0; i < 1; i++) {
		for (int j = 0; j < 3; j++) {
			dp[i][j] = arr[i][j];
		}
	}
	for (int i = 1; i < dp.length; i++) {
		for (int j = 0; j < 3; j++) {
			if (j == 0) {
				dp[i][j] = arr[i][j] + Math.min(dp[i-1][1], dp[i-1][2]);
			}else if (j==1) {
				dp[i][j] = arr[i][j] + Math.min(dp[i-1][0], dp[i-1][2]);
			}else if (j == 2) {
				dp[i][j] = arr[i][j] + Math.min(dp[i-1][0], dp[i-1][1]);
			}
		}
	}
	int ans = 1000001;
	for (int i = 0; i < 3; i++) {
		if (ans > dp[n-1][i]) {
			ans = dp[n-1][i];
		}
	}
	System.out.println(ans);
		}
}