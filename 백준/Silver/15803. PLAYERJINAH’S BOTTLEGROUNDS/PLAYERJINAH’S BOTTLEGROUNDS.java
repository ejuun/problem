import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double x1 = sc.nextInt();
        double y1 = sc.nextInt();
        double x2 = sc.nextInt();
        double y2 = sc.nextInt();
        double x3 = sc.nextInt();
        double y3 = sc.nextInt();

        if(x1==x2 || x2==x3 || x3==x1) {
            if(x1==x2 && x2==x3)
                System.out.println("WHERE IS MY CHICKEN?");
            else
                System.out.println("WINNER WINNER CHICKEN DINNER!");
        }

        else if(y1==y2 || y2==y3 || y3==y1) {
            if(y1==y2 && y2==y3)
                System.out.println("WHERE IS MY CHICKEN?");
            else
                System.out.println("WINNER WINNER CHICKEN DINNER!");
        }

        else {
            if((y2-y1)/(x2-x1)==(y3-y1)/(x3-x1))
                System.out.println("WHERE IS MY CHICKEN?");
            else
                System.out.println("WINNER WINNER CHICKEN DINNER!");
        }
    }
}