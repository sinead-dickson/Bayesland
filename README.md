# Bayesland - Agent Based Modelling

Bayesland is place where people walk around with boards listing things on which they would place a bet. If they meet a person whose odds on an event differs substantially from their own odds on that event, then the two will make a bet.

**This lab looks into a similar problem:**
* 3 agents bet on a probability of a coin coming up heads.
* The coin is simulated through a Bernoulli process (the probability of heads is 60%).
* In the beginning of each round, each agent initializes:
  * A key (random integer between 1 and 5)
  * A hypothesis regarding the probability of heads
  * Some idea of the past events (gives them an advantage)
  * A bankroll
* When two agents meet, they compare keys.
* If they have the same keys and a difference of opinion regarding the probability of heads, they make a bet.
* Each participant is willing to bet 5% of their bankroll (the final bet is going to be the average of whatever they are willing to bet).
* Each agent should have a slightly different recollection of the past events (controlled in a probabilistic manner).
