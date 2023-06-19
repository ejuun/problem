import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int five = N / 5;
	int three = 0;
	int i = 0;
	while (five - i >= 0) {
		int div = N - 5 * (five - i);
		if (div % 3 == 0) {
			three = div / 3;
			break;
		}
		i += 1;
	}
	if (five - i <= 0 && three == 0) {
		System.out.println(-1);
	}
	else {
		System.out.println((five - i) + three);
	}
	}
}