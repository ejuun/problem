import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));

		int a = Integer.parseInt(br1.readLine());
		int b = Integer.parseInt(br1.readLine());

 		System.out.println(a+b);
	}
}