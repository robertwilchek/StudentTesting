public class SumBug {
    public static int sum(int[] nums) {
        int total = 0;
        for (int i = 0; i <= nums.length; i++) { 
            total += nums[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] data = {2, 3, 5};
        System.out.println(sum(data)); 
    }
}