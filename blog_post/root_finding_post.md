# 📘 Root Finding Methods – Project & Blog Planning Outline

This outline is designed to guide your implementation and help shape your blog post for **Pencils & Pythons**, while reinforcing the learning process. No full code, just structure and thinking prompts.

---

## 1. 🔧 Define the Problem

- Choose a nonlinear function `f(x)` with at least one real root
- Sketch or describe the behavior of the function
- Determine a reasonable interval where the root lies

**Questions to answer:**
- What is the function?
- Why did you choose it?
- Where do you believe the root is?
- Can you visualize or sketch it?

---

## 2. ✂️ Bisection Method Planning

- Describe the algorithm in your own words
- Identify required inputs: `f(x)`, interval `[a, b]`, tolerance, max iterations
- Think through edge cases (e.g., `f(a)` and `f(b)` have the same sign)

**Pseudocode elements:**
- Midpoint calculation
- Sign check to update interval
- Convergence criteria
- Loop counter

**Checklist:**
- [ ] Can you explain the logic to someone non-technical?
- [ ] What stops the loop?
- [ ] How will you measure or track error?

---

## 3. ⚡ Newton-Raphson Method Planning

- Write down the update formula  
  `xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)`
- Identify:
  - Function `f(x)`
  - Derivative `f'(x)`
  - Initial guess `x₀`
- Consider:
  - What if the derivative is 0?
  - What makes a "good" initial guess?

**Checklist:**
- [ ] Can you run a few steps manually?
- [ ] What are common failure modes?
- [ ] Do you want to implement the derivative manually or use symbolic differentiation?

---

## 4. 📊 Method Comparison Plan

- Decide how you’ll evaluate:
  - Speed (iteration count)
  - Accuracy (closeness to true root)
  - Reliability (failure rate)
- Choose your output:
  - Console print?
  - Table comparison?
  - Convergence plot (error vs iteration)?

**Checklist:**
- [ ] What metrics are you comparing?
- [ ] Will you graph anything?
- [ ] How will you log the iterations?

---

## 5. 🔬 Real-World Contexts

**Civil Engineering:**
- What is an example of using root-finding?  
  E.g., pipe friction losses, energy balance in flow systems

**Quant Finance:**
- Example: Solving for IRR or implied volatility  
  Can you explain how root-finding fits in?

**Checklist:**
- [ ] One real-world engineering application
- [ ] One finance/quant modeling application

---

## 6. 📦 Code Structure Planning

Break the implementation into clean, modular parts.

**Suggested functions:**
- `f(x)` → your main function
- `f_prime(x)` → the derivative (for Newton)
- `bisection(f, a, b, tol)` → method
- `newton(f, f_prime, x0, tol)` → method

**Checklist:**
- [ ] Will your code be reusable for other functions?
- [ ] Will you print step-by-step results or just final outputs?
- [ ] Will you log errors for plotting later?

---

## 7. 🧠 Reflection & Notes (for Blog Writing)

As you work through the problem, keep notes on:

- Points of confusion
- Errors you had to debug
- What concepts finally “clicked”
- Things you’d explain differently to your past self

**Checklist:**
- [ ] What was harder than expected?
- [ ] What surprised you?
- [ ] What tip would you give a beginner trying this?

---

## 🗂️ Optional Folder Setup

01_root_finding/
├── notes.md # This planning outline
├── root_finding.py # Your final implementation
├── bisection_log.txt # Optional: error logs or iteration data
├── newton_log.txt # Optional: same as above
├── error_plot.png # If plotting error vs iteration
└── README.md # Summary of what you implemented


---

## 🚀 Next Steps

Once this module is complete:
- Write your blog post using your notes above
- Link back to this repo
- Share insights or surprises in your “Lessons Learned” section


