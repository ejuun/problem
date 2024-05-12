import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		int [] self = new int [15000];
		for (int i = 0; i < 10001; i++) {
			int n = d(i);
			self[n] += 1;
		}
		for (int i = 1; i < 10001; i++) {
			if(self[i] == 0) {
				System.out.println(i);
			}
		}
	}
	static int d(int n) {
		int val = 0;
		int temp = n;
		while(temp > 0) {
			int div = temp % 10;
			temp = temp / 10;
			val += div;
		}
		return val + n;
	} 
}