import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [] arr = new int [N];
	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < arr.length; i++) {
		int n = Integer.parseInt(st.nextToken());
		arr[i] = n;
	}
	Arrays.sort(arr);
	int sum = 0;
	for (int i = 0; i < arr.length; i++) {
		sum += (N-i) * arr[i];
	}
	System.out.println(sum);
		}
}