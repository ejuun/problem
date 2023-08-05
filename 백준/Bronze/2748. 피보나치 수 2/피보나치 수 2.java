import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long [] arr = new long [91];
		arr[0] = 0;
		arr[1] = 1;
		for (int i = 2; i < arr.length; i++) {
			arr[i] = arr[i-2]+arr[i-1];
		}
		int N = Integer.parseInt(br.readLine());
		System.out.println(arr[N]);
		
	}
	}