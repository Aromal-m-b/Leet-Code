# 🧠 LeetCode Daily Solutions

This repository contains my daily solutions to LeetCode problems. Each solution includes a detailed explanation of the logic and reasoning behind the code. The goal of this project is to improve problem-solving skills, understand algorithms deeply, and maintain consistency in coding practice.  
After every explanation, a direct Markdown link to the corresponding solution file is provided.

---

## 📌 Problem Solutions

### **[Two Sum](./two_sum.py) – Explanation & Code**
This solution covers both the brute-force method and the optimized hash-map approach. The explanation describes how using a dictionary enables constant-time lookups, significantly improving time complexity compared to nested loops. 

---

### **[2211-Count Collisions on a Road](./2211-collision.py)**
We have an infinitely long road containing *i* cars in a line.  
Each car is represented by one of the following states:

- **L** → Car moving to the **left**
- **R** → Car moving to the **right**
- **S** → Car that is **stationary**

Collision rules:

- When a **moving car collides with a stationary (S)** car → **Collision Score +1**
- When **two moving cars collide (L ↔ R)** → **Collision Score +2**
- After any collision, all involved cars become **S (stationary)**.

---

 #### **Aim**
Determine the **total number of collisions** that will occur.

---

#### **Given**
A string/list representing the state of each car in order.


---

#### **Solution Logic**

1. **Identify collision-possible (danger) zones**  
   - A car on the **leftmost end moving left (L)** will never collide.  
   - A car on the **rightmost end moving right (R)** will never collide.  
   - Therefore, we trim away these “safe” boundary cars to isolate the **danger zone** where collisions can occur.

2. **Extract the danger zone**  
   Slice the string from:
   - the first non-L character  
   - to the last non-R character  

   All cars inside this zone are guaranteed to collide eventually because movement leads them into obstacles.

3. **Count collisions inside the danger zone**  
   - Every **moving car (L or R)** in the danger zone will eventually hit something → contributes to collisions.
   - Stationary cars (**S**) absorb collisions with only **+1** score.
   - Moving vs moving collisions contribute **+2**.

4. **Final collision count approach**
   - Count how many cars are **not stationary (L or R)** in the danger zone.
   - Each of those cars will produce a collision.  
   - Cars colliding with **S** → +1  
   - Cars colliding with **moving cars** → +2  
   - By subtracting the number of stationary cars in the zone, we account for +1 vs +2 collision rules.

---

