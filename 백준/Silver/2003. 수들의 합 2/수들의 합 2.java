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
	int [] seq = new int [n];
	StringTokenizer num = new StringTokenizer(br.readLine());
	for (int i = 0; i < n; i++) {
		seq[i] = Integer.parseInt(num.nextToken());
		}
	int end = 0;
	int cnt = 0;
	int interval = 0;
	
	for (int start = 0; start < n; start++) {
		while (interval < m && end < n) {
			interval += seq[end];
			end += 1;
		}
		if (interval == m) {
			cnt += 1;
		}
		interval -= seq[start];
	}
	System.out.println(cnt);
	}
}