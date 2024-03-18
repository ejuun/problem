import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static int ans = 0;
	public static int[]arr;
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		arr = new int[N];
			
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
					int n = Integer.parseInt(st1.nextToken());
					arr[i] = n;
				
		}
		recur(0, 0, N, S);
		System.out.println(ans);
			}
	
	public static void recur(int idx, int hap, int N, int S) {
		if (idx >= N) {
			return;
		}
		hap += arr[idx];
		
		if (hap == S) {
			ans += 1;
		}
		recur(idx+1, hap, N, S);
		recur(idx+1, hap-arr[idx], N, S);
	}
}