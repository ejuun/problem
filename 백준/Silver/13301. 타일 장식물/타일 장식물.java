import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(br.readLine());
	int [] arr = new int [82];
	arr[1] = 1;
	arr[2] = 1;
	for (int i = 3; i < 82; i++) {
		arr[i] = arr[i-1] + arr[i-2];
	}
	int ans = 2 * (arr[n+1] + arr[n]);
	
	System.out.println(ans);
	}
}