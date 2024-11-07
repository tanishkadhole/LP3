public class knapsack01 {
    
    public static int knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        int[][] dp = new int[n + 1][capacity + 1];
        
        // Build table dp[][] in bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0)
                    dp[i][w] = 0;
                else if (weights[i - 1] <= w)
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                else
                    dp[i][w] = dp[i - 1][w];
            }
        }
        
        // Store the result of Knapsack
        int result = dp[n][capacity];
        
        // Find the items that were included in the knapsack
        System.out.println("Selected items:");
        int w = capacity;
        for (int i = n; i > 0 && result > 0; i--) {
            if (result != dp[i - 1][w]) {
                System.out.println("Item " + i + " (Weight: " + weights[i - 1] + ", Value: " + values[i - 1] + ")");
                result -= values[i - 1];
                w -= weights[i - 1];
            }
        }
        
        // Return the maximum value we can get
        return dp[n][capacity];
    }
    
    public static void main(String[] args) {
        int[] values = {60, 100, 120};
        int[] weights = {10, 20, 30};
        int capacity = 50;
        
        int maxValue = knapsack(weights, values, capacity);
        System.out.println("Maximum value: " + maxValue);
    }
}