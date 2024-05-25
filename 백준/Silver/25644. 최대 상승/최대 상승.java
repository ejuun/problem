import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		long [] arr = new long [n];
		long min = 1000000000;
		long diff = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			long num = Long.parseLong(st.nextToken());
			if(min > num) {
				min = num;
			}
			if(i >= 1) {
				if(num - min > diff) {
					diff = num -min;
				}
			}
		}
		System.out.println(diff);
    }
}