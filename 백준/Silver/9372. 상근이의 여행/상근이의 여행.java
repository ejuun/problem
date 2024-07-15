import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			for (int j = 0; j < m; j++) {
				StringTokenizer st1 = new StringTokenizer(br.readLine());
				int n1 = Integer.parseInt(st1.nextToken());
				int m1 = Integer.parseInt(st1.nextToken());
				
			}
			System.out.println(n-1);
		}
	}
}