# Overview

A fundamental challenge in finance is how an agent can effectively buy or sell a large volume of shares while minimizing adverse price movements caused by their own trades. This involves balancing a trade-off between price impact (trading quickly, which can move the market price) and price risk (taking longer, which can expose the agent to market fluctuations).

## Execution Costs

Execution cost is defined as the difference between a benchmark price and the actual price (measured as the average price per share). When the benchmark is the asset's mid-price at the time the order is placed (known as the arrival price), this execution cost is referred to as the implementation shortfall or slippage.

## Key Variables and Notations

- **$V_t$**: Trading rate
- **$Q_t$**: Agent’s inventory
- **$S_t$**: Mid-price process
- **$\hat{S_t}$**: Execution price
- **$X_t$**: Agent’s cash
- **$g$**: Permanent price impact
- **$f$**: Temporary price impact

Price impact is often assumed to be linear with respect to trading speed:

$$
f(V_t) = k \cdot V_t
$$

Price impact varies throughout the day: it is highest in the morning, stabilizes during the day, and decreases toward market close.

## Formulas and Dynamics

**Inventory Control**:

$$
dQ_t = \pm V_t \cdot dt
$$

**Mid-Price Process**:

$$
dS_t = \pm g(V_t) + O \cdot dW_t
$$

**Execution Price**:

$$
\hat{S_t} = S_t \pm (\text{half spread} + f(V_t))
$$

**Cash Process**:

$$
dX_t = \hat{S_t} \cdot V_t \cdot dt
$$

## Liquidation Strategies

### 1. Liquidation Without Penalties (Temporary Impact Only)

The agent uses market orders to liquidate $n$ shares over a period from $t = 0$ to $T$. The optimal trading speed is:

$$
\text{Optimal speed} = \frac{n}{T}
$$

This strategy follows the Time-Weighted Average Price (TWAP).

### 2. Optimal Acquisition with Terminal Penalty and Temporary Impact

The agent may use strategies that don't meet the total inventory target ($Q_T < n$). Any shortfall is covered by a market order, incurring an additional penalty $a$. The optimal trading speed is:

$$
\text{Optimal speed} = \frac{t n}{T + \frac{k}{a}}
$$

As the penalty $a$ approaches infinity, this strategy converges to TWAP. For any values of $a$ and $k$, it's optimal to leave some shares for execution at the terminal date.

## Liquidation with Permanent Price Impact

The trade have both a temporary and a permanent price impact. There is also a running inventory penalty. This running inventory penalty is not (and should not be considered) a financial cost to the agent’s strategy. Rather it allows to incorporate the agent’s urgency for executing the trade.

The optimal speed to trade is still proportional to the investor’s current inventory level, but now the proportionality factor depends non-linearly on time.

## Execution with Exponential Utility Maximization

If the agent is risk-neutral and aims to maximize expected terminal wealth, they will execute trades in a manner similar to a risk-averse agent who is inventory-averse. When considering risk aversion with exponential utility, the behavior aligns with that of a risk-neutral but inventory-averse agent.

## Non-Linear Price Impact Models

We assumed that the price impact function f to be linear in the speed of trading, which is a good approximation but some researchers have shown that a power law with power less than one fits the data better. Others also argue that given the extremely complexity arising from moving away from a linear model would outweighs any gains from better describing market impact. The result is that as the power law parameter decreases, so that orders of the same size have less and less of an impact, the agent liquidates faster. The intuition here is that since trading does not impact prices as much, the agent prefers to liquidate shares early and reduce her inventory risk, and doing so does not cause her to lose too much from temporary market impact. In some sense the agent behaves as if he has a larger urgency parameter, but still uses a linear impact model.
