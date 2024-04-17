import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while (T > 0) {
			PriorityQueue<Long> files = new PriorityQueue<>();
			int K = Integer.parseInt(br.readLine());
			String [] strs = br.readLine().split(" ");
			for (int i = 0; i < K; i++) {
				long f = Long.parseLong(strs[i]);
				files.add(f);
			}
			long ans = 0;
			while(files.size() != 1) {
				long file1 = files.poll();
				long file2 = files.poll();
				long new_file = file1 + file2;
				ans += new_file;
				files.add(new_file);
			}
			System.out.println(ans);
			T -= 1;
		}
	}
}