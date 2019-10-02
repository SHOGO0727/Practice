import java.util.*;

public class maxmin{
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.print("length of array:");
      int n=sc.nextInt();


      int[] a = new int[n];
      System.out.print("elements of array("+n+"):");
      for(int i=0;i<n;i++){
        a[i]=sc.nextInt();
      }

      int max = cmax(a,n);
      int min = cmin(a,n);


      System.out.println("max="+max);
      System.out.print("min="+min);

    }

    public static int cmax(int[] aa,int nn){
      int max1=aa[0];
      for(int j=1;j<nn;j++){
        if(aa[j]>max1){
          max1=aa[j];
        }
      }
      return max1;
    }
    public static int cmin(int[] bb,int nn){
      int min1=bb[0];
      for(int j=1;j<nn;j++){
        if(bb[j]<min1){
          min1=bb[j];
        }
      }
      return min1;
    }


}
