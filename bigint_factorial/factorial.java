import java.lang.System;
import java.util.Scanner;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.PriorityQueue;

class factorial {
	
	private static ArrayList<Integer> sieve(int n) {
		boolean[] composites = new boolean[n + 1];

		for (int i = 2; i < (int)Math.sqrt(n + 1) + 1; i++) {
			if (!composites[i]) {
				for (int j = i * i; j < n + 1; j += i) {
					composites[j] = true;
				}
			}
		}
		
		ArrayList<Integer> primes = new ArrayList<Integer>();
		
		for (int i = 2; i < n + 1; i++) {
			if (!composites[i]) {
				primes.add(i);
			}
		}
		return primes;
	}

	private static BigInteger fac(int n) {
		long start = System.currentTimeMillis();
		ArrayList<Integer> primes = sieve(n);
		PriorityQueue<BigInteger> queue = new PriorityQueue<BigInteger>(primes.size());
		for (Integer prime : primes) {
			int exp = 0;
			int div = prime;
			while (n >= div) {
				exp += n / div;
				div *= prime;
			}
			queue.add(BigInteger.valueOf(prime).pow(exp));
		}
		long end = System.currentTimeMillis();
		//System.out.printf("other time: %f\n", (float)(end - start) / 1000);
		
		while (queue.size() > 1) {
			queue.add(queue.poll().multiply(queue.poll()));
			//System.out.println(queue.peek());
		}
		return queue.poll();
	}


	private static BigInteger fac2(int n) {
		PriorityQueue<BigInteger> queue = new PriorityQueue<BigInteger>(n);
		for (int i = 2; i <= n; i++) {
			queue.add(BigInteger.valueOf(i));
		}
		while (queue.size() > 1) {
			queue.add(queue.poll().multiply(queue.poll()));
			//System.out.println(queue.peek());
		}
		return queue.poll();
	}

	public static void main(String[] args) {
		int n = 100000;

		long start = System.currentTimeMillis();
		BigInteger fac = fac(n);
		long end = System.currentTimeMillis();

		//System.out.printf("%d! == %s\n", n, fac.toString());

		System.out.printf("%d! is %d bits long\n", n, fac.bitLength());
		System.out.printf("Duration: %f\n", (float)(end - start) / 1000);
	}
}
