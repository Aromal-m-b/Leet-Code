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
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Hash Table
|  |
| ------- |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Math
|  |
| ------- |
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Geometry
|  |
| ------- |
| [3625-count-number-of-trapezoids-ii](https://github.com/Aromal-m-b/Leet-Code/tree/master/3625-count-number-of-trapezoids-ii) |
## Sorting
|  |
| ------- |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
| [3531-count-covered-buildings](https://github.com/Aromal-m-b/Leet-Code/tree/master/3531-count-covered-buildings) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
## Simulation
|  |
| ------- |
| [3433-count-mentions-per-user](https://github.com/Aromal-m-b/Leet-Code/tree/master/3433-count-mentions-per-user) |
## String
|  |
| ------- |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
| [3606-coupon-code-validator](https://github.com/Aromal-m-b/Leet-Code/tree/master/3606-coupon-code-validator) |
## Dynamic Programming
|  |
| ------- |
| [2110-number-of-smooth-descent-periods-of-a-stock](https://github.com/Aromal-m-b/Leet-Code/tree/master/2110-number-of-smooth-descent-periods-of-a-stock) |
| [2147-number-of-ways-to-divide-a-long-corridor](https://github.com/Aromal-m-b/Leet-Code/tree/master/2147-number-of-ways-to-divide-a-long-corridor) |
<!---LeetCode Topics End-->