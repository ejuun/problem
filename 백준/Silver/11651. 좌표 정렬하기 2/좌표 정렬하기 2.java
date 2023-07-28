import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());
	int [][] arr = new int [N][2];
	for (int i = 0; i < arr.length; i++) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int j = 0; j < 2; j++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i][j] = n;
		}
	}
	Arrays.sort(arr, (arr_1, arr_2) -> {
		if(arr_1[1] == arr_2[1]) {
			return arr_1[0] - arr_2[0];
		}
		else {
			return arr_1[1] - arr_2[1];
		}
	});
	StringBuilder sb = new StringBuilder();

	for(int i=0; i<N; i++) {
		sb.append(arr[i][0] + " " + arr[i][1]).append('\n');
	}

	System.out.println(sb);
	}
			}