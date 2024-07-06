import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
	    int [] arr = new int [10001];
	    for (int i = 0; i < arr.length; i++) {
			if(i < 6) {
	    	arr[i] = i;
			}else {
			arr[i] = arr[i-3] + (arr[i-2] - arr[i-5]) + 1;
			}
		}
	    int N = Integer.parseInt(br.readLine());
	    for (int i = 0; i < N; i++) {
			int n = Integer.parseInt(br.readLine());
			System.out.println(arr[n]);
		}
	}
}