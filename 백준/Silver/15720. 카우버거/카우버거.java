import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        StringTokenizer st = new StringTokenizer(br.readLine());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        
        List<Integer> b = new LinkedList<Integer>();
        StringTokenizer st1 = new StringTokenizer(br.readLine());
	    for (int i = 0; i < B; i++) {
	    	int num = Integer.parseInt(st1.nextToken());
	    	b.add(num);
	    	}
	    List<Integer> s = new LinkedList<Integer>();
        StringTokenizer st2 = new StringTokenizer(br.readLine());
	    for (int i = 0; i < C; i++) {
	    	int num = Integer.parseInt(st2.nextToken());
	    	s.add(num);
	    	}
	    List<Integer> d = new LinkedList<Integer>();
        StringTokenizer st3 = new StringTokenizer(br.readLine());
	    for (int i = 0; i < D; i++) {
	    	int num = Integer.parseInt(st3.nextToken());
	    	d.add(num);
	    	}
		Collections.sort(b,Collections.reverseOrder());
		Collections.sort(s,Collections.reverseOrder());
		Collections.sort(d,Collections.reverseOrder());
		
		int min_val = Math.min(B, C);
		int m = Math.min(min_val, D);
		
		int no_sale = 0;
		int sale = 0;
		
		for (int i = 0; i < B; i++) {
			if(i < m) {
				sale += (0.9 * b.get(i)); 
			}else {
				sale += b.get(i);
			}
			no_sale += b.get(i);
		}
		for (int i = 0; i < C; i++) {
			if(i < m) {
				sale += (0.9 * s.get(i)); 
			}else {
				sale += s.get(i);
			}
			no_sale += s.get(i);
		}
		for (int i = 0; i < D; i++) {
			if(i < m) {
				sale += (0.9 * d.get(i)); 
			}else {
				sale += d.get(i);
			}
			no_sale += d.get(i);
		}
		System.out.println(no_sale);
		System.out.println(sale);
		}
}