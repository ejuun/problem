import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr.add(n);
		}
        Collections.sort(arr);
        System.out.println(arr.get((N-1)/2));
	}
}