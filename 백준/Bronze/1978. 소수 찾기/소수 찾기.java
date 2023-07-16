import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int[] arr = new int [1001];
	for (int i = 2; i < (int)Math.sqrt(1001)+1; i++) {
		if (arr[i] == 0) {
			for (int j = i*2; j < arr.length; j+=i) {
				arr[j] = 1;
			}
		}
	}
	ArrayList<Integer> prime = new ArrayList<>();
	for (int i = 2; i < arr.length; i++) {
		if (arr[i] == 0) {
			prime.add(i);
		}
	}
	int N = Integer.parseInt(br.readLine());
	int [] num = new int [N];
	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < num.length; i++) {
		int n = Integer.parseInt(st.nextToken());
		num[i] = n;
	}
	int cnt = 0;
	for (int i = 0; i < num.length; i++) {
		if (prime.contains(num[i]) == true) {
			cnt += 1;
		}
		}
	System.out.println(cnt);
	}
}