import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [] arr = new int [N];

	StringTokenizer st = new StringTokenizer(br.readLine());
	
	for (int i = 0; i < arr.length; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
	}
	int [] dp = new int [N];
	for (int i = 0; i < dp.length; i++) {
		dp[i] = 1;
	}
	
	if (N == 1) {
		System.out.println(1);
	}else {
		for (int i = 0; i < dp.length; i++) {
			int find = 0;
			for (int j = i; j > -1 ; j--) {
				if (arr[i] > arr[j]) {
					if (dp[i] <= dp[j]) {
						find = 1;
						dp[i] = dp[j];
					}
				}
			}
			if (find == 1) {
				dp[i] += 1;
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