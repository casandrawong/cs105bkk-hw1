# HW1 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?

I created a food delivery system with three classes (Menultem, Promoltem, and Order) and a helper function called cheapest. I added a rule (price.setter) to Menultem.price that prevents invalid pricing by issueing a Value Error if someone sttempts to set a price of 0 or less. Also, I used a shortcut loop to print all the receipt lines, then I tetstes cheapest() to determine the lowest price

## What broke, and how did you fix it?

At first, I wrote lines = [] inside Order.**init** which made different orders share the same list when i used Order.add() So i fixed that by switching to lines = None and lines.copy()

## What would you do differently next time?

Next time, I would run pytest cases right after each function and dont forget to save cus i always forget to do that.
