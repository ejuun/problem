import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int N = Integer.parseInt(st.nextToken());
	int T = Integer.parseInt(st.nextToken());
	int [] arr = new int [T+1];
	
	for (int i = 0; i < N; i++) {
		StringTokenizer sts = new StringTokenizer(br.readLine());
		
		int time = Integer.parseInt(sts.nextToken());
		int score = Integer.parseInt(sts.nextToken());
		
		for (int j = T; j > time-1; j--) {
			arr[j] = Math.max(arr[j], arr[j-time] + score);
		}
	}
	System.out.println(arr[T]);
	}
}