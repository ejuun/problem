import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cnt = 1;
		while(true) {
			int N = Integer.parseInt(br.readLine());
			if(N == 0) {
				break;
			}
			String [] arr = new String[N];
			for (int i = 0; i < N; i++) {
				String lst = br.readLine();
				arr[i] = lst;
			}
			Arrays.sort(arr);
			System.out.println(cnt++);
			for (String list: arr ) {
				System.out.println(list);
			}
		}
	}
}