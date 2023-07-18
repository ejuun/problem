import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int num1 = Integer.parseInt(st.nextToken());
	int num2 = Integer.parseInt(st.nextToken());
	int gcd = 1;
	int cnt = 1;
	while (cnt <= num1 && cnt <= num2) {
		if (num1 % cnt == 0 && num2 % cnt == 0) {
			gcd = cnt;
		}
		cnt += 1;
	}
	int n_1 = num1 / gcd;
	int n_2 = num2 / gcd;
	int lcm = n_1 * n_2 * gcd;
	System.out.println(gcd);
	System.out.println(lcm);
	}
}