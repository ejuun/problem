import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());  
		int [] arr = new int[N];
		int ans = -1;		
		for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int n = Integer.parseInt(st.nextToken());
				arr[i] = n;
		}
		Arrays.sort(arr);
		
		int c= N-1;
		while(c > 1) {
			if(arr[c] >= arr[c-1] + arr[c-2]) {
				c -= 1;
			}
			else {
				ans = arr[c] + arr[c-1] + arr[c-2];
				break;
			}
		}
		System.out.println(ans);
	}
}