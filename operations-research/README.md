# Operations Research Resources

A curated, topic-based reference for **operations research**, **mathematical optimization**, **stochastic modeling**, **simulation**, **decision analysis**, and related computational methods.

Operations research uses mathematical models, algorithms, probability, simulation, and data to improve decisions in complex systems.

Common objectives include:

- Minimizing cost, delay, risk, waste, or energy use
- Maximizing profit, throughput, reliability, coverage, or service quality
- Allocating scarce resources
- Scheduling people, machines, vehicles, and projects
- Designing systems that remain effective under uncertainty
- Understanding trade-offs between competing objectives

> This README is organized as a reference index, not as a prescribed learning sequence. Use the separate learning-roadmap document for recommended study order.

---

## Contents

1. [How to Use This Repository](#1-how-to-use-this-repository)
2. [What Is Operations Research?](#2-what-is-operations-research)
3. [Mathematical and Computational Foundations](#3-mathematical-and-computational-foundations)
4. [Modeling and Problem Formulation](#4-modeling-and-problem-formulation)
5. [Deterministic Optimization](#5-deterministic-optimization)
6. [Stochastic Models and Optimization Under Uncertainty](#6-stochastic-models-and-optimization-under-uncertainty)
7. [Simulation](#7-simulation)
8. [Dynamic Programming and Stochastic Control](#8-dynamic-programming-and-stochastic-control)
9. [Decision Analysis and Game Theory](#9-decision-analysis-and-game-theory)
10. [Heuristics and Metaheuristics](#10-heuristics-and-metaheuristics)
11. [Data-Driven Operations Research](#11-data-driven-operations-research)
12. [Applications by Domain](#12-applications-by-domain)
13. [Modeling Languages, Solvers, and Libraries](#13-modeling-languages-solvers-and-libraries)
14. [Benchmark Datasets and Instance Libraries](#14-benchmark-datasets-and-instance-libraries)
15. [Courses, Books, Notes, and Videos](#15-courses-books-notes-and-videos)
16. [GitHub Resources](#16-github-resources)
17. [Research, Publications, and Communities](#17-research-publications-and-communities)

---

# 1. How to Use This Repository

Resources are organized by subject rather than by a required study order.

The following labels can be used when adding new resources:

- **Overview** — Introductory explanation or survey
- **Course** — Structured lectures, assignments, or course notes
- **Book** — Textbook, open book, or substantial reference
- **Notes** — Lecture notes, concise technical notes, or tutorials
- **Docs** — Official software documentation
- **Code** — Implementations, examples, or reusable libraries
- **Dataset** — Benchmark instances or practice data
- **Application** — Domain-specific case study or model
- **Advanced** — Graduate-level or research-oriented material

Suggested difficulty labels:

- **Beginner** — Little prior operations research knowledge required
- **Intermediate** — Assumes familiarity with mathematical modeling, probability, or algorithms
- **Advanced** — Assumes upper-level undergraduate or graduate mathematics

When reviewing a resource, consider:

- Is it technically accurate?
- Is it maintained or historically important?
- Is it legally accessible?
- Does it contain exercises, examples, code, or datasets?
- Is the intended audience clear?
- Does it add something not already covered by stronger resources?

---

# 2. What Is Operations Research?

**Operations research** is the use of mathematical modeling, optimization, probability, simulation, algorithms, and data analysis to support better decisions.

General references:

- [Operations research — Wikipedia](https://en.wikipedia.org/wiki/Operations_research)
- [INFORMS: What Is Operations Research?](https://www.informs.org/Explore/Operations-Research-Analytics)
- [Cornell Computational Optimization Open Textbook](https://optimization.cbe.cornell.edu/)
- [Mathematical optimization — Wikipedia](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Google OR-Tools](https://developers.google.com/optimization)
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [Health Service Modelling Associates Programme](https://github.com/hsma-programme)
- [COIN-OR](https://www.coin-or.org/)

Operations research models often contain:

- **Decision variables:** quantities controlled by the decision-maker
- **Parameters:** known or estimated inputs
- **An objective:** a measure to minimize or maximize
- **Constraints:** limits that feasible decisions must satisfy
- **Uncertainty:** unknown future values or random outcomes
- **A decision policy:** a rule for selecting actions as information changes

A generic mathematical optimization model is:

```math
\begin{aligned}
\min_{x} \quad & f(x) \\
\text{subject to} \quad & g_i(x) \le 0, \qquad i = 1,\ldots,m, \\
& h_j(x) = 0, \qquad j = 1,\ldots,p, \\
& x \in \mathcal{X}.
\end{aligned}
```

The choice of the functions, feasible set, uncertainty representation, and solution method determines the model class.

---

# 3. Mathematical and Computational Foundations

## 3.1 Linear Algebra

Important topics:

- Vectors, matrices, and tensors
- Matrix multiplication
- Linear independence and rank
- Systems of linear equations
- Vector spaces, null spaces, and ranges
- Eigenvalues and eigenvectors
- Positive semidefinite matrices
- Norms and inner products
- Least-squares problems
- Sparse matrices and factorizations

Resources:

- [Introduction to Applied Linear Algebra — Boyd and Vandenberghe](https://web.stanford.edu/~boyd/vmls/)
- [MIT 18.06: Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [MIT 18.065: Matrix Methods in Data Analysis, Signal Processing, and Machine Learning](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/)

## 3.2 Calculus and Mathematical Analysis

Important topics:

- Limits and continuity
- Partial derivatives
- Gradients, Jacobians, and Hessians
- Taylor approximations
- Convexity
- Integration
- Ordinary differential equations
- Constrained extrema
- Lagrange multipliers

For a differentiable function, a first-order approximation near a point is:

```math
f(x + d) \approx f(x) + \nabla f(x)^\mathsf{T}d.
```

A second-order approximation is:

```math
f(x + d) \approx f(x) + \nabla f(x)^\mathsf{T}d
+ \frac{1}{2}d^\mathsf{T}\nabla^2 f(x)d.
```

## 3.3 Probability and Statistics

Important topics:

- Probability spaces and events
- Conditional probability and Bayes' rule
- Random variables
- Common discrete and continuous distributions
- Expectation, variance, and covariance
- Laws of large numbers
- Central limit theorem
- Estimation and confidence intervals
- Regression
- Bayesian inference
- Sampling and experimental design

Resources:

- [MIT 6.041SC: Probabilistic Systems Analysis and Applied Probability](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/)
- [Harvard Stat 110: Probability](https://projects.iq.harvard.edu/stat110)
- [Introduction to Probability — Blitzstein and Hwang](https://projects.iq.harvard.edu/stat110/home)

## 3.4 Algorithms and Data Structures

Important topics:

- Computational complexity
- Asymptotic analysis
- Graphs and trees
- Heaps and priority queues
- Hash tables
- Sorting and searching
- Greedy algorithms
- Dynamic programming
- Recursion and backtracking
- Approximation algorithms
- Randomized algorithms

Resources:

- [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [MIT 6.006 video lectures](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY)
- [COMP 285: Analysis of Algorithms lectures](https://youtube.com/playlist?list=PL0KKKLEqGOyJR1-dEOKq9QRdCMX0Ho8hu)

## 3.5 Numerical Computing

Important topics:

- Floating-point arithmetic
- Numerical stability
- Scaling and conditioning
- Sparse matrix computation
- Iterative linear solvers
- Automatic differentiation
- Reproducibility
- Random seeds
- Profiling and performance measurement

Useful libraries:

- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [pandas](https://pandas.pydata.org/)
- [JAX](https://jax.readthedocs.io/)
- [Julia](https://julialang.org/)

---

# 4. Modeling and Problem Formulation

Operations research is not only a collection of algorithms. A complete project connects a real decision to a mathematical or computational model.

## 4.1 Problem Framing

Clarify:

- Who makes the decision?
- Which decisions are controllable?
- What is the time horizon?
- What is the unit of analysis?
- What constitutes a good outcome?
- Which constraints are mandatory?
- Which preferences are negotiable?
- Which quantities are uncertain?
- How will the model's output be used?

## 4.2 Sets, Parameters, and Variables

A formulation should clearly distinguish:

- **Sets and indices**
- **Input parameters**
- **Decision variables**
- **Derived quantities**
- **Objective terms**
- **Constraints**
- **Domains**

Example notation:

| Symbol | Meaning |
|---|---|
| `i` | Facility index |
| `j` | Customer index |
| `F` | Set of candidate facilities |
| `C` | Set of customers |
| `f_i` | Fixed cost of opening facility `i` |
| `c_{ij}` | Cost of serving customer `j` from facility `i` |
| `y_i` | Binary facility-opening decision |
| `x_{ij}` | Assignment decision |

## 4.3 Units and Dimensional Consistency

Every parameter and variable should have units. Constraints should compare quantities with compatible dimensions.

Examples:

- Cost per item multiplied by items gives cost.
- Processing time per job multiplied by jobs gives time.
- Flow on an arc should use the same quantity and time units as capacity.

## 4.4 Verification and Validation

- **Verification:** Was the model implemented correctly?
- **Validation:** Does the model adequately represent the real system?

Recommended checks:

- Solve a small instance by hand.
- Test extreme parameter values.
- Remove constraints one at a time.
- Confirm expected monotonic behavior.
- Check units.
- Compare against a baseline policy.
- Validate outputs with domain experts.
- Record assumptions and known limitations.

## 4.5 Infeasibility, Unboundedness, and Numerical Issues

A model may fail because:

- The constraints are mutually inconsistent.
- A necessary bound is missing.
- A sign or unit is incorrect.
- A Big-M value is too small or too large.
- Coefficients differ by many orders of magnitude.
- The solver terminates before proving optimality.
- The model allows an unintended decision.

Useful concepts:

- Irreducible infeasible subsystem
- Feasibility relaxation
- Presolve
- Scaling
- Solver tolerances
- Primal and dual bounds
- Optimality gap
- Termination status

## 4.6 Reproducible Computational Experiments

Record:

```text
instance name
data source
model version
algorithm or solver
solver version
hardware
operating system
time limit
memory limit
random seed
objective value
best bound
optimality gap
runtime
termination status
```

A relative optimality gap is commonly reported as:

```math
\mathrm{gap}
=
\frac{\left|z_{\text{primal}} - z_{\text{bound}}\right|}
{\max\left\{1,\left|z_{\text{primal}}\right|\right\}}.
```

---

# 5. Deterministic Optimization

## 5.1 Linear Programming

Linear programming optimizes a linear objective subject to linear constraints and continuous decision variables.

A common primal form is:

```math
\begin{aligned}
\max_{x} \quad & c^\mathsf{T}x \\
\text{subject to} \quad & Ax \le b, \\
& x \ge 0.
\end{aligned}
```

Important topics:

- Standard, canonical, and inequality forms
- Feasible regions and extreme points
- Basic feasible solutions
- Simplex method
- Revised simplex method
- Dual simplex method
- Interior-point methods
- Degeneracy
- Alternative optima
- Infeasibility and unboundedness
- Sensitivity analysis
- Post-optimality analysis

Applications:

- Production planning
- Resource allocation
- Blending
- Transportation
- Workforce capacity planning
- Cash-flow matching
- Diet and nutrition models

Resources:

- [Linear programming — Wikipedia](https://en.wikipedia.org/wiki/Linear_programming)
- [Cornell: Linear Programming](https://optimization.cbe.cornell.edu/index.php?title=Linear_programming)
- [MIT 15.053: Optimization Methods in Management Science](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/)
- [MIT 15.093J: Optimization Methods](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/)
- [Gurobi Modeling Examples](https://www.gurobi.com/jupyter_models/)
- [AMPL books and teaching materials](https://dev.ampl.com/ampl/books/)

## 5.2 Duality and Sensitivity Analysis

For the primal linear program

```math
\begin{aligned}
\max_{x} \quad & c^\mathsf{T}x \\
\text{subject to} \quad & Ax \le b, \\
& x \ge 0,
\end{aligned}
```

a corresponding dual is:

```math
\begin{aligned}
\min_{y} \quad & b^\mathsf{T}y \\
\text{subject to} \quad & A^\mathsf{T}y \ge c, \\
& y \ge 0.
\end{aligned}
```

Important topics:

- Weak duality
- Strong duality
- Complementary slackness
- Shadow prices
- Reduced costs
- Sensitivity ranges
- Economic interpretation of dual variables
- Lagrangian interpretation

## 5.3 Integer and Mixed-Integer Programming

Integer programming introduces discrete variables for yes/no choices, counts, assignments, sequences, and logical conditions.

A mixed-integer linear program can be written as:

```math
\begin{aligned}
\min_{x,y} \quad & c^\mathsf{T}x + d^\mathsf{T}y \\
\text{subject to} \quad & Ax + By \le b, \\
& x \in \mathbb{R}^{n}, \\
& y \in \mathbb{Z}^{p}.
\end{aligned}
```

Important concepts:

- Binary variables
- General integer variables
- LP relaxations
- Strong and weak formulations
- Big-M formulations
- Indicator constraints
- Logical implications
- Symmetry
- Valid inequalities
- Cutting planes
- Primal heuristics
- Branch-and-bound
- Branch-and-cut
- Branch-and-price
- Presolve
- Optimality gaps

A common linear implication is:

```math
x \le My,
```

where `y` is binary and `M` must be chosen carefully.

Typical problems:

- Facility location
- Network design
- Project selection
- Capital budgeting
- Lot sizing
- Unit commitment
- Set covering
- Bin packing
- Scheduling
- Routing

Resources:

- [Mixed-integer programming — Wikipedia](https://en.wikipedia.org/wiki/Integer_programming)
- [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)
- [Branch and cut](https://en.wikipedia.org/wiki/Branch_and_cut)
- [OR-Tools Integer Optimization](https://developers.google.com/optimization/mip)
- [SCIP Optimization Suite](https://www.scipopt.org/)
- [MIPLIB 2017](https://miplib.zib.de/)

## 5.4 Network Optimization and Network Flows

Network models use graphs with nodes, arcs, capacities, costs, and flows.

Major problem types:

- Shortest path
- All-pairs shortest path
- Maximum flow
- Minimum cut
- Minimum-cost flow
- Assignment
- Bipartite matching
- Transportation
- Multicommodity flow
- Network design
- Steiner tree problems

A minimum-cost flow model is:

```math
\begin{aligned}
\min_{x} \quad
& \sum_{(i,j)\in A} c_{ij}x_{ij} \\
\text{subject to} \quad
& \sum_{j:(i,j)\in A} x_{ij}
-
\sum_{j:(j,i)\in A} x_{ji}
= b_i,
\qquad i \in V, \\
& 0 \le x_{ij} \le u_{ij},
\qquad (i,j)\in A.
\end{aligned}
```

Algorithms:

- Dijkstra
- Bellman-Ford
- Floyd-Warshall
- A-star
- Ford-Fulkerson
- Edmonds-Karp
- Dinic
- Push-relabel
- Successive shortest path
- Cycle canceling
- Network simplex
- Hungarian algorithm

Applications:

- Transportation routing
- Telecommunications
- Supply-chain distribution
- Power systems
- Water networks
- Crew scheduling
- Evacuation planning

Resources:

- [OR-Tools Network Flows](https://developers.google.com/optimization/flow)
- [NetworkX](https://networkx.org/)
- [Google Network Optimization](https://github.com/google/network-opt)

## 5.5 Nonlinear Optimization

Nonlinear optimization includes models with nonlinear objectives or constraints.

A general nonlinear program is:

```math
\begin{aligned}
\min_{x} \quad & f(x) \\
\text{subject to} \quad & g_i(x) \le 0,
\qquad i = 1,\ldots,m, \\
& h_j(x) = 0,
\qquad j = 1,\ldots,p.
\end{aligned}
```

Important topics:

- Unconstrained optimization
- Constrained optimization
- Local and global optima
- First- and second-order conditions
- Gradient descent
- Newton methods
- Quasi-Newton methods
- BFGS and L-BFGS
- Line-search methods
- Trust-region methods
- Sequential quadratic programming
- Penalty and barrier methods
- Derivative-free optimization
- Nonsmooth optimization
- Global optimization
- Mixed-integer nonlinear programming

Resources:

- [Cornell: Nonlinear Programming](https://optimization.cbe.cornell.edu/index.php?title=Nonlinear_programming)
- [Cornell: Sequential Quadratic Programming](https://optimization.cbe.cornell.edu/index.php?title=Sequential_quadratic_programming)
- [Cornell: Derivative-Free Optimization](https://optimization.cbe.cornell.edu/index.php?title=Derivative_free_optimization)
- [NEOS Guide: Nonlinear Programming](https://neos-guide.org/guide/types/nonlin/)

## 5.6 Convex Optimization

A set is convex when the line segment between any two points in the set remains in the set:

```math
\theta x + (1-\theta)y \in \mathcal{C},
\qquad
x,y \in \mathcal{C},
\qquad
0 \le \theta \le 1.
```

A function is convex when:

```math
f\!\left(\theta x + (1-\theta)y\right)
\le
\theta f(x) + (1-\theta)f(y),
\qquad
0 \le \theta \le 1.
```

Important topics:

- Convex sets and cones
- Convex and concave functions
- Subgradients
- Lagrangian duality
- Karush-Kuhn-Tucker conditions
- Slater's condition
- Projected gradient methods
- Proximal methods
- Interior-point methods
- Alternating direction method of multipliers
- Disciplined convex programming

For a differentiable constrained problem, the Lagrangian is:

```math
\mathcal{L}(x,\lambda,\nu)
=
f(x)
+
\sum_{i=1}^{m}\lambda_i g_i(x)
+
\sum_{j=1}^{p}\nu_j h_j(x).
```

Resources:

- [Convex Optimization — Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/)
- [Stanford EE364a: Convex Optimization I](https://web.stanford.edu/class/ee364a/)
- [Stanford EE364b: Convex Optimization II](https://web.stanford.edu/class/ee364b/)
- [CVXPY](https://www.cvxpy.org/)
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)

## 5.7 Quadratic, Conic, and Semidefinite Optimization

A quadratic program has the form:

```math
\begin{aligned}
\min_{x} \quad
& \frac{1}{2}x^\mathsf{T}Qx + c^\mathsf{T}x \\
\text{subject to} \quad
& Ax \le b.
\end{aligned}
```

A second-order cone constraint often has the form:

```math
\lVert Ax + b \rVert_2
\le
c^\mathsf{T}x + d.
```

A semidefinite constraint has the form:

```math
X \succeq 0.
```

Topics:

- Convex quadratic programming
- Quadratically constrained programming
- Second-order cone programming
- Semidefinite programming
- Exponential and power cones
- Conic duality
- Robust counterparts expressed as conic programs

Resources:

- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [CVXPY Examples](https://www.cvxpy.org/examples/)
- [Stanford CVX](http://cvxr.com/cvx/)

## 5.8 Constraint Programming

Constraint programming is especially useful for logical, scheduling, sequencing, allocation, and combinatorial problems.

Core topics:

- Constraint satisfaction problems
- Variable domains
- Constraint propagation
- Global constraints
- Backtracking search
- Search heuristics
- Conflict learning
- CP-SAT
- Hybrid CP and MIP models

A constraint-satisfaction model seeks:

```math
x \in \mathcal{D}
```

such that:

```math
C_k(x) = \text{true},
\qquad
k = 1,\ldots,m.
```

Resources:

- [OR-Tools Constraint Optimization](https://developers.google.com/optimization/cp)
- [OR-Tools CP-SAT Solver](https://developers.google.com/optimization/cp/cp_solver)
- [MiniZinc](https://www.minizinc.org/)
- [MiniZinc Handbook](https://docs.minizinc.dev/)

## 5.9 Combinatorial Optimization

Common problem families:

- Traveling Salesman Problem
- Vehicle Routing Problem
- Knapsack
- Set covering and set partitioning
- Facility location
- Graph coloring
- Maximum independent set
- Clique
- Cutting stock
- Bin packing
- Assignment
- Matching
- Network design

Approaches:

- Exact algorithms
- Dynamic programming
- Branch-and-bound
- Cutting planes
- Approximation algorithms
- Parameterized algorithms
- Heuristics and metaheuristics
- Decomposition
- Problem-specific algorithms

Resources:

- [Combinatorial optimization — Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)
- [Williamson and Shmoys: The Design of Approximation Algorithms](https://www.designofapproxalgs.com/)
- [Concorde TSP Solver](https://www.math.uwaterloo.ca/tsp/concorde.html)

## 5.10 Scheduling and Sequencing

Common scheduling environments:

- Single machine
- Parallel machines
- Flow shop
- Job shop
- Open shop
- Flexible job shop
- Project scheduling
- Workforce scheduling
- Timetabling
- Crew scheduling

Common objectives:

```math
\min \quad C_{\max}
```

```math
\min \quad \sum_j C_j
```

```math
\min \quad \sum_j w_j T_j
```

where the quantities represent makespan, completion times, and weighted tardiness.

Important topics:

- Precedence constraints
- Release dates
- Due dates
- Sequence-dependent setup times
- Resource constraints
- Calendars and breaks
- Alternative machines
- No-overlap constraints
- Disjunctive formulations
- Time-indexed formulations
- Event-based formulations

Resources:

- [OR-Tools Scheduling](https://developers.google.com/optimization/scheduling)
- [NASA Dorado Scheduling](https://github.com/nasa/dorado-scheduling)
- [SchedulingLab](https://github.com/simonseo/schedulinglab)
- [IBM STOMP](https://github.com/IBM/stomp)

## 5.11 Decomposition and Large-Scale Optimization

Important methods:

- Benders decomposition
- Logic-based Benders decomposition
- Dantzig-Wolfe decomposition
- Column generation
- Branch-and-price
- Lagrangian relaxation
- Lagrangian decomposition
- Progressive hedging
- Alternating direction method of multipliers
- Delayed constraint generation
- Cutting-plane and outer-approximation methods

A two-block model may be written as:

```math
\begin{aligned}
\min_{x,y} \quad
& c^\mathsf{T}x + d^\mathsf{T}y \\
\text{subject to} \quad
& Ax + By \ge b, \\
& x \in \mathcal{X}, \\
& y \in \mathcal{Y}.
\end{aligned}
```

Decomposition exploits separability, block structure, or a distinction between complicating and easy variables.

Resources:

- [GCG: Generic Column Generation](https://gcg.or.rwth-aachen.de/)
- [SCIP Optimization Suite](https://www.scipopt.org/)
- [Pyomo.DAE and Pyomo decomposition extensions](https://pyomo.readthedocs.io/)

## 5.12 Multi-Objective Optimization

A multi-objective model is:

```math
\min_{x \in \mathcal{X}}
\left(
f_1(x), f_2(x), \ldots, f_k(x)
\right).
```

Important concepts:

- Pareto dominance
- Pareto frontier
- Weighted-sum method
- Epsilon-constraint method
- Goal programming
- Lexicographic optimization
- Reference-point methods
- Multi-criteria decision support

A weighted-sum scalarization is:

```math
\min_{x \in \mathcal{X}}
\sum_{r=1}^{k} w_r f_r(x),
\qquad
w_r \ge 0.
```

Resources:

- [pymoo](https://pymoo.org/)
- [jMetalPy](https://jmetal.github.io/jMetalPy/)
- [MOEA Framework](https://moeaframework.org/)

---

# 6. Stochastic Models and Optimization Under Uncertainty

## 6.1 Stochastic Processes

A stochastic process is a collection of random variables indexed by time or another ordered set:

```math
\left\{X_t : t \in \mathcal{T}\right\}.
```

Topics:

- Discrete- and continuous-time processes
- Independent increments
- Stationarity
- Ergodicity
- Poisson processes
- Renewal processes
- Markov chains
- Martingales
- Brownian motion
- Gaussian processes
- First-passage times

Resources:

- [MIT 6.262: Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/)
- [MIT 18.445: Introduction to Stochastic Processes](https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/)
- [Applied Stochastic Processes — Cornell](https://sidbanerjee.orie.cornell.edu/courses/orie6500/)
- [Stat 243: Stochastic Process Lecture Notes](https://bookdown.org/jkang37/stochastic-process-lecture-notes/)
- [University of Auckland stochastic processes course](https://www.stat.auckland.ac.nz/~fewster/325/index.php)
- [Caltech stochastic systems courses](https://murray.cds.caltech.edu/Stochastic_systems_courses)
- [Probability and Stochastic Processes — METU](https://ocw.metu.edu.tr/course/view.php?id=323)

Video playlists:

- [Probability, Random Variables, and Stochastic Processes](https://www.youtube.com/playlist?list=PLYemDO44RhzSgZmCQgubQ_Vn9QQ9s3kN4)
- [Stochastic Processes](https://www.youtube.com/playlist?list=PLTDbRVt9ixKRO0T0qmP43IyDrbh1i_5kW)
- [Advanced Stochastic Processes](https://www.youtube.com/playlist?list=PLV3oHJg9b1NRk4_LKUdqXPoN9jOWRypKI)
- [Stochastic Process](https://www.youtube.com/playlist?list=PLvpcUbGDkR2Cu_FGZifjh0Lgh1wNs2exH)

## 6.2 Markov Chains and Markov Processes

The Markov property is:

```math
\Pr\left(
X_{t+1}=j
\mid
X_t=i, X_{t-1},\ldots,X_0
\right)
=
\Pr\left(
X_{t+1}=j
\mid
X_t=i
\right).
```

Topics:

- Discrete-time Markov chains
- Continuous-time Markov chains
- Transition matrices
- Communicating classes
- Irreducibility
- Recurrence and transience
- Periodicity
- Stationary distributions
- Absorbing chains
- First-passage and hitting times
- Markov reward processes
- Birth-death processes
- Semi-Markov processes
- Aggregation and decomposition

A stationary distribution satisfies:

```math
\pi^\mathsf{T}P = \pi^\mathsf{T}
```

and:

```math
\sum_i \pi_i = 1.
```

Resources:

- [Markov chain — Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [MIT 6.262: Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/)
- [Applied Stochastic Processes — Cornell](https://sidbanerjee.orie.cornell.edu/courses/orie6500/)
- [Chinese Restaurant Process](https://en.wikipedia.org/wiki/Chinese_restaurant_process)

Applications:

- Reliability
- Customer behavior
- Inventory systems
- Epidemic models
- Credit ratings
- Maintenance
- Communication networks

## 6.3 Queueing Theory

Queueing theory studies systems with random arrivals, service times, waiting, congestion, and capacity constraints.

Core concepts:

- Arrival processes
- Service-time distributions
- Number of servers
- Queue discipline
- Capacity limits
- Customer population
- Balking
- Reneging
- Blocking
- Utilization
- Waiting time
- Queue length
- Throughput
- Service levels

Kendall notation:

```math
A/S/c/K/N/D.
```

For an M/M/1 queue, utilization is:

```math
\rho = \frac{\lambda}{\mu}.
```

When:

```math
\rho < 1,
```

the steady-state expected number in the system is:

```math
L = \frac{\rho}{1-\rho},
```

and the expected time in the system is:

```math
W = \frac{1}{\mu-\lambda}.
```

Little's law is:

```math
L = \lambda W.
```

Methods:

- Birth-death processes
- Continuous-time Markov chains
- Embedded Markov chains
- Transform methods
- Queueing networks
- Heavy-traffic approximations
- Diffusion approximations
- Simulation

Resources:

- [Queueing theory — Wikipedia](https://en.wikipedia.org/wiki/Queueing_theory)
- [MIT 15.072J: Queues — Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/)
- [Birth-death process](https://en.wikipedia.org/wiki/Birth%E2%80%93death_process)
- [Ciw](https://ciw.readthedocs.io/)
- [SimPy](https://simpy.readthedocs.io/)
- [queueing-tool](https://github.com/djordon/queueing-tool)

Applications:

- Call centers
- Hospitals
- Computer networks
- Cloud services
- Airports
- Manufacturing lines
- Checkout systems
- Public-service operations

## 6.4 Inventory Theory

Inventory theory studies stock decisions under demand, lead-time, supply, and service uncertainty.

The classical economic order quantity is:

```math
Q^*
=
\sqrt{\frac{2DK}{h}},
```

where `D` is demand rate, `K` is order cost, and `h` is holding cost per unit per period.

The newsvendor critical fractile is:

```math
F(Q^*)
=
\frac{C_u}{C_u+C_o},
```

where `C_u` is underage cost and `C_o` is overage cost.

Core models:

- Economic order quantity
- Newsvendor
- Base-stock policies
- Reorder-point policies
- Continuous-review policies
- Periodic-review policies
- Lost sales and backorders
- Perishable inventory
- Multi-item inventory
- Multi-echelon systems
- Spare-parts inventory
- Joint replenishment

Methods:

- Renewal theory
- Dynamic programming
- Markov decision processes
- Stochastic programming
- Approximation
- Simulation

Resources:

- [stockpyl](https://github.com/LarrySnyder/stockpyl)
- [Inventory control — Wikipedia](https://en.wikipedia.org/wiki/Inventory_control)
- [MIT supply-chain course materials](https://ocw.mit.edu/search/?q=inventory)

## 6.5 Reliability and Maintenance

Reliability is the probability that a component or system survives beyond time `t`:

```math
R(t)
=
\Pr(T>t).
```

The hazard rate is:

```math
h(t)
=
\frac{f(t)}{R(t)}.
```

Topics:

- Failure-time distributions
- Survival functions
- Hazard rates
- Mean time to failure
- Mean time between failures
- Series and parallel systems
- k-out-of-n systems
- Fault trees
- Reliability block diagrams
- Repairable systems
- Preventive maintenance
- Condition-based maintenance
- Replacement policies
- Spare-parts planning
- Degradation models

Methods:

- Renewal processes
- Markov and semi-Markov models
- Survival analysis
- Simulation
- Dynamic programming
- Optimization

## 6.6 Stochastic Programming

Stochastic programming models decisions with explicit random variables and probability distributions.

A two-stage stochastic program is:

```math
\min_{x \in \mathcal{X}}
\left\{
c^\mathsf{T}x
+
\mathbb{E}_{\xi}\left[Q(x,\xi)\right]
\right\},
```

where the recourse function is:

```math
Q(x,\xi)
=
\min_y
\left\{
q(\xi)^\mathsf{T}y
:
W(\xi)y
=
h(\xi)-T(\xi)x,
\;
y \ge 0
\right\}.
```

Topics:

- Two-stage recourse
- Multistage stochastic programs
- Scenario trees
- Nonanticipativity
- Chance constraints
- Risk measures
- Value of the stochastic solution
- Expected value of perfect information
- Sample average approximation
- L-shaped method
- Progressive hedging
- Stochastic decomposition

A chance constraint is:

```math
\Pr\left(g(x,\xi)\le 0\right)
\ge
1-\alpha.
```

Resources:

- [PySP documentation](https://pysp.readthedocs.io/)
- [mpi-sppy](https://github.com/Pyomo/mpi-sppy)
- [StochasticPrograms.jl](https://github.com/martinbiel/StochasticPrograms.jl)
- [SPJulia ecosystem](https://github.com/JuliaStochOpt)

## 6.7 Robust Optimization

Robust optimization seeks decisions that remain feasible or effective for every realization in an uncertainty set.

A robust model is:

```math
\begin{aligned}
\min_{x} \quad & f(x) \\
\text{subject to} \quad
& g(x,u) \le 0,
\qquad
\forall u \in \mathcal{U}.
\end{aligned}
```

Topics:

- Box uncertainty
- Polyhedral uncertainty
- Ellipsoidal uncertainty
- Budgeted uncertainty
- Robust counterparts
- Adjustable robust optimization
- Two-stage robust optimization
- Affine decision rules
- Price of robustness
- Robust feasibility
- Min-max and regret models

Resources:

- [Robust optimization — Wikipedia](https://en.wikipedia.org/wiki/Robust_optimization)
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [RSOME](https://xiongpengnus.github.io/rsome/)
- [JuMPeR](https://github.com/IainNZ/JuMPeR.jl)

## 6.8 Distributionally Robust Optimization

Distributionally robust optimization protects against uncertainty in the probability distribution itself.

A generic model is:

```math
\min_{x \in \mathcal{X}}
\sup_{\mathbb{P}\in\mathcal{P}}
\mathbb{E}_{\mathbb{P}}
\left[
f(x,\xi)
\right].
```

Topics:

- Ambiguity sets
- Moment-based ambiguity
- Phi-divergence ambiguity
- Wasserstein ambiguity
- Distributionally robust chance constraints
- Out-of-sample guarantees
- Data-driven uncertainty sets

## 6.9 Risk Measures

Expected loss alone may not represent tail risk.

Conditional value at risk can be written as:

```math
\mathrm{CVaR}_{\alpha}(L)
=
\min_{\eta}
\left\{
\eta
+
\frac{1}{1-\alpha}
\mathbb{E}
\left[
(L-\eta)_+
\right]
\right\}.
```

Topics:

- Value at risk
- Conditional value at risk
- Mean-semideviation
- Entropic risk
- Coherent risk measures
- Risk-averse stochastic programming
- Regret

---

# 7. Simulation

Simulation is useful when a system is too complex, stochastic, dynamic, or nonlinear for convenient closed-form analysis.

## 7.1 Discrete-Event Simulation

Discrete-event simulation represents system changes as events occurring at particular times.

Core elements:

- Entities
- Resources
- Processes
- Events
- Event calendars
- Queues
- Attributes
- State variables
- Routing logic
- Schedules
- Failures and repairs

Experimental topics:

- Warm-up periods
- Terminating and steady-state simulations
- Independent replications
- Batch means
- Confidence intervals
- Common random numbers
- Input modeling
- Output analysis
- Verification
- Validation

Resources:

- [Discrete-event simulation — Wikipedia](https://en.wikipedia.org/wiki/Discrete-event_simulation)
- [SimPy Documentation](https://simpy.readthedocs.io/)
- [SimPy in 10 Minutes](https://simpy.readthedocs.io/en/latest/simpy_intro/)
- [Ciw Documentation](https://ciw.readthedocs.io/)
- [Kalasim](https://github.com/holgerbrandl/kalasim)
- [OpenQTSim](https://github.com/TUDelft-CITG/OpenQTSim)
- [HSMA Programme](https://github.com/hsma-programme)

## 7.2 Monte Carlo Simulation

Monte Carlo methods estimate quantities using random sampling.

An expectation can be estimated by:

```math
\widehat{\mu}_n
=
\frac{1}{n}
\sum_{i=1}^{n}g(X_i).
```

Topics:

- Pseudorandom number generation
- Sampling distributions
- Confidence intervals
- Variance reduction
- Antithetic variables
- Control variates
- Importance sampling
- Stratified sampling
- Latin hypercube sampling
- Quasi-Monte Carlo
- Rare-event simulation
- Uncertainty propagation

## 7.3 Agent-Based Simulation

Agent-based simulation models autonomous entities whose local interactions produce system-level behavior.

Topics:

- Agents and environments
- Rules and state transitions
- Social and spatial networks
- Emergent behavior
- Calibration
- Validation
- Sensitivity analysis
- Policy experimentation

Resources:

- [Agent-based model — Wikipedia](https://en.wikipedia.org/wiki/Agent-based_model)
- [Mesa](https://mesa.readthedocs.io/)
- [Agents.jl](https://juliadynamics.github.io/Agents.jl/stable/)

## 7.4 System Dynamics

System dynamics models aggregate stocks, flows, delays, and feedback loops.

A stock evolves according to:

```math
\frac{dS(t)}{dt}
=
\mathrm{inflow}(t)
-
\mathrm{outflow}(t).
```

Topics:

- Stocks and flows
- Positive and negative feedback
- Delays
- Causal-loop diagrams
- Differential equations
- Policy resistance
- Scenario analysis

Resources:

- [System dynamics — Wikipedia](https://en.wikipedia.org/wiki/System_dynamics)
- [PySD](https://github.com/SDXorg/pysd)

## 7.5 Simulation Optimization

Simulation optimization searches for good decisions when performance is evaluated through a stochastic simulator.

A generic problem is:

```math
\min_{x \in \mathcal{X}}
\mathbb{E}
\left[
Y(x,\omega)
\right],
```

where the expectation is estimated through simulation.

Topics:

- Ranking and selection
- Multiple-comparison procedures
- Response-surface methods
- Stochastic approximation
- Sample-path optimization
- Bayesian optimization
- Surrogate modeling
- Optimal computing budget allocation
- Common random numbers
- Simulation-based gradient estimation

Applications:

- Staffing
- Facility design
- Healthcare capacity
- Manufacturing systems
- Transportation operations
- Supply-chain policies

---

# 8. Dynamic Programming and Stochastic Control

Dynamic programming studies multistage decisions in which current actions affect future states.

## 8.1 Bellman Recursion

For a finite-horizon problem:

```math
V_t(s)
=
\min_{a \in \mathcal{A}(s)}
\left\{
c_t(s,a)
+
\mathbb{E}
\left[
V_{t+1}(S_{t+1})
\mid
S_t=s,
A_t=a
\right]
\right\}.
```

Core concepts:

- State
- Action
- Transition
- Stage cost
- Terminal cost
- Horizon
- Policy
- Principle of optimality
- Curse of dimensionality

## 8.2 Deterministic Dynamic Programming

Applications:

- Knapsack
- Shortest path
- Equipment replacement
- Lot sizing
- Resource allocation
- Sequence alignment

## 8.3 Markov Decision Processes

An MDP is described by:

- State space
- Action space
- Transition probabilities
- Rewards or costs
- Discount factor or average-cost criterion

For a discounted MDP:

```math
V(s)
=
\min_{a \in \mathcal{A}(s)}
\left\{
c(s,a)
+
\gamma
\sum_{s'}
P(s' \mid s,a)
V(s')
\right\}.
```

Methods:

- Value iteration
- Policy iteration
- Linear programming
- Relative value iteration
- Policy evaluation
- Modified policy iteration

Resources:

- [Markov decision process — Wikipedia](https://en.wikipedia.org/wiki/Markov_decision_process)
- [MIT 6.231: Dynamic Programming and Stochastic Control](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)
- [scikit-decide](https://github.com/airbus/scikit-decide)
- [MDPtoolbox](https://github.com/sawcordwell/pymdptoolbox)

## 8.4 Partially Observable Markov Decision Processes

A POMDP uses a belief state when the true system state cannot be directly observed.

Belief-state updating follows Bayes' rule:

```math
b'(s')
=
\eta
O(o \mid s',a)
\sum_s
P(s' \mid s,a)b(s),
```

where `eta` is a normalizing constant.

Resources:

- [pomdp-py](https://github.com/h2r/pomdp-py)
- [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl)

## 8.5 Approximate Dynamic Programming

Topics:

- Value-function approximation
- Policy approximation
- Rollout
- Approximate policy iteration
- Temporal-difference learning
- Monte Carlo methods
- Post-decision states
- Basis functions
- Neural value functions
- Simulation-based optimization

## 8.6 Stochastic Control

Topics:

- Controlled Markov processes
- Linear-quadratic regulation
- Kalman filtering
- Model predictive control
- Hamilton-Jacobi-Bellman equations
- Optimal stopping
- Impulse control
- Inventory and capacity control

A discrete-time linear system is:

```math
x_{t+1}
=
Ax_t + Bu_t + w_t.
```

A quadratic objective may be:

```math
\mathbb{E}
\left[
\sum_{t=0}^{T-1}
\left(
x_t^\mathsf{T}Qx_t
+
u_t^\mathsf{T}Ru_t
\right)
+
x_T^\mathsf{T}Q_Tx_T
\right].
```

---

# 9. Decision Analysis and Game Theory

## 9.1 Decision Analysis

Decision analysis studies choices under uncertainty, risk, preferences, and multiple objectives.

Core concepts:

- Decision trees
- Influence diagrams
- Utility theory
- Risk aversion
- Bayesian decision analysis
- Value of information
- Sensitivity analysis
- Multi-criteria decision analysis

Expected utility is:

```math
\mathbb{E}
\left[
u(X)
\right]
=
\sum_x u(x)\Pr(X=x)
```

for a discrete random outcome.

The expected value of perfect information is:

```math
\mathrm{EVPI}
=
\mathbb{E}
\left[
\max_a U(a,\xi)
\right]
-
\max_a
\mathbb{E}
\left[
U(a,\xi)
\right].
```

Applications:

- Research and development
- Medical decisions
- Investment
- Policy analysis
- Technology selection
- Portfolio and project selection

## 9.2 Multi-Criteria Decision Analysis

Methods:

- Weighted scoring
- Analytic hierarchy process
- Analytic network process
- ELECTRE
- PROMETHEE
- TOPSIS
- Goal programming
- Multi-attribute utility theory

Use care when:

- Criteria overlap
- Weights are elicited inconsistently
- Scales are not comparable
- Rankings are highly sensitive
- Stakeholder preferences conflict

## 9.3 Game Theory

Game theory studies strategic interaction among multiple decision-makers.

Topics:

- Normal-form games
- Extensive-form games
- Dominance
- Best responses
- Nash equilibrium
- Mixed strategies
- Subgame-perfect equilibrium
- Bayesian games
- Perfect Bayesian equilibrium
- Repeated games
- Evolutionary games
- Cooperative games
- Bargaining
- Matching
- Voting
- Auctions
- Mechanism design
- Principal-agent models

For a two-player zero-sum game with payoff matrix `A`, the row player's problem can be written as:

```math
\begin{aligned}
\max_{p,v} \quad & v \\
\text{subject to} \quad
& A^\mathsf{T}p \ge v\mathbf{1}, \\
& \mathbf{1}^\mathsf{T}p = 1, \\
& p \ge 0.
\end{aligned}
```

Applications:

- Pricing
- Competition
- Auctions
- Procurement
- Security
- Negotiation
- Market design
- Network routing
- Resource sharing

### Introductory Game Theory Playlists

- [Game Theory 1: Introduction](https://youtube.com/playlist?list=PLcrc6i6xwaQQGOK095_Im781aFOQ1BFix)
- [Game Theory 2: Basic Solution Concepts](https://youtube.com/playlist?list=PLcrc6i6xwaQQGTAVXv25E3KP-cU5J9zLV)
- [Game Theory 3: Nash Equilibrium](https://youtube.com/playlist?list=PLcrc6i6xwaQTbWV-ayb4lky14yR6VqtAQ)
- [Game Theory 4: Mixed Strategies](https://youtube.com/playlist?list=PLcrc6i6xwaQQAbAPvrhpFsKPvcx_3sF-q)
- [Game Theory 5: Contracts](https://youtube.com/playlist?list=PLcrc6i6xwaQQqoZarpUJW2G3lfLFMan1U)
- [Game Theory 6: Extensive-Form Games with Perfect Information](https://youtube.com/playlist?list=PLcrc6i6xwaQTZI1YXJj4q_ndfEzMaPOZf)
- [Game Theory 7: Imperfect Information](https://youtube.com/playlist?list=PLcrc6i6xwaQRU-5Q_zRTu6GCiQSaKWJ-1)
- [Game Theory 8: Repeated Games](https://youtube.com/playlist?list=PLcrc6i6xwaQSbYxbSoY2JINrz5kb7-fGp)
- [Game Theory 9: Bayesian Nash Equilibrium](https://youtube.com/playlist?list=PLcrc6i6xwaQT6eIKWHkTXWz9zSFDpkTZm)
- [Game Theory 10: Perfect Bayesian Equilibrium](https://youtube.com/playlist?list=PLcrc6i6xwaQRP-e4fCBAnOmkbn860TX1_)
- [Game Theory 11: Principal-Agent Models](https://youtube.com/playlist?list=PLcrc6i6xwaQRa1ZsTG5-7a1AUltDvo-wS)

### Advanced Game Theory Playlists

- [Strategic-Form Games with Complete Information](https://youtube.com/playlist?list=PLcrc6i6xwaQRyvwICKDdh8zmvmXBcNaYg)
- [Extensive-Form Games](https://youtube.com/playlist?list=PLcrc6i6xwaQTlpwcoyC0m52oCPsWnAQ0t)
- [Solving Extensive-Form Games](https://youtube.com/playlist?list=PLcrc6i6xwaQSY7I2-UZxcQt_SodDN-L2r)
- [Cooperative Game Theory](https://youtube.com/playlist?list=PLcrc6i6xwaQSw8553tgt1p8XOMFEdQCbl)
- [Nash Bargaining](https://youtube.com/playlist?list=PLcrc6i6xwaQRcbvlbqNS94dRnF-UH1AZw)
- [Bankruptcy Problems](https://youtube.com/playlist?list=PLcrc6i6xwaQQo2li8WHSWiDnSnYaAH-g5)
- [Matching Theory](https://youtube.com/playlist?list=PLcrc6i6xwaQTmyz-hqitTB2WUI6eZiMIg)
- [Voting](https://youtube.com/playlist?list=PLcrc6i6xwaQTw1cDHdu8iEjo8nuYJG245)
- [Bayesian Games](https://youtube.com/playlist?list=PLcrc6i6xwaQSqqMfgqSYKITGV4i6RK9WI)
- [Auction Theory](https://youtube.com/playlist?list=PLcrc6i6xwaQT52YtKdIpdARVZ4BTFOrQP)
- [Mechanism Design](https://youtube.com/playlist?list=PLcrc6i6xwaQQWi7prJYkI9SoRzDXEV01X)

---

# 10. Heuristics and Metaheuristics

Heuristics seek good solutions when exact optimization is too slow, unnecessary, or unavailable.

## 10.1 Constructive Heuristics

- Greedy algorithms
- Insertion heuristics
- Savings algorithms
- Priority rules
- Randomized construction
- Regret insertion

## 10.2 Local Search

- Hill climbing
- First improvement
- Best improvement
- Swap neighborhoods
- Relocate neighborhoods
- Two-opt and three-opt
- Ejection chains
- Large neighborhoods
- Multi-start search
- Iterated local search

## 10.3 Metaheuristics

- Simulated annealing
- Tabu search
- Genetic algorithms
- Evolution strategies
- Differential evolution
- Ant colony optimization
- Particle swarm optimization
- GRASP
- Variable neighborhood search
- Adaptive large neighborhood search
- Scatter search
- Memetic algorithms

A simulated-annealing acceptance probability is often:

```math
\Pr(\text{accept})
=
\min
\left\{
1,
\exp\left(
-\frac{\Delta}{T}
\right)
\right\}.
```

## 10.4 Matheuristics and Hybrid Methods

- Fix-and-optimize
- Relax-and-fix
- Local branching
- RINS
- Feasibility pump
- MIP-based neighborhoods
- CP and MIP hybrids
- Simulation and optimization hybrids
- Learning-assisted heuristics

## 10.5 Evaluation

Compare methods using:

- Solution quality
- Runtime
- Gap from optimum or best-known solution
- Robustness across instances
- Sensitivity to parameters
- Reproducibility across seeds
- Scalability
- Memory use
- Feasibility rate
- Anytime performance

Resources:

- [ALNS](https://github.com/N-Wouda/ALNS)
- [PyVRP](https://github.com/PyVRP/PyVRP)
- [pymoo](https://pymoo.org/)
- [DEAP](https://deap.readthedocs.io/)
- [OR-Tools Routing](https://developers.google.com/optimization/routing)

---

# 11. Data-Driven Operations Research

## 11.1 Predict-Then-Optimize

A forecast is generated first and then inserted into an optimization model.

Potential issue: a model with better predictive accuracy may not produce better decisions.

Topics:

- Demand forecasting for inventory
- Travel-time prediction for routing
- Failure prediction for maintenance
- Price prediction for procurement
- Calibration and uncertainty propagation

## 11.2 Prescriptive Analytics

Prescriptive analytics combines prediction, uncertainty, and optimization to recommend actions.

A contextual decision problem can be written as:

```math
\min_{x \in \mathcal{X}}
\mathbb{E}
\left[
c(x,\xi)
\mid
Z=z
\right],
```

where `Z` contains observed context.

## 11.3 Decision-Focused Learning

Decision-focused learning trains predictive models using downstream decision quality rather than prediction error alone.

Topics:

- Differentiating through optimization
- Surrogate decision losses
- Structured prediction
- End-to-end learning
- SPO loss
- Differentiable convex optimization layers

Resources:

- [cvxpylayers](https://github.com/cvxpy/cvxpylayers)
- [DiffOpt.jl](https://github.com/jump-dev/DiffOpt.jl)
- [PyEPO](https://github.com/khalil-research/PyEPO)

## 11.4 Inverse Optimization

Inverse optimization infers objective coefficients, constraints, or preferences from observed decisions.

A generic inverse problem is:

```math
\mathrm{find} \quad \theta
```

such that observed decisions are approximately optimal for:

```math
\min_{x \in \mathcal{X}(\theta)}
f(x;\theta).
```

Applications:

- Preference learning
- Route-choice inference
- Clinical decision analysis
- Market behavior
- Personalized recommendations

## 11.5 Machine Learning for Combinatorial Optimization

Topics:

- Learned branching
- Learned cut selection
- Learned primal heuristics
- Neural construction methods
- Graph neural networks
- Learning to rank candidate moves
- Algorithm configuration
- Runtime prediction
- Instance classification

Resources:

- [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co)
- [Ecole](https://doc.ecole.ai/)
- [Distributional MIPLIB](https://sites.google.com/usc.edu/distributional-miplib/home)
- [OR-Gym](https://github.com/hubbs5/or-gym)
- [Maro](https://github.com/microsoft/maro)

## 11.6 Reinforcement Learning and OR

Useful distinctions:

1. OR models may provide structure, constraints, and benchmarks for reinforcement learning.
2. Reinforcement learning may approximate policies in large dynamic programs.
3. Optimization may be embedded inside an RL policy.
4. RL may guide search in combinatorial optimization.

Important concerns:

- Constraint satisfaction
- Safety
- Sample efficiency
- Out-of-distribution behavior
- Benchmark quality
- Comparison with strong OR baselines

---

# 12. Applications by Domain

## 12.1 Supply Chain and Logistics

- Facility location
- Network design
- Transportation
- Vehicle routing
- Inventory
- Warehousing
- Order fulfillment
- Supplier selection
- Procurement
- Last-mile delivery
- Reverse logistics
- Humanitarian logistics

## 12.2 Manufacturing

- Production planning
- Lot sizing
- Cutting and packing
- Job scheduling
- Maintenance planning
- Line balancing
- Quality control
- Capacity planning
- Process design

## 12.3 Healthcare

- Operating-room scheduling
- Appointment scheduling
- Bed capacity
- Emergency-department flow
- Ambulance location
- Workforce planning
- Blood inventory
- Organ allocation
- Treatment planning
- Public-health logistics

Resources:

- [HSMA Programme](https://github.com/hsma-programme)

## 12.4 Energy and Utilities

- Unit commitment
- Economic dispatch
- Optimal power flow
- Capacity expansion
- Storage operation
- Renewable integration
- Demand response
- Grid resilience
- Hydrothermal scheduling
- Water-resource planning

## 12.5 Finance and Economics

- Portfolio optimization
- Asset-liability management
- Risk management
- Option pricing
- Market design
- Dynamic pricing
- Revenue management
- Credit-risk modeling
- Capital budgeting

A mean-variance portfolio model is:

```math
\begin{aligned}
\min_{x} \quad
& x^\mathsf{T}\Sigma x \\
\text{subject to} \quad
& \mu^\mathsf{T}x \ge r_{\min}, \\
& \mathbf{1}^\mathsf{T}x = 1, \\
& x \in \mathcal{X}.
\end{aligned}
```

## 12.6 Telecommunications and Computing

- Network routing
- Capacity planning
- Cloud scheduling
- Load balancing
- Data-center operations
- Congestion control
- Cache placement
- Service placement
- Edge computing

## 12.7 Transportation

- Transit planning
- Airline scheduling
- Fleet assignment
- Crew scheduling
- Railway timetabling
- Traffic assignment
- Ride sharing
- Autonomous fleet management
- Port and terminal operations

## 12.8 Public Systems and Policy

- Emergency response
- Disaster logistics
- School assignment
- Election logistics
- Public transportation
- Infrastructure planning
- Environmental policy
- Criminal-justice resource allocation
- Social-service delivery

## 12.9 Defense and Security

- Search and detection
- Patrol allocation
- Adversarial planning
- Interdiction
- Surveillance allocation
- Resilient logistics
- Cybersecurity resource allocation

## 12.10 Sports

- Tournament scheduling
- Player selection
- Lineup optimization
- Draft strategy
- Travel scheduling
- Performance analysis
- Ticket pricing

---

# 13. Modeling Languages, Solvers, and Libraries

A **modeling language or interface** helps express a problem. A **solver** implements algorithms that attempt to solve a particular problem class. Some software contains both modeling and solving components.

## 13.1 Python Modeling Tools

| Tool | Primary use |
|---|---|
| [Pyomo](https://www.pyomo.org/) | General algebraic optimization modeling |
| [CVXPY](https://www.cvxpy.org/) | Convex optimization and disciplined convex programming |
| [PuLP](https://github.com/coin-or/pulp) | Accessible LP and MIP modeling |
| [OR-Tools](https://developers.google.com/optimization) | CP-SAT, routing, flows, assignment, LP, and MIP |
| [python-mip](https://www.python-mip.com/) | Mixed-integer linear programming |
| [PySCIPOpt](https://github.com/scipopt/PySCIPOpt) | Python interface to SCIP |
| [gurobipy](https://www.gurobi.com/documentation/) | Gurobi Python API |
| [docplex](https://github.com/IBMDecisionOptimization/docplex-doc) | IBM CPLEX modeling for Python |
| [RSOME](https://xiongpengnus.github.io/rsome/) | Robust and distributionally robust optimization |
| [Linopy](https://linopy.readthedocs.io/) | Linear optimization with labeled multidimensional data |

## 13.2 Julia Modeling Tools

| Tool | Primary use |
|---|---|
| [JuMP](https://jump.dev/JuMP.jl/stable/) | General mathematical optimization |
| [Convex.jl](https://jump.dev/Convex.jl/stable/) | Disciplined convex programming |
| [InfiniteOpt.jl](https://github.com/infiniteopt/InfiniteOpt.jl) | Infinite-dimensional optimization |
| [StochasticPrograms.jl](https://github.com/martinbiel/StochasticPrograms.jl) | Stochastic programming |
| [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl) | POMDP and MDP modeling |
| [Metaheuristics.jl](https://github.com/jmejia8/Metaheuristics.jl) | Metaheuristic optimization |

## 13.3 Algebraic Modeling Systems

- [AMPL](https://ampl.com/)
- [GAMS](https://www.gams.com/)
- [AIMMS](https://www.aimms.com/)
- [MiniZinc](https://www.minizinc.org/)
- [MOSEL](https://www.fico.com/en/products/fico-xpress-optimization)

## 13.4 Open-Source Solvers

| Solver | Common model classes |
|---|---|
| [HiGHS](https://highs.dev/) | LP, MIP, and convex QP |
| [SCIP](https://www.scipopt.org/) | MIP, constraint integer programming, and MINLP |
| [CBC](https://github.com/coin-or/Cbc) | MILP |
| [CLP](https://github.com/coin-or/Clp) | LP |
| [Ipopt](https://github.com/coin-or/Ipopt) | Large-scale nonlinear optimization |
| [OSQP](https://osqp.org/) | Convex quadratic programming |
| [SCS](https://www.cvxgrp.org/scs/) | Conic optimization |
| [ECOS](https://github.com/embotech/ecos) | Embedded conic optimization |
| [GLPK](https://www.gnu.org/software/glpk/) | LP and MIP |
| [Bonmin](https://github.com/coin-or/Bonmin) | Convex MINLP |
| [Couenne](https://github.com/coin-or/Couenne) | Global MINLP |
| [CSDP](https://github.com/coin-or/Csdp) | Semidefinite programming |

## 13.5 Commercial Solvers

- [Gurobi](https://www.gurobi.com/)
- [IBM ILOG CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio)
- [FICO Xpress](https://www.fico.com/en/products/fico-xpress-optimization)
- [MOSEK](https://www.mosek.com/)
- [Artelys Knitro](https://www.artelys.com/solvers/knitro/)
- [LocalSolver / Hexaly](https://www.hexaly.com/)
- [COPT](https://www.shanshu.ai/copt)

Check academic licensing and current license terms directly with each provider.

## 13.6 Routing and Scheduling Libraries

- [OR-Tools Routing](https://developers.google.com/optimization/routing)
- [PyVRP](https://github.com/PyVRP/PyVRP)
- [VRPy](https://github.com/Kuifje02/vrpy)
- [PyHygese](https://github.com/chkwon/PyHygese)
- [ALNS](https://github.com/N-Wouda/ALNS)
- [pyworkforce](https://github.com/rodrigo-arenas/pyworkforce)
- [Taskpacker](https://github.com/Edinburgh-Genome-Foundry/Taskpacker)

## 13.7 Simulation Libraries

- [SimPy](https://simpy.readthedocs.io/)
- [Ciw](https://ciw.readthedocs.io/)
- [Kalasim](https://github.com/holgerbrandl/kalasim)
- [Salabim](https://www.salabim.org/)
- [Mesa](https://mesa.readthedocs.io/)
- [Agents.jl](https://juliadynamics.github.io/Agents.jl/stable/)

## 13.8 Graph and Path-Planning Libraries

- [NetworkX](https://networkx.org/)
- [igraph](https://igraph.org/)
- [graph-tool](https://graph-tool.skewed.de/)
- [Google Network Optimization](https://github.com/google/network-opt)
- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
- [PathPlanning](https://github.com/zhm-real/PathPlanning)

## 13.9 Choosing Software

Consider:

- Problem class
- Model size
- Convexity
- Integer variables
- Required solver features
- Licensing
- Supported languages
- Documentation
- Community
- Deployment environment
- Need for callbacks
- Need for decomposition
- Repeated solve performance
- Numerical robustness

Always inspect:

- Solver status
- Termination condition
- Primal feasibility
- Dual feasibility when applicable
- Objective value
- Best bound
- Optimality gap
- Runtime
- Warnings
- Numerical diagnostics

---

# 14. Benchmark Datasets and Instance Libraries

Benchmark instances allow formulations and algorithms to be compared on shared problems.

## 14.1 General Mathematical Optimization

- [MIPLIB 2017](https://miplib.zib.de/)
- [MINLPLib](https://www.minlplib.org/)
- [QPLIB](https://qplib.zib.de/)
- [NETLIB LP collection](https://netlib.org/lp/)
- [OR-Library](https://www.brunel.ac.uk/~mastjjb/jeb/info.html)
- [Mathprog-ORlib](https://andreas-ernst.github.io/Mathprog-ORlib/)
- [COIN-OR Data](https://github.com/coin-or-tools/Data-Sample)

## 14.2 Routing

- [TSPLIB](https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
- [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/)
- [Solomon VRPTW instances](https://www.sintef.no/projectweb/top/vrptw/solomon-benchmark/)
- [Homberger VRPTW instances](https://www.sintef.no/projectweb/top/vrptw/homberger-benchmark/)
- [VRPLIB Python package](https://github.com/leonlan/VRPLIB)
- [PDPTW instances](https://github.com/cssartori/pdptw-instances)

## 14.3 Scheduling

- [OR-Library scheduling datasets](https://www.brunel.ac.uk/~mastjjb/jeb/orlib/files/)
- [Taillard scheduling instances](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html)
- [PSPLIB](https://www.om-db.wi.tum.de/psplib/)
- [Flexible Job Shop instances](https://people.idsia.ch/~monaldo/fjsp.html)
- [International Timetabling Competition](https://www.itc2019.org/)

## 14.4 Assignment, Location, and Covering

- [QAPLIB](https://qaplib.mgi.polymtl.ca/)
- [OR-Library facility-location instances](https://www.brunel.ac.uk/~mastjjb/jeb/orlib/capinfo.html)
- [Set covering instances](https://www.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html)

## 14.5 Packing and Cutting

- [BPPLIB](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library)
- [Cutting and Packing benchmark resources](https://www.euro-online.org/websites/esicup/data-sets/)

## 14.6 Stochastic and ML-Guided Optimization

- [Distributional MIPLIB](https://sites.google.com/usc.edu/distributional-miplib/home)
- [Ecole examples and environments](https://doc.ecole.ai/)
- [OR-Gym](https://github.com/hubbs5/or-gym)

## 14.7 Reporting Benchmark Results

For every experiment, report:

```text
problem class
instance source
instance name
objective convention
method
software version
solver version
hardware
time limit
memory limit
number of threads
random seed
objective value
best bound
optimality gap
runtime
feasibility status
termination reason
```

Do not compare runtimes without reporting hardware, thread count, software versions, and time limits.

---

# 15. Courses, Books, Notes, and Videos

## 15.1 General Optimization

- [Cornell Computational Optimization Open Textbook](https://optimization.cbe.cornell.edu/)
- [MIT 15.053: Optimization Methods in Management Science](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/)
- [MIT 15.093J: Optimization Methods](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/)
- [NEOS Guide](https://neos-guide.org/)
- [AMPL books](https://dev.ampl.com/ampl/books/)
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [Open Optimization OR Book](https://github.com/open-optimization/open-optimization-or-book)

## 15.2 Convex Optimization

- [Convex Optimization — Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/)
- [Stanford EE364a](https://web.stanford.edu/class/ee364a/)
- [Stanford EE364b](https://web.stanford.edu/class/ee364b/)
- [Introduction to Applied Linear Algebra](https://web.stanford.edu/~boyd/vmls/)

## 15.3 Algorithms and Combinatorial Optimization

- [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [MIT 6.046J: Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
- [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/)
- [COMP 285: Analysis of Algorithms](https://youtube.com/playlist?list=PL0KKKLEqGOyJR1-dEOKq9QRdCMX0Ho8hu)
- [MIT 6.006 video lectures](https://youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY)

## 15.4 Probability and Stochastic Processes

- [MIT 6.041SC: Probabilistic Systems Analysis](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/)
- [MIT 6.262: Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/)
- [MIT 18.445: Introduction to Stochastic Processes](https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/)
- [Applied Stochastic Processes — Cornell](https://sidbanerjee.orie.cornell.edu/courses/orie6500/)
- [Stochastic Process Lecture Notes](https://bookdown.org/jkang37/stochastic-process-lecture-notes/)

## 15.5 Queueing

- [MIT 15.072J: Queues — Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/)
- [Ciw Documentation](https://ciw.readthedocs.io/)
- [SimPy Documentation](https://simpy.readthedocs.io/)

## 15.6 Dynamic Programming and Control

- [MIT 6.231: Dynamic Programming and Stochastic Control](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)
- [Underactuated Robotics](https://underactuated.mit.edu/)
- [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)

## 15.7 Modeling and Software Tutorials

- [Pyomo Documentation](https://pyomo.readthedocs.io/)
- [JuMP Learning Materials](https://jump.dev/pages/learn/)
- [CVXPY User Guide](https://www.cvxpy.org/tutorial/)
- [OR-Tools Guides](https://developers.google.com/optimization)
- [Gurobi Modeling Examples](https://www.gurobi.com/jupyter_models/)
- [MOSEK Tutorials](https://github.com/MOSEK/Tutorials)

---

# 16. GitHub Resources

Repositories are grouped by purpose. Inclusion does not imply that a repository is actively maintained or suitable for production. Review documentation, licensing, issue activity, and test coverage before adoption.

## 16.1 General Optimization and Modeling

- [google/or-tools](https://github.com/google/or-tools) — General OR toolkit
- [Pyomo/pyomo](https://github.com/Pyomo/pyomo) — Official Pyomo repository
- [coin-or/pulp](https://github.com/coin-or/pulp) — LP and MIP modeling
- [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) — Convex optimization modeling
- [jump-dev/JuMP.jl](https://github.com/jump-dev/JuMP.jl) — Julia optimization modeling
- [scipopt/PySCIPOpt](https://github.com/scipopt/PySCIPOpt) — Python interface to SCIP
- [feloopy](https://github.com/ktafakkori/feloopy) — Optimization modeling framework
- [optimization-demo-files](https://github.com/bruscalia/optimization-demo-files) — Demonstration models
- [optimization-tutorial](https://github.com/ekhoda/optimization-tutorial) — Tutorial material
- [open-optimization-or-book](https://github.com/open-optimization/open-optimization-or-book) — Open textbook repository
- [operations-research](https://github.com/je-suis-tm/operations-research) — Example models
- [Operations-Research-Theory](https://github.com/tanmoyie/Operations-Research-Theory) — Theory notes and examples
- [Operations-Research](https://github.com/YashBansod/Operations-Research) — Educational repository

## 16.2 Mixed-Integer and Combinatorial Optimization

- [scipopt/scip](https://github.com/scipopt/scip) — SCIP solver
- [ERGO-Code/HiGHS](https://github.com/ERGO-Code/HiGHS) — HiGHS solver
- [coin-or/Cbc](https://github.com/coin-or/Cbc) — CBC MILP solver
- [coin-or/Clp](https://github.com/coin-or/Clp) — CLP LP solver
- [emadehsan/csp](https://github.com/emadehsan/csp) — Constraint-satisfaction examples
- [Taskpacker](https://github.com/Edinburgh-Genome-Foundry/Taskpacker) — Small scheduling and packing tasks

## 16.3 Routing and Logistics

- [PyVRP/PyVRP](https://github.com/PyVRP/PyVRP) — Vehicle-routing solver
- [N-Wouda/ALNS](https://github.com/N-Wouda/ALNS) — Adaptive large neighborhood search
- [chkwon/PyHygese](https://github.com/chkwon/PyHygese) — Hybrid genetic search interface
- [leonlan/VRPLIB](https://github.com/leonlan/VRPLIB) — VRPLIB instance parser
- [cssartori/pdptw-instances](https://github.com/cssartori/pdptw-instances) — Pickup-and-delivery instances
- [samirsaci/picking-route](https://github.com/samirsaci/picking-route) — Warehouse-picking examples
- [google/network-opt](https://github.com/google/network-opt) — Network optimization
- [Kuifje02/vrpy](https://github.com/Kuifje02/vrpy) — Vehicle routing in Python

## 16.4 Scheduling and Workforce Planning

- [lbiedma/shift-scheduling](https://github.com/lbiedma/shift-scheduling) — Shift-scheduling example
- [rodrigo-arenas/pyworkforce](https://github.com/rodrigo-arenas/pyworkforce) — Workforce planning
- [giangstrider/scheduling-optimization-ortools](https://github.com/giangstrider/scheduling-optimization-ortools) — OR-Tools scheduling examples
- [nasa/dorado-scheduling](https://github.com/nasa/dorado-scheduling) — NASA scheduling framework
- [simonseo/schedulinglab](https://github.com/simonseo/schedulinglab) — Scheduling research code
- [IBM/stomp](https://github.com/IBM/stomp) — Scheduling algorithms
- [lg-li/Genetic-Algorithm-Flexible-Job-Shop-Scheduling-Problem](https://github.com/lg-li/Genetic-Algorithm-Flexible-Job-Shop-Scheduling-Problem) — Genetic algorithm for flexible job-shop scheduling

## 16.5 Queueing and Simulation

- [CiwPython/Ciw](https://github.com/CiwPython/Ciw) — Queueing-network simulation
- [simpx/simpy](https://github.com/simpx/simpy) — Discrete-event simulation
- [holgerbrandl/kalasim](https://github.com/holgerbrandl/kalasim) — Kotlin simulation
- [TUDelft-CITG/OpenQTSim](https://github.com/TUDelft-CITG/OpenQTSim) — Queueing simulation
- [joelparkerhenderson/queueing-theory](https://github.com/joelparkerhenderson/queueing-theory) — Queueing references
- [guanzgrace/edX-queueing-theory](https://github.com/guanzgrace/edX-queueing-theory) — Queueing course material
- [AbdeltwabMF/queueing-modelsim](https://github.com/AbdeltwabMF/queueing-modelsim) — Queueing models
- [kargaranamir/M-M-1-Queue-Simulator](https://github.com/kargaranamir/M-M-1-Queue-Simulator) — M/M/1 simulator
- [birdepy/birdepy_project](https://github.com/birdepy/birdepy_project) — Birth-death process inference

## 16.6 Inventory and Supply Chain

- [LarrySnyder/stockpyl](https://github.com/LarrySnyder/stockpyl) — Inventory and supply-chain models
- [microsoft/maro](https://github.com/microsoft/maro) — Resource optimization platform

## 16.7 Dynamic Programming, MDPs, and Planning

- [hubbs5/or-gym](https://github.com/hubbs5/or-gym) — OR reinforcement-learning environments
- [h2r/pomdp-py](https://github.com/h2r/pomdp-py) — POMDP framework
- [airbus/scikit-decide](https://github.com/airbus/scikit-decide) — Decision-making framework
- [OpenSourceEconomics/respy](https://github.com/OpenSourceEconomics/respy) — Dynamic discrete-choice models
- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) — Robotics and path planning
- [zhm-real/PathPlanning](https://github.com/zhm-real/PathPlanning) — Path-planning algorithms

## 16.8 Machine Learning for Operations Research

- [Thinklab-SJTU/awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) — ML for combinatorial optimization resources
- [ds4dm/learn2branch](https://github.com/ds4dm/learn2branch) — Learned branching
- [dydx/easy-mip-learning](https://github.com/learning-lp/easy-mip-learning) — Learning for MIP examples
- [cvxpy/cvxpylayers](https://github.com/cvxpy/cvxpylayers) — Differentiable convex optimization layers
- [khalil-research/PyEPO](https://github.com/khalil-research/PyEPO) — Predict-then-optimize and end-to-end learning
- [ds4dm/ecole](https://github.com/ds4dm/ecole) — Learning environments for combinatorial optimization

## 16.9 Tutorials and Example Collections

- [MOSEK/Tutorials](https://github.com/MOSEK/Tutorials) — MOSEK tutorials
- [Gurobi modeling examples](https://github.com/Gurobi/modeling-examples) — Gurobi notebooks
- [Pyomo examples](https://github.com/Pyomo/pyomo-gallery) — Pyomo example gallery
- [Google OR-Tools examples](https://github.com/google/or-tools/tree/stable/examples) — OR-Tools examples
- [OptimizationExpert/Pyomo](https://github.com/OptimizationExpert/Pyomo) — Independent Pyomo examples

---

# 17. Research, Publications, and Communities

## 17.1 Professional Organizations

- [INFORMS](https://www.informs.org/)
- [EURO](https://www.euro-online.org/)
- [IFORS](https://www.ifors.org/)
- [The Operational Research Society](https://www.theorsociety.com/)
- [Mathematical Optimization Society](https://www.mathopt.org/)
- [SIAM](https://www.siam.org/)

## 17.2 Preprints and Technical Reports

- [Optimization Online](https://optimization-online.org/)
- [arXiv: Optimization and Control](https://arxiv.org/list/math.OC/recent)
- [arXiv: Operations Research](https://arxiv.org/list/math.OC/recent)
- [HAL](https://hal.science/)
- [INFORMS PubsOnLine](https://pubsonline.informs.org/)

## 17.3 Journals

- Operations Research
- Management Science
- Mathematics of Operations Research
- INFORMS Journal on Computing
- Transportation Science
- Manufacturing & Service Operations Management
- European Journal of Operational Research
- Computers & Operations Research
- Mathematical Programming
- Mathematical Programming Computation
- Journal of Global Optimization
- Networks
- Queueing Systems
- Naval Research Logistics
- Omega
- Decision Support Systems
- Journal of Scheduling
- Transportation Research series

## 17.4 Discussion and Q&A

- [Operations Research Stack Exchange](https://or.stackexchange.com/)
- [Math Stack Exchange](https://math.stackexchange.com/)
- [Cross Validated](https://stats.stackexchange.com/)
- [Julia Discourse: Optimization](https://discourse.julialang.org/c/domain/opt/13)
- [Pyomo Forum](https://github.com/Pyomo/pyomo/discussions)
- [OR-Tools Discussion Forum](https://groups.google.com/g/or-tools-discuss)

## 17.5 Conferences

- INFORMS Annual Meeting
- INFORMS Computing Society Conference
- EURO Conference
- IFORS Conference
- Mathematical Optimization Society International Symposium
- IPCO
- ISMP
- CPAIOR
- GECCO
- Winter Simulation Conference
- NeurIPS workshops related to optimization and decision-making
