import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int [] arr = new int [N];
		int [] sum = new int [N];
		StringTokenizer starr = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			int n = Integer.parseInt(starr.nextToken());
			arr[i] = n;
		}
		
		sum[0] = arr[0] % M;
		for (int i = 1; i < sum.length; i++) {
			sum[i] = (sum[i-1] + arr[i]) % M;
		}
		
		long [] cnt = new long [M];
		for (int i = 0; i < N; i++) {
			cnt[sum[i]] += 1;
		}
		
		long ans = 0;
		for (int i = 0; i < cnt.length; i++) {
			if(i == 0) {
				ans += (cnt[i] * (cnt[i]+1)) / 2;
			}
			else {
				ans += (cnt[i] * (cnt[i]-1)) / 2;
			}
		}		
		System.out.println(ans);

	}
}