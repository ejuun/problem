import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	long [] arr = new long [N];
	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < arr.length; i++) {
		arr[i] = Long.parseLong(st.nextToken());
	}
        
	long ans = 2000000000;
	int end = N-1;
	int start = 0;
	long small = 0;
	long large = 0;
        
	while (start < end) {
		long hap = arr[start] + arr[end];
		
		if (Math.abs(hap) < ans) {
			small = arr[start];
			large = arr[end];
			ans = Math.abs(hap);
			
			if (hap == 0) {
				break;
			}
		}
		if (hap < 0 ) {
			start += 1;
		}else {
			end -= 1;
		}
	}
	System.out.print(small);
	System.out.print(' ');
	System.out.print(large);
	}
}