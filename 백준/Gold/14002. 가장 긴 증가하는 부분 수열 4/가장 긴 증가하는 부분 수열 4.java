import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int [N];
 		int[] dp = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
 		for(int i = 0; i < N; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
			dp[i] = 1;
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < i; j++) {
				if (arr[i] > arr[j]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
				}
			}
		}
		int len = 0;
		int max_val = 0;
		for (int i = 0; i < N; i++) {
			if(len < dp[i]) {
				len = dp[i];
				max_val = arr[i];
			}
		}
		int len_ans = len;
		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = N-1; i >= 0; i--) {
			if (dp[i] == len && arr[i] <= max_val) {
				ans.add(arr[i]);
				len -= 1;
				max_val = arr[i];
			}
		}
		System.out.println(len_ans);
		for (int i = ans.size()-1; i >= 0; i--) {
			System.out.print(ans.get(i)+" ");
		}
	}
}