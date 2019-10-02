import java.util.Scanner;

class randGen{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Upper bound of prime is:");
    int n =sc.nextInt(); // generate prime less than n+1

    int[] numbers = new int[n];
    int[] primes = new int[n];
    int check;
    int cnt=1;
    int rndP;

    System.out.print("How many ramdom primes in the bound ?:");
    int numP = sc.nextInt(); //numbers of generated primes

    for(int i=3;i<n;i++){
      numbers[i]=i;
      for(int j=2;j<i;j++){
        check = numbers[i]%j;
        if(check==0 && j!=numbers[i]){
          break;
        }
        else if(j+1==numbers[i]){
          if(cnt%20!=0){
            System.out.print(numbers[i]+",");
            cnt++;
          }
          else if(cnt%20==0){
              System.out.println(numbers[i]+",");
              cnt++;
          }
          primes[cnt]=numbers[i];
        }
      }
    }
    for(int k=0;k<numP;k++){
      System.out.println("");
      System.out.print("ramdom prime"+(k+1)+":");
      rndP =(int)(Math.random()*cnt)%cnt;
      System.out.print(primes[rndP]);
    }
  }
}
