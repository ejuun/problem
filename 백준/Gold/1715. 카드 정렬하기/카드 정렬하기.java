import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
			PriorityQueue<Integer> files = new PriorityQueue<>();
			for (int i = 0; i < N; i++) {
				int K = Integer.parseInt(br.readLine());
				files.add(K);	
			}
			int ans = 0;
			while(files.size() != 1) {
				int file1 = files.poll();
				int file2 = files.poll();
				int new_file = file1 + file2;
				ans += new_file;
				files.add(new_file);
			}
			System.out.println(ans);
	}
}