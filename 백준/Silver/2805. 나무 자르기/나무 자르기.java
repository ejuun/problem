import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] trees = new int[N];
		int low = 0;
		int high = 0;
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i < N; i++) {
			trees[i] = Integer.parseInt(st.nextToken());

			if(high < trees[i]) {
				high = trees[i];
			}
		}
		
		while(low < high) {
			
			int mid = (low + high) / 2;
			long able = 0;
			for(int tree : trees) {

				if(tree - mid > 0) { 
					able += (tree - mid);
				}
			}

			if(able < M) {
				high = mid;
			}

			else {
				low = mid + 1;
			}
		}
		System.out.println(low - 1);
	}
}