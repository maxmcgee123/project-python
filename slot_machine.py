
import random
from collections import Counter

# -------------------------------
# CONFIGURATION
# -------------------------------
STARTING_BALANCE = 100        # Default starting credits
MIN_BET = 1
MAX_BET = 100

# Symbol frequencies (weights) approximate "rarity" on each reel.
# Higher numbers = more common; lower numbers = rarer.
SYMBOL_WEIGHTS = {
    "7": 2,        # rare
    "BAR": 4,
    "🔔": 6,
    "⭐": 8,
    "🍋": 10,
    "🍒": 12       # most common
}

# Payouts for 3-of-a-kind on the CENTER payline (multiplier of bet)
PAYOUTS_3OAK = {
    "7": 50,
    "BAR": 20,
    "🔔": 10,
    "⭐": 8,
    "🍋": 5,
    "🍒": 3
}

# Small consolation payout for two cherries on the payline
TWO_CHERRIES_PAYOUT = 1  # returns 1x bet if exactly two 🍒 on the line

# -------------------------------
# CORE MECHANICS
# -------------------------------
def build_reel(symbol_weights):
    "Return a list representing a single reel strip built from weights."
    reel = []
    for sym, w in symbol_weights.items():
        reel.extend([sym] * int(w))
    return reel

def spin_reels(rng, reels):
    "Spin three reels and return the symbols on the single center payline."
    return tuple(rng.choice(reel) for reel in reels)

def evaluate_payline(line, bet):
    "Return (payout, message). payout is the CREDIT amount (not multiplier)."
    c = Counter(line)
    # 3-of-a-kind
    for sym in PAYOUTS_3OAK:
        if c[sym] == 3:
            win = PAYOUTS_3OAK[sym] * bet
            return win, f"3-of-a-kind {sym}! You win {win} credits."
    # Two cherries consolation
    if c["🍒"] == 2:
        win = TWO_CHERRIES_PAYOUT * bet
        return win, f"Two 🍒! You win {win} credits."
    # No win
    return 0, "No win. Better luck next spin!"

def prompt_bet(balance):
    while True:
        raw = input(f"Enter your bet ({MIN_BET}-{MAX_BET}) or 'q' to cash out: ").strip().lower()
        if raw == 'q':
            return None
        if not raw.isdigit():
            print("Please enter a whole number or 'q'.")
            continue
        amt = int(raw)
        if amt < MIN_BET or amt > MAX_BET:
            print(f"Bet must be between {MIN_BET} and {MAX_BET}.")
            continue
        if amt > balance:
            print("You cannot bet more than your current balance.")
            continue
        return amt

def main():
    print("🎰 Welcome to the Gamble3000! (Go All In Or You Are A Softie)")
    print("Symbols: 7, BAR, 🔔, ⭐, 🍋, 🍒")
    print(f"Payouts (3-of-a-kind, x bet): {PAYOUTS_3OAK}")
    print(f"Consolation: exactly two 🍒 pays {TWO_CHERRIES_PAYOUT}x bet")
    print()

    rng = random.Random()  # independent RNG for testability (can set seed if desired)
    reels = [build_reel(SYMBOL_WEIGHTS) for _ in range(3)]
    balance = STARTING_BALANCE

    print(f"Starting balance: {balance} credits.")
    while True:
        bet = prompt_bet(balance)
        if bet is None:
            print(f"Cashing out with {balance} credits. Thanks for playing!")
            break

        balance -= bet
        line = spin_reels(rng, reels)
        print(f"Spin: {' | '.join(line)}")
        win, msg = evaluate_payline(line, bet)
        print(msg)
        balance += win
        print(f"Balance: {balance} credits\n")

        if balance < MIN_BET:
            print("You are below the minimum bet. Ur Washed.")
            print(f"Final cashout: {balance} credits.")
            break

if __name__ == "__main__":
    main()
