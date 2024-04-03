import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		if(N < 100) {
			System.out.println(N);
		}
		else {
			int ans = 99;
			for (int i = 100; i <= N; i++) {
				int h = i / 100;
				int t = (i /10) % 10;
				int o = i % 10;
				if ((h-t) == (t-o)) {
					ans += 1;
				}
			}
			System.out.println(ans);
		}
	}
}