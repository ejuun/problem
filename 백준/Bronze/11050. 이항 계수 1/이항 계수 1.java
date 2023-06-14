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
	int ans = 0;
	int div = 0;
	div = Fac(K) * Fac(N-K);
	ans = Fac(N) / div;
	System.out.println(ans);
	}
	
	static int Fac(int num) {
		int n = 1;
		if (num == 0) {
			return 1;
		}
		for (int i = 1; i <= num; i++) {
			n = n * i;
		}
		return n;
	}
}