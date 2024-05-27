import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long [] A = new long [46];
		long [] B = new long [46];
		B[1] = 1;
		for (int i = 2; i < 46; i++) {
			A[i] = B[i-1];
			B[i] = A[i-1] + B[i-1];
		}
		System.out.print(A[n]+ " " + B[n]);
	} 
}