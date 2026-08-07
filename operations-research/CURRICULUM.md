# Two-Year Operations Research Curriculum

A project-centered curriculum for developing broad competence in operations research, mathematical optimization, stochastic modeling, simulation, and decision analysis.

This document specifies a study sequence. The separate operations research resources README should be used as the larger topic and reference index.

---

## Curriculum Principles

The curriculum is built around five recurring activities:

1. **Formulate:** Translate an operational problem into a precise model.
2. **Analyze:** Understand the mathematical structure and assumptions.
3. **Implement:** Build a reproducible solver or simulation workflow.
4. **Evaluate:** Test correctness, sensitivity, scalability, and robustness.
5. **Communicate:** Explain results, limitations, and operational recommendations.

Do not measure progress only by chapters read or lectures watched. Each quarter should end with a polished artifact demonstrating that the material can be used.

### Recommended workload

Scale the curriculum to the time available. A sustainable pattern is more important than a fixed weekly hour target. When time is limited:

- Preserve formulation exercises and projects.
- Reduce optional readings.
- Implement fewer algorithms from scratch.
- Study fewer advanced topics in greater depth.
- Do not skip model validation or result interpretation.

### Resource labels

- **Primary:** Main resource for the quarter
- **Theory:** Deeper mathematical treatment
- **Supplemental:** Alternative explanation or additional examples
- **Implementation:** Software documentation, notebooks, or code
- **Optional depth:** Material that can be postponed without disrupting the curriculum

---

# 0. Setup and Prerequisite Review

**Suggested duration:** Two to four weeks, extended if the diagnostic work reveals substantial gaps.

## Goals

- Establish a reproducible Python environment.
- Select the main modeling tools and solver.
- Review the mathematics required for later quarters.
- Choose one broad operations research textbook as a reference spine.
- Create a repository structure that will be reused throughout the curriculum.

## 0.1 Core Software

### Programming language

Use **Python** as the primary language.

