import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BigInteger [] arr = new BigInteger [10001];
		arr[0] = BigInteger.ZERO;
		arr[1] = BigInteger.ONE;
		for (int i = 2; i < arr.length; i++) {
			arr[i] = arr[i-2].add(arr[i-1]);
		}
		int N = Integer.parseInt(br.readLine());
		System.out.println(arr[N]);
	}
	}