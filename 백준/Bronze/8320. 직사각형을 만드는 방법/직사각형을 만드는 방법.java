import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int ans = N;
	int n = 0;
	for (int i = 2; i < N+1; i++) {
		n = (N / i) - (i - 1);
		if (n < 1) {
			break;
		}
		ans += n;
	}
	System.out.println(ans);

	}
}