import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [][] arr = new int [N][N];
	for (int i = 0; i < arr.length; i++) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int j = 0; j < i+1; j++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i][j] = n;
		}
	}
	int [][] dp = new int [N][N];
	if (N == 1) {
		System.out.println(arr[0][0]);
	}
	else if (N==2) {
		dp[0][0] = arr[0][0];
		System.out.println(dp[0][0]+Math.max(arr[1][0], arr[1][1]));
	}
	else {
		dp[0][0] = arr[0][0];
		
		for (int i = 1; i < dp.length; i++) {
			for (int j = 0; j < i+1; j++) {
				if (j == 0) {
					dp[i][j] = arr[i][j] +  dp[i-1][j];
				}
				else if (j == i) {
					dp[i][j] = arr[i][j] +  dp[i-1][j-1];

				}else {
				dp[i][j] = arr[i][j] + Math.max(dp[i-1][j-1], dp[i-1][j]);
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < dp.length; i++) {
			if (ans < dp[dp.length-1][i]) {
				ans = dp[dp.length-1][i];
			}	
			}
		System.out.println(ans);
	}
	
	}
			}