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
	int [] arr = new int [K+1];
	
	for (int i = 0; i < N; i++) {
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int weight = Integer.parseInt(st1.nextToken());
		int value = Integer.parseInt(st1.nextToken());
		
		for (int j = K; j > weight-1; j--) {
			arr[j] = Math.max(arr[j], arr[j-weight]+value);
		}
	}	
	System.out.println(arr[K]);
	}
}