#### **Result**
By evaluating only the **danger zone** and counting the moving cars that will inevitably collide, we compute the total number of collisions while correctly applying the scoring rules for different collision types.

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/Aromal-m-b/Leet-Code/tree/master/0001-two-sum) |
| [0014-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0014-longest-common-prefix) |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/Aromal-m-b/Leet-Code/tree/master/0027-remove-element) |
| [0033-search-in-rotated-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0033-search-in-rotated-sorted-array) |
| [0035-search-insert-position](https://github.com/Aromal-m-b/Leet-Code/tree/master/0035-search-insert-position) |
| [0048-rotate-image](https://github.com/Aromal-m-b/Leet-Code/tree/master/0048-rotate-image) |
| [0066-plus-one](https://github.com/Aromal-m-b/Leet-Code/tree/master/0066-plus-one) |
| [0118-pascals-triangle](https://github.com/Aromal-m-b/Leet-Code/tree/master/0118-pascals-triangle) |
| [0119-pascals-triangle-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/0119-pascals-triangle-ii) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0128-longest-consecutive-sequence](https://github.com/Aromal-m-b/Leet-Code/tree/master/0128-longest-consecutive-sequence) |
| [0153-find-minimum-in-rotated-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0153-find-minimum-in-rotated-sorted-array) |
| [0154-find-minimum-in-rotated-sorted-array-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/0154-find-minimum-in-rotated-sorted-array-ii) |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [0840-magic-squares-in-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/0840-magic-squares-in-grid) |
| [0944-delete-columns-to-make-sorted](https://github.com/Aromal-m-b/Leet-Code/tree/master/0944-delete-columns-to-make-sorted) |
| [1306-jump-game-iii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1306-jump-game-iii) |
| [1340-jump-game-v](https://github.com/Aromal-m-b/Leet-Code/tree/master/1340-jump-game-v) |
| [1345-jump-game-iv](https://github.com/Aromal-m-b/Leet-Code/tree/master/1345-jump-game-iv) |
| [1665-minimum-initial-energy-to-finish-tasks](https://github.com/Aromal-m-b/Leet-Code/tree/master/1665-minimum-initial-energy-to-finish-tasks) |
| [1674-minimum-moves-to-make-array-complementary](https://github.com/Aromal-m-b/Leet-Code/tree/master/1674-minimum-moves-to-make-array-complementary) |
| [1752-check-if-array-is-sorted-and-rotated](https://github.com/Aromal-m-b/Leet-Code/tree/master/1752-check-if-array-is-sorted-and-rotated) |
| [1861-rotating-the-box](https://github.com/Aromal-m-b/Leet-Code/tree/master/1861-rotating-the-box) |
| [1914-cyclically-rotating-a-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/1914-cyclically-rotating-a-grid) |
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [2126-destroying-asteroids](https://github.com/Aromal-m-b/Leet-Code/tree/master/2126-destroying-asteroids) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/Aromal-m-b/Leet-Code/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [2540-minimum-common-value](https://github.com/Aromal-m-b/Leet-Code/tree/master/2540-minimum-common-value) |
| [2553-separate-the-digits-in-an-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/2553-separate-the-digits-in-an-array) |
| [2574-left-and-right-sum-differences](https://github.com/Aromal-m-b/Leet-Code/tree/master/2574-left-and-right-sum-differences) |
| [2657-find-the-prefix-common-array-of-two-arrays](https://github.com/Aromal-m-b/Leet-Code/tree/master/2657-find-the-prefix-common-array-of-two-arrays) |
| [2770-maximum-number-of-jumps-to-reach-the-last-index](https://github.com/Aromal-m-b/Leet-Code/tree/master/2770-maximum-number-of-jumps-to-reach-the-last-index) |
| [2784-check-if-array-is-good](https://github.com/Aromal-m-b/Leet-Code/tree/master/2784-check-if-array-is-good) |
| [3043-find-the-length-of-the-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/3043-find-the-length-of-the-longest-common-prefix) |
| [3093-longest-common-suffix-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3093-longest-common-suffix-queries) |
| [3161-block-placement-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3161-block-placement-queries) |
| [3300-minimum-element-after-replacement-with-digit-sum](https://github.com/Aromal-m-b/Leet-Code/tree/master/3300-minimum-element-after-replacement-with-digit-sum) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3562-maximum-profit-from-trading-stocks-with-discounts](https://github.com/Aromal-m-b/Leet-Code/tree/master/3562-maximum-profit-from-trading-stocks-with-discounts) |
| [3573-best-time-to-buy-and-sell-stock-v](https://github.com/Aromal-m-b/Leet-Code/tree/master/3573-best-time-to-buy-and-sell-stock-v) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
| [3633-earliest-finish-time-for-land-and-water-rides-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3633-earliest-finish-time-for-land-and-water-rides-i) |
| [3635-earliest-finish-time-for-land-and-water-rides-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3635-earliest-finish-time-for-land-and-water-rides-ii) |
| [3652-best-time-to-buy-and-sell-stock-using-strategy](https://github.com/Aromal-m-b/Leet-Code/tree/master/3652-best-time-to-buy-and-sell-stock-using-strategy) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/Aromal-m-b/Leet-Code/tree/master/0001-two-sum) |
| [0013-roman-to-integer](https://github.com/Aromal-m-b/Leet-Code/tree/master/0013-roman-to-integer) |
| [0128-longest-consecutive-sequence](https://github.com/Aromal-m-b/Leet-Code/tree/master/0128-longest-consecutive-sequence) |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [0756-pyramid-transition-matrix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0756-pyramid-transition-matrix) |
| [0840-magic-squares-in-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/0840-magic-squares-in-grid) |
| [1345-jump-game-iv](https://github.com/Aromal-m-b/Leet-Code/tree/master/1345-jump-game-iv) |
| [1674-minimum-moves-to-make-array-complementary](https://github.com/Aromal-m-b/Leet-Code/tree/master/1674-minimum-moves-to-make-array-complementary) |
| [2540-minimum-common-value](https://github.com/Aromal-m-b/Leet-Code/tree/master/2540-minimum-common-value) |
| [2657-find-the-prefix-common-array-of-two-arrays](https://github.com/Aromal-m-b/Leet-Code/tree/master/2657-find-the-prefix-common-array-of-two-arrays) |
| [2784-check-if-array-is-good](https://github.com/Aromal-m-b/Leet-Code/tree/master/2784-check-if-array-is-good) |
| [3043-find-the-length-of-the-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/3043-find-the-length-of-the-longest-common-prefix) |
| [3120-count-the-number-of-special-characters-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3120-count-the-number-of-special-characters-i) |
| [3121-count-the-number-of-special-characters-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3121-count-the-number-of-special-characters-ii) |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Math
|  |
| ------- |
| [0013-roman-to-integer](https://github.com/Aromal-m-b/Leet-Code/tree/master/0013-roman-to-integer) |
| [0048-rotate-image](https://github.com/Aromal-m-b/Leet-Code/tree/master/0048-rotate-image) |
| [0066-plus-one](https://github.com/Aromal-m-b/Leet-Code/tree/master/0066-plus-one) |
| [0069-sqrtx](https://github.com/Aromal-m-b/Leet-Code/tree/master/0069-sqrtx) |
| [0070-climbing-stairs](https://github.com/Aromal-m-b/Leet-Code/tree/master/0070-climbing-stairs) |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [0788-rotated-digits](https://github.com/Aromal-m-b/Leet-Code/tree/master/0788-rotated-digits) |
| [0840-magic-squares-in-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/0840-magic-squares-in-grid) |
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
| [3300-minimum-element-after-replacement-with-digit-sum](https://github.com/Aromal-m-b/Leet-Code/tree/master/3300-minimum-element-after-replacement-with-digit-sum) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
| [3751-total-waviness-of-numbers-in-range-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3751-total-waviness-of-numbers-in-range-i) |
| [3753-total-waviness-of-numbers-in-range-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3753-total-waviness-of-numbers-in-range-ii) |
## Geometry
|  |
| ------- |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Sorting
|  |
| ------- |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [1340-jump-game-v](https://github.com/Aromal-m-b/Leet-Code/tree/master/1340-jump-game-v) |
| [1665-minimum-initial-energy-to-finish-tasks](https://github.com/Aromal-m-b/Leet-Code/tree/master/1665-minimum-initial-energy-to-finish-tasks) |
| [2126-destroying-asteroids](https://github.com/Aromal-m-b/Leet-Code/tree/master/2126-destroying-asteroids) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/Aromal-m-b/Leet-Code/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [2784-check-if-array-is-good](https://github.com/Aromal-m-b/Leet-Code/tree/master/2784-check-if-array-is-good) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
| [3633-earliest-finish-time-for-land-and-water-rides-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3633-earliest-finish-time-for-land-and-water-rides-i) |
| [3635-earliest-finish-time-for-land-and-water-rides-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3635-earliest-finish-time-for-land-and-water-rides-ii) |
## Simulation
|  |
| ------- |
| [1914-cyclically-rotating-a-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/1914-cyclically-rotating-a-grid) |
| [2553-separate-the-digits-in-an-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/2553-separate-the-digits-in-an-array) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
## String
|  |
| ------- |
| [0013-roman-to-integer](https://github.com/Aromal-m-b/Leet-Code/tree/master/0013-roman-to-integer) |
| [0014-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0014-longest-common-prefix) |
| [0756-pyramid-transition-matrix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0756-pyramid-transition-matrix) |
| [0796-rotate-string](https://github.com/Aromal-m-b/Leet-Code/tree/master/0796-rotate-string) |
| [0944-delete-columns-to-make-sorted](https://github.com/Aromal-m-b/Leet-Code/tree/master/0944-delete-columns-to-make-sorted) |
| [1871-jump-game-vii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1871-jump-game-vii) |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
| [3043-find-the-length-of-the-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/3043-find-the-length-of-the-longest-common-prefix) |
| [3093-longest-common-suffix-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3093-longest-common-suffix-queries) |
| [3120-count-the-number-of-special-characters-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3120-count-the-number-of-special-characters-i) |
| [3121-count-the-number-of-special-characters-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3121-count-the-number-of-special-characters-ii) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
## Dynamic Programming
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/Aromal-m-b/Leet-Code/tree/master/0070-climbing-stairs) |
| [0118-pascals-triangle](https://github.com/Aromal-m-b/Leet-Code/tree/master/0118-pascals-triangle) |
| [0119-pascals-triangle-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/0119-pascals-triangle-ii) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0788-rotated-digits](https://github.com/Aromal-m-b/Leet-Code/tree/master/0788-rotated-digits) |
| [1340-jump-game-v](https://github.com/Aromal-m-b/Leet-Code/tree/master/1340-jump-game-v) |
| [1871-jump-game-vii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1871-jump-game-vii) |
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
| [2770-maximum-number-of-jumps-to-reach-the-last-index](https://github.com/Aromal-m-b/Leet-Code/tree/master/2770-maximum-number-of-jumps-to-reach-the-last-index) |
| [3562-maximum-profit-from-trading-stocks-with-discounts](https://github.com/Aromal-m-b/Leet-Code/tree/master/3562-maximum-profit-from-trading-stocks-with-discounts) |
| [3573-best-time-to-buy-and-sell-stock-v](https://github.com/Aromal-m-b/Leet-Code/tree/master/3573-best-time-to-buy-and-sell-stock-v) |
| [3751-total-waviness-of-numbers-in-range-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3751-total-waviness-of-numbers-in-range-i) |
| [3753-total-waviness-of-numbers-in-range-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3753-total-waviness-of-numbers-in-range-ii) |
## Tree
|  |
| ------- |
| [0222-count-complete-tree-nodes](https://github.com/Aromal-m-b/Leet-Code/tree/master/0222-count-complete-tree-nodes) |
| [3562-maximum-profit-from-trading-stocks-with-discounts](https://github.com/Aromal-m-b/Leet-Code/tree/master/3562-maximum-profit-from-trading-stocks-with-discounts) |
## Depth-First Search
|  |
| ------- |
| [1306-jump-game-iii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1306-jump-game-iii) |
| [3562-maximum-profit-from-trading-stocks-with-discounts](https://github.com/Aromal-m-b/Leet-Code/tree/master/3562-maximum-profit-from-trading-stocks-with-discounts) |
## Sliding Window
|  |
| ------- |
| [1871-jump-game-vii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1871-jump-game-vii) |
| [3652-best-time-to-buy-and-sell-stock-using-strategy](https://github.com/Aromal-m-b/Leet-Code/tree/master/3652-best-time-to-buy-and-sell-stock-using-strategy) |
## Prefix Sum
|  |
| ------- |
| [1674-minimum-moves-to-make-array-complementary](https://github.com/Aromal-m-b/Leet-Code/tree/master/1674-minimum-moves-to-make-array-complementary) |
| [1871-jump-game-vii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1871-jump-game-vii) |
| [2574-left-and-right-sum-differences](https://github.com/Aromal-m-b/Leet-Code/tree/master/2574-left-and-right-sum-differences) |
| [3652-best-time-to-buy-and-sell-stock-using-strategy](https://github.com/Aromal-m-b/Leet-Code/tree/master/3652-best-time-to-buy-and-sell-stock-using-strategy) |
## Backtracking
|  |
| ------- |
| [0756-pyramid-transition-matrix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0756-pyramid-transition-matrix) |
## Bit Manipulation
|  |
| ------- |
| [0222-count-complete-tree-nodes](https://github.com/Aromal-m-b/Leet-Code/tree/master/0222-count-complete-tree-nodes) |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [0756-pyramid-transition-matrix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0756-pyramid-transition-matrix) |
| [0868-binary-gap](https://github.com/Aromal-m-b/Leet-Code/tree/master/0868-binary-gap) |
| [2657-find-the-prefix-common-array-of-two-arrays](https://github.com/Aromal-m-b/Leet-Code/tree/master/2657-find-the-prefix-common-array-of-two-arrays) |
## Matrix
|  |
| ------- |
| [0048-rotate-image](https://github.com/Aromal-m-b/Leet-Code/tree/master/0048-rotate-image) |
| [0840-magic-squares-in-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/0840-magic-squares-in-grid) |
| [1861-rotating-the-box](https://github.com/Aromal-m-b/Leet-Code/tree/master/1861-rotating-the-box) |
| [1914-cyclically-rotating-a-grid](https://github.com/Aromal-m-b/Leet-Code/tree/master/1914-cyclically-rotating-a-grid) |
## String Matching
|  |
| ------- |
| [0796-rotate-string](https://github.com/Aromal-m-b/Leet-Code/tree/master/0796-rotate-string) |
## Linked List
|  |
| ------- |
| [0061-rotate-list](https://github.com/Aromal-m-b/Leet-Code/tree/master/0061-rotate-list) |
## Two Pointers
|  |
| ------- |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0026-remove-duplicates-from-sorted-array) |
| [0027-remove-element](https://github.com/Aromal-m-b/Leet-Code/tree/master/0027-remove-element) |
| [0061-rotate-list](https://github.com/Aromal-m-b/Leet-Code/tree/master/0061-rotate-list) |
| [1861-rotating-the-box](https://github.com/Aromal-m-b/Leet-Code/tree/master/1861-rotating-the-box) |
| [2540-minimum-common-value](https://github.com/Aromal-m-b/Leet-Code/tree/master/2540-minimum-common-value) |
| [3633-earliest-finish-time-for-land-and-water-rides-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3633-earliest-finish-time-for-land-and-water-rides-i) |
| [3635-earliest-finish-time-for-land-and-water-rides-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3635-earliest-finish-time-for-land-and-water-rides-ii) |
## Greedy
|  |
| ------- |
| [1665-minimum-initial-energy-to-finish-tasks](https://github.com/Aromal-m-b/Leet-Code/tree/master/1665-minimum-initial-energy-to-finish-tasks) |
| [2126-destroying-asteroids](https://github.com/Aromal-m-b/Leet-Code/tree/master/2126-destroying-asteroids) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/Aromal-m-b/Leet-Code/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [3633-earliest-finish-time-for-land-and-water-rides-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3633-earliest-finish-time-for-land-and-water-rides-i) |
| [3635-earliest-finish-time-for-land-and-water-rides-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3635-earliest-finish-time-for-land-and-water-rides-ii) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/Aromal-m-b/Leet-Code/tree/master/0070-climbing-stairs) |
## Binary Search
|  |
| ------- |
| [0033-search-in-rotated-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0033-search-in-rotated-sorted-array) |
| [0035-search-insert-position](https://github.com/Aromal-m-b/Leet-Code/tree/master/0035-search-insert-position) |
| [0069-sqrtx](https://github.com/Aromal-m-b/Leet-Code/tree/master/0069-sqrtx) |
| [0153-find-minimum-in-rotated-sorted-array](https://github.com/Aromal-m-b/Leet-Code/tree/master/0153-find-minimum-in-rotated-sorted-array) |
| [0154-find-minimum-in-rotated-sorted-array-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/0154-find-minimum-in-rotated-sorted-array-ii) |
| [0222-count-complete-tree-nodes](https://github.com/Aromal-m-b/Leet-Code/tree/master/0222-count-complete-tree-nodes) |
| [0268-missing-number](https://github.com/Aromal-m-b/Leet-Code/tree/master/0268-missing-number) |
| [2540-minimum-common-value](https://github.com/Aromal-m-b/Leet-Code/tree/master/2540-minimum-common-value) |
| [3161-block-placement-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3161-block-placement-queries) |
| [3633-earliest-finish-time-for-land-and-water-rides-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3633-earliest-finish-time-for-land-and-water-rides-i) |
| [3635-earliest-finish-time-for-land-and-water-rides-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3635-earliest-finish-time-for-land-and-water-rides-ii) |
## Breadth-First Search
|  |
| ------- |
| [1306-jump-game-iii](https://github.com/Aromal-m-b/Leet-Code/tree/master/1306-jump-game-iii) |
| [1345-jump-game-iv](https://github.com/Aromal-m-b/Leet-Code/tree/master/1345-jump-game-iv) |
## Trie
|  |
| ------- |
| [0014-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/0014-longest-common-prefix) |
| [3043-find-the-length-of-the-longest-common-prefix](https://github.com/Aromal-m-b/Leet-Code/tree/master/3043-find-the-length-of-the-longest-common-prefix) |
| [3093-longest-common-suffix-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3093-longest-common-suffix-queries) |
## Binary Tree
|  |
| ------- |
| [0222-count-complete-tree-nodes](https://github.com/Aromal-m-b/Leet-Code/tree/master/0222-count-complete-tree-nodes) |
## Union-Find
|  |
| ------- |
| [0128-longest-consecutive-sequence](https://github.com/Aromal-m-b/Leet-Code/tree/master/0128-longest-consecutive-sequence) |
## Binary Indexed Tree
|  |
| ------- |
| [3161-block-placement-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3161-block-placement-queries) |
## Segment Tree
|  |
| ------- |
| [3161-block-placement-queries](https://github.com/Aromal-m-b/Leet-Code/tree/master/3161-block-placement-queries) |
## Enumeration
|  |
| ------- |
| [3751-total-waviness-of-numbers-in-range-i](https://github.com/Aromal-m-b/Leet-Code/tree/master/3751-total-waviness-of-numbers-in-range-i) |
<!---LeetCode Topics End-->