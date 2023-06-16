import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int N = Integer.parseInt(st.nextToken());
	int K = Integer.parseInt(st.nextToken());
	Queue<Integer> queue = new LinkedList<Integer>();
	
	for (int i = 1; i <= N; i++) {
		queue.offer(i);
	}
	int num = 0;
	int cnt = 1;
	System.out.print("<");
	while (!queue.isEmpty()) {
		for (int i = 1; i <K; i++) {
			num = queue.poll();
			queue.offer(num);
			}
		num = queue.poll();
		System.out.print(num);
		if (!queue.isEmpty()) {
			System.out.print(',');
			System.out.print(" ");
		}
		}
	System.out.print(">");
	}
}