import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String s1 = new String(br.readLine());
	String s2 = new String(br.readLine());
	int len_s1 = s1.length();
	int len_s2 = s2.length();

	int [][] arr = new int [len_s1][len_s2];
	int ans = 0;
	
	for (int i = 0; i < len_s1; i++) {
		for (int j = 0; j < len_s2; j++) {
			if (i==0 || j == 0) {
				if (s1.charAt(i) == s2.charAt(j)) {
					arr[i][j] = 1;
				}
			}
			else {
				if (s1.charAt(i) == s2.charAt(j)) {
					arr[i][j] = arr[i-1][j-1] + 1;
				}
			}
			if (ans < arr[i][j]) {
				ans = arr[i][j];
			}
		}
	}
	System.out.println(ans);
	}
}