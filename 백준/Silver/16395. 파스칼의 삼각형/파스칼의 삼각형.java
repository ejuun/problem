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
		
		int [][] arr = new int [N+1][N+1];
		arr[1][1] = 1;
		
        for (int i = 2; i < arr.length; i++) {
			for (int j = 1; j <= i; j++) {
				arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
			}
		}
		System.out.println(arr[N][K]);
	}
}