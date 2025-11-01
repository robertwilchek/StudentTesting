public class Task2 {
    // Sum the numbers. BUG: off-by-one in the loop bound causes ArrayIndexOutOfBoundsException
    public static int sum(int[] nums) {
        int total = 0;
        for (int i = 0; i < nums.length; i++) { // BUG: should be i < nums.length
            total += nums[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] data = {2, 3, 5};
        System.out.println(sum(data)); // expected 10
    }
}