Recommended foundation:

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [SciPy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)
- [NetworkX](https://networkx.org/)

### Optimization stack

Use one main tool for each major modeling class:

| Purpose | Recommended tool |
|---|---|
| General LP and MIP modeling | [Pyomo](https://www.pyomo.org/) |
| Convex optimization | [CVXPY](https://www.cvxpy.org/) |
| CP-SAT, routing, and specialized network models | [Google OR-Tools](https://developers.google.com/optimization) |
| Default open-source LP/MIP solver | [HiGHS](https://highs.dev/) |
| Discrete-event simulation | [SimPy](https://simpy.readthedocs.io/) |
| Queueing-network simulation | [Ciw](https://ciw.readthedocs.io/) |

PuLP is a reasonable lightweight alternative to Pyomo, but there is little benefit in learning both at the beginning. Choose one primary algebraic modeling package and become comfortable with it.

Commercial solvers are optional:

- [Gurobi academic program](https://www.gurobi.com/academia/academic-program-and-licenses/)
- [IBM ILOG CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio)
- [FICO Xpress](https://www.fico.com/en/products/fico-xpress-optimization)
- [MOSEK](https://www.mosek.com/)

Academic licenses must only be used according to their current terms.

## 0.2 Development Practices

Set up:

- Git and a remote repository
- A Python virtual environment
- JupyterLab or another notebook environment
- A source directory separate from notebooks
- Automated tests with `pytest`
- Formatting and linting
- A dependency file
- Fixed random seeds for experiments
- Logging of solver status and run metadata

Suggested initial structure:

```text
operations-research-curriculum/
├── README.md
├── environment.yml
├── pyproject.toml
├── src/
├── tests/
├── notebooks/
├── data/
├── models/
├── experiments/
├── reports/
└── references/
```

## 0.3 Mathematics Diagnostic

Before Year 1, verify familiarity with the following.

### Linear algebra

- Vectors and matrices
- Matrix multiplication
- Systems of linear equations
- Linear independence and rank
- Vector spaces and null spaces
- Eigenvalues and eigenvectors
- Positive semidefinite matrices
- Norms and inner products

Resources:

- **Primary review:** [Introduction to Applied Linear Algebra — Boyd and Vandenberghe](https://web.stanford.edu/~boyd/vmls/)
- **Supplemental course:** [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

### Calculus

- Partial derivatives
- Gradients
- Jacobians
- Hessians
- Taylor approximations
- Constrained extrema
- Lagrange multipliers
- Basic ordinary differential equations

A first-order approximation is:

```math
f(x+d)
\approx
f(x)
+
\nabla f(x)^\mathsf{T}d.
```

### Probability

- Conditional probability
- Bayes' rule
- Random variables
- Expectation and variance
- Covariance and correlation
- Common distributions
- Law of large numbers
- Central limit theorem
- Conditional expectation
- Poisson processes at an introductory level

Resources:

- **Primary review:** [MIT 6.041SC Probabilistic Systems Analysis and Applied Probability](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/)
- **Supplemental:** [Harvard Stat 110](https://projects.iq.harvard.edu/stat110)

### Algorithms

- Big-O notation
- Sorting and searching
- Graph representations
- Breadth-first and depth-first search
- Priority queues
- Greedy algorithms
- Recursion
- Basic dynamic programming

Resources:

- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)

## 0.4 Spine Resources

### Broad operations research reference

- **Primary:** [Hillier and Lieberman, *Introduction to Operations Research*](https://www.mheducation.com/highered/product/introduction-to-operations-research-hillier.html)

Use it as a broad reference rather than treating every chapter as mandatory.

### Mathematical optimization course

- **Primary applied course:** [MIT 15.053 Optimization Methods in Management Science](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/)
- **Advanced supplemental course:** [MIT 15.093J Optimization Methods](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/)

MIT 15.093J is graduate-level and unusually broad. Use selected lectures in the quarter where the topic belongs rather than attempting the entire course at once.

### Linear optimization theory reference

- **Theory:** [Bertsimas and Tsitsiklis, *Introduction to Linear Optimization*](https://www.mit.edu/~dbertsim/books.html)

Use selected chapters and exercises for geometry, duality, networks, integer optimization, and complexity.

## Setup Deliverable

Create a small repository containing:

- A linear optimization model solved through Pyomo and HiGHS
- A graph problem solved through NetworkX
- A short SimPy process
- Automated tests for at least one model
- A script that records package versions and run metadata
- A README explaining how to reproduce the results

---

# Year 1: Core Operations Research Toolbox

# Q1 — Modeling, Linear Programming, and Solver Literacy

**Months:** 1–3

## Goals

- Translate verbal decision problems into linear programs.
- Understand the geometry and algebra of linear programming.
- Interpret primal and dual solutions.
- Diagnose common model and solver failures.
- Build reproducible optimization projects in Python.

## Core Topics

### Modeling

- Sets, indices, parameters, and decision variables
- Units and dimensional consistency
- Objectives and constraints
- Hard constraints versus preferences
- Boundary cases
- Verification and validation
- Model assumptions
- Data-model separation

### Linear programming

A common linear program is:

```math
\begin{aligned}
\mathrm{maximize}_{x} \quad
& c^\mathsf{T}x \\
\text{subject to} \quad
& Ax \le b, \\
& x \ge 0.
\end{aligned}
```

Study:

- Standard and canonical forms
- Slack and surplus variables
- Feasible regions
- Extreme points
- Basic feasible solutions
- Simplex method
- Revised simplex method
- Degeneracy
- Alternative optima
- Unboundedness
- Infeasibility
- Interior-point methods at a conceptual level

### Duality

For the primal model:

```math
\begin{aligned}
\mathrm{maximize}_{x} \quad
& c^\mathsf{T}x \\
\text{subject to} \quad
& Ax \le b, \\
& x \ge 0,
\end{aligned}
```

a corresponding dual is:

```math
\begin{aligned}
\mathrm{minimize}_{y} \quad
& b^\mathsf{T}y \\
\text{subject to} \quad
& A^\mathsf{T}y \ge c, \\
& y \ge 0.
\end{aligned}
```

Study:

- Weak duality
- Strong duality
- Complementary slackness
- Shadow prices
- Reduced costs
- Sensitivity ranges
- Economic interpretation

### Solver literacy

- Solver status and termination conditions
- Primal and dual feasibility
- Presolve
- Scaling
- Numerical tolerances
- Infeasibility diagnosis
- Feasibility relaxation
- Repeated solves
- Parameter sweeps

## Primary Resources

- Hillier and Lieberman: introductory modeling, LP, simplex, duality, and sensitivity chapters
- [MIT 15.053 lecture notes and recitations](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/pages/lecture-notes/)
- Selected early lectures from [MIT 15.093J](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/pages/lecture-notes/)
- [Cornell Computational Optimization Open Textbook](https://optimization.cbe.cornell.edu/)

## Supplemental Resources

- **Theory:** Bertsimas and Tsitsiklis, selected chapters on polyhedra and duality
- **Alternative advanced text:** [Nemirovski, *Introduction to Linear Optimization*](https://www2.isye.gatech.edu/~nemirovs/WSPrinted.pdf)
- **Reference:** [NEOS Guide](https://neos-guide.org/)
- **Model examples:** [Gurobi Modeling Examples](https://github.com/Gurobi/modeling-examples)
- **AMPL references and books:** [AMPL book collection](https://dev.ampl.com/ampl/books/)

## Implementation Resources

- [Pyomo documentation](https://www.pyomo.org/documentation)
- [HiGHS documentation](https://ergo-code.github.io/HiGHS/dev/)
- [SciPy linear programming documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

## Required Practice

Formulate and solve at least six LPs from different families:

- Product mix
- Blending
- Transportation
- Diet
- Workforce capacity
- Cash-flow matching
- Advertising allocation
- Multi-period production planning

Perform hand simplex on only one or two small problems. The goal is to understand the method, not to spend the quarter doing tableau arithmetic.

## Quarter Project

Build one LP project through the full modeling lifecycle:

1. Frame the decision and stakeholders.
2. Define data, units, assumptions, variables, objective, and constraints.
3. Solve a small instance by hand or inspection.
4. Implement the complete model.
5. Validate the implementation.
6. Conduct sensitivity analysis.
7. Explain the dual values operationally.
8. Write a short model-audit report.

## Mastery Check

By the end of Q1, you should be able to:

- Formulate an LP without copying a template.
- Derive and interpret a dual.
- Explain why a model is infeasible or unbounded.
- Check solver termination rather than assuming success.
- Describe which assumptions materially affect the recommendation.

---

# Q2 — Network Optimization, Mixed-Integer Programming, and CP-SAT

**Months:** 4–6

## Goals

- Recognize and exploit graph structure.
- Model discrete decisions using binary and integer variables.
- Understand branch-and-bound and relaxation-based reasoning.
- Compare network, MILP, and constraint-programming formulations.
- Evaluate formulation strength rather than only solver output.

## Core Topics

## Network optimization

Study:

- Shortest path
- Minimum spanning tree
- Maximum flow
- Minimum cut
- Minimum-cost flow
- Transportation
- Assignment
- Bipartite matching
- Multicommodity flow
- Network design

A minimum-cost flow model is:

```math
\begin{aligned}
\mathrm{minimize}_{x} \quad
& \sum_{(i,j)\in A} c_{ij}x_{ij} \\
\text{subject to} \quad
& \sum_{j:(i,j)\in A}x_{ij}
-
\sum_{j:(j,i)\in A}x_{ji}
=
b_i,
\qquad i \in V, \\
& 0 \le x_{ij} \le u_{ij},
\qquad (i,j)\in A.
\end{aligned}
```

Algorithms:

- Dijkstra
- Bellman-Ford
- Floyd-Warshall
- Ford-Fulkerson
- Edmonds-Karp
- Push-relabel
- Successive shortest path
- Network simplex
- Hungarian algorithm

## Mixed-integer programming

A mixed-integer linear program is:

```math
\begin{aligned}
\mathrm{minimize}_{x,y} \quad
& c^\mathsf{T}x + d^\mathsf{T}y \\
\text{subject to} \quad
& Ax + By \le b, \\
& x \in \mathbb{R}^{n}, \\
& y \in \mathbb{Z}^{p}.
\end{aligned}
```

Study:

- Binary and general integer variables
- Fixed-charge models
- Logical conditions
- Either-or constraints
- Big-M formulations
- Indicator constraints
- LP relaxation
- Integrality gap
- Strong and weak formulations
- Valid inequalities
- Symmetry
- Branch-and-bound
- Cutting planes
- Branch-and-cut
- Primal heuristics
- Presolve
- Primal and dual bounds
- Optimality gaps

A common implication is represented by:

```math
x \le My,
```

where `y` is binary. The value of `M` should be justified from valid bounds rather than chosen arbitrarily.

## Constraint programming and CP-SAT

Study:

- Variable domains
- Constraint propagation
- Global constraints
- No-overlap constraints
- Optional intervals
- Search strategies
- Conflict learning
- CP-SAT modeling
- When CP is preferable to MILP

## Primary Resources

- Hillier and Lieberman: transportation, assignment, network, and integer-programming chapters
- [MIT 15.053 network and integer optimization material](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/)
- [Ahuja, Magnanti, and Orlin, *Network Flows*](https://mitmgmtfaculty.mit.edu/jorlin/network-flows/)
- Selected network and discrete-optimization lectures from [MIT 15.093J](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/)

## Supplemental Resources

- **Theory:** Bertsimas and Tsitsiklis, network and integer optimization chapters
- **Approximation algorithms:** [Williamson and Shmoys, *The Design of Approximation Algorithms*](https://www.designofapproxalgs.com/)
- **MIP solver reference:** [SCIP Optimization Suite](https://www.scipopt.org/)
- **Benchmark models:** [MIPLIB 2017](https://miplib.zib.de/)
- **Network exercises:** [Network Flows solution materials](https://mitmgmtfaculty.mit.edu/jorlin/solution-manual/)

## Implementation Resources

- [NetworkX algorithms](https://networkx.org/documentation/stable/reference/algorithms/)
- [OR-Tools network flows](https://developers.google.com/optimization/flow)
- [OR-Tools MIP guide](https://developers.google.com/optimization/mip)
- [OR-Tools CP-SAT guide](https://developers.google.com/optimization/cp/cp_solver)
- [PySCIPOpt](https://github.com/scipopt/PySCIPOpt)

## Required Practice

Implement from scratch:

- Dijkstra's algorithm
- One maximum-flow algorithm
- A small branch-and-bound method for binary knapsack or another compact problem

Then compare the implementations against mature libraries.

Formulate:

- Facility location
- Set covering
- Bin packing
- Capital budgeting
- Assignment
- A small scheduling problem

## Quarter Project

Use one logistics problem in multiple formulations:

1. A network-flow model for the continuous routing component
2. A facility-location MILP with fixed opening decisions
3. A CP-SAT or alternative discrete formulation for a scheduling or assignment extension

Compare:

- Model size
- Continuous-relaxation bound
- Runtime
- Optimality gap
- Ease of adding logical constraints
- Ease of explaining the model

## Mastery Check

You should be able to:

- Recognize when a problem is a standard network model.
- Explain how an LP relaxation supports branch-and-bound.
- Identify a weak Big-M formulation.
- Report both incumbent and bound for an unfinished MIP.
- Explain why CP-SAT may outperform MILP on some scheduling models.

---

# Q3 — Applied Probability, Markov Models, Queueing, and Stochastic Inventory

**Months:** 7–9

## Goals

- Model systems that evolve randomly through time.
- Analyze congestion and service capacity.
- Connect analytical queueing results with simulation.
- Formulate inventory decisions under uncertain demand.
- Recognize when stochastic assumptions are unrealistic.

## Month 1: Applied Probability and Markov Models

Review:

- Conditional probability
- Conditional expectation
- Poisson and exponential distributions
- Memorylessness
- Poisson processes
- Basic renewal ideas

### Discrete-time Markov chains

The Markov property is:

```math
\Pr\left(
X_{t+1}=j
\mid
X_t=i,X_{t-1},\ldots,X_0
\right)
=
\Pr\left(
X_{t+1}=j
\mid
X_t=i
\right).
```

Study:

- Transition matrices
- Communicating classes
- Irreducibility
- Periodicity
- Recurrence and transience
- Stationary distributions
- Absorbing chains
- Hitting times
- Markov reward models

A stationary distribution satisfies:

```math
\pi^\mathsf{T}P
=
\pi^\mathsf{T}
```

and:

```math
\sum_i \pi_i
=
1.
```

### Continuous-time Markov chains

Study:

- Generator matrices
- Holding times
- Transition rates
- Birth-death chains
- Stationary equations
- Uniformization at a conceptual level

## Month 2: Queueing

Study:

- Kendall notation
- Arrival and service processes
- Queue disciplines
- Utilization
- Little's law
- M/M/1
- M/M/c
- Finite-capacity queues
- Priority queues at an introductory level
- Queueing networks at an introductory level
- Model assumption failures

Little's law is:

```math
L
=
\lambda W.
```

For an M/M/1 queue:

```math
\rho
=
\frac{\lambda}{\mu}.
```

When:

```math
\rho < 1,
```

the expected time in the system is:

```math
W
=
\frac{1}{\mu-\lambda}.
```

Treat M/G/1 derivations and heavy-traffic limits as optional depth unless queueing is a specialization.

## Month 3: Stochastic Inventory

Focus on genuinely stochastic models:

- Newsvendor
- Safety stock
- Cycle-service and fill-rate concepts
- Base-stock policies
- Continuous-review policies
- Reorder points
- Lost sales and backorders
- Stochastic lead times
- Perishable inventory at an introductory level

The newsvendor critical fractile is:

```math
F(Q^*)
=
\frac{C_u}{C_u+C_o}.
```

The deterministic EOQ model may be reviewed briefly, but it should not dominate this quarter.

## Primary Resources

- [MIT 6.262 Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/)
- [MIT 6.262 video lectures](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/video_galleries/video-lectures/)
- [MIT 15.072J Queues: Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/)
- Hillier and Lieberman: queueing and inventory chapters

## Supplemental Resources

- **Open stochastic-process notes:** [MIT 6.262 course notes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/pages/course-notes/)
- **Queueing depth:** Kleinrock, *Queueing Systems, Volume I*
- **Alternative notes:** [Applied Stochastic Processes — Cornell](https://sidbanerjee.orie.cornell.edu/courses/orie6500/)
- **Inventory software and examples:** [stockpyl](https://github.com/LarrySnyder/stockpyl)
- **Optional depth:** Renewal theory, M/G/1, Jackson networks, and heavy-traffic approximation

## Implementation Resources

- [Ciw](https://ciw.readthedocs.io/)
- [SimPy](https://simpy.readthedocs.io/)
- [NumPy random sampling](https://numpy.org/doc/stable/reference/random/index.html)
- [SciPy statistical distributions](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Required Practice

- Compute stationary distributions.
- Compute hitting probabilities and expected hitting times.
- Analyze an M/M/1 and an M/M/c model.
- Verify Little's law numerically.
- Solve a newsvendor problem analytically and by simulation.
- Test the effect of non-Poisson arrivals or non-exponential service.

## Quarter Project

Choose one system, such as a call center, clinic, checkout system, repair facility, or inventory operation.

1. Build an analytical baseline.
2. Build a simulation of the same system.
3. Compare the analytical and simulated results.
4. Explain discrepancies.
5. Optimize one controllable parameter.
6. Stress-test the policy when assumptions fail.

## Mastery Check

You should be able to:

- Determine whether a stationary distribution exists in a finite example.
- Translate CTMC transition rates into balance equations.
- Apply Little's law correctly.
- Explain why utilization near one creates severe congestion.
- Distinguish safety stock from cycle stock.
- Identify when simulation is preferable to a closed-form queueing model.

---

# Q4 — Simulation, Experimental Design, and Introductory Metaheuristics

**Months:** 10–12

## Goals

- Conduct a complete and statistically defensible simulation study.
- Model systems that are too complex for convenient analytical treatment.
- Compare policies using controlled computational experiments.
- Gain a focused introduction to local search and metaheuristics.

## Core Simulation Topics

### Discrete-event simulation

- Entities
- Resources
- Events
- Processes
- State variables
- Event calendars
- Queues
- Routing logic
- Failures and repairs
- Time-varying arrivals
- Resource schedules

### Simulation-study design

- Conceptual modeling
- Scope and abstraction
- Verification
- Validation
- Input-distribution fitting
- Terminating versus steady-state systems
- Warm-up periods
- Independent replications
- Batch means
- Confidence intervals
- Common random numbers
- Antithetic variables
- Control variates
- Sensitivity analysis
- Experimental design
- Reproducibility

A Monte Carlo estimate of an expectation is:

```math
\widehat{\mu}_n
=
\frac{1}{n}
\sum_{i=1}^{n}g(X_i).
```

### Simulation optimization

- Ranking and selection
- Grid and factorial search
- Response surfaces
- Stochastic approximation
- Bayesian optimization at an introductory level
- Surrogate modeling
- Common random numbers in policy comparison

## Focused Metaheuristics Module

Spend approximately three to four weeks on:

- Greedy construction
- Neighborhood design
- Local search
- Multi-start methods
- Simulated annealing
- Tabu search
- Adaptive large neighborhood search
- Matheuristics at an introductory level

A simulated-annealing acceptance probability is:

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

Do not attempt to survey every nature-inspired algorithm. Neighborhood design, evaluation methodology, and comparison against credible baselines matter more.

## Primary Resources

- [Law, *Simulation Modeling and Analysis*](https://www.mheducation.com/highered/product/simulation-modeling-and-analysis-law.html)
- Hillier and Lieberman: simulation and metaheuristics chapters
- [SimPy documentation](https://simpy.readthedocs.io/)
- [Ciw documentation](https://ciw.readthedocs.io/)

## Supplemental Resources

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [Winter Simulation Conference archive](https://informs-sim.org/)
- [HSMA discrete-event simulation resources](https://github.com/hsma-programme)
- [ALNS](https://github.com/N-Wouda/ALNS)
- [PyVRP](https://github.com/PyVRP/PyVRP)
- [OR-Tools routing guide](https://developers.google.com/optimization/routing)

## Required Practice

- Write a small custom event loop before relying entirely on SimPy.
- Build terminating and steady-state simulations.
- Estimate confidence intervals across replications.
- Compare two policies with common random numbers.
- Implement at least two neighborhoods for a routing or scheduling problem.
- Compare a heuristic against exact solutions on small instances.

## Quarter Project

Build a complete simulation study of one system:

- Emergency-department triage
- Warehouse picking
- Manufacturing line
- Airport checkpoint
- Call center
- Repair and maintenance operation

The report should include:

- Conceptual model
- Input assumptions
- Verification tests
- Validation evidence
- Warm-up and replication choices
- Uncertainty intervals
- Policy comparison
- Operational recommendations
- Limitations

Add a small simulation-optimization or metaheuristic component if it improves the decision problem naturally.

## Mastery Check

You should be able to:

- Distinguish a model bug from stochastic variability.
- Justify a warm-up period and replication count.
- Report uncertainty rather than a single simulation mean.
- Explain why comparing heuristic runtimes without equal conditions is misleading.
- Design a useful neighborhood for a combinatorial problem.

---

# Year 2: Advanced Methods and Specialization

# Q5 — Nonlinear and Convex Optimization

**Months:** 13–15

## Goals

- Analyze smooth nonlinear optimization problems.
- Recognize convex structure.
- Derive first- and second-order conditions.
- Understand KKT conditions and duality.
- Build and diagnose convex optimization models.

## Core Topics

### Unconstrained optimization

- Gradient descent
- Steepest descent
- Newton's method
- Quasi-Newton methods
- BFGS and L-BFGS
- Line search
- Trust regions
- Convergence concepts
- Conditioning
- Automatic differentiation

A gradient step is:

```math
x_{k+1}
=
x_k
-
\alpha_k \nabla f(x_k).
```

Newton's method uses:

```math
x_{k+1}
=
x_k
-
\left[
\nabla^2 f(x_k)
\right]^{-1}
\nabla f(x_k).
```

### Constrained optimization

A general constrained problem is:

```math
\begin{aligned}
\mathrm{minimize}_{x} \quad
& f(x) \\
\text{subject to} \quad
& g_i(x) \le 0,
\qquad i=1,\ldots,m, \\
& h_j(x) = 0,
\qquad j=1,\ldots,p.
\end{aligned}
```

The Lagrangian is:

```math
\mathcal{L}(x,\lambda,\nu)
=
f(x)
+
\sum_{i=1}^{m}\lambda_i g_i(x)
+
\sum_{j=1}^{p}\nu_j h_j(x).
```

Study:

- Constraint qualifications
- KKT conditions
- Penalty methods
- Barrier methods
- Sequential quadratic programming
- Projected methods
- Proximal methods

### Convex optimization

Study:

- Convex sets
- Convex functions
- Epigraphs
- Cones
- Separating hyperplanes
- Subgradients
- Conjugate functions at an introductory level
- Slater's condition
- Lagrangian duality
- Interior-point methods
- Disciplined convex programming

A function is convex when:

```math
f\left(
\theta x+(1-\theta)y
\right)
\le
\theta f(x)
+
(1-\theta)f(y),
\qquad
0 \le \theta \le 1.
```

### Important model classes

- Quadratic programming
- Quadratically constrained programming
- Second-order cone programming
- Semidefinite programming
- Regularized regression
- Portfolio optimization
- Robust least squares

A convex quadratic program is:

```math
\begin{aligned}
\mathrm{minimize}_{x} \quad
& \frac{1}{2}x^\mathsf{T}Qx+c^\mathsf{T}x \\
\text{subject to} \quad
& Ax \le b,
\end{aligned}
```

where:

```math
Q \succeq 0.
```

## Primary Resources

- [Boyd and Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/)
- [Stanford EE364a lecture slides](https://web.stanford.edu/class/ee364a/lectures.html)
- [MIT 15.084J Nonlinear Programming](https://ocw.mit.edu/courses/15-084j-nonlinear-programming-spring-2004/)
- Hillier and Lieberman: nonlinear-programming chapter for a broad overview

## Supplemental Resources

- [Stanford Convex Optimization Short Course](https://web.stanford.edu/~boyd/papers/cvx_short_course.html)
- [MIT 6.252J Nonlinear Programming](https://ocw.mit.edu/courses/6-252j-nonlinear-programming-spring-2003/)
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [NEOS Guide: nonlinear optimization](https://neos-guide.org/guide/types/nonlin/)
- Nocedal and Wright, *Numerical Optimization*, as an optional numerical-methods reference

## Implementation Resources

- [CVXPY tutorial](https://www.cvxpy.org/tutorial/)
- [CVXPY examples](https://www.cvxpy.org/examples/)
- [SciPy optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [JAX automatic differentiation](https://docs.jax.dev/en/latest/automatic-differentiation.html)
- [Ipopt](https://github.com/coin-or/Ipopt)
- [OSQP](https://osqp.org/)

## Required Practice

- Implement gradient descent with line search.
- Implement Newton's method on a small unconstrained problem.
- Check gradients numerically.
- Derive KKT conditions for several models.
- Prove or disprove convexity for selected functions and feasible sets.
- Express models using disciplined convex programming.

## Quarter Project

Complete two projects:

### Method project

Implement and compare:

- Gradient descent
- Newton or quasi-Newton
- A library optimizer

Evaluate convergence, conditioning, and initialization sensitivity.

### Decision-model project

Choose one:

- Portfolio optimization
- Network utility maximization
- Resource allocation with diminishing returns
- Robust least squares
- Trajectory smoothing
- Convex relaxation of a discrete model

The report must explain why the formulation is convex or identify exactly which part is nonconvex.

## Mastery Check

You should be able to:

- Apply first- and second-order optimality conditions.
- Write and interpret KKT conditions.
- Recognize common convex functions and constraints.
- Distinguish local from global guarantees.
- Diagnose poor scaling and convergence.

---

# Q6 — Dynamic Programming and Markov Decision Processes

**Months:** 16–18

## Goals

- Model sequential decisions using states and policies.
- Derive Bellman recursions.
- Implement finite- and infinite-horizon algorithms.
- Evaluate policies through simulation.
- Understand the curse of dimensionality.

## Core Topics

### Dynamic programming

- Principle of optimality
- State design
- Actions
- Transitions
- Stage costs
- Terminal conditions
- Finite and infinite horizons
- Deterministic and stochastic transitions
- Optimal stopping
- Post-decision states

A finite-horizon Bellman recursion is:

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
S_t=s,A_t=a
\right]
\right\}.
```

### Markov decision processes

Study:

- Discounted reward and cost
- Average-cost models at an introductory level
- Policy evaluation
- Value iteration
- Policy iteration
- Modified policy iteration
- Linear programming formulations
- Convergence and stopping criteria

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
P(s' \mid s,a)V(s')
\right\}.
```

### Approximate methods

- State aggregation
- Value-function approximation
- Rollout
- Approximate policy iteration
- Simulation-based policy evaluation
- Reinforcement-learning connections
- POMDPs as optional depth

## Primary Resources

- [MIT 6.231 Dynamic Programming and Stochastic Control](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)
- Hillier and Lieberman: dynamic-programming chapter
- [Puterman, *Markov Decision Processes*](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887)

Use Puterman as a reference; it is not necessary to complete the entire book.

## Supplemental Resources

- [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)
- [Berkeley CS 285](https://rail.eecs.berkeley.edu/deeprlcourse/)
- [Underactuated Robotics](https://underactuated.mit.edu/)
- [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl)
- [pomdp-py](https://github.com/h2r/pomdp-py)

## Implementation Resources

- [MDPtoolbox](https://github.com/sawcordwell/pymdptoolbox)
- [scikit-decide](https://github.com/airbus/scikit-decide)
- [Gymnasium](https://gymnasium.farama.org/)
- NumPy for direct implementation of tabular methods

## Required Practice

- Solve finite-horizon recursion by hand.
- Implement value iteration.
- Implement policy iteration.
- Express a small discounted MDP as an LP.
- Evaluate policies by simulation.
- Construct a poor state representation and explain why it fails.
- Compare an optimal policy with a simple heuristic.

## Quarter Project

Choose one sequential decision problem:

- Inventory replenishment
- Equipment replacement
- Capacity expansion
- Dynamic pricing
- Maintenance
- Admission control
- Energy storage

Implement:

1. Finite-horizon backward induction
2. Infinite-horizon value or policy iteration when appropriate
3. Simulation-based policy evaluation
4. A simple heuristic baseline
5. Sensitivity to state discretization and discounting

## Mastery Check

You should be able to:

- Define a Markov state.
- Derive a Bellman equation from a problem statement.
- Explain value iteration and policy iteration.
- Recognize state-space explosion.
- Separate a model-based MDP from model-free reinforcement learning.

---

# Q7 — Stochastic Programming, Robust Optimization, and Data-Driven OR

**Months:** 19–21

## Goals

- Compare major approaches to optimization under uncertainty.
- Formulate two-stage stochastic and robust models.
- Evaluate policies out of sample.
- Understand the limitations of predict-then-optimize workflows.
- Connect machine learning outputs to operational decisions responsibly.

## Month 1: Stochastic Programming

A two-stage stochastic program is:

```math
\mathrm{minimize}_{x \in \mathcal{X}}
\left\{
c^\mathsf{T}x
+
\mathbb{E}_{\xi}
\left[
Q(x,\xi)
\right]
\right\},
```

where the recourse problem is:

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

Study:

- First-stage and recourse decisions
- Scenario generation
- Scenario trees
- Nonanticipativity
- Expected-value model
- Wait-and-see model
- Value of the stochastic solution
- Expected value of perfect information
- Sample average approximation
- Chance constraints
- Risk-averse objectives
- L-shaped decomposition at a conceptual level
- Progressive hedging at a conceptual level

A chance constraint is:

```math
\Pr
\left(
g(x,\xi)\le 0
\right)
\ge
1-\alpha.
```

## Month 2: Robust Optimization

A robust model is:

```math
\begin{aligned}
\mathrm{minimize}_{x} \quad
& f(x) \\
\text{subject to} \quad
& g(x,u) \le 0,
\qquad
\forall u \in \mathcal{U}.
\end{aligned}
```

Study:

- Box uncertainty
- Polyhedral uncertainty
- Ellipsoidal uncertainty
- Budgeted uncertainty
- Robust counterparts
- Price of robustness
- Adjustable robustness
- Affine decision rules
- Two-stage robust optimization
- Distributionally robust optimization at an introductory level

## Month 3: Data-Driven OR

Study:

- Forecast-then-optimize
- Out-of-sample policy evaluation
- Prescriptive analytics
- Contextual optimization
- Decision-focused learning
- Inverse optimization
- Differentiable optimization
- ML-guided combinatorial optimization as optional depth

A contextual decision model is:

```math
\mathrm{minimize}_{x \in \mathcal{X}}
\mathbb{E}
\left[
c(x,\xi)
\mid
Z=z
\right].
```

Important questions:

- Does better predictive accuracy improve decisions?
- Are uncertainty estimates calibrated?
- Is the evaluation performed on unseen data?
- Is a simple OR baseline included?
- Are operational constraints respected?
- How does the policy behave under distribution shift?

## Primary Resources

- [Birge and Louveaux, *Introduction to Stochastic Programming*](https://link.springer.com/book/10.1007/978-1-4614-0237-4)
- Selected robust-optimization material from [MIT 15.093J](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/)
- Boyd and Vandenberghe: uncertainty, duality, and robust convex examples where relevant
- [MIT teaching page for 15.095 Machine Learning Under a Modern Optimization Lens](https://dbertsim.mit.edu/teaching)

## Supplemental Resources

- Shapiro, Dentcheva, and Ruszczynski, *Lectures on Stochastic Programming*
- Ben-Tal, El Ghaoui, and Nemirovski, *Robust Optimization*
- Bertsimas and den Hertog, *Robust and Adaptive Optimization*
- [MOSEK Modeling Cookbook](https://docs.mosek.com/modeling-cookbook/)
- [Machine Learning for Combinatorial Optimization: A Methodological Tour d'Horizon](https://arxiv.org/abs/1811.06128)
- [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co)

## Implementation Resources

- [mpi-sppy](https://github.com/Pyomo/mpi-sppy)
- [StochasticPrograms.jl](https://github.com/martinbiel/StochasticPrograms.jl)
- [RSOME](https://xiongpengnus.github.io/rsome/)
- [cvxpylayers](https://github.com/cvxpy/cvxpylayers)
- [PyEPO](https://github.com/khalil-research/PyEPO)
- [Ecole](https://doc.ecole.ai/)

## Required Practice

- Build a two-stage stochastic LP.
- Compute expected-value and wait-and-see benchmarks.
- Implement sample average approximation.
- Formulate robust counterparts for simple uncertain constraints.
- Compare multiple uncertainty-set sizes.
- Build a forecast-then-optimize pipeline.
- Evaluate decisions on held-out scenarios rather than only training data.

## Quarter Project

Use one capacity, inventory, staffing, energy, or supply-chain problem.

Build four approaches:

1. Deterministic expected-value model
2. Scenario-based stochastic model
3. Robust model
4. Forecast-driven model

Evaluate every policy on a common set of unseen scenarios.

Compare:

- Mean cost
- Tail cost
- Constraint violations
- Service level
- Stability
- Computation time
- Interpretability

## Mastery Check

You should be able to:

- Distinguish here-and-now and recourse decisions.
- Explain nonanticipativity.
- Calculate the value of the stochastic solution in a small model.
- Construct and interpret a robust uncertainty set.
- Explain why training prediction error is not sufficient for evaluating a decision system.

---

# Q8 — Decision Analysis, Game Theory, Specialization, and Capstone

**Months:** 22–24

## Goals

- Add a decision-theoretic and strategic perspective.
- Complete one or two specialization modules.
- Finish and communicate a substantial capstone.
- Produce a coherent portfolio showing breadth and depth.

## 8.1 Decision Analysis

Study:

- Decision trees
- Influence diagrams
- Expected utility
- Risk attitudes
- Value of information
- Bayesian decision analysis
- Multi-criteria decision analysis
- Sensitivity analysis
- Stakeholder preferences

Expected utility is:

```math
\mathbb{E}
\left[
u(X)
\right]
=
\sum_x u(x)\Pr(X=x).
```

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

Resources:

- Hillier and Lieberman: decision-analysis chapter
- [MIT 15.053 decision-tree material](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/)
- [Stanford Decision Analysis resources](https://decision.stanford.edu/)
- Optional: Keeney and Raiffa, *Decisions with Multiple Objectives*

## 8.2 Game Theory

Study:

- Normal-form games
- Dominance
- Best responses
- Nash equilibrium
- Mixed strategies
- Extensive-form games
- Subgame perfection
- Bayesian games
- Repeated games
- Bargaining
- Matching
- Auctions
- Mechanism design

For a two-player zero-sum game with payoff matrix `A`, one player's mixed strategy can be found through:

```math
\begin{aligned}
\mathrm{maximize}_{p,v} \quad
& v \\
\text{subject to} \quad
& A^\mathsf{T}p \ge v\mathbf{1}, \\
& \mathbf{1}^\mathsf{T}p = 1, \\
& p \ge 0.
\end{aligned}
```

Resources:

- Hillier and Lieberman: game-theory chapter
- [Osborne and Rubinstein, *A Course in Game Theory*](https://sites.math.rutgers.edu/~zeilberg/EM20/OsborneRubinsteinMasterpiece.pdf)
- [Yale Open Courses: Game Theory](https://oyc.yale.edu/economics/econ-159)
- Use the game-theory video playlists in the broader resources README for additional lectures.

## 8.3 Specialization Options

Select one or two areas. Do not attempt all of them.

### Supply Chain and Logistics

Topics:

- Vehicle routing
- Network design
- Production planning
- Multi-echelon inventory
- Warehousing
- Humanitarian logistics

Resources:

- [MIT Center for Transportation and Logistics](https://ctl.mit.edu/)
- [PyVRP](https://github.com/PyVRP/PyVRP)
- [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/)
- [stockpyl](https://github.com/LarrySnyder/stockpyl)

### Revenue Management and Pricing

Topics:

- Capacity control
- Dynamic pricing
- Overbooking
- Network revenue management
- Assortment optimization

Resources:

- Talluri and van Ryzin, *The Theory and Practice of Revenue Management*
- [MIT OpenCourseWare revenue-management search](https://ocw.mit.edu/search/?q=revenue%20management)

### Energy Systems

Topics:

- Economic dispatch
- Unit commitment
- Optimal power flow
- Storage
- Renewable integration
- Capacity expansion

Resources:

- [PyPSA](https://pypsa.org/)
- [MATPOWER](https://matpower.org/)
- [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl)

### Healthcare Operations

Topics:

- Patient flow
- Appointment scheduling
- Operating-room planning
- Workforce capacity
- Bed management
- Emergency logistics

Resources:

- [HSMA Programme](https://github.com/hsma-programme)
- [INFORMS Health Applications Society](https://www.informs.org/Community/HAS)

### Manufacturing and Scheduling

Topics:

- Job shop
- Flow shop
- Lot sizing
- Maintenance
- Cutting and packing
- Production control

Resources:

- [OR-Tools scheduling](https://developers.google.com/optimization/scheduling)
- [PSPLIB](https://www.om-db.wi.tum.de/psplib/)
- [Taillard benchmark instances](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html)

### Technology Platforms and Market Design

Topics:

- Matching
- Auctions
- Ride-sharing
- Ad allocation
- Congestion
- Platform pricing
- Recommendation under constraints

Resources:

- Game theory and mechanism-design material
- Matching and assignment literature
- Network optimization and online optimization references

## 8.4 Capstone Requirements

The capstone should begin before Q8. Q8 is for final analysis, validation, and communication.

A strong capstone:

1. Starts from a messy real decision.
2. Identifies stakeholders and competing objectives.
3. Uses real or defensibly generated data.
4. Selects a modeling paradigm because it fits the decision.
5. Implements a reproducible model or simulator.
6. Includes credible baselines.
7. Performs scenario and sensitivity analysis.
8. Reports computational limitations.
9. Explains operational recommendations.
10. Documents risks, assumptions, and conditions for deployment.

Do not force every technique into one project. A well-justified LP or simulation can be stronger than an incoherent hybrid of MIP, machine learning, dynamic programming, and reinforcement learning.

## Capstone Outputs

- Problem statement
- Stakeholder and decision map
- Data dictionary
- Mathematical formulation or conceptual simulation model
- Reproducible code
- Automated tests
- Baseline comparisons
- Experiment log
- Sensitivity and scenario analysis
- Results visualizations
- Model card or audit report
- Final written report
- Presentation or recorded walkthrough
- Concise portfolio README

## Mastery Check

You should be able to:

- Explain when expected utility is appropriate.
- Formulate a zero-sum game as an LP.
- Identify strategic interactions ignored by a single-decision-maker model.
- Defend the capstone's modeling choices.
- Communicate what the model does not establish.

---

# Long-Running Capstone Timeline

Do not wait until the final quarter to start.

| Period | Milestone |
|---|---|
| Setup and Q1 | Identify domains and collect candidate problems |
| Q2 | Build a deterministic baseline |
| Q3 | Identify uncertainty and operational variability |
| Q4 | Add simulation or conduct a simulation-based validation |
| Q5 | Test convex, nonlinear, or relaxation-based alternatives where relevant |
| Q6 | Consider whether the problem is genuinely sequential |
| Q7 | Add stochastic, robust, or data-driven evaluation where appropriate |
| Q8 | Finalize validation, writeup, presentation, and repository |

A method should only be added when it improves the decision model.

---

# Quarterly Portfolio Requirements

At the end of every quarter, publish:

1. **One polished project**
2. **One mathematical derivation or proof-oriented assignment**
3. **One replication of a textbook or published result**
4. **One model-audit document**
5. **One retrospective**

The retrospective should answer:

- What can I now formulate that I could not formulate before?
- Which assumptions caused the most difficulty?
- What failed during implementation?
- Which result surprised me?
- What would I do differently on a larger instance?
- Which topic requires another pass?

---

# Weekly Working Pattern

A useful default allocation is:

- **Theory: 25–30%**
- **Exercises: 30–35%**
- **Implementation and experiments: 35–45%**

Every week should include:

- At least one formulation exercise
- At least one pencil-and-paper derivation
- At least one executable model, algorithm, or simulation experiment
- A short written interpretation of results

Every month should include:

- One closed-book review
- One model built from a prose description
- One code-cleanup and documentation session
- One comparison against a baseline
- One review of assumptions and limitations

At the end of each quarter, solve one synthesis problem combining several topics from that quarter.

---

# Model and Project Evaluation Rubric

Evaluate projects across the following dimensions.

| Dimension | Questions |
|---|---|
| Problem framing | Is the decision and stakeholder context clear? |
| Formulation | Are variables, objective, constraints, assumptions, and units correct? |
| Correctness | Has the implementation been verified on small cases? |
| Method choice | Does the selected method fit the structure of the problem? |
| Computational analysis | Are runtime, bounds, gaps, uncertainty, and versions reported? |
| Validation | Is there evidence that the model represents the intended system? |
| Baselines | Is the method compared with credible simple alternatives? |
| Sensitivity | Are important parameters and assumptions tested? |
| Communication | Are results and limitations understandable? |
| Reproducibility | Can another person run the project from the repository? |

---

# Computational Experiment Checklist

Record:

```text
project version
data source
instance name
model version
solver or algorithm
software versions
hardware
operating system
time limit
memory limit
number of threads
random seed
objective value
best bound
optimality gap
runtime
termination status
warnings
```

A common relative optimality-gap convention is:

```math
\mathrm{gap}
=
\frac{
\left|
z_{\text{primal}}-z_{\text{bound}}
\right|
}{
\max
\left\{
1,
\left|
z_{\text{primal}}
\right|
\right\}
}.
```

State the exact convention used by the solver or report.

---

# Final Curriculum Summary

| Quarter | Focus |
|---|---|
| Setup | Mathematics review, Python, Git, modeling tools, and reproducibility |
| Q1 | Modeling, LP, duality, sensitivity, and solver literacy |
| Q2 | Network flows, MIP, strong formulations, and CP-SAT |
| Q3 | Applied probability, Markov models, queueing, and stochastic inventory |
| Q4 | Simulation, experimental design, validation, and focused metaheuristics |
| Q5 | Nonlinear and convex optimization |
| Q6 | Dynamic programming and MDPs |
| Q7 | Stochastic programming, robust optimization, and data-driven OR |
| Q8 | Decision analysis, game theory, specialization, and capstone completion |

The intended progression is:

```text
modeling
→ deterministic optimization
→ discrete and network structure
→ stochastic systems
→ simulation
→ advanced continuous optimization
→ sequential decisions
→ optimization under uncertainty
→ specialization and synthesis
```

---

## Maintenance Notes

- Resource links should be checked periodically.
- Prefer official course, author, publisher, and software pages.
- Treat supplemental books as references unless a quarter explicitly identifies them as primary.
- Keep mathematical formalisms in display LaTeX blocks.
- Update software choices when a tool becomes unmaintained or substantially changes scope.
