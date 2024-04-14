import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int [] arr = new int [N+1];
		StringTokenizer st1 = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
        	arr[i] = arr[i-1]+Integer.parseInt(st1.nextToken());
        }
        int max = -10000001;
        for (int i = K; i <= N; i++) {
            int sum = arr[i]-arr[i-K];
            if (max < sum) max = sum;
        }
        System.out.println(max);
	}
}