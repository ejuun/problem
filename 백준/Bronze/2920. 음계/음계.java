import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int [] arr = new int [8];
	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < arr.length; i++) {
		int num = Integer.parseInt(st.nextToken());
		arr[i] = num;
	}
	int up = 0;
	int down = 0;
	for (int i = 0; i < arr.length-1; i++) {
		if (arr[i] > arr[i+1]) {
			down += 1;
		}else{
			up += 1;
		}
	}
	if (up == 7) {
		System.out.println("ascending");
	}else if (down == 7) {
		System.out.println("descending");
	}else {
		System.out.println("mixed");
	}
	}
}