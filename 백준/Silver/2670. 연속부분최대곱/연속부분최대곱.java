import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
        double[] arr = new double[n];
        double[] dp = new double[n];
		for (int i = 0; i < n; i++) {
			double num = Double.parseDouble(br.readLine());
			arr[i] = num;
		}
		dp[0] = arr[0];
		for (int i = 1; i < dp.length; i++) {
			dp[i] = Math.max(arr[i], dp[i-1]*arr[i]);
		}
		
		double max = 0;
		for (int i = 0; i < dp.length; i++) {
			if(max < dp[i]) {
				max = dp[i];
			}
		} 
		System.out.print(String.format("%.3f",max));
	}
}