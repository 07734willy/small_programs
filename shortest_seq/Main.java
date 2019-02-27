public class Main {
	public static void main(String[] args) {
		int m = 79123;
		int n = 84132;
		int counter = 0;
		float ntemp;

		if (m > n) {
			counter = m - n;
			System.out.println("result: " + counter);
			return;
		}

		while (m != n) {
			ntemp = n;
			while (m < ntemp) {
				ntemp = ntemp / 2;
			}
			if (m < ntemp + 1) {
				m = m * 2;
				System.out.println("*2");
			} else {
				m = m - 1;
				System.out.println("-1");
			}
			counter++;
		}
		System.out.println("result: " + counter);
	}
}
