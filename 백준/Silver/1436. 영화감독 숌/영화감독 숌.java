import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int cnt = 1;
	int start = 666;
	while (cnt != N) {
		start += 1;
		if (String.valueOf(start).contains("666")) {
			cnt += 1;
		}
	}
	System.out.println(start);
	}
}