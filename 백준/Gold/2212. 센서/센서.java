import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		ArrayList<Integer> sensor = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());			
		for (int i = 0; i < N; i++) {
			int n = Integer.parseInt(st.nextToken());
			sensor.add(n);
		}
		Collections.sort(sensor);
		ArrayList<Integer> diff = new ArrayList<>();
		for (int i = 1; i < sensor.size(); i++) {
			diff.add(sensor.get(i) - sensor.get(i-1));
		}
		Collections.sort(diff);
		
		int ans = 0;
		for (int i = 0; i < diff.size() - K + 1; i++) {
			ans += diff.get(i);
		}
		System.out.println(ans);
	}
}