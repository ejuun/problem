import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
	public static void main (String [] args) throws IOException {
	Queue<Integer> queue = new LinkedList<Integer>();
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int num = 0;
	for (int i = 1; i <= N; i++) {
		queue.offer(i);
	}
	while (queue.size()!=1) {
		queue.poll();
		if (queue.size() == 1) {
			break;
		}
		num = queue.poll();
		queue.offer(num);
		}
	num = queue.poll();
	System.out.println(num);
	}
}
