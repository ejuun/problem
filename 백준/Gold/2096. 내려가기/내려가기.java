import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(br.readLine());
	int [][] arr = new int [n][3];
	for (int i = 0; i < arr.length; i++) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int j = 0; j < 3; j++) {
			int m = Integer.parseInt(st.nextToken());
			arr[i][j] = m;
		}
	}
	int [][] high = new int [n][3];
	for (int i = 0; i < 1; i++) {
		for (int j = 0; j < 3; j++) {
			high[i][j] = arr[i][j];
		}
	}
	if (n >= 2) {
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				if (j == 0) {
					high[i][j] =  Math.max(high[i-1][j], high[i-1][j+1]) + arr[i][j];	
				}
				else if (j == 1) {
					int big = Math.max(high[i-1][0], high[i-1][1]);
					int bigger = Math.max(big, high[i-1][2]);
					high[i][j] = bigger + arr[i][j];
				}
				else {
					high[i][j] =  Math.max(high[i-1][j], high[i-1][j-1]) + arr[i][j];	
				}
			}
		}
	}
	int compare = Math.max(high[n-1][0], high[n-1][1]);
	int ans1 = Math.max(compare, high[n-1][2]);	

	int [][] row = new int [n][3];
	for (int i = 0; i < 1; i++) {
		for (int j = 0; j < 3; j++) {
			row[i][j] = arr[i][j];
		}
	}
	if (n >= 2) {
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				if (j == 0) {
					row[i][j] =  Math.min(row[i-1][j], row[i-1][j+1]) + arr[i][j];	
				}
				else if (j == 1) {
					int small = Math.min(row[i-1][0], row[i-1][1]);
					int smaller = Math.min(small, row[i-1][2]);
					row[i][j] = smaller + arr[i][j];
				}
				else {
					row[i][j] =  Math.min(row[i-1][j], row[i-1][j-1]) + arr[i][j];	
				}
			}
		}
	}
	int compare2 = Math.min(row[n-1][0], row[n-1][1]);
	int ans2 = Math.min(compare2, row[n-1][2]);
	
	System.out.print(ans1);
	System.out.print(' ');
	System.out.print(ans2);
	}
}