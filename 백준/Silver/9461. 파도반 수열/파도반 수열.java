import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
//import java.util.Arrays;
//import java.util.Iterator;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	long [] dp = new long[101];
	
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
        
	for (int i = 6; i < 101; i++) {
		dp[i] = dp[i-1] + dp[i-5];
	}
	
	for (int i = 0; i < N; i++) {
		int n = Integer.parseInt(br.readLine());
		System.out.println(dp[n]);
	}
	}
}