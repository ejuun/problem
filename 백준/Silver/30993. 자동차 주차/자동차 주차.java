import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
	        Scanner scanner = new Scanner(System.in);
	        int N = scanner.nextInt();
	        int A = scanner.nextInt();
	        int B = scanner.nextInt();
	        int C = scanner.nextInt();
	        scanner.close();
	        
	        System.out.println(factorial(N) / (factorial(A) * factorial(B) * factorial(C)));
	    }

	    public static long factorial(int n) {
	        if (n == 1) {
	            return 1;
	        }
	        return n * factorial(n - 1);
}
}