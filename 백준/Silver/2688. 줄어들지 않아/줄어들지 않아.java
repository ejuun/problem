import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
//import java.util.Iterator;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int T = Integer.parseInt(br.readLine());
	long [] dp = new long [65];
	long [][] arr = new long [65][10];

	dp[1] = 10;
	dp[2] = 55;
	for (int i = 0; i < 10; i++) {
		arr[2][i] = i+1;
	}
	
	for (int i = 3; i < 65; i++) {
		long hap = 0;
		for (int j = 0; j < 10; j++) {
			if (j == 0) {
				arr[i][j] = 1;
			}else {
				arr[i][j] = arr[i-1][j] + arr[i][j-1];
			}
			hap += arr[i][j];
		}
		dp[i] = hap;
	}
	for (int i = 0; i < T; i++) {
		int n = Integer.parseInt(br.readLine());
		System.out.println(dp[n]);
	}
				}
}