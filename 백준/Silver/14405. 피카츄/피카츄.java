import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(sc.nextLine().replace("pi"," ").replace("ka"," ").replace("chu"," ").replace(" ","").length()>0?"NO":"YES");	
    }
}