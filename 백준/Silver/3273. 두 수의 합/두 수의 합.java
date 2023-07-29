import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [] arr = new int [N];
	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < arr.length; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
	}
	int x = Integer.parseInt(br.readLine());
	Arrays.sort(arr);
	
	int end = N-1;
	int start = 0;
	int ans = 0;
	
	while (start < end) {
		
		int hap = arr[start] + arr[end];
		if (hap == x) {
			ans += 1;
			end -=1;
			start += 1;
		}
		else if (hap > x) {
			end -= 1;
		}else {
			start += 1;
		}
	}
	System.out.println(ans);
	}
			}