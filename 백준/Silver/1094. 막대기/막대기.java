import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int [] stick = {64, 32, 16, 8, 4, 2,1};
		int X = Integer.parseInt(br.readLine());
		int ans = 0;
		
		for (int i = 0; i < stick.length; i++) {
			if(X >= stick[i]) {
				ans += 1;
				X -= stick[i];
		}
			if (X == 0) {
				break;
			}
		}
		System.out.println(ans);
	}
}