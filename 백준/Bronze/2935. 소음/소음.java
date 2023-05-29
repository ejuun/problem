import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BigInteger a = new BigInteger(br.readLine());
		String sign = br.readLine();
		BigInteger b = new BigInteger(br.readLine());
		if (sign.equals("+")) {
			System.out.println(a.add(b));
		}else {
			System.out.println(a.multiply(b));
		}
	}
}