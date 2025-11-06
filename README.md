# 🎰 Terminal Slot Machine (Final Project)

A small, focused slot machine you can play in the terminal. It uses a single **center payline** and weighted symbols to simulate reel rarity. Built to satisfy the project’s five process requirements.

---

## 1) Idea (10 pts)

**Build a minimal slot machine** you can play from the terminal:
- You start with credits.
- Choose a bet (1–10 credits).
- Spin 3 reels and read the result on the center payline.
- Get paid for **3-of-a-kind** and a small consolation for **two cherries**.
- Cash out any time.

Clear, simple scope with just enough interesting mechanics (weights/rarity + payouts).

---

## 2) Research (35 pts)

**Real-world mechanics**
- Slots have physical reels with fixed symbol strips and a payline (or many). Payouts depend on symbol rarity and alignments.
- “Rarer” symbols (e.g., 7) pay more when matched.

**Computer representation**
- Represent each reel as a list of symbols repeated by **weight** (frequency). Picking a random element simulates a reel stop.
- Use Python’s `random` to simulate randomness.
- Use a dictionary for **payout tables**, and `collections.Counter` to count symbols after a spin.

**Concrete choices**
- One center payline (keep evaluation simple and traceable).
- Symbols: `["7", "BAR", "🔔", "⭐", "🍋", "🍒"]`
- Weights (rarity): `{ "7":2, "BAR":4, "🔔":6, "⭐":8, "🍋":10, "🍒":12 }`
- Payouts (3-of-a-kind, multiplier of bet): `{ "7":50, "BAR":20, "🔔":10, "⭐":8, "🍋":5, "🍒":3 }`
- Consolation: exactly two `🍒` pays `1x` bet.

**Why these choices?**
- Weighted reels let you *feel* that 7s are rare and cherries are common.
- A single payline and a short payout table keep logic transparent and easy to debug.

---

## 3) Make the Computer Do One Concrete Thing (15 pts)

**Concrete action:** stop each reel at one symbol and report the **center payline** result, e.g., `BAR | 🍒 | 🔔`.

- Build each reel by repeating symbols by weight (e.g., cherries appear 12 times).
- Randomly choose one symbol from each reel to produce a 3-symbol line.
- Evaluate against a small payout table.

This mirrors the class example (mapping a physical action to a simple numeric/list computation).

---

## 4) Translate to Python (15 pts)

Key pieces of code (see `slot_machine.py`):
- **Reel building:** repeat symbols by weight into a list.
- **Spinning:** `rng.choice(reel)` for each of 3 reels.
- **Evaluation:** `Counter` to detect 3-of-a-kind or two-cherries case.
- **Loop & I/O:** prompt for bets, update balance, print outcomes.

Libraries used:
- `random` (RNG)
- `collections.Counter` (tally symbols)

---

## 5) Debug & Iterate (25 pts)

**Strategy used**
- Start with the **spin** and **evaluate** functions in isolation.
- Seed the RNG during testing (e.g., `random.Random(0)`) to reproduce spins.
- Add temporary `print()` traces around:
  - bets and balance changes,
  - the chosen payline,
  - evaluation branches (3-of-a-kind vs. two cherries vs. no win).

**Bugs I looked for**
- Off-by-one in bet validation (bet under/over limits).
- Balance going negative (subtract bet *before* payout, add winnings after).
- Two-cherries logic firing on mixed cases (ensure **exactly** two 🍒).

**Next-step ideas (if I need more scope)**
- Add a simple **RTP estimator**: run 100k spins (no I/O) and print expected return.
- Add **multiple paylines** (top/middle/bottom) and evaluate each.
- Add a **wild** symbol with simple substitution rules.
- Add a **--seed** CLI option and a `--demo` mode that auto-spins.

---

## How to Run

1. Ensure Python 3.8+ is installed.
2. Run:
   ```bash
   python3 slot_machine.py
   ```
3. Follow the prompts: enter a bet or `q` to cash out.

---

## File Map

- `slot_machine.py` — the playable terminal game.
- `sample_run.txt` — an example transcript captured with a fixed RNG seed.
- `README.md` — this document mapping work to the rubric.

---

## Example (what you’ll see)

```
🎰 Welcome to the Terminal Slot Machine! (single center payline)
Symbols: 7, BAR, 🔔, ⭐, 🍋, 🍒
Payouts (3-of-a-kind, x bet): {'7': 50, 'BAR': 20, '🔔': 10, '⭐': 8, '🍋': 5, '🍒': 3}
Consolation: exactly two 🍒 pays 1x bet

Starting balance: 100 credits.
Enter your bet (1-10) or 'q' to cash out:
```

---

## Notes for the Mini‑Interview

- I can walk through the **data model** (weights → reel strips → random choice).
- Show how evaluation logic maps to the payout table.
- Demonstrate testability by setting a **fixed seed** for reproducible spins.
- Discuss potential extensions and how they’d change data structures.