import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> prime = new ArrayList<>();
		for (int i = 1; i < Math.sqrt(n)+1; i++) {
			prime.add(i*i);
		}
		int [] dp = new int [n+1];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = 100000;
		}
		for (int i = 1; i < n+1; i++) {
			for(int p : prime) {
				if(p == i) {
					dp[i] = 1;
				}
			}
			if(dp[i] != 1) {
				for (int j : prime) {
					if(i > j) {
						dp[i] = Math.min(dp[i], dp[i-j]+1);
					}
					
				}
			}
		}
		System.out.println(dp[n]);
	} 
}