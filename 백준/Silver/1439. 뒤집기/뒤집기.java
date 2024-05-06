import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int cnt = 0;
		for (int i = 0; i < str.length()-1; i++) {
			if (str.charAt(i) != str.charAt(i+1)) {
				cnt += 1;
			}
		}
		if (cnt % 2 == 1) {
			cnt += 1;
		}
		int ans = cnt / 2;
		System.out.println(ans);
	}
}