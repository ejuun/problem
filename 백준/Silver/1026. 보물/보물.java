import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int [] A = new int[N];
		int [] B = new int[N];
		int ans = 0;	
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
				int n = Integer.parseInt(st.nextToken());
				A[i] = n;
		}
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
				int n = Integer.parseInt(st1.nextToken());
				B[i] = n;
		}
		Arrays.sort(A);
		Arrays.sort(B);
		for (int i = 0; i < N; i++) {
			ans += A[i] * B[N-1-i];
		}
		System.out.println(ans);
			}
}