import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int result = Integer.parseInt(st.nextToken());
		int ans = 0;
		int[] arr = new int[n];
		
		for (int i = 0; i < arr.length; i++) {
			int coin_value = Integer.parseInt(br.readLine());
			arr[i] = coin_value;
		}
		
		int share = 0;
		for (int i = n-1; i >= 0; i--) {
			if (result >= arr[i]) {
				share = result / arr[i];
				ans += share;
				result -= arr[i] * share;
			}
			if (result == 0) {
				break;
			}
		}
		System.out.println(ans);
	}
}