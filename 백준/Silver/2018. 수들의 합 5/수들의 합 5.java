import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int [(N+1)/2+1];
        
		for (int i = 0; i < arr.length; i++) {
			arr[i] = i;
		}
		int e = 1;
		int ans = 1;
		int hap = 0;
		if(N != 1) {
			for (int i = 1; i < arr.length; i++) {
				while (e < arr.length && hap < N) {
					hap += arr[e];
					e+= 1;
				}
				if(hap == N) {
					ans +=1 ;
				}
				hap -= arr[i];
			}
		}
		System.out.println(ans);
	}
}