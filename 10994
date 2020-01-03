/* BOJ 10994 별찍기 19 */


import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		scan.close();
		int x=4*n-3;
		int center=(4*n-3)/2;
		char[][] a =new char[x][x];
		
		a[center][center]='*';
		
		for(int i=0;i<n;i++) {
			for(int z=center-2*i;z<=center+2*i;z++) {
				a[center-2*i][z]='*';
				a[center+2*i][z]='*';
				a[z][center-2*i]='*';
				a[z][center+2*i]='*';
			}
		}
		//출력
		for(int i=0;i<x;i++) {
			for(int y=0;y<x;y++) {
				System.out.print(a[i][y]);
			}
			System.out.println("");
		}
	}
}
