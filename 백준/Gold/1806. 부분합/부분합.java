import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int n = Integer.parseInt(st.nextToken());
	int s = Integer.parseInt(st.nextToken());
	int [] seq = new int [n];
	StringTokenizer num = new StringTokenizer(br.readLine());
	for (int i = 0; i < n; i++) {
		seq[i] = Integer.parseInt(num.nextToken());
		}
	int end = 0;
	int len = 100000;
	int interval_sum = 0;
	
	for (int start = 0; start < n; start++) {
		while (interval_sum < s && end < n) {
			interval_sum += seq[end];
			end += 1;
		}
		if (interval_sum >= s) {
			if (len > (end - 1) - start + 1) {
				len = (end - 1) - start + 1;
			}
		}
		interval_sum -= seq[start];
	}
	if (len == 100000) {
		len = 0;
	}
	System.out.println(len);
	}
}