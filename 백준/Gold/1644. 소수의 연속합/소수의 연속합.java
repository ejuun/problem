import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int[] arr = new int [N+1];
	for (int i = 2; i < (int)Math.sqrt(N)+1; i++) {
		if (arr[i] == 0) {
			for (int j = i*2; j < arr.length; j+=i) {
				arr[j] = 1;
			}
		}
	}
	ArrayList<Integer> prime = new ArrayList<>();
	for (int i = 2; i < arr.length; i++) {
		if (arr[i] == 0) {
			prime.add(i);
		}
	}
	int end = 0;
	int cnt = 0;
	int hap = 0;
	for (int i = 0; i < prime.size(); i++) {
		
		while (hap < N && end < prime.size()) {
			hap += prime.get(end);
			end += 1;			
		}
		if (hap == N) {
			cnt += 1;
		}	
		hap -= prime.get(i);

	}
	System.out.println(cnt);
	}
}