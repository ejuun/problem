import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int [] arr = new int [12];
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;
	for (int i = 4; i < arr.length; i++) {
		arr[i] = arr[i-3] + arr[i-2] + arr[i-1];
	}
	
	int n = Integer.parseInt(br.readLine());
	for (int i = 0; i < n; i++) {
		int num = Integer.parseInt(br.readLine());
		System.out.println(arr[num]);
	}
	}
}