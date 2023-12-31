####Metacognitive evaluation technique########
META_EVALi_SYSTEM="""
You are an expert in math reasoning. Asses the following solution. During the evaluation, perfrom the following: 
1)Ensure that the problem's conditions are taken into account.
2)Assess the appropriateness of the methods and formulas used
3)Ensure every calculation and logical step is correct and clearly explained.
4)Verify if the final answer is accurate and addresses the question."
""".strip()

META_EVAL="""
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8. <END>
E:  Problem's Conditions: The problem states that Olivia has $23 and she buys five bagels, each costing $3. The solution takes into account both the amount Olivia initially has and the total cost of the bagels.

    Appropriateness of Methods and Formulas: The solution uses multiplication to find the total cost of the bagels (5 bagels at $3 each) and subtraction to determine the remaining amount of money. These are the correct mathematical operations for this problem.

    Accuracy of Calculations and Logical Steps:
        Calculation for the cost of bagels: 5 bagels × $3/bagel = $15. This is correct.
        Calculation for the remaining money: $23 - $15 = $8. This is also correct.

    Accuracy of the Final Answer: The final answer is $8, which correctly addresses the question of how much money Olivia has left after purchasing the bagels.

    Conclusion: The solution correctly applies the appropriate methods and calculations, and the final answer accurately resolves the question. The solution is correct.<END>

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many of balls did he have at the end of wednesday?
A: # Python code, return ans, ans should be a number
golf_balls_initial = 58
golf_balls_lost_tuesday = 23
golf_balls_lost_wednesday = 2
golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
ans = golf_balls_left
E: Problem's Conditions: The problem states that Michael initially had 58 golf balls, lost 23 on Tuesday, and lost 2 more on Wednesday. The solution correctly takes into account all these conditions.

    Appropriateness of Methods and Formulas: The solution uses subtraction to calculate the number of golf balls lost on each day and then the total remaining. This is the appropriate method for this type of problem.

    Accuracy of Calculations and Logical Steps:
        Initial number of golf balls: 58
        Golf balls lost on Tuesday: 23
        Golf balls lost on Wednesday: 2
        Calculation: 58−23−2=3358−23−2=33. The code correctly performs these calculations.

    Accuracy of the Final Answer: The final answer, as per the executed Python code, is 33. This correctly addresses the question of how many golf balls Michael had at the end of Wednesday.

Conclusion: The solution accurately applies the appropriate methods and calculations, and the final answer of 33 golf balls is correct, addressing the question effectively.<END>

Q:Angela is a bike messenger in New York. She needs to deliver 8 times as many packages as meals. If she needs to deliver 27 meals and packages combined, how many meals does she deliver?
A:System of linear equations: (Do not simplify)
% Assume Angela delivers x meals:
meals = x
% She needs to deliver 8 times as many packages as meals:
packages = 8 * meals
% She needs to deliver 27 meals and packages combined:
packages + meals = 27
% How many meals does she deliver? The answer is meals:
ans = meals
E:     Problem's Conditions: The solution sets up a system of linear equations based on the conditions given in the problem: Angela delivers xx meals (meals = xx), and she delivers 8 times as many packages as meals (packages = 8×x8×x). The total number of meals and packages is 27 (packages + meals = 27).

    Appropriateness of Methods and Formulas: Using a system of linear equations is an appropriate method to solve this problem. It allows for the expression of the relationship between the number of meals and packages and their total.

    Accuracy of Calculations and Logical Steps: However, the provided solution does not perform the calculations to solve the system of equations. We need to express the packages in terms of meals and substitute this into the total equation to find the value of xx (meals). Let's solve it:
        We have meals=xmeals=x and packages=8×xpackages=8×x.
        The equation packages+meals=27packages+meals=27 becomes 8x+x=278x+x=27.

Let's solve this equation to find the value of xx (the number of meals).

    Final Answer: We need to calculate the value of xx to find out how many meals Angela delivers.

After solving the equation, we find that Angela delivers 3 meals. The solution is correct. <END>

Q:{question}
A:{answer}
E:
""".strip()
