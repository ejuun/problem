import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		long [][] arr = new long [N][M];

		
		for (int i = 0; i < M; i++) {
	        String[] st1 = br.readLine().split(" ");
			for (int j = 0; j < N; j++) {
				long s = Long.parseLong(st1[j]);
				arr[j][i] = s;
			}
		}
        
		for (int i = 0; i < N; i++) {
			Arrays.sort(arr[i]);
		}
        
		int middle = 0;
		if(N%2 == 0) {
			middle = M /2;
		}else {
			middle = (M-1)/2;
		}
        
		long [] dot = new long [N];
		long ans = 0;
		for (int i = 0; i < N; i++) {
			dot[i] = arr[i][middle];
			for (int j = 0; j < M; j++) {
				ans += Math.abs(arr[i][middle] - arr[i][j]);
			}
		}
        
		System.out.println(ans);
		for (int i = 0; i < dot.length; i++) {
			System.out.print(dot[i]+" ");
		}
	}
}