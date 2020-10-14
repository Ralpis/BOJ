/*BOJ 10250번 ACM 호텔 */

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
	
		for(int i=0;i<n;i++) {
			int a=scan.nextInt();
			int b=scan.nextInt();
			int c=scan.nextInt();
			if(c%a!=0) {
				System.out.println((c%a)*100+(c/a)+1);
			}
			else {
				System.out.println((a * 100)+(c/a));
			}
			
		}
		
	}
}
