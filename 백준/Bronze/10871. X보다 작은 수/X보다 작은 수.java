import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		StringTokenizer num_list = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(num_list.nextToken());
			if (num < x) {
				System.out.print(num);
				System.out.print(' ');
			}
		}
	}
}