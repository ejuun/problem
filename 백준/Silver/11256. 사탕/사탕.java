import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());  //테스트 케이스 개수

		for(int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int candy = Integer.parseInt(st.nextToken());  //사탕 개수
			int box = Integer.parseInt(st.nextToken());  //상자 개수
			int cnt = 0;
			
			Integer[] box_list = new Integer[box];
					
			for(int j = 0; j < box; j++) {
				st = new StringTokenizer(br.readLine());
				
				int r = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				box_list[j] = r * c;
				
			}
			Arrays.sort(box_list, Comparator.reverseOrder());  //내림차순 정렬
			for(int k = 0; k < box; k++) {
				candy = candy - box_list[k];
				cnt ++;			
				if(candy <= 0) {
					break;
				}
			}
			System.out.println(cnt);	
		}
	}
}