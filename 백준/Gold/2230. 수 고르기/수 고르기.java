import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());

	int N = Integer.parseInt(st.nextToken());
	int M = Integer.parseInt(st.nextToken());
	int [] arr = new int [N];
	
	for (int i = 0; i < arr.length; i++) {
			int n = Integer.parseInt(br.readLine());
			arr[i] = n;
	}
	Arrays.sort(arr);
	
	int end = 0;
	int ans = 2000000001;
	for (int start = 0; start < arr.length; start++) {
		
		while (end < N) {
			int diff = arr[end] - arr[start];
			if (diff >= M) {
				if (ans > diff) {
					ans = diff;					
				}
				break;
			}else {
				end += 1;
			}
		}
	}
	System.out.println(ans);
	}
			}