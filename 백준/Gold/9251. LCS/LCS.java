import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
	public static void main (String [] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String word1 = br.readLine();
	String word2 = br.readLine();

	char [] arr1 = new char [word1.length()+1];
	for (int i = 1; i < arr1.length; i++) {
		arr1[i] = word1.charAt(i-1);
	}
	char [] arr2 = new char [word2.length()+1];
	for (int i = 1; i < arr2.length; i++) {
		arr2[i] = word2.charAt(i-1);
	}
	
	int [][] lcs = new int [arr1.length][arr2.length];
	
	for (int i = 0; i < arr1.length; i++) {
		for (int j = 0; j < arr2.length; j++) {
			if (i != 0 && j != 0) {
				if (arr1[i] == arr2[j]) {
					lcs[i][j] = lcs[i-1][j-1] + 1;
				}else {
					lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
				}
			}
		}
	}
	System.out.println(lcs[arr1.length-1][arr2.length-1]);
		}
}