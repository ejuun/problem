import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
 
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        // 입력된 수열의 길이를 N에 저장
        int N = Integer.parseInt(br.readLine());
        
        // 입력된 수열을 공백을 기준으로 나눠 input 배열에 저장
        String[] input = br.readLine().split(" ");
        int[] arr = new int[N];
        
        // input 배열을 int 배열로 변환
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }
        
        // 배열을 오름차순으로 정렬
        Arrays.sort(arr);
        
        // 정렬된 배열을 공백으로 구분하여 출력
        for (int i = 0; i < N; i++) {
            bw.write(arr[i] + " ");
        }
        
        // 입출력 스트림 닫기
        br.close();
        bw.flush();
        bw.close();
    }
}