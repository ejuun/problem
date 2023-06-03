import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int ans_index = 0;
		int ans_value = 0;
		for (int i = 0; i < 9; i++) {
			int num = Integer.parseInt(br.readLine());
			if (ans_value < num) {
				ans_value = num;
				ans_index = i+1;
			}
		}
		System.out.println(ans_value);
		System.out.println(ans_index);
	} 
}