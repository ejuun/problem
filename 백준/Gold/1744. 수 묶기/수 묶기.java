import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		ArrayList<Long> p = new ArrayList<>();
		ArrayList<Long> m = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			long n = Long.parseLong(st.nextToken());
			if (n > 0) {
				p.add(n);
			}
			else {
				m.add(n);
			}
		}
		Collections.sort(p);
		Collections.sort(m);
		
		long ans = 0;
		while(p.size() >= 2) {
			long p1 = p.remove(p.size()-1);
			long p2 = p.remove(p.size()-1);
			if (p1 == 1 || p2 == 1) {
				ans += p1 + p2;
			}
			else {
				ans += p1 *p2;
			}
		}
		if (p.size() == 1) {
			long p3 = p.remove(p.size()-1);
			ans += p3;
		}
		
		while(m.size() >= 2) {
			long m1 = m.remove(0);
			long m2 = m.remove(0);
			ans += m1 *m2;
		}
		if (m.size() == 1) {
			long m3 = m.remove(0);
			ans += m3;
		}
		System.out.println(ans);
	}
}