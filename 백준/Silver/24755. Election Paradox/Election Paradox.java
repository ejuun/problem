import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int N = Integer.parseInt(br.readLine());
        List<Integer> arr = new LinkedList<Integer>();
        StringTokenizer st = new StringTokenizer(br.readLine());
	    for (int i = 0; i < N; i++) {
	    	int num = Integer.parseInt(st.nextToken());
	    	arr.add(num);
	    	}
		Collections.sort(arr);
		
		int ans = 0;
		for (int i = 0; i < N; i++) {
			if(i <= N /2) {
				ans += arr.get(i) / 2;
			}else {
				ans += arr.get(i);
			}
		}
		System.out.println(ans);
	}
}