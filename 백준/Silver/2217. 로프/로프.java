import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int[N];
		for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int n = Integer.parseInt(st.nextToken());
				arr[i] = n;
		}
		Arrays.sort(arr);
		
		int ans = arr[N-1];
		for (int i = N-1; i >=0; i--) {
			ans = Math.max(ans, arr[i] * (N-i));
		}
		System.out.println(ans);
			}
}