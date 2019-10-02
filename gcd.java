import java.util.*;

public class gcd{
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);

      double a = sc.nextDouble();
      double b = sc.nextDouble();

/* not necessary
      if(a<b){
        double tmp = b;
        b = a;
        a = tmp;
      }
      if a<b,then euku(b,a%b)=euku(b,a)
*/

      double ans = euku(a,b);

      System.out.println("GCD(a,b)="+(int)ans);

    }

    public static double euku(double a,double b){

      if(a%b!=0){
        return euku(b,a%b);
      }
      else{
        return b;
      }

    }

}
