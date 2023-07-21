import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int n = Integer.parseInt(st.nextToken());
	int m = Integer.parseInt(st.nextToken());
	int [] arr = new int [m+1];
	arr[1] = 1;
	for (int i = 2; i < (int)Math.sqrt(m)+1; i++) {
		if (arr[i] == 0) {
			for (int j = i*2; j < m+1; j+=i) {
				arr[j] = 1;
			}
		}
	}
	for (int i = n; i < arr.length; i++) {
		if (arr[i] == 0) {
			System.out.println(i);
		}
	}
		}
}