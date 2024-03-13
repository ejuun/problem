import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nh = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(nh.nextToken());
		int H = Integer.parseInt(nh.nextToken());
		int [] arr = new int[H+1];
		int [] front = new int[H+1];
		int [] back = new int[H+1];
		
		for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int n = Integer.parseInt(st.nextToken());
				if (i% 2 != 0) {
					front[n] +=1;					
				}
				else {
					back[H - n +1] += 1;
				}
		}
		for (int i = H; i > 0; i--) {
			front[i-1] += front[i];
		}
		for (int i = 0; i < H; i++) {
			back[i+1] += back[i];
		}
		for (int i = 0; i < arr.length; i++) {
			arr[i] = front[i] + back[i];
		}
		int val = 200000;
		int cnt = 0;
		for (int i = 1; i < H+1; i++) {
			if (val > arr[i]) {
				val = arr[i];
				cnt = 1;
			}
			else if (val == arr[i]) {
				cnt += 1;
			}
		}
		System.out.print(val);
		System.out.print(" ");
		System.out.println(cnt);
	}
}