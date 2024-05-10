import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	
	static ArrayList<Long> val = new ArrayList<>();

	public static void main(String[] args) throws IOException {	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Long [] arr = new Long [N];
		StringTokenizer st = new StringTokenizer(br.readLine());
 		for(int i = 0; i < N; i++) {
			Long n = Long.parseLong(st.nextToken());
			arr[i] = n;
		}
 		val.add(arr[0]);
		for(int i = 1; i < N; i++) {
			if (val.get(val.size()-1) < arr[i]) {
				val.add(arr[i]);
			}else {
				int idx = bi(val, arr[i]);
				val.set(idx, arr[i]);
			}
		}
		System.out.println(val.size());
	}
	static int bi(ArrayList<Long> arr, Long num) {
		int l = 0;
		int r = arr.size()-1;
		while(l <= r) {
			int mid = (l+r) /2;
			if(arr.get(mid) < num) {
				l = mid + 1;
			}else {
				r = mid - 1;
			}
		}
		return l;
	}
}