import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int [] arr = new int [10];
	for (int i = 0; i < 10; i++) {
		int N = Integer.parseInt(br.readLine());
		arr[i] = N % 42;
	}
	Set<Integer> set = new HashSet<Integer>();
	for (int i = 0; i < arr.length; i++) {
		set.add(arr[i]);
	}
	System.out.println(set.size());
	}
}