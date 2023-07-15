results = [input() for _ in range(3)]  # Read the weighting results

# Initialize coin weights
coin_weights = {'A': 0, 'B': 0, 'C': 0}

# Process the results
for result in results:
    coin1, relation, coin2 = result  # Split the result into coin1, relation, and coin2

    if relation == '>':
        coin_weights[coin1] += 1  # Increment the weight of coin1
        coin_weights[coin2] -= 1  # Decrement the weight of coin2
    else:
        coin_weights[coin1] -= 1  # Decrement the weight of coin1
        coin_weights[coin2] += 1  # Increment the weight of coin2

# Check the coin weights and determine the order
if coin_weights['A'] == coin_weights['B'] == coin_weights['C']:
    print("Impossible")  # Weighting results are contradictory
else:
    # Sort the coins based on their weights in increasing order
    ordered_coins = sorted(coin_weights, key=lambda x: coin_weights[x])

    # Print the rearrangement of letters A, B, and C representing the coins in increasing order of their weights
    print("".join(ordered_coins))
