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
	int [] visited = new int[100001];
	visited[N] = 1;
	
	Queue<Integer> queue = new LinkedList<Integer>();
	queue.offer(N);
	int [] move = new int[3];
	int num = 0;
	int new_num = 0;
	if (N==K) {
		System.out.println(0);
	}
	else {
		while (!queue.isEmpty()) {
			num = queue.poll();
			for (int i = 0; i < move.length; i++) {
				if (i==0) {
					new_num = num -1;
				}
				else if (i == 1) {
					new_num = num + 1;
				}
				else {
					new_num = num + num;
				}
				if (new_num == K) {
					visited[new_num] = visited[num] + 1;
					break;
				}
				
				if (new_num >= 0 && new_num <= 100000 && visited[new_num] == 0) {
					queue.offer(new_num);
					visited[new_num] = visited[num] + 1;
				}
			}
			if (new_num == K) {
				break;
			}
			
		}
		System.out.println(visited[K]-1);
	}
	}
}