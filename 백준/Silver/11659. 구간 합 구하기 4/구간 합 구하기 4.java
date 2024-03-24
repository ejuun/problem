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
		int [] arr = new int [N+1];
		
		StringTokenizer starr = new StringTokenizer(br.readLine());
		for (int i = 1; i < N+1; i++) {
			int n = Integer.parseInt(starr.nextToken());
			arr[i] = arr[i-1] + n;
		}
		
		for (int i = 0; i < M; i++) {
			int ans = 0;
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st1.nextToken());
			int e = Integer.parseInt(st1.nextToken());
			
			ans = arr[e] - arr[s-1];
			System.out.println(ans);
		}

	}
}
