import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int N = Integer.parseInt(st.nextToken());
	int K = Integer.parseInt(st.nextToken());
	int [][] arr = new int [K][2];
	int [] ans = new int [N+1];
	
	for (int i = 0; i < K; i++) {
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int needs = Integer.parseInt(st1.nextToken());
		int time = Integer.parseInt(st1.nextToken());
		arr[i][0] = needs;
		arr[i][1] = time;
	}
	
	for (int i = 0; i < arr.length; i++) {
		for (int j = N; j >= arr[i][1]; j--) {
			if (ans[j] < ans[j-arr[i][1]] + arr[i][0]) {
				ans[j] = ans[j-arr[i][1]] + arr[i][0];
			}
		}
	}
	System.out.println(ans[N]);
	}
}
