# Chai Tea Machine Program Manual

## Menu (sample values)

| Drink | Water | Milk | Tea leaves | Price |
|---|---|---|---|---|
| Masala Chai | 100 ml | 100 ml | 6 g | ₹20 |
| Ginger Chai | 100 ml | 120 ml | 6 g | ₹25 |
| Cutting Chai | 50 ml | 50 ml | 4 g | ₹10 |

## Requirements

1. **Prompt the user.** Ask "What would you like? (masala/ginger/cutting):" and check the input to decide the next step. The prompt shows again after every completed action, to serve the next customer.

2. **Turn off.** Entering "off" is the maintainers' secret word. The program ends execution.

3. **Print report.** Entering "report" shows the current resource values, for example:
   Water: 500ml
   Milk: 400ml
   Tea leaves: 100g
   Money: ₹0

4. **Check resources.** When a drink is chosen, check that there are enough resources. If not, print "Sorry, there is not enough water." (or milk, or tea leaves) and do not continue. Check every ingredient, not just the first.

5. **Process coins.** If resources are sufficient, ask the user to insert coins: ₹1, ₹2, ₹5 and ₹10. Calculate the total value. For example, 1 × ₹10 + 2 × ₹2 + 1 × ₹1 = ₹15.

6. **Check the transaction.**
   - If the money is less than the price, print "Sorry, that's not enough money. Money refunded."
   - If the money is enough, add the price to the machine's money, so it shows in the next report.
   - If the user paid extra, print "Here is ₹X in change."

7. **Make the chai.** Deduct the ingredients from the machine's resources, then print "Here is your masala chai. Enjoy!" (using the chosen drink's name).

