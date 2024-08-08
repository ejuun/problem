import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long max = 0;
        long min = 1000000000;
        for (int i = 0; i < n; i++) {
			long num = Long.parseLong(st.nextToken());
			if(max < num) {
				max = num;
			}
			if(min > num) {
				min = num;
			}
		}
        long ans = 2 * (max - min);
        System.out.println(ans);      
	}
}