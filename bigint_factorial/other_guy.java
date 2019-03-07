import java.math.BigInteger;
class other_guy {
private static final int SIMPLE_THRESHOLD = 10;
private static BigInteger fac6(int n) {
    return subfac(1, n);
}

/**
 * compute a * (a+1) * ... *(b-1) * b
 * The interval [a,b] includes the endpoints a and b.
 *
 * @param a the interval start.
 * @param b the interval end, inclusive.
 * @return the product.
 */
private static BigInteger subfac(int a, int b) {
    if ((b-a) < SIMPLE_THRESHOLD) {
        BigInteger result = BigInteger.ONE;
        for (int i=a; i<=b; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    } else {
        int mid = a + (b-a) / 2;
        return subfac(a, mid).multiply(subfac(mid+1, b));
    }

}
public static void main(String[] args) {
    int n = 100000;
    long start = System.currentTimeMillis();
    BigInteger fac = fac6(n);
    long end = System.currentTimeMillis();
    float total = end - start;

    System.out.printf("%d! is %d bits long, took %f seconds to compute", n, fac.bitLength(), total / 1000);
}
}
