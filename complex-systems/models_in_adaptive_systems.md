# Models Embedded in Adaptive Systems
## Prediction, Intervention, Feedback, Reflexivity, and Endogenous Change

## Purpose of this guide

This guide studies a specific class of adaptive-system problems:

> **Systems in which models, metrics, predictions, decision rules, or measurements become causal components of the system they are intended to describe.**

The central concern is not adaptive-system modeling in general. It is the narrower problem of **model endogeneity**: once a model is observed, deployed, optimized against, institutionalized, or used to allocate actions, the model can change the future system from which its own data are generated.

A useful summary is:

$$
\text{model} \rightarrow \text{decision or deployment}
\rightarrow \text{system response}
\rightarrow \text{new observations}
\rightarrow \text{model update}.
$$

The resulting system is neither an ordinary prediction problem nor a conventional open-loop intervention problem. It is a **closed adaptive loop** in which prediction, action, learning, institutions, and system evolution can become mutually endogenous.

This document has five goals:

1. provide a common conceptual and mathematical language for embedded-model problems;
2. organize the major intellectual traditions that have studied variants of the phenomenon;
3. explain the modeling methods appropriate to different response mechanisms;
4. develop a deployment-aware methodology for validation, experimentation, and governance; and
5. provide a structured learning curriculum that can support research on models embedded in complex adaptive systems.

The guide is intentionally interdisciplinary. Economics, sociology, machine learning, control, causal inference, system dynamics, evolutionary theory, game theory, and simulation often describe closely related feedback structures using different vocabularies. The goal is not to collapse them into one theory, but to make their differences and connections explicit.

---

# Table of Contents

- [Part I. Core Conceptual Framework](#part-i-core-conceptual-framework)
  - [1. The Embedded-Model Problem](#1-the-embedded-model-problem)
  - [2. A General Formal Architecture](#2-a-general-formal-architecture)
  - [3. What Exactly Enters the System?](#3-what-exactly-enters-the-system)
  - [4. Mechanisms of Adaptation](#4-mechanisms-of-adaptation)
  - [5. Time, State, Memory, and Path Dependence](#5-time-state-memory-and-path-dependence)
  - [6. Dynamical Regimes Created by Repeated Deployment](#6-dynamical-regimes-created-by-repeated-deployment)
  - [7. Four Distinctions That Prevent Conceptual Confusion](#7-four-distinctions-that-prevent-conceptual-confusion)
  - [8. What Can Be Made Stable?](#8-what-can-be-made-stable)
- [Part II. Major Intellectual Traditions](#part-ii-major-intellectual-traditions)
  - [9. Lucas Critique and Policy-Regime Dependence](#9-lucas-critique-and-policy-regime-dependence)
  - [10. Goodhart, Campbell, and Proxy Failure](#10-goodhart-campbell-and-proxy-failure)
  - [11. Self-Fulfilling Predictions and Reflexivity](#11-self-fulfilling-predictions-and-reflexivity)
  - [12. Performativity of Models and Institutions](#12-performativity-of-models-and-institutions)
  - [13. Policy Resistance and System Dynamics](#13-policy-resistance-and-system-dynamics)
  - [14. Evolutionary Response and Red-Queen Dynamics](#14-evolutionary-response-and-red-queen-dynamics)
  - [15. Strategic Classification and Adversarial Adaptation](#15-strategic-classification-and-adversarial-adaptation)
  - [16. Observation Reactivity and the Hawthorne Family](#16-observation-reactivity-and-the-hawthorne-family)
  - [17. Mechanism Design as a Constructive Response](#17-mechanism-design-as-a-constructive-response)
  - [18. Comparative Map of Traditions](#18-comparative-map-of-traditions)
- [Part III. Modeling and Analysis Toolkit](#part-iii-modeling-and-analysis-toolkit)
  - [19. Causal Inference, Intervention, and Invariance](#19-causal-inference-intervention-and-invariance)
  - [20. Performative Prediction](#20-performative-prediction)
  - [21. Concept Drift and Endogenous Distribution Shift](#21-concept-drift-and-endogenous-distribution-shift)
  - [22. Sequential Decision Models: MDPs, POMDPs, and Dynamic Policies](#22-sequential-decision-models-mdps-pomdps-and-dynamic-policies)
  - [23. Online Learning, Bandits, and Exploration](#23-online-learning-bandits-and-exploration)
  - [24. Adaptive Control, System Identification, and Dual Control](#24-adaptive-control-system-identification-and-dual-control)
  - [25. Agent-Based Modeling](#25-agent-based-modeling)
  - [26. Games, Learning, and Multi-Agent Adaptation](#26-games-learning-and-multi-agent-adaptation)
  - [27. Hybrid Modeling](#27-hybrid-modeling)
  - [28. Method-Selection Matrix](#28-method-selection-matrix)
- [Part IV. Data, Validation, and Deployment](#part-iv-data-validation-and-deployment)
  - [29. Endogenous Observation and Selective Labels](#29-endogenous-observation-and-selective-labels)
  - [30. Prediction Is Not Decision](#30-prediction-is-not-decision)
  - [31. A Deployment-Aware Validation Stack](#31-a-deployment-aware-validation-stack)
  - [32. Experimentation, Off-Policy Evaluation, and Prospective Testing](#32-experimentation-off-policy-evaluation-and-prospective-testing)
  - [33. Monitoring Adaptive Response](#33-monitoring-adaptive-response)
  - [34. Accuracy, Stability, Welfare, and System Value](#34-accuracy-stability-welfare-and-system-value)
  - [35. Governance of Embedded Models](#35-governance-of-embedded-models)
- [Part V. Recurring Case Studies](#part-v-recurring-case-studies)
  - [36. Credit and Lending](#36-credit-and-lending)
  - [37. Recommendation Platforms](#37-recommendation-platforms)
  - [38. Predictive Policing and Endogenous Measurement](#38-predictive-policing-and-endogenous-measurement)
  - [39. AI Agents and Model-Mediated Environments](#39-ai-agents-and-model-mediated-environments)
- [Part VI. Learning Curriculum](#part-vi-learning-curriculum)
  - [Module 1. The Embedded-Model Problem](#module-1-the-embedded-model-problem)
  - [Module 2. Reflexivity and Expectations](#module-2-reflexivity-and-expectations)
  - [Module 3. Metrics, Targets, and Strategic Response](#module-3-metrics-targets-and-strategic-response)
  - [Module 4. Feedback and Dynamics](#module-4-feedback-and-dynamics)
  - [Module 5. Models as Institutions](#module-5-models-as-institutions)
  - [Module 6. Causality and Invariance](#module-6-causality-and-invariance)
  - [Module 7. Sequential Decisions](#module-7-sequential-decisions)
  - [Module 8. Adaptive Control and Identification](#module-8-adaptive-control-and-identification)
  - [Module 9. Performative Prediction](#module-9-performative-prediction)
  - [Module 10. Strategic and Multi-Agent Systems](#module-10-strategic-and-multi-agent-systems)
  - [Module 11. Evolution and Coevolution](#module-11-evolution-and-coevolution)
  - [Module 12. Simulation and Hybrid Models](#module-12-simulation-and-hybrid-models)
  - [Module 13. Evaluation and Governance](#module-13-evaluation-and-governance)
  - [Module 14. Research Frontiers and Capstone](#module-14-research-frontiers-and-capstone)
- [Part VII. Research Questions and Frontier Directions](#part-vii-research-questions-and-frontier-directions)
- [References](#references)

---

# Part I. Core Conceptual Framework

## 1. The Embedded-Model Problem

The ordinary predictive-learning abstraction assumes that a model observes data generated by an external process:

$$
D \sim P,
$$

and learns a model:

$$
M = L(D).
$$

Deployment is then treated as if it were separate from the data-generating process.

The embedded-model problem begins when deployment changes what happens next. A prediction can alter expectations; a score can change eligibility; a metric can redirect effort; a ranking can reorganize organizations; an allocation rule can determine which labels become observable; a recommendation can reshape preferences; a defensive model can change an adversary's strategy; and a policy model can change the regime it was estimated under.

A minimal closed loop is therefore:

$$
M_t \rightarrow A_t \rightarrow S_{t+1} \rightarrow O_{t+1} \rightarrow M_{t+1}.
$$

The central methodological principle is:

> **A deployed model must be evaluated as part of the causal system it helps create, not only as a predictor evaluated against pre-deployment data.**

This principle appears in distinct forms in the Lucas Critique [R01](#r01), Goodhart and Campbell [R07](#r07) [R11](#r11), performativity [R25](#r25), system dynamics [R39](#r39), performative prediction [R29](#r29), strategic classification [R33](#r33), evolutionary adaptation [R43](#r43), and mechanism design [R53](#r53).

### What makes this a distinct problem class?

Three properties usually coexist:

1. **The model is actionable.** Someone or something uses it.
2. **The system can respond.** Actors, institutions, populations, or physical processes change after action.
3. **Future learning depends on the altered system.** The response affects later observations, labels, or states.

When those properties hold, the model is not merely describing the system. It is participating in it.

---

## 2. A General Formal Architecture

A useful generic representation separates latent state, observation, model, action, adaptation, and learning.

Let:

- `S_t` be the latent system state;
- `O_t` be observations available to the decision process;
- `M_t` be the model or model parameters;
- `A_t` be an action, allocation, prediction-mediated decision, or intervention;
- `H_t` be endogenous adaptation by people, organizations, adversaries, institutions, or populations;
- `U_t` be exogenous change not caused by the model;
- `D_{0:t}` be accumulated data;
- `L` be the model-update procedure.

The observation process can be written as:

$$
O_t = G(S_t, A_{0:t-1}, M_{0:t}, H_{0:t}).
$$

The model informs action:

$$
A_t = \pi(M_t, O_t).
$$

The system evolves:

$$
S_{t+1} = F(S_t, A_t, H_t, U_t).
$$

Agents or institutions may adapt according to:

$$
H_t = \mathcal{R}(M_t, A_t, S_t, I_t),
$$

where `I_t` represents information available to the adapting actors.

Finally, the model is updated:

$$
M_{t+1} = L(M_t, D_{0:t}).
$$

This architecture is intentionally broad. Different research traditions specialize different terms:

- Lucas focuses on how policy changes alter expectations and behavioral rules [R01](#r01).
- Goodhart and Campbell focus on how optimization and incentives change measured behavior [R07](#r07) [R11](#r11).
- performative prediction models the dependence of future data distributions on deployed models [R29](#r29);
- system dynamics emphasizes the internal feedback structure of `F` [R39](#r39);
- strategic classification formalizes adaptive choice inside `R` [R33](#r33);
- adaptive control treats action, identification, and state evolution jointly [R69](#r69);
- POMDPs treat decisions under hidden state and model-based belief updates [R67](#r67);
- evolutionary models interpret `H_t` as selection and population change [R43](#r43).

The value of the common architecture is not that every field becomes equivalent. It is that each field can be located by asking: **which arrows are endogenous, which response mechanisms are modeled, what state is remembered, and what objective is being optimized?**

---

## 3. What Exactly Enters the System?

The phrase “the model changes the system” hides important distinctions. Different artifacts enter through different causal channels.

| Embedded object | Example | Typical causal channel |
|---|---|---|
| Observation | participant knows they are observed | observation changes behavior |
| Measurement | hospital wait-time dashboard | attention and resource allocation shift |
| Metric | standardized test score | incentives target the proxy |
| Forecast | bank-run forecast | beliefs alter behavior |
| Classification | credit-risk score | eligibility and strategic feature changes |
| Ranking | university ranking | organizational resource reallocation |
| Recommendation | content recommender | exposure changes consumption and future data |
| Policy model | macroeconomic forecast | policy regime and expectations change |
| Decision rule | admissions threshold | population selection changes |
| Control policy | adaptive controller | control changes the plant and observations |
| Theory | option-pricing formula | market institutions adopt categories and practices |
| Mechanism | auction or matching rule | actors optimize within designed rules |
| Learning algorithm | repeated retraining | prior deployment changes subsequent training data |

This taxonomy matters because the appropriate model depends on the causal channel. A ranking that reallocates university resources is not adequately represented by the same mechanism as a physical controller, even if both create feedback.

### Information, rule, and infrastructure

A useful higher-level distinction, adapted from the performativity literature [R25](#r25) [R28](#r28), is that a model may enter a system:

1. **as information** — actors observe it and react;
2. **as a rule** — rewards, penalties, access, or allocations are tied to it;
3. **as infrastructure** — software, standards, contracts, accounting systems, or institutions instantiate it.

The deeper the model is embedded, the less plausible it becomes to treat deployment as an external post-processing step.

---

## 4. Mechanisms of Adaptation

Different embedded-model failures can look similar in data while arising from very different mechanisms. The learner should therefore identify *how* the system adapts before selecting a modeling method.

### 4.1 Cognitive adaptation

Actors revise beliefs, expectations, or interpretations.

Examples:
- inflation expectations after a policy announcement;
- investor expectations following a market forecast;
- users learning how a recommendation system behaves.

Relevant traditions: Lucas, rational expectations, self-fulfilling prophecy, Bayesian learning.

### 4.2 Strategic adaptation

Actors deliberately change behavior to improve outcomes under a known or inferred rule.

Examples:
- résumé keyword optimization;
- search-engine optimization;
- credit-feature manipulation;
- fraud evasion;
- tax avoidance.

Relevant methods: strategic classification, game theory, mechanism design, adversarial learning.

### 4.3 Behavioral adaptation

Actors change through heuristics, imitation, social learning, habits, or boundedly rational responses rather than explicit optimization.

This is often better modeled with agent-based models or behavioral rules than equilibrium-only models.

### 4.4 Organizational adaptation

Organizations redistribute resources, redesign processes, alter documentation practices, or create local workarounds around measured targets.

Campbell's Law, audit studies, and organizational performativity are especially relevant [R11](#r11) [R10](#r10).

### 4.5 Institutional adaptation

Rules, norms, market structures, categories, and governance arrangements change.

This is central to performativity: the model can alter the infrastructure within which future behavior occurs [R25](#r25) [R28](#r28).

### 4.6 Population adaptation

The composition of the population changes through sorting, entry, exit, migration, eligibility, attrition, or differential access.

A model may therefore change the data distribution even if no individual changes behavior.

### 4.7 Evolutionary adaptation

Interventions change selection pressures, causing traits or strategies to become more or less prevalent over generations [R43](#r43) [R46](#r46).

### 4.8 Physical and dynamical compensation

The system responds through stocks, flows, delays, congestion, inventories, resource constraints, and physical feedback without any actor explicitly “gaming” the model [R39](#r39).

### 4.9 Model-mediated adaptation

Repeated retraining, ranking, recommendation, filtering, or data acquisition itself changes the information environment. The learning system becomes part of the adaptation mechanism.

This mechanism is central to performative prediction [R29](#r29), recommendation feedback [R78](#r78), and modern agentic AI systems [R81](#r81).

---

## 5. Time, State, Memory, and Path Dependence

A central modeling choice is whether the system's response depends only on the current deployment or also on accumulated history.

### Memoryless response

$$
D_{t+1} = F(M_t).
$$

This abstraction can be useful for theoretical analysis, but it assumes that the same deployed model induces the same distribution regardless of history.

### Stateful response

$$
S_{t+1} = F(S_t, M_t).
$$

Brown, Hod, and Kalemaj extend performative prediction to this setting, where the population response depends on both the current classifier and the current population state [R31](#r31).

### Path-dependent response

$$
S_{t+1} = F(S_{0:t}, M_{0:t}).
$$

This matters when:

- trust accumulates or erodes;
- institutions develop around a metric;
- reputations persist;
- skills change slowly;
- market participants coordinate on conventions;
- populations sort over time;
- previous recommendations affect preferences;
- technical debt or model-induced infrastructure persists.

Arthur's work on increasing returns and path dependence is useful for understanding why early contingencies can become self-reinforcing [R23](#r23).

### Multiple timescales

A single deployment can trigger adaptation at different speeds:

- **seconds to hours:** clicks, routing, bids, fraud attempts;
- **days to months:** individual investment, workflow changes, hiring strategies;
- **months to years:** organizational redesign, market entry, regulatory adaptation;
- **years to generations:** institutional evolution, skill distributions, biological evolution.

A model can appear stable over one horizon while destabilizing the system over another. Validation must therefore specify the relevant timescale explicitly.

---

## 6. Dynamical Regimes Created by Repeated Deployment

“The model changes the system” does not tell us the direction or long-run structure of the change.

Repeated deployment can create:

### Stable equilibrium

The system converges toward a fixed configuration:

$$
S_{t+1} \rightarrow S^*.
$$

### Performative equilibrium or stability

A deployed model induces a data distribution under which retraining reproduces the same model [R29](#r29).

### Self-fulfilling dynamics

Belief or prediction causes behavior that makes the predicted outcome more likely.

### Self-defeating dynamics

Deployment causes actors to prevent or offset the prediction.

### Oscillation

Response and counter-response prevent convergence. Delays can intensify this behavior.

### Arms race or Red-Queen dynamics

Two or more adaptive populations continually improve relative to one another while no actor secures a lasting advantage [R43](#r43).

### Lock-in

Positive feedback and switching costs make an early configuration difficult to reverse [R23](#r23).

### Hysteresis

The system's state depends on the path by which parameters or policies reached their current values.

### Tipping or bifurcation

A small change in parameter or intervention can move the system into a qualitatively different regime.

### Persistent nonstationarity

The system never settles because exogenous drift and endogenous adaptation continue simultaneously.

This motivates a more powerful question than “does the model stay accurate?”:

> **What dynamical regime does repeated deployment create, and is that regime desirable, stable, and recoverable?**

---

## 7. Four Distinctions That Prevent Conceptual Confusion

### 7.1 Observation versus intervention

An observational relationship does not automatically characterize what happens when an action is taken.

A useful causal distinction is:

$$
P(Y \mid X=x)
\neq
P(Y \mid do(X=x))
$$

in general.

Many traditions in this guide can be interpreted as warnings against assuming observational relationships remain invariant after intervention, although they arrived at that problem through different conceptual routes.

### 7.2 Exogenous versus endogenous drift

**Exogenous drift** occurs when the environment changes independently of the model:

$$
D_{t+1}=F(D_t,U_t).
$$

**Endogenous drift** occurs when deployment contributes to the shift:

$$
D_{t+1}=F(D_t,M_t,A_t).
$$

**Mixed drift** contains both:

$$
D_{t+1}=F(D_t,M_t,A_t,U_t).
$$

Classical concept-drift work focuses mainly on changing streams [R66](#r66). Performative prediction focuses on endogenous shift [R29](#r29). Recent work on partially performative prediction explicitly combines endogenous model effects with external time variation [R32](#r32).

### 7.3 World shift versus observation shift versus label-selection shift

A model can change:

- the underlying state of the world;
- which parts of the world are observed;
- which labels become available;
- the measurement process itself.

Predictive-policing feedback offers a clean example of **observation shift**: increased patrol allocation can create more discovered crime in the very locations selected by the model, even when underlying rates do not justify the resulting concentration [R74](#r74).

Selective labels provide a clean example of **label-selection shift**: rejected loan applicants do not generate repayment outcomes, so the decision rule determines which labels exist [R73](#r73).

### 7.4 Prediction versus decision

Prediction aims to estimate quantities about outcomes. Decision problems ask which action should be taken.

A generic predictor solves something like:

$$
\hat{f} = \arg\min_f \mathbb{E}[\ell(f(X),Y)].
$$

A decision policy instead aims at:

$$
\pi^* = \arg\max_{\pi} \mathbb{E}[U(S,A) \mid A=\pi(O)].
$$

The best predictor need not induce the best decisions, especially when decisions affect which outcomes are observed or how the population evolves [R73](#r73).

---

## 8. What Can Be Made Stable?

No single notion of “stability” covers the entire field. Different traditions seek different kinds of invariance or robustness.

### Parameter invariance

Do estimated behavioral parameters remain valid after a policy regime changes? This is the Lucas concern [R01](#r01).

### Causal invariance

Does a structural relationship persist across interventions or environments? Invariant causal prediction makes this idea explicit [R72](#r72).

### Performative stability

Does retraining on the distribution induced by a deployed model reproduce that model [R29](#r29)?

### Equilibrium stability

If actors adapt repeatedly, does the system return to or approach a stable equilibrium?

### Robustness

Does performance remain acceptable under uncertainty, misspecification, or unmodeled responses?

### Incentive compatibility

Does following the intended strategy remain optimal for strategic participants [R53](#r53)?

### Low regret

Can the learner adapt over time without incurring large cumulative loss [R30](#r30)?

### Adaptive tracking

Can the model or controller follow a moving environment fast enough to remain useful?

### Resilience

Can the overall sociotechnical system continue delivering acceptable value when assumptions fail?

The broader methodological objective is therefore not simply invariance. It is to determine **what must remain stable, what is allowed to adapt, and what learning or governance process keeps the combined system within acceptable regimes**.

---
# Part II. Major Intellectual Traditions

## 9. Lucas Critique and Policy-Regime Dependence

### Core idea

The Lucas Critique is one of the clearest early statements of the embedded-model problem in policy analysis. Lucas argued that behavioral relationships estimated from historical data need not remain invariant after a policy rule changes because individuals alter behavior when their expectations about policy change [R01](#r01).

The mechanism is not merely “policy has side effects.” It is:

$$
\text{policy rule}
\rightarrow
\text{expectations}
\rightarrow
\text{behavioral rule}
\rightarrow
\text{aggregate relationship}.
$$

A model estimated under regime `rho_0` may therefore fail under regime `rho_1`:

$$
P_{\rho_0}(Y \mid X)
\not\approx
P_{\rho_1}(Y \mid X).
$$

Sargent and Wallace developed closely related rational-expectations consequences for policy analysis [R02](#r02) [R03](#r03). Kydland and Prescott showed how strategic anticipation creates time inconsistency: a plan optimal before private response can become undesirable after actors react [R04](#r04).

### What to learn from this tradition

- distinguish a policy variable from a policy **regime**;
- ask which behavioral relations are policy-dependent;
- represent expectations explicitly where they mediate response;
- distinguish reduced-form predictive relationships from structural mechanisms;
- treat credibility, anticipation, and commitment as endogenous system variables.

### Critiques and limits

Later work emphasizes that Lucas identifies a possible source of model failure, not a theorem that every reduced-form relationship changes under every intervention. Ericsson examines empirical testing of invariance [R05](#r05), while Hoover and Lawson broaden the methodological question of what social-scientific regularities can remain stable after intervention [R06](#r06).

### Modeling methods

Useful methods include structural econometrics, equilibrium models, games with expectations, causal models, and adaptive-agent simulations.

---

## 10. Goodhart, Campbell, and Proxy Failure

### Goodhart's Law

Goodhart's original monetary-policy observation concerned indicators whose empirical relationships weaken once authorities attempt to control them [R07](#r07). The general mechanism is:

$$
\text{proxy is predictive}
\rightarrow
\text{proxy becomes target}
\rightarrow
\text{behavior reorganizes around proxy}
\rightarrow
\text{proxy-goal relationship degrades}.
$$

Manheim and Garrabrant distinguish four useful forms [R08](#r08):

- **regressional Goodhart** — selection on noisy extremes;
- **extremal Goodhart** — optimization leaves the domain in which the proxy was reliable;
- **causal Goodhart** — intervention targets a correlate rather than the actual causal driver;
- **adversarial Goodhart** — agents strategically manipulate the proxy.

### Campbell's Law

Campbell places more emphasis on stakes, institutional pressure, and corruption of the activity being measured [R11](#r11). A high-stakes indicator changes both the evidence and the organization generating it.

Examples include teaching to standardized tests, hospital target gaming, crime statistics, organizational KPIs, and performance rankings [R12](#r12) [R13](#r13).

### Sociology of quantification

Strathern, Power, Espeland and Sauder, and Muller broaden the analysis from statistical proxy failure to institutional reorganization [R09](#r09) [R10](#r10) [R14](#r14). Rankings and audits can influence budgets, staffing, identities, admissions strategies, and the meaning of success itself.

### Modeling questions

For any metric, ask:

1. What latent objective is the metric intended to represent?
2. Who receives rewards or penalties based on it?
3. Which features of the metric are controllable?
4. Can actors improve the metric without improving the objective?
5. Can optimization move the system outside the metric's validation domain?
6. What secondary outcomes are crowded out?
7. How does the organization change when the metric becomes infrastructure?

---

## 11. Self-Fulfilling Predictions and Reflexivity

### Self-fulfilling prophecy

Merton's classic formulation describes an initially false definition of a situation that evokes behavior making the belief true [R15](#r15). The Thomas theorem provides an important precursor: situations defined as real can be real in their consequences [R16](#r16).

The basic feedback is:

$$
\text{belief}
\rightarrow
\text{behavior}
\rightarrow
\text{outcome}
\rightarrow
\text{confirmation of belief}.
$$

Diamond and Dybvig give a canonical formal example in bank runs, where expectations about others' withdrawals can select between stable and crisis equilibria [R18](#r18). Schelling's work on expectations, focal points, and coordination helps explain how shared beliefs can select among multiple equilibria [R17](#r17).

### Reflexive prediction

The philosophy-of-science literature on reflexive prediction asks what changes when publication of a forecast causally influences its truth value [R19](#r19). A forecast can be:

- self-fulfilling;
- self-defeating;
- partially self-canceling;
- amplifying;
- destabilizing.

### Soros and recursive reflexivity

Soros emphasizes an ongoing two-way relation between participants' fallible interpretations and the reality altered by their actions [R21](#r21). Unlike a one-shot self-fulfilling prophecy, reflexive feedback can remain recursive:

$$
B_t \rightarrow A_t \rightarrow S_{t+1} \rightarrow B_{t+1}.
$$

Arthur's work on increasing returns adds path dependence and lock-in to this family of phenomena [R23](#r23).

### Modeling methods

Multiple-equilibrium games, expectation models, system dynamics, agent-based models, and Bayesian learning are all useful depending on the mechanism.

---

## 12. Performativity of Models and Institutions

Performativity makes a stronger claim than “people react to forecasts.” Models, theories, categories, and calculative devices can become part of the infrastructure through which markets and organizations operate.

Callon's edited volume is foundational for this perspective [R25](#r25). Barnes provides an earlier account of social classifications becoming self-validating through collective use [R26](#r26).

MacKenzie and Millo's study of options markets is a canonical empirical analysis of a theory becoming materially embedded in market practice [R27](#r27). MacKenzie distinguishes cases where model use makes the world resemble the theory more closely from **counterperformativity**, where model use undermines the conditions supporting the model [R28](#r28).

This gives a richer causal sequence:

$$
\text{theory}
\rightarrow
\text{device or convention}
\rightarrow
\text{institutional practice}
\rightarrow
\text{market structure}
\rightarrow
\text{data resembling or contradicting theory}.
$$

### Distinctive contribution

Performativity is especially useful when the model does not merely inform individual choices but changes:

- categories;
- contracts;
- technical systems;
- accounting conventions;
- professional practices;
- market infrastructure;
- standards of evaluation.

It therefore occupies a different level of analysis from strategic classification or one-step performative prediction.

---

## 13. Policy Resistance and System Dynamics

System dynamics focuses on feedback, stocks, flows, accumulation, nonlinearities, and delays. Adaptive response need not be conscious or strategic.

Forrester's foundational work established the method [R36](#r36) [R37](#r37). His “Counterintuitive Behavior of Social Systems” emphasized that interventions often fail because decision-makers omit important feedback loops from their mental models [R38](#r38).

Sterman's formulation of **policy resistance** is particularly relevant [R39](#r39): interventions trigger compensating responses elsewhere in the system, weakening or reversing intended effects.

A generic feedback representation is:

$$
A_t \rightarrow S_{t+1} \rightarrow O_{t+1} \rightarrow A_{t+1}.
$$

With delay `tau`:

$$
A_t = \pi(O_{t-\tau}).
$$

Delayed feedback can create overshoot, oscillation, or instability even when actors are individually rational.

### Why it belongs in this guide

System dynamics generalizes the embedded-model problem beyond explicit strategic response. The modeler must ask whether “side effects” are actually endogenous consequences of a boundary that was drawn too narrowly.

### Modeling methods

- causal-loop diagrams;
- stock-and-flow models;
- nonlinear differential or difference equations;
- feedback dominance analysis;
- sensitivity analysis;
- policy simulation.

---

## 14. Evolutionary Response and Red-Queen Dynamics

Evolutionary analogues show that model invalidation does not require cognition or foresight.

An intervention changes selection pressures:

$$
\text{intervention}
\rightarrow
\text{differential fitness}
\rightarrow
\text{population composition}
\rightarrow
\text{new response distribution}.
$$

Van Valen's Red Queen hypothesis describes continuing adaptation generated by coevolving competitors [R43](#r43). Later work develops the role of antagonistic coevolution across hosts, parasites, predators, prey, and competitors [R45](#r45).

Human interventions can create rapid evolution through antibiotics, pesticides, harvesting, and other selection pressures [R46](#r46) [R47](#r47).

### Relation to embedded models

Lucas focuses on within-agent behavioral adaptation after a policy change. Evolutionary models focus on **population-level adaptation through selection**. In both cases, the response function estimated before intervention can cease to describe the post-intervention population.

### Modeling methods

- replicator dynamics;
- evolutionary games;
- population models;
- adaptive landscapes;
- agent-based evolutionary simulation.

---

## 15. Strategic Classification and Adversarial Adaptation

Strategic classification formalizes settings where people know that a classifier affects them and can change observable features at some cost [R33](#r33).

A stylized agent solves:

$$
x' = \arg\max_{z} \left[ u(h(z)) - c(x,z) \right],
$$

where `h` is the deployed classifier and `c(x,z)` is the cost of moving from original features `x` to reported or acquired features `z`.

The learner therefore faces a response map:

$$
D(h),
$$

rather than a fixed distribution.

Earlier adversarial-classification work in spam and security made a related point: the classifier changes the adversary's optimization problem [R34](#r34) [R48](#r48).

### Improvement versus gaming

A critical distinction is whether the response improves the underlying target or merely changes observables. Kleinberg and Raghavan study when classifiers induce socially valuable effort rather than cosmetic gaming [R35](#r35). Milli and colleagues show that robustness to strategic behavior does not by itself guarantee good social outcomes [R35a](#r35a).

### Cybersecurity

Security provides an extreme form of adaptive feedback. Attackers probe defenses, infer rules, and adapt strategies. Evaluation against a static historical distribution can therefore dramatically overstate deployed performance [R48](#r48) [R49](#r49) [R50](#r50).

---

## 16. Observation Reactivity and the Hawthorne Family

The Hawthorne-effect literature concerns behavior change caused by participation in research or awareness of observation.

The historical studies are associated with Roethlisberger and Dickson and Mayo [R51](#r51). Modern reassessment is important: the evidence does not support treating “the Hawthorne effect” as one universal mechanism. Systematic review recommends treating research-participation effects as a heterogeneous family [R52](#r52).

The relevant structure is:

$$
\text{measurement process}
\rightarrow
\text{awareness}
\rightarrow
\text{behavior}
\rightarrow
\text{measured outcome}.
$$

This is narrower than Goodhart or strategic classification because no explicit reward, target, or optimization rule is necessary.

### Why it matters methodologically

Observation itself can be an intervention. Embedded-model research should therefore ask whether data collection, transparency, explanation, auditing, or disclosure changes the behavior being measured.

---

## 17. Mechanism Design as a Constructive Response

Mechanism design reverses the perspective. Rather than complaining that agents adapt, it attempts to design rules while anticipating strategic response.

Hurwicz's work treats institutions as communication and decision systems constrained by decentralized information [R53](#r53). Gibbard and Satterthwaite establish fundamental limits on strategy-proof voting systems [R54](#r54). Myerson develops optimal auction design under private information [R55](#r55), and implementation theory asks when desired social outcomes can be realized as equilibria of designed games [R56](#r56).

The design problem is:

$$
\text{choose mechanism } \mathcal{M}
\quad \text{such that} \quad
\text{equilibrium response under } \mathcal{M}
\text{ has desirable properties}.
$$

### What mechanism design contributes

- explicit modeling of private information;
- strategic response as part of the design problem;
- incentive compatibility;
- equilibrium implementation;
- impossibility results showing trade-offs that no rule can avoid.

### Limits

Mechanism design solves an embedded-response problem only relative to its behavioral model. Real actors may learn differently, collude, form new institutions, change preferences, exploit unmodeled actions, or alter the surrounding game.

---

## 18. Comparative Map of Traditions

| Tradition | What enters the system? | Primary response mechanism | Characteristic failure or phenomenon | Useful modeling lens |
|---|---|---|---|---|
| Lucas Critique | policy regime | expectations and optimization | parameters change | structural/equilibrium modeling |
| Goodhart | metric target | proxy optimization | proxy detaches from objective | statistics + causal + incentives |
| Campbell | high-stakes indicator | gaming and organizational pressure | data/activity corruption | organizational/institutional analysis |
| Self-fulfilling prophecy | belief or forecast | coordination | prediction creates outcome | games / expectations |
| Reflexivity | participants' beliefs | recursive belief-reality feedback | boom, bust, path dependence | dynamic models |
| Performativity | theory or calculative device | institutional reconstruction | model remakes market/practice | sociotechnical analysis |
| Performative prediction | deployed predictor | decision-induced distribution shift | training distribution becomes obsolete | optimization / learning |
| Strategic classification | classifier | feature manipulation/investment | features change meaning | game theory |
| Policy resistance | intervention | feedback and compensation | policy weakened or reversed | system dynamics |
| Red Queen | adaptation by others | coevolution | no lasting relative advantage | evolutionary dynamics |
| Hawthorne family | observation | participant reactivity | observed behavior differs | experimental methodology |
| Mechanism design | institutional rule | equilibrium strategy | implementation succeeds/fails | game theory/design |
| Adaptive control | controller | physical/behavioral plant response | model and plant co-evolve | control + identification |
| Concept drift | changing environment | exogenous or mixed change | stale predictor | online learning |
| ABM | rule/policy/model | heterogeneous local adaptation | emergent macro behavior | simulation |

The comparative lesson is that “feedback” is not one mechanism. The response channel determines the appropriate formalism, data requirements, validation strategy, and intervention design.

---
# Part III. Modeling and Analysis Toolkit

## 19. Causal Inference, Intervention, and Invariance

Causal inference provides a formal language for separating prediction from intervention.

A predictive relationship may estimate:

$$
P(Y \mid X=x),
$$

while an intervention asks about:

$$
P(Y \mid do(X=x)).
$$

The two coincide only under assumptions about causal structure.

### Why causal structure matters for embedded models

If a model's action changes variables in the system, associations learned from observational data may no longer characterize the post-intervention environment. Causal models attempt to identify mechanisms that are more stable under intervention.

Invariant causal prediction explicitly exploits the idea that causal relationships should remain stable across suitable environments and interventions [R72](#r72).

### Key concepts to learn

- structural causal models;
- interventions and do-operators;
- confounding;
- mediation;
- transportability/generalization;
- interference;
- time-varying treatment;
- invariant prediction;
- policy learning.

### Important limitation

Causal invariance is not magical permanence. An intervention can alter mechanisms, agents can adapt, and institutions can change. A causal model is useful only relative to a sufficiently complete representation of the mechanisms that remain stable over the intervention range of interest.

### Policy learning

Athey and Wager show how estimated causal effects can be used to learn treatment-assignment policies under practical constraints [R71](#r71). This helps bridge the gap between estimating causal effects and selecting actions.

The conceptual progression is:

$$
\text{association}
\rightarrow
\text{causal effect}
\rightarrow
\text{policy value}
\rightarrow
\text{adaptive policy}.
$$

For embedded systems, the final step often requires modeling how repeated policy use changes the system itself.

---

## 20. Performative Prediction

Performative prediction is the clearest contemporary mathematical framework for a predictor whose deployment changes the future data distribution. Hardt and Mendler-Dünner provide a mature survey of the field, including the distinction between learning and steering and the related notion of performative power [R80](#r80). A 2026 comprehensive survey provides a complementary map of solution concepts, information assumptions about the distribution map, and connections to neighboring fields [R83](#r83).

Perdomo, Zrnic, Mendler-Dünner, and Hardt formalize a distribution map:

$$
\theta \mapsto D(\theta),
$$

where deploying model parameters `theta` induces a distribution `D(theta)` [R29](#r29).

The performative risk is therefore:

$$
PR(\theta)
=
\mathbb{E}_{Z \sim D(\theta)}[\ell(Z;\theta)].
$$

This differs from ordinary risk minimization because the distribution itself depends on the chosen model.

### Performative stability

A performatively stable point is one at which retraining on the distribution induced by the deployed model returns the same model. Conceptually:

$$
\theta^*
=
\arg\min_{\theta}
\mathbb{E}_{Z \sim D(\theta^*)}[\ell(Z;\theta)].
$$

Perdomo et al. distinguish this from performative optimality; a fixed point of retraining need not globally minimize performative risk [R29](#r29).

### Deployment frequency

Mendler-Dünner and colleagues analyze the difference between updating model parameters and actually redeploying the model. Redeployment triggers environmental response, creating a trade-off between frequent “greedy” deployment and less frequent “lazy” deployment [R30a](#r30a).

### Stateful performativity

Brown, Hod, and Kalemaj introduce a state-dependent response:

$$
D_{t+1}=F(D_t,\theta_t),
$$

allowing present response to depend on prior population state [R31](#r31).

This is crucial for accumulated resources, uneven adaptation speeds, institutional memory, and path dependence.

### Performative feedback and exploration

Jagadeesan, Zrnic, and Mendler-Dünner study learning when the distribution map is unknown and must be learned through deployment. The learner receives samples from the model-induced distribution, creating a richer feedback structure than ordinary bandit reward feedback [R30](#r30).

### Mixed endogenous and exogenous drift

Partially performative prediction extends the framework to environments that change both because of deployment and because the world is changing independently [R32](#r32):

$$
D_{t+1}=F(D_t,\theta_t,U_t).
$$

### Research questions to carry

- Is the response map known, learned, or partially identified?
- Is it memoryless or stateful?
- Is the goal stability, optimality, regret minimization, or social welfare?
- How often should deployment occur?
- What happens when several models interact?
- How much power does the model owner have to reshape the distribution?

---

## 21. Concept Drift and Endogenous Distribution Shift

Concept drift research studies changing predictive relationships in data streams. Gama and colleagues provide a major survey of detection, understanding, and adaptation methods [R66](#r66).

A useful generic representation is:

$$
P_t(X,Y) \neq P_{t+1}(X,Y).
$$

But embedded-model research requires decomposing why the shift occurred.

### Exogenous concept drift

Examples:
- seasonality;
- macroeconomic change;
- demographic shifts;
- technology changes unrelated to deployment.

### Endogenous distribution shift

Examples:
- model-driven eligibility changes applicant composition;
- ranking changes effort allocation;
- recommendation changes preferences;
- classifier changes adversarial strategy.

### Mixed drift

Real systems often contain both. This creates an identification problem:

> Which observed changes are caused by the model, and which would have happened anyway?

That question affects retraining policy. Blind retraining can track exogenous drift while amplifying endogenous feedback.

### Useful methods

- drift detection;
- sliding windows;
- online updating;
- change-point detection;
- domain adaptation;
- causal monitoring;
- counterfactual baselines;
- randomized holdouts;
- state-space models.

The important conceptual point is that **adaptation to drift is not the same as understanding its cause**.

---

## 22. Sequential Decision Models: MDPs, POMDPs, and Dynamic Policies

Many embedded-model problems are better represented as sequential decision problems than as repeated supervised prediction.

### Markov decision processes

An MDP represents states `S_t`, actions `A_t`, rewards `R_t`, and transition dynamics:

$$
P(S_{t+1} \mid S_t,A_t).
$$

A policy selects actions:

$$
A_t \sim \pi(\cdot \mid S_t).
$$

The objective is usually long-run expected value:

$$
\max_{\pi}
\mathbb{E}_{\pi}
\left[
\sum_{t=0}^{\infty}\gamma^t R_t
\right].
$$

This immediately captures something supervised learning often omits: **today's action changes tomorrow's state**.

### Partially observable MDPs

In many systems, the true state is not observable. A POMDP maintains a belief state over possible states and chooses actions under uncertainty. Krishnamurthy's modern treatment integrates POMDPs, Bayesian filtering, controlled sensing, reinforcement learning, and inverse reinforcement learning [R67](#r67).

This is especially relevant when:

- model deployment changes what becomes observable;
- latent user preferences must be inferred;
- state evolves while the model is learning;
- measurement itself is selective.

### Dynamic treatment regimes

Murphy's work on dynamic treatment regimes provides a causal-statistical analogue: decisions are tailored over time to evolving individual state [R68](#r68).

### Why this matters

A static model asks:

> What is likely to happen?

A sequential model asks:

> What action should I take now, given that it changes what happens and what I will know later?

That distinction is fundamental to embedded-model systems.

---

## 23. Online Learning, Bandits, and Exploration

When the learner does not know the environment's response to deployment, actions can serve both operational and informational purposes.

### Exploration-exploitation

The learner must trade off:

- **exploitation:** choose actions that appear best now;
- **exploration:** choose actions that reveal information useful for future decisions.

A bandit formulation chooses action `A_t` and observes a reward associated with that action. Performative-feedback settings are richer because deployment may reveal a sample from an entire induced distribution rather than only a scalar reward [R30](#r30).

### Why passive retraining can fail

If the current policy determines what data arrive, a purely exploitative learner can become trapped in a self-confirming region of the state space. It never observes outcomes that its own policy suppresses.

### Useful concepts

- contextual bandits;
- Thompson/posterior sampling;
- upper-confidence methods;
- regret;
- exploration under constraints;
- safe exploration;
- active data collection;
- performative feedback.

### Research question

> When should a deployed system deliberately take an action that is not currently estimated to be optimal because the action is valuable for learning the response function?

This question connects online learning directly to dual control.

---

## 24. Adaptive Control, System Identification, and Dual Control

Control engineering provides a mature constructive tradition for acting on systems while learning their dynamics.

### System identification

System identification estimates dynamic models from observed input-output behavior. Ljung's *System Identification: Theory for the User* is a foundational reference [R70](#r70).

A simplified model is:

$$
S_{t+1}=F_{\phi}(S_t,A_t)+W_t,
$$

where unknown parameters `phi` must be estimated from interaction.

### Adaptive control

Adaptive control updates controller parameters as the plant or environment is learned or changes.

The key conceptual shift is that the deployed controller and the identification process cannot always be separated.

### Dual control

Dual control makes this explicit. An action has two effects:

1. **control effect:** it moves the system toward an objective;
2. **information effect:** it generates observations that improve knowledge of the system.

Schematically:

$$
A_t
\rightarrow
\begin{cases}
S_{t+1} & \text{control},\\
I_{t+1} & \text{learning}.
\end{cases}
$$

Adaptive dual-control research studies precisely this joint problem [R69](#r69).

### Why this is a crucial complement to reflexivity

Much of the social-science literature treats intervention-induced change as a threat to validity. Control theory adds a constructive perspective:

> **Intervention can be designed not only to achieve an objective but also to make the system more learnable.**

This creates connections to active learning, experimental design, bandits, and adaptive policy.

### Limits in sociotechnical settings

Control methods often assume a reasonably specified state/action space and a stable objective. Human institutions may change goals, create new actions, resist control, or object to being treated as a plant. The control perspective is powerful, but its boundary assumptions must be explicit.

---

## 25. Agent-Based Modeling

Agent-based modeling is particularly useful when heterogeneous adaptive responses cannot plausibly be compressed into a single analytical response function.

Wilensky and Rand provide a hands-on introduction emphasizing natural, social, and engineered complex systems [R75](#r75).

### Why ABM fits embedded-model problems

An ABM can represent agents who:

- observe model outputs;
- differ in information and resources;
- learn at different rates;
- imitate others;
- game decision rules;
- enter or leave the population;
- form networks;
- coordinate;
- evolve strategies;
- change the environment that generates future data.

A generic loop is:

$$
M_t
\rightarrow
\text{agent perceptions}
\rightarrow
\text{heterogeneous actions}
\rightarrow
S_{t+1}
\rightarrow
D_{t+1}
\rightarrow
M_{t+1}.
$$

### Strengths

- heterogeneous agents;
- local interactions;
- bounded rationality;
- nonlinear macro emergence;
- institutional rules;
- explicit counterfactual simulation.

### Risks

ABMs can generate interesting behavior without strong empirical discipline. The modeler must justify:

- behavioral rules;
- parameter values;
- network structure;
- calibration targets;
- validation criteria;
- sensitivity to assumptions.

The ODD protocol provides a standardized structure for documenting agent-based and related simulation models, improving clarity, replication, and structural realism [R76](#r76).

---

## 26. Games, Learning, and Multi-Agent Adaptation

Embedded-model problems often involve several adaptive actors rather than one learner and one passive population.

Examples:

- attacker and defender;
- regulator and firms;
- platform, advertisers, creators, and users;
- competing recommendation systems;
- market makers and traders;
- multiple autonomous AI agents.

### Repeated games and learning in games

Fudenberg and Levine study equilibrium as the possible long-run result of learning processes rather than as a purely static rationality assumption [R77](#r77).

This is valuable because embedded systems often exhibit:

$$
\text{strategy}_t
\rightarrow
\text{others' responses}
\rightarrow
\text{belief update}
\rightarrow
\text{strategy}_{t+1}.
$$

### Evolutionary games

Replicator dynamics can model population shares of strategies:

$$
\dot{x}_i
=
x_i\left(f_i(x)-\bar{f}(x)\right).
$$

This is useful when successful strategies spread through selection or imitation rather than explicit rational optimization.

### Stackelberg structure

Strategic classification often has a leader-follower form: a decision-maker commits to a rule and agents respond. But many systems are more symmetric, with continual mutual adaptation.

### Multi-agent learning

As multiple learning systems interact, each learner's environment becomes nonstationary because other learners are updating too. This complicates convergence, evaluation, and accountability.

### Key questions

- Who moves first?
- What information is observable?
- Can agents infer the rule?
- Are responses myopic or forward-looking?
- Do coalitions form?
- Does learning converge to equilibrium?
- Are there multiple equilibria?
- Is the equilibrium socially desirable?

---

## 27. Hybrid Modeling

No single method is sufficient for many embedded sociotechnical systems.

Useful combinations include:

### Causal model + policy optimization

Estimate intervention effects, then optimize a policy subject to constraints.

### System dynamics + ABM

Use aggregate stocks and flows for infrastructure while representing strategic or heterogeneous human actors individually.

### ABM + machine learning

Simulate adaptive agents, deploy a learning model into the simulation, and study retraining feedback.

### POMDP + causal model

Represent partial observability and sequential action while distinguishing observational from interventional relationships.

### Game theory + performative prediction

Model the induced distribution as the result of strategic response rather than an opaque distribution map.

### Control + online learning

Use adaptive estimation while explicitly accounting for information gained through action.

### Network model + ABM

Represent adaptation through social, technical, or economic interaction networks.

The important principle is **model decomposition by mechanism**. Hybridization should not mean indiscriminately combining methods. Each component should correspond to a specific feedback channel or timescale.

---

## 28. Method-Selection Matrix

| Problem feature | Primary modeling approaches | Main question |
|---|---|---|
| policy changes expectations | structural economics, games, ABM | how do behavioral rules change under regime change? |
| target becomes proxy | Goodhart analysis, causal modeling, incentives | can metric improve while objective worsens? |
| actors manipulate features | strategic classification, Stackelberg games | what is the best response to the rule? |
| model changes future distribution | performative prediction | where does repeated deployment converge? |
| feedback and delays dominate | system dynamics | what loop structure creates observed behavior? |
| environment drifts independently | concept-drift methods, online learning | how quickly should the learner adapt? |
| state is hidden | POMDP/state estimation | what action is best under partial observability? |
| actions change future states | MDP/RL | what policy maximizes long-run value? |
| actions reveal information | dual control, bandits | how should control and learning be balanced? |
| heterogeneous agents adapt locally | ABM | what macro behavior emerges from local responses? |
| several adaptive actors interact | repeated/evolutionary games, multi-agent learning | does strategic learning converge? |
| intervention changes observation | causal sampling models, selective-label methods | what is missing because of prior decisions? |
| model becomes institutional infrastructure | performativity, sociotechnical analysis | how does the model reshape practices and categories? |
| adaptive adversary | adversarial ML, games, security models | how will defenses reshape attack strategy? |
| biological/population response | evolutionary dynamics | what traits or strategies are selected? |
| need incentive-compatible rules | mechanism design | what outcomes arise at equilibrium under designed rules? |

The matrix should be treated as a starting point. Most real systems occupy several rows simultaneously.

---
# Part IV. Data, Validation, and Deployment

## 29. Endogenous Observation and Selective Labels

An embedded model can change not only the world but also the process through which the world becomes observable.

Suppose the latent outcome is `Y`, but it is observed only when decision `A=1`:

$$
Y_{obs} = Y \cdot \mathbf{1}(A=1).
$$

If `A` depends on the model, the training labels are policy-dependent.

### Selective labels

Credit decisions provide a canonical example. If a loan is denied, whether that applicant would have repaid is never observed. Kilbertus and colleagues show that in such settings “learning to predict” can be inferior to directly learning decision policies [R73](#r73).

This creates a feedback loop:

$$
M_t
\rightarrow
A_t
\rightarrow
\text{which outcomes become observable}
\rightarrow
D_{t+1}
\rightarrow
M_{t+1}.
$$

### Predictive policing

Ensign and colleagues show how predictive policing can create runaway feedback when discovered incidents are generated partly by patrol allocation [R74](#r74).

The distinction is crucial:

$$
\text{observed incidents}
=
\text{underlying incidents}
+
\text{detection process induced by allocation}.
$$

A model can therefore appear to confirm itself because it directs observation toward places where it then discovers more evidence.

### Other examples

- medical models that determine who receives diagnostic tests;
- fraud models that determine which transactions are investigated;
- content filters that determine which examples moderators label;
- hiring models that determine who enters the workforce and generates performance data;
- recommendation systems that determine what users have an opportunity to consume.

### Modeling requirements

Embedded-model research should distinguish:

- latent state;
- exposure;
- measurement;
- label availability;
- censoring;
- missingness mechanism;
- policy that created the observation process.

Failing to model the observation mechanism can turn deployment feedback into apparent “ground truth.”

---

## 30. Prediction Is Not Decision

A highly accurate prediction can support a poor policy, and a less accurate predictor can support a better policy.

The distinction becomes especially important when actions alter future states or observations.

### Predictive objective

$$
\min_f
\mathbb{E}[\ell(f(X),Y)].
$$

### Decision objective

$$
\max_{\pi}
\mathbb{E}[U(Y,A,S')],
$$

where future state `S_next` may depend on the action.

### Why the objectives diverge

- prediction error may be concentrated on cases that do not affect decisions;
- action costs and benefits may be asymmetric;
- actions may change future outcomes;
- actions may create or remove future labels;
- the policy may alter the composition of the population;
- welfare depends on consequences not represented in the prediction target.

Kilbertus et al. make this point explicitly in selective-label settings [R73](#r73). Athey and Wager provide a causal policy-learning perspective [R71](#r71). Murphy's dynamic treatment regimes extend the issue to sequential decisions [R68](#r68).

### Practical implication

A deployment study should state separately:

1. **prediction target**;
2. **decision rule**;
3. **utility or objective**;
4. **state-transition assumptions**;
5. **long-run evaluation criteria**.

Conflating them hides the mechanism through which deployment changes the system.

---

## 31. A Deployment-Aware Validation Stack

Conventional machine-learning validation often follows:

$$
\text{train} \rightarrow \text{test} \rightarrow \text{deploy}.
$$

For embedded models, deployment itself can invalidate the test environment. A stronger validation process is:

$$
\text{train}
\rightarrow
\text{static test}
\rightarrow
\text{response model}
\rightarrow
\text{intervention test}
\rightarrow
\text{staged deployment}
\rightarrow
\text{dynamic monitoring}
\rightarrow
\text{update}.
$$

### 31.1 Static predictive validation

Ask:

- Does the model predict held-out data?
- Is calibration acceptable?
- How does performance vary across relevant subpopulations?

Necessary, but insufficient.

### 31.2 Causal/intervention validation

Ask:

- What actions will be taken because of the prediction?
- What causal pathways do those actions activate?
- Do observational associations survive the intervention?

### 31.3 Behavioral-response validation

Ask:

- Do agents know the rule?
- Can they infer it?
- What can they change?
- At what cost?
- Do they respond strategically, heuristically, socially, or not at all?

### 31.4 Dynamic validation

Ask:

- What happens after repeated deployment?
- Does the loop converge?
- Does it oscillate?
- Are there delays or hidden stocks?
- Does retraining amplify previous interventions?

### 31.5 Equilibrium validation

If a model reaches a stable state, ask:

- Is the equilibrium unique?
- Is it locally stable?
- Is it desirable?
- Is stability an artifact of suppressed participation or selection?

### 31.6 Welfare/system-value validation

Ask:

- Who benefits and who bears costs?
- Does the system improve the underlying objective or only its proxy?
- Are there externalities?
- What happens to nonparticipants?
- Does long-run performance differ from one-step performance?

### 31.7 Model-boundary validation

Sterman's systems perspective suggests a final question [R39](#r39):

> Are the apparent “side effects” actually endogenous consequences omitted from the model boundary?

---

## 32. Experimentation, Off-Policy Evaluation, and Prospective Testing

Embedded systems create a tension: the most informative way to learn the response to a policy may be to deploy it, but deployment itself has consequences.

### Randomized rollout

Randomization can identify causal effects of deployment when ethically and operationally feasible.

Useful designs include:

- individual randomized trials;
- cluster randomization;
- geographic rollout;
- stepped-wedge rollout;
- randomized thresholds;
- holdout populations.

### Shadow mode

Run the model without allowing it to affect decisions. This estimates static predictive behavior but **does not identify performative response**. Shadow mode is therefore useful but limited.

### Canary deployment

Expose a small fraction of the system to the model and monitor both direct performance and behavioral adaptation.

### Off-policy evaluation

When logged data include sufficient action variation and propensities, estimate the value of policies not actually deployed. This is central to contextual bandits, reinforcement learning, and causal policy evaluation.

### Deliberate exploration

When the existing policy suppresses informative data, constrained exploration may be necessary. But exploration has real costs and should be governed accordingly.

### Simulation before deployment

ABMs, system dynamics, games, or digital environments can be used to test response hypotheses before real-world rollout. Simulation should not be mistaken for empirical validation, but it can expose feedback mechanisms static evaluation misses.

### Natural experiments and regime changes

Policy changes, product launches, threshold changes, and institutional reforms can provide evidence about response functions when controlled experimentation is impossible.

---

## 33. Monitoring Adaptive Response

Monitoring should be designed around the feedback mechanism, not just conventional predictive metrics.

### Predictive monitoring

- accuracy;
- calibration;
- loss;
- subgroup performance.

### Distribution monitoring

- covariate shift;
- label shift;
- concept drift;
- population composition;
- missingness.

### Behavioral monitoring

- feature manipulation;
- strategic responses;
- changes in participation;
- investment behavior;
- avoidance or evasion;
- response lag.

### Observation-process monitoring

- who receives exposure;
- who receives testing;
- who generates labels;
- detection intensity;
- censoring changes.

### Institutional monitoring

- process changes;
- resource reallocation;
- new intermediaries;
- workarounds;
- policy changes;
- emergent standards.

### Dynamic monitoring

- convergence rate;
- oscillation;
- delayed deterioration;
- path dependence;
- regime shifts;
- recovery after model removal.

### Counterfactual monitoring

Maintain comparison groups or baselines where possible so that endogenous model effects can be distinguished from external drift.

A monitoring system that only asks “is accuracy falling?” is not sufficient for an embedded adaptive system.

---

## 34. Accuracy, Stability, Welfare, and System Value

One of the most important conceptual upgrades is to distinguish several objectives that are often conflated.

### Predictive accuracy

Does the model correctly predict outcomes under the observed distribution?

### Calibration

Do predicted probabilities correspond to realized frequencies?

### Performative stability

Does repeated retraining converge to a fixed point [R29](#r29)?

### Performative optimality

Does the model minimize loss under the distribution its own deployment creates?

### Decision quality

Do model-informed actions improve the operational objective?

### Equilibrium quality

Is the long-run stable configuration desirable?

### Social or system welfare

Do benefits exceed costs across stakeholders and time?

### Resilience

Does the system remain acceptable under unexpected adaptation or misspecification?

These objectives can conflict.

Liu and colleagues demonstrate that static fairness criteria can have delayed population effects that differ from their one-step intent [R79](#r79). Strategic-classification work similarly shows that manipulation-robust prediction does not automatically produce socially beneficial incentives [R35a](#r35a).

A stable model may stabilize a bad equilibrium. A highly accurate recommender may accurately predict preferences it helped manufacture. A robust classifier may impose costly behavioral burdens. A policy may improve its target while degrading unmeasured outcomes.

Therefore the evaluation hierarchy should often be:

1. predictive validity;
2. decision validity;
3. dynamic validity;
4. equilibrium quality;
5. long-run system value.

---

## 35. Governance of Embedded Models

Because deployment changes the object being modeled, governance must address both the model and the feedback loop.

### Governance questions

- Who has authority to deploy or modify the model?
- Who can observe the model or infer its rule?
- Who bears adaptation costs?
- Who benefits from gaming or strategic response?
- What outcomes are optimized and which are omitted?
- What evidence triggers retraining, rollback, or redesign?
- What feedback loops must be monitored?
- How can model-induced change be distinguished from exogenous change?
- What happens when the model is removed?

### Controls to consider

- staged deployment;
- randomized audit samples;
- protected exploration budgets;
- metric rotation or metric portfolios where appropriate;
- causal monitoring;
- independent outcome measurement;
- adversarial testing;
- model/version logs;
- explicit rollback criteria;
- delayed-impact reviews;
- stakeholder feedback;
- periodic re-examination of the objective itself.

### Transparency is not unconditionally beneficial

Transparency can improve accountability, but it can also change strategic response. Secrecy can reduce gaming while undermining legitimacy and due process. The appropriate degree of transparency is therefore itself part of the system design problem.

### Model retirement

Embedded models can leave institutional residue after removal. Workflows, categories, incentives, and accumulated data may continue to reflect earlier deployment. Governance should therefore include **decommissioning analysis**, not just launch and retraining.

---

# Part V. Recurring Case Studies

## 36. Credit and Lending

Credit provides an unusually rich recurring example because nearly every phenomenon in the guide appears in one system.

### Stage 1: ordinary prediction

Estimate:

$$
P(\text{default} \mid X).
$$

### Stage 2: decision rule

Approve loans when estimated value exceeds a threshold.

### Stage 3: selective labels

Only approved applicants generate repayment outcomes [R73](#r73).

### Stage 4: strategic adaptation

Applicants may change observable features that affect approval.

### Stage 5: productive investment versus gaming

Some feature changes may improve genuine creditworthiness; others may merely change the score [R35](#r35).

### Stage 6: population effects

Credit access can change wealth, employment, debt burden, and future creditworthiness.

### Stage 7: performativity

The model's decisions alter the population on which future versions are trained.

### Stage 8: sequential policy

Credit-line changes, collections, refinancing, and repeated borrowing make the problem dynamic.

### Stage 9: welfare and regulation

The objective must extend beyond default prediction to borrower welfare, lender risk, access, fairness, and system stability.

### Modeling exercise

Build progressively richer versions of the same credit system using:

1. supervised learning;
2. causal decision model;
3. strategic response model;
4. performative prediction;
5. MDP or POMDP;
6. ABM with heterogeneous borrowers.

Compare what each model can and cannot represent.

---

## 37. Recommendation Platforms

Recommendation systems are another canonical embedded-model environment.

The loop is:

$$
\text{recommendation}
\rightarrow
\text{exposure}
\rightarrow
\text{consumption}
\rightarrow
\text{observed preference}
\rightarrow
\text{next recommendation}.
$$

Schmit and Riquelme formally show that recommendations can affect the user data used for subsequent estimation, making naive estimators inconsistent [R78](#r78).

### Additional actors

A realistic platform contains more than users:

- users adapt consumption;
- creators adapt content to ranking incentives;
- advertisers adapt bids and targeting;
- the platform updates ranking models;
- moderators and regulators intervene;
- competitors alter outside options.

### Phenomena to study

- popularity feedback;
- preference shaping;
- creator optimization;
- content homogenization;
- filter effects;
- exploration versus exploitation;
- delayed welfare;
- ecosystem entry/exit;
- multi-agent strategic adaptation.

### Why this case is powerful

Recommendation demonstrates that a model can both **predict preferences and participate in producing the preferences it predicts**.

---

## 38. Predictive Policing and Endogenous Measurement

Predictive policing illustrates how allocation can change the evidence used to justify future allocation.

Suppose observed incidents in location `i` depend on both underlying incidence `C_i` and patrol effort `P_i`:

$$
O_i = g(C_i,P_i).
$$

A model then allocates patrol based on observed incidents:

$$
P_{i,t+1}=\pi(O_{i,t}).
$$

The closed loop becomes:

$$
P_{i,t}
\rightarrow
O_{i,t}
\rightarrow
P_{i,t+1}.
$$

Ensign et al. show how such feedback can produce runaway concentration in discovered crime [R74](#r74).

### Lessons

- observed data are not automatically passive measurements;
- allocation policies can determine the sampling process;
- feedback can amplify disparities in observation even without corresponding disparities in latent state;
- evaluation should distinguish reported incidents from incidents discovered through model-directed activity.

This case is broadly applicable to inspections, fraud detection, medical screening, compliance monitoring, and anomaly detection.

---

## 39. AI Agents and Model-Mediated Environments

Modern AI systems increasingly act rather than only predict. They call APIs, generate public content, modify software, interact with users, and sometimes interact with other models.

Pan and colleagues show that feedback loops involving language models can produce in-context reward hacking that static datasets fail to reveal [R81](#r81).

A generic agentic loop is:

$$
M_t
\rightarrow
A_t
\rightarrow
E_{t+1}
\rightarrow
C_{t+1}
\rightarrow
M_t\text{'s next action},
$$

where `E` is the external environment and `C` is the context observed by the model.

### New research issues

- model outputs become future training or context data;
- several agents change one another's environments;
- evaluation targets themselves may become optimization surfaces;
- static benchmark behavior may diverge from closed-loop behavior;
- model-generated content can alter human preferences and future data;
- tool use creates persistent environmental state;
- reward hacking can emerge only through repeated interaction.

### Why this belongs as an emerging frontier

The underlying problem is not new: action changes future evidence. What is new is the speed, scale, and autonomy with which model-mediated actions can feed back into subsequent inference and behavior.

---
# Part VI. Learning Curriculum

The curriculum is organized around capabilities rather than reading alone. Each module has an intellectual objective, a modeling exercise, a concrete artifact, and a mastery criterion.

A good pace is one module every one to two weeks, with additional time for Modules 7–12 if implementing models computationally.

---

## Module 1. The Embedded-Model Problem

### Learning objectives

By the end of this module, you should be able to:

- distinguish passive prediction from embedded deployment;
- draw the full model-action-response-data loop;
- identify the latent state, observation process, decision rule, adaptive response, and learning update;
- distinguish world change, observation change, and label-selection change;
- identify the timescale of relevant adaptation.

### Core readings

- Perdomo et al., “Performative Prediction” [R29](#r29).
- Sterman, “Learning from Evidence in a Complex World” [R39](#r39).
- Lucas, “Econometric Policy Evaluation: A Critique” [R01](#r01).

### Exercise

Choose one deployed model from a real system: credit scoring, recommendation, admissions, fraud, demand forecasting, staffing, predictive maintenance, or risk scoring.

Draw:

$$
S_t \rightarrow O_t \rightarrow M_t \rightarrow A_t \rightarrow H_t \rightarrow S_{t+1}.
$$

For every arrow, state the causal mechanism and the evidence that would be needed to estimate it.

### Artifact

A 2–4 page **embedded-model system map**.

### Mastery check

You can explain at least three distinct ways in which the model could become invalid after deployment without using the generic phrase “distribution shift.”

---

## Module 2. Reflexivity and Expectations

### Learning objectives

- understand policy-regime dependence;
- distinguish self-fulfilling from self-defeating prediction;
- understand multiple equilibria and expectation coordination;
- identify when beliefs themselves belong in the state model.

### Core readings

- Lucas [R01](#r01).
- Merton [R15](#r15).
- Schelling, selected chapters [R17](#r17).
- Diamond and Dybvig [R18](#r18).

### Selective/deeper readings

- Soros [R21](#r21).
- Arthur on path dependence [R23](#r23).
- Buck on reflexive predictions [R19](#r19).

### Exercise

Construct a simple two-equilibrium model in which a published risk prediction changes agent behavior and can select the realized equilibrium.

### Artifact

A formal or computational note explaining:

- what actors believe;
- what they observe;
- why the prediction changes behavior;
- the conditions under which the prediction becomes self-fulfilling or self-defeating.

### Mastery check

You can explain why the accuracy of a public forecast cannot always be assessed independently of its dissemination policy.

---

## Module 3. Metrics, Targets, and Strategic Response

### Learning objectives

- distinguish Goodhart mechanisms;
- understand Campbell's institutional corruption pressure;
- distinguish gaming from productive improvement;
- analyze proxy/objective divergence.

### Core readings

- Goodhart [R07](#r07).
- Manheim and Garrabrant [R08](#r08).
- Campbell [R11](#r11).
- Espeland and Sauder [R14](#r14).
- Hardt et al., strategic classification [R33](#r33).

### Exercise

Select a KPI used in a real organization. Define:

- latent objective `Y`;
- proxy `Z`;
- target rule;
- actor action set;
- manipulation cost;
- possible productive effort;
- possible harmful adaptation.

Then classify likely failure modes as regressional, extremal, causal, or adversarial Goodhart.

### Artifact

A **metric stress-test memo** with proposed alternative measurements or governance controls.

### Mastery check

You can identify a case where “better metric performance” and “better system performance” move in opposite directions and explain the mechanism.

---

## Module 4. Feedback and Dynamics

### Learning objectives

- understand reinforcing and balancing feedback;
- model delays and accumulations;
- recognize oscillation, overshoot, lock-in, and hysteresis;
- distinguish one-step response from long-run dynamics.

### Core readings

- Forrester [R38](#r38).
- Sterman, selected chapters from *Business Dynamics* [R40](#r40).
- Sterman [R39](#r39).

### Exercise

Build a small stock-and-flow or difference-equation model of one embedded system, such as:

- congestion prediction and routing;
- hospital target management;
- hiring and skill investment;
- recommendation and content production.

Introduce a delay and examine whether it changes stability.

### Artifact

A simulation notebook plus a one-page explanation of the dominant feedback loops.

### Mastery check

You can explain why an intervention with a positive immediate effect can produce a negative long-run effect without invoking strategic gaming.

---

## Module 5. Models as Institutions

### Learning objectives

- understand performativity beyond individual response;
- recognize models as standards, devices, categories, and infrastructure;
- distinguish performativity from performative prediction;
- analyze institutional path dependence.

### Core readings

- Callon [R25](#r25).
- MacKenzie and Millo [R27](#r27).
- MacKenzie, *An Engine, Not a Camera* [R28](#r28).

### Exercise

Choose a model or score that has become institutional infrastructure. Examples: credit ratings, option pricing, university rankings, ad auctions, risk scores, accounting rules.

Trace:

$$
\text{model}
\rightarrow
\text{device}
\rightarrow
\text{practice}
\rightarrow
\text{institution}
\rightarrow
\text{new empirical regularity}.
$$

### Artifact

A case analysis separating individual behavioral response from institutional reconstruction.

### Mastery check

You can explain why a model can become more empirically “accurate” because institutions reorganize around it.

---

## Module 6. Causality and Invariance

### Learning objectives

- distinguish observational from interventional queries;
- understand causal mechanisms and invariance;
- connect causal estimation to policy learning;
- identify where adaptation breaks causal transportability.

### Core readings

- Peters, Bühlmann, and Meinshausen [R72](#r72).
- Athey and Wager [R71](#r71).
- Lawson [R06](#r06) as a contrasting broader methodological interpretation.

### Exercise

For the recurring credit case, draw a structural causal model including:

- applicant characteristics;
- score;
- approval;
- interest rate;
- borrower investment/behavior;
- repayment;
- later training-data inclusion.

Identify which causal relationships might themselves change after deployment.

### Artifact

A causal diagram plus a written **invariance audit**.

### Mastery check

You can distinguish a stable causal relation from an assumption that a causal mechanism is stable over the intervention range.

---

## Module 7. Sequential Decisions

### Learning objectives

- formulate MDPs and POMDPs;
- understand belief state and partial observability;
- distinguish immediate predictive accuracy from long-run policy value;
- understand dynamic treatment regimes.

### Core readings

- Krishnamurthy, selected POMDP chapters [R67](#r67).
- Murphy [R68](#r68).
- Sutton and Barto, selected chapters [R82](#r82).

### Exercise

Convert a static risk-scoring problem into an MDP or POMDP:

- define state;
- observation;
- action;
- transition;
- reward;
- discount horizon;
- hidden variables.

### Artifact

A complete sequential-decision specification and a small value-iteration, policy-iteration, or simulation implementation.

### Mastery check

You can explain a case where the action with highest immediate expected value produces lower long-run value because it changes future state or information.

---

## Module 8. Adaptive Control and Identification

### Learning objectives

- understand system identification;
- understand adaptive control;
- understand the dual effect of action;
- connect control-theoretic learning to embedded-model feedback.

### Core readings

- Ljung, selected chapters [R70](#r70).
- adaptive dual-control overview [R69](#r69).

### Exercise

Simulate a system with an unknown parameter. Compare:

1. certainty-equivalent control using the current parameter estimate;
2. an exploratory policy that sacrifices short-run reward to identify the system better.

### Artifact

A notebook showing how informative interventions can improve future control.

### Mastery check

You can explain why intervention-induced data change is not always a nuisance: sometimes the intervention should be chosen partly for the information it creates.

---

## Module 9. Performative Prediction

### Learning objectives

- understand model-induced distribution maps;
- distinguish performative stability from performative optimality;
- understand repeated retraining;
- analyze stateful and partially performative environments;
- understand performative feedback and regret.

### Core readings

- Perdomo et al. [R29](#r29).
- Mendler-Dünner et al. [R30a](#r30a).
- Brown, Hod, and Kalemaj [R31](#r31).
- Jagadeesan, Zrnic, and Mendler-Dünner [R30](#r30).
- Hardt and Mendler-Dünner [R80](#r80).
- Kehrenberg et al. [R83](#r83).

### Current extension

- Lee and Zrnic on partially performative prediction [R32](#r32).

### Exercise

Implement a toy model with:

$$
D(\theta)=\mathcal{N}(a+b\theta,\sigma^2)
$$

or another simple induced-distribution map. Compare:

- empirical risk minimization;
- repeated retraining;
- direct performative-risk optimization if available;
- stateful response.

### Artifact

A short technical report showing where stability and optimality differ.

### Mastery check

You can explain why “retrain whenever performance drops” is not a complete strategy when retraining and redeployment themselves alter the distribution.

---

## Module 10. Strategic and Multi-Agent Systems

### Learning objectives

- model best responses to classifiers or rules;
- understand Stackelberg structure;
- understand learning in repeated games;
- recognize co-adaptation among multiple learning systems.

### Core readings

- Hardt et al. [R33](#r33).
- Fudenberg and Levine [R77](#r77).
- Hurwicz / mechanism-design foundations [R53](#r53).

### Selective readings

- Kleinberg and Raghavan [R35](#r35).
- adversarial learning sources [R48](#r48) [R49](#r49).

### Exercise

Create a two-player model in which a platform deploys a classification or ranking rule and agents choose costly responses. Then allow the platform to retrain.

### Artifact

An equilibrium analysis or simulation of repeated platform-agent adaptation.

### Mastery check

You can distinguish a one-shot best-response model from a learning process that may or may not converge to that equilibrium.

---

## Module 11. Evolution and Coevolution

### Learning objectives

- understand selection-driven adaptation;
- understand Red-Queen dynamics;
- model replicator dynamics;
- distinguish within-agent learning from population change.

### Core readings

- Van Valen [R43](#r43).
- Brockhurst et al. [R45](#r45).
- Palumbi [R46](#r46).

### Exercise

Construct a two-strategy replicator model in which an intervention changes relative fitness. Then make fitness frequency-dependent so that the intervention itself changes the evolutionary landscape.

### Artifact

A simulation and explanation of transient versus long-run intervention effects.

### Mastery check

You can explain how a model calibrated to individual response can fail even if no individual changes behavior, because the composition of the population changes.

---

## Module 12. Simulation and Hybrid Models

### Learning objectives

- know when ABM is appropriate;
- document simulation assumptions;
- combine complementary methods by mechanism;
- conduct sensitivity and robustness analysis.

### Core readings

- Wilensky and Rand [R75](#r75).
- Grimm et al., ODD protocol [R76](#r76).
- Sterman on model boundaries [R40a](#r40a).

### Exercise

Build an ABM of the recurring credit or recommendation case with heterogeneous agents who differ in:

- resources;
- response cost;
- information;
- adaptation speed.

Embed a predictive model and retraining loop.

### Artifact

- model code;
- ODD-style model description;
- experiment design;
- sensitivity analysis.

### Mastery check

You can identify which emergent findings are robust to behavioral assumptions and which depend on a narrow parameterization.

---

## Module 13. Evaluation and Governance

### Learning objectives

- design deployment-aware validation;
- distinguish static performance from dynamic impact;
- monitor endogenous observation;
- analyze long-run welfare;
- define governance triggers and rollback criteria.

### Core readings

- Ensign et al. [R74](#r74).
- Kilbertus et al. [R73](#r73).
- Liu et al. [R79](#r79).
- Schmit and Riquelme [R78](#r78).

### Exercise

Write an evaluation plan for a model before deployment. Include:

- static validation;
- causal hypotheses;
- response hypotheses;
- staged rollout;
- feedback metrics;
- observation-process metrics;
- long-run welfare metrics;
- model retirement conditions.

### Artifact

A **deployment and feedback governance plan**.

### Mastery check

You can explain what evidence would distinguish model-caused distribution shift from unrelated external drift.

---

## Module 14. Research Frontiers and Capstone

### Learning objectives

- integrate several traditions in one research problem;
- identify an unresolved modeling gap;
- design a research strategy that combines theory, simulation, and empirical evidence;
- evaluate both model behavior and system behavior.

### Frontier readings

- current performative-prediction extensions [R32](#r32).
- AI-agent feedback loops [R81](#r81).
- delayed-impact ML [R79](#r79).
- recommendation feedback [R78](#r78).

### Capstone requirement

Choose one real embedded-model system and analyze it using **at least three different modeling paradigms**.

Examples:

- credit: causal model + strategic classification + POMDP;
- recommendation: performative prediction + ABM + multi-agent game;
- fraud: adversarial learning + system dynamics + dual control;
- healthcare: dynamic treatment regime + causal inference + institutional Goodhart analysis;
- AI agent: control model + performative feedback + system-level safety analysis.

### Capstone deliverables

1. system boundary and causal-loop map;
2. taxonomy of adaptation mechanisms;
3. formal model;
4. empirical identification strategy;
5. simulation or computational experiment;
6. validation plan;
7. long-run welfare/system-value analysis;
8. discussion of model limits and unmodeled adaptation;
9. governance recommendations;
10. research questions for further work.

### Mastery check

You can explain why the three modeling paradigms produce different answers, which assumptions generate those differences, and which evidence would adjudicate between them.

---

# Part VII. Research Questions and Frontier Directions

The field remains fragmented partly because different disciplines isolate different arrows in the embedded-model loop. A productive research agenda asks how those arrows can be modeled jointly without creating models too complex to identify or validate.

## 1. Identifying the response map

Performative prediction often represents response abstractly as:

$$
\theta \mapsto D(\theta).
$$

A central empirical question is how to estimate this map safely and credibly.

Questions include:

- Can the response map be identified from historical regime changes?
- When is randomized deployment necessary?
- How should exploration be constrained?
- How can causal structure reduce the amount of experimentation required?

## 2. Stateful and path-dependent performativity

Many real systems remember earlier deployments.

Research questions:

- What state representation is sufficient?
- How should one detect hidden hysteresis?
- When does retraining produce convergence versus cycles?
- How do different adaptation timescales interact?

## 3. Endogenous observation

A particularly important frontier is jointly modeling latent outcomes and model-directed measurement.

Questions:

- How can latent incidence be estimated when observation is allocation-dependent?
- How should exploration be designed when labels are selectively observed?
- Can protected random sampling prevent self-confirming datasets?

## 4. Multiple adaptive populations

Most simple frameworks have one model and one responding population. Real ecosystems have many learning actors.

Questions:

- What happens when multiple models train on data generated by one another?
- Can multi-agent retraining converge?
- What equilibrium concepts are appropriate when models are continually updated?
- How does market structure affect performative power?

## 5. Prediction, persuasion, and preference formation

Recommendation and generative systems may not merely predict preferences; they may shape them.

Questions:

- When should preference change be treated as welfare improvement versus manipulation?
- Can a meaningful “pre-intervention preference” baseline be defined?
- How should evaluation work when preferences are endogenous to exposure?

## 6. Adaptive institutions

Performativity suggests that long-run model effects may be mediated by organizational and institutional change rather than direct individual response.

Questions:

- How can institutional state be represented computationally?
- Can ABM connect micro-response to organizational restructuring?
- How should model governance account for institutional lock-in?

## 7. Model retirement and reversibility

Embedded systems may not return to baseline after deployment stops.

Questions:

- Which effects are reversible?
- How can hysteresis be measured empirically?
- What transition policies are needed when retiring a model?

## 8. Dynamic welfare and fairness

Static decision criteria can create delayed effects [R79](#r79).

Questions:

- Which welfare objectives remain coherent when populations adapt?
- How should intertemporal trade-offs be represented?
- When does a fairness constraint improve or worsen long-run conditions?
- How should burdens of adaptation be included in evaluation?

## 9. AI agents in writable environments

Agentic AI systems create fast feedback between model output and persistent environment state [R81](#r81).

Questions:

- Which static evaluations fail under closed-loop interaction?
- How can tool-use environments be instrumented for causal feedback analysis?
- How do multiple AI agents co-adapt?
- Can reward hacking emerge through environmental modification rather than parameter updates?

## 10. A unifying research program

A mature research program on models embedded in adaptive systems would jointly ask:

1. **Representation:** What is the relevant latent state?
2. **Observation:** How is that state measured, and how does policy affect measurement?
3. **Prediction:** What is the model estimating?
4. **Decision:** What action does the model induce?
5. **Response:** Who or what adapts, by which mechanism?
6. **Dynamics:** What state persists across time?
7. **Learning:** How is the model updated from endogenous data?
8. **Evaluation:** What happens after repeated deployment?
9. **Welfare:** Is the resulting system desirable, not merely predictable?
10. **Governance:** Who can change the model, objective, deployment rule, or monitoring system?

The central modeling problem is therefore:

> **jointly model the model, the decisions it informs, the system's adaptive response, the observations generated by that response, and the learning process that updates the model.**

That is the narrow but deep territory this guide is intended to support.

---
# References

The references below include both the foundational literature from the original bibliography and the additional material used to extend the guide into a methods-oriented curriculum. Body citations link directly to these entries.

## Policy-regime dependence, metrics, and reflexivity

<a id="r01"></a>**[R01] Lucas, Robert E., Jr. (1976). “Econometric Policy Evaluation: A Critique.” _Carnegie-Rochester Conference Series on Public Policy_ 1: 19–46.**  
https://doi.org/10.1016/S0167-2231(76)80003-6

<a id="r02"></a>**[R02] Sargent, Thomas J., and Neil Wallace. (1975). “Rational Expectations, the Optimal Monetary Instrument, and the Optimal Money Supply Rule.” _Journal of Political Economy_ 83(2): 241–254.**  
https://www.jstor.org/stable/1830921

<a id="r03"></a>**[R03] Sargent, Thomas J., and Neil Wallace. (1976). “Rational Expectations and the Theory of Economic Policy.” _Journal of Monetary Economics_ 2(2): 169–183.**  
https://doi.org/10.1016/0304-3932(76)90032-5

<a id="r04"></a>**[R04] Kydland, Finn E., and Edward C. Prescott. (1977). “Rules Rather than Discretion: The Inconsistency of Optimal Plans.” _Journal of Political Economy_ 85(3): 473–491.**  
https://doi.org/10.1086/260580

<a id="r05"></a>**[R05] Ericsson, Neil R. (1995). “The Lucas Critique in Practice.” In _Testing Exogeneity_, edited by Neil R. Ericsson and John S. Irons. Oxford University Press.**  
https://global.oup.com/academic/product/testing-exogeneity-9780198774044

<a id="r06"></a>**[R06] Lawson, Tony. (1995). “The ‘Lucas Critique’: A Generalisation.” _Cambridge Journal of Economics_ 19(2): 257–276.**  
https://www.jstor.org/stable/23599580

<a id="r07"></a>**[R07] Goodhart, Charles A. E. (1975). “Problems of Monetary Management: The U.K. Experience.” In _Papers in Monetary Economics_, vol. 1. Reserve Bank of Australia.**  
https://www.rba.gov.au/publications/confs/1975/

<a id="r08"></a>**[R08] Manheim, David, and Scott Garrabrant. (2019). “Categorizing Variants of Goodhart’s Law.” _arXiv:1803.04585_.**  
https://arxiv.org/abs/1803.04585

<a id="r09"></a>**[R09] Strathern, Marilyn. (1997). “‘Improving Ratings’: Audit in the British University System.” _European Review_ 5(3): 305–321.**  
https://doi.org/10.1002/(SICI)1234-981X(199707)5:3%3C305::AID-EURO184%3E3.0.CO;2-4

<a id="r10"></a>**[R10] Power, Michael. (1997). _The Audit Society: Rituals of Verification_. Oxford University Press.**  
https://global.oup.com/academic/product/the-audit-society-9780198296034

<a id="r11"></a>**[R11] Campbell, Donald T. (1976/1979). _Assessing the Impact of Planned Social Change_. Reprinted in _Evaluation and Program Planning_ 2(1): 67–90.**  
https://doi.org/10.1016/0149-7189(79)90048-X

<a id="r12"></a>**[R12] Jacob, Brian A., and Steven D. Levitt. (2003). “Rotten Apples: An Investigation of the Prevalence and Predictors of Teacher Cheating.” _Quarterly Journal of Economics_ 118(3): 843–877.**  
https://doi.org/10.1162/00335530360698441

<a id="r13"></a>**[R13] Bevan, Gwyn, and Christopher Hood. (2006). “What’s Measured Is What Matters: Targets and Gaming in the English Public Health Care System.” _Public Administration_ 84(3): 517–538.**  
https://doi.org/10.1111/j.1467-9299.2006.00600.x

<a id="r14"></a>**[R14] Espeland, Wendy Nelson, and Michael Sauder. (2007). “Rankings and Reactivity: How Public Measures Recreate Social Worlds.” _American Journal of Sociology_ 113(1): 1–40.**  
https://doi.org/10.1086/517897

<a id="r15"></a>**[R15] Merton, Robert K. (1948). “The Self-Fulfilling Prophecy.” _Antioch Review_ 8(2): 193–210.**  
https://doi.org/10.2307/4609267

<a id="r16"></a>**[R16] Thomas, William I., and Dorothy Swaine Thomas. (1928). _The Child in America: Behavior Problems and Programs_. Knopf.**  
https://archive.org/details/childinamerica00thom

<a id="r17"></a>**[R17] Schelling, Thomas C. (1960). _The Strategy of Conflict_. Harvard University Press.**  
https://www.hup.harvard.edu/books/9780674840317

<a id="r18"></a>**[R18] Diamond, Douglas W., and Philip H. Dybvig. (1983). “Bank Runs, Deposit Insurance, and Liquidity.” _Journal of Political Economy_ 91(3): 401–419.**  
https://doi.org/10.1086/261155

<a id="r19"></a>**[R19] Buck, Roger C. (1963). “Reflexive Predictions.” _Philosophy of Science_ 30(4): 359–369.**  
https://doi.org/10.1086/287954

<a id="r20"></a>**[R20] Romanos, George D. (1973). “Reflexive Predictions.” _Philosophy of Science_ 40(1): 97–109.**  
https://www.jstor.org/stable/186492

<a id="r21"></a>**[R21] Soros, George. (1987). _The Alchemy of Finance_. Simon & Schuster.**  
https://www.simonandschuster.com/books/The-Alchemy-of-Finance/George-Soros/9780471445494

<a id="r22"></a>**[R22] Soros, George. (2013). “Fallibility, Reflexivity, and the Human Uncertainty Principle.” _Journal of Economic Methodology_ 20(4): 309–329.**  
https://doi.org/10.1080/1350178X.2013.859415

<a id="r23"></a>**[R23] Arthur, W. Brian. (1994). _Increasing Returns and Path Dependence in the Economy_. University of Michigan Press.**  
https://press.umich.edu/Books/I/Increasing-Returns-and-Path-Dependence-in-the-Economy

<a id="r24"></a>**[R24] Arthur, W. Brian. (2015). “Complexity and the Economy.” _Oxford Review of Economic Policy_ 31(2): 199–211.**  
https://doi.org/10.1093/oxrep/grv012

## Performativity and performative prediction

<a id="r25"></a>**[R25] Callon, Michel, ed. (1998). _The Laws of the Markets_. Blackwell.**  
https://www.wiley.com/en-us/The+Laws+of+the+Markets-p-9780631206088

<a id="r26"></a>**[R26] Barnes, Barry. (1983). “Social Life as Bootstrapped Induction.” _Sociology_ 17(4): 524–545.**  
https://doi.org/10.1177/0038038583017004004

<a id="r27"></a>**[R27] MacKenzie, Donald, and Yuval Millo. (2003). “Constructing a Market, Performing Theory: The Historical Sociology of a Financial Derivatives Exchange.” _American Journal of Sociology_ 109(1): 107–145.**  
https://doi.org/10.1086/374404

<a id="r28"></a>**[R28] MacKenzie, Donald. (2006). _An Engine, Not a Camera: How Financial Models Shape Markets_. MIT Press.**  
https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/

<a id="r29"></a>**[R29] Perdomo, Juan C., Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. (2020). “Performative Prediction.” _ICML_, PMLR 119:7599–7609.**  
https://proceedings.mlr.press/v119/perdomo20a.html

<a id="r30"></a>**[R30] Jagadeesan, Meena, Tijana Zrnic, and Celestine Mendler-Dünner. (2022). “Regret Minimization with Performative Feedback.” _ICML_, PMLR 162:9760–9785.**  
https://proceedings.mlr.press/v162/jagadeesan22a.html

<a id="r30a"></a>**[R30a] Mendler-Dünner, Celestine, Juan C. Perdomo, Tijana Zrnic, and Moritz Hardt. (2020). “Stochastic Optimization for Performative Prediction.” _NeurIPS 33_.**  
https://proceedings.neurips.cc/paper/2020/hash/33e75ff09dd601bbe69f351039152189-Abstract.html

<a id="r31"></a>**[R31] Brown, Gavin, Shlomi Hod, and Iden Kalemaj. (2022). “Performative Prediction in a Stateful World.” _AISTATS_, PMLR 151:6045–6061.**  
https://proceedings.mlr.press/v151/brown22a.html

<a id="r32"></a>**[R32] Lee, Jaewook, and Tijana Zrnic. (2026). “Partially Performative Prediction.” _arXiv:2606.07890_.**  
https://arxiv.org/abs/2606.07890

<a id="r80"></a>**[R80] Hardt, Moritz, and Celestine Mendler-Dünner. (2025). “Performative Prediction: Past and Future.” _Statistical Science_ 40(3): 417–436.**  
https://doi.org/10.1214/25-STS986

<a id="r83"></a>**[R83] Kehrenberg, Thomas, Javier Sanguino, Jose A. Lozano, and Novi Quadrianto. (2026). “Dissecting Performative Prediction: A Comprehensive Survey.” _ACM Computing Surveys_ 58(13), Article 331.**  
https://doi.org/10.1145/3816429

## Strategic classification, adversarial response, and mechanism design

<a id="r33"></a>**[R33] Hardt, Moritz, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. (2016). “Strategic Classification.” _ITCS 2016_: 111–122.**  
https://doi.org/10.1145/2840728.2840730

<a id="r34"></a>**[R34] Dalvi, Nilesh, Pedro Domingos, Sumit Sanghai, and Deepak Verma. (2004). “Adversarial Classification.” _KDD 2004_: 99–108.**  
https://doi.org/10.1145/1014052.1014066

<a id="r35"></a>**[R35] Kleinberg, Jon, and Manish Raghavan. (2020). “How Do Classifiers Induce Agents to Invest Effort Strategically?” _ACM Transactions on Economics and Computation_ 8(4).**  
https://doi.org/10.1145/3417742

<a id="r35a"></a>**[R35a] Milli, Smitha, John Miller, Anca D. Dragan, and Moritz Hardt. (2019). “The Social Cost of Strategic Classification.” _FAT* 2019_.**  
https://doi.org/10.1145/3287560.3287576

<a id="r48"></a>**[R48] Lowd, Daniel, and Christopher Meek. (2005). “Adversarial Learning.” _KDD 2005_: 641–647.**  
https://doi.org/10.1145/1081870.1081950

<a id="r49"></a>**[R49] Barreno, Marco, Blaine Nelson, Russell Sears, Anthony D. Joseph, and J. D. Tygar. (2006). “Can Machine Learning Be Secure?” _ASIACCS 2006_.**  
https://doi.org/10.1145/1128817.1128824

<a id="r50"></a>**[R50] Biggio, Battista, and Fabio Roli. (2018). “Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning.” _Pattern Recognition_ 84: 317–331.**  
https://doi.org/10.1016/j.patcog.2018.07.023

<a id="r53"></a>**[R53] Hurwicz, Leonid. (1960). “Optimality and Informational Efficiency in Resource Allocation Processes.” In _Mathematical Methods in the Social Sciences_. Stanford University Press.**  
https://www.nobelprize.org/prizes/economic-sciences/2007/hurwicz/lecture/

<a id="r54"></a>**[R54] Gibbard, Allan. (1973). “Manipulation of Voting Schemes: A General Result.” _Econometrica_ 41(4): 587–601; and Satterthwaite, Mark A. (1975). “Strategy-Proofness and Arrow’s Conditions.” _Journal of Economic Theory_ 10(2): 187–217.**  
https://doi.org/10.2307/1914083  
https://doi.org/10.1016/0022-0531(75)90050-2

<a id="r55"></a>**[R55] Myerson, Roger B. (1981). “Optimal Auction Design.” _Mathematics of Operations Research_ 6(1): 58–73.**  
https://doi.org/10.1287/moor.6.1.58

<a id="r56"></a>**[R56] Maskin, Eric. (1999). “Nash Equilibrium and Welfare Optimality.” _Review of Economic Studies_ 66(1): 23–38.**  
https://doi.org/10.1111/1467-937X.00076

## System dynamics and evolutionary response

<a id="r36"></a>**[R36] Forrester, Jay W. (1961). _Industrial Dynamics_. MIT Press.**  
https://archive.org/details/industrialdynami0000forr

<a id="r37"></a>**[R37] Forrester, Jay W. (1969). _Urban Dynamics_. MIT Press.**  
https://archive.org/details/urbandynamics0000forr

<a id="r38"></a>**[R38] Forrester, Jay W. (1971). “Counterintuitive Behavior of Social Systems.” _Theory and Decision_ 2: 109–140.**  
https://doi.org/10.1007/BF00148991

<a id="r39"></a>**[R39] Sterman, John D. (2006). “Learning from Evidence in a Complex World.” _American Journal of Public Health_ 96(3): 505–514.**  
https://doi.org/10.2105/AJPH.2005.066043

<a id="r40"></a>**[R40] Sterman, John D. (2000). _Business Dynamics: Systems Thinking and Modeling for a Complex World_. Irwin/McGraw-Hill.**  
https://mitmgmtfaculty.mit.edu/jsterman/business-dynamics/

<a id="r40a"></a>**[R40a] Sterman, John D. (2002). “All Models Are Wrong: Reflections on Becoming a Systems Scientist.” _System Dynamics Review_ 18(4): 501–531.**  
https://doi.org/10.1002/sdr.261

<a id="r43"></a>**[R43] Van Valen, Leigh. (1973). “A New Evolutionary Law.” _Evolutionary Theory_ 1: 1–30.**  
https://ebme.marine.rutgers.edu/HistoryEarthSystems/HistEarthSystems_Fall2008/VanValen%201973%20Evol%20Theory.pdf

<a id="r44"></a>**[R44] Bell, Graham. (1982). _The Masterpiece of Nature: The Evolution and Genetics of Sexuality_. University of California Press.**

<a id="r45"></a>**[R45] Brockhurst, Michael A., et al. (2014). “Running with the Red Queen: The Role of Biotic Conflicts in Evolution.” _Proceedings of the Royal Society B_ 281.**  
https://doi.org/10.1098/rspb.2014.1382

<a id="r46"></a>**[R46] Palumbi, Stephen R. (2001). _The Evolution Explosion: How Humans Cause Rapid Evolutionary Change_. W. W. Norton.**  
https://wwnorton.com/books/9780393323382

<a id="r47"></a>**[R47] Hendry, Andrew P., Kiyoko M. Gotanda, and Erik I. Svensson. (2017). “Human Influences on Evolution, and the Ecological and Societal Consequences.” _Philosophical Transactions of the Royal Society B_ 372.**  
https://doi.org/10.1098/rstb.2016.0028

## Observation reactivity

<a id="r51"></a>**[R51] Roethlisberger, F. J., and William J. Dickson. (1939). _Management and the Worker_. Harvard University Press.**  
https://archive.org/details/managementworker00roet

<a id="r52"></a>**[R52] McCambridge, Jim, John Witton, and Diana R. Elbourne. (2014). “Systematic Review of the Hawthorne Effect: New Concepts Are Needed to Study Research Participation Effects.” _Journal of Clinical Epidemiology_ 67(3): 267–277.**  
https://doi.org/10.1016/j.jclinepi.2013.08.015

## Causality, sequential decisions, control, and online learning

<a id="r66"></a>**[R66] Gama, João, Indrė Žliobaitė, Albert Bifet, Mykola Pechenizkiy, and Abdelhamid Bouchachia. (2014). “A Survey on Concept Drift Adaptation.” _ACM Computing Surveys_ 46(4), Article 44.**  
https://doi.org/10.1145/2523813

<a id="r67"></a>**[R67] Krishnamurthy, Vikram. (2025). _Partially Observed Markov Decision Processes: Filtering, Learning and Controlled Sensing_, 2nd ed. Cambridge University Press.**  
https://doi.org/10.1017/9781009449441

<a id="r68"></a>**[R68] Murphy, Susan A. (2003). “Optimal Dynamic Treatment Regimes.” _Journal of the Royal Statistical Society: Series B_ 65(2): 331–355.**  
https://doi.org/10.1111/1467-9868.00389

<a id="r69"></a>**[R69] Wittenmark, Björn. (1995). “Adaptive Dual Control Methods: An Overview.” _IFAC Proceedings Volumes_ 28(13): 67–72.**  
https://doi.org/10.1016/S1474-6670(17)45327-4

<a id="r70"></a>**[R70] Ljung, Lennart. (1999). _System Identification: Theory for the User_, 2nd ed. Prentice Hall.**  
https://www.control.isy.liu.se/books/sysid/

<a id="r71"></a>**[R71] Athey, Susan, and Stefan Wager. (2021). “Policy Learning with Observational Data.” _Econometrica_ 89(1): 133–161.**  
https://doi.org/10.3982/ECTA15732

<a id="r72"></a>**[R72] Peters, Jonas, Peter Bühlmann, and Nicolai Meinshausen. (2016). “Causal Inference by Using Invariant Prediction: Identification and Confidence Intervals.” _Journal of the Royal Statistical Society: Series B_ 78(5): 947–1012.**  
https://doi.org/10.1111/rssb.12167

<a id="r82"></a>**[R82] Sutton, Richard S., and Andrew G. Barto. (2018). _Reinforcement Learning: An Introduction_, 2nd ed. MIT Press.**  
http://incompleteideas.net/book/the-book-2nd.html

## Endogenous observation, delayed impacts, and simulation

<a id="r73"></a>**[R73] Kilbertus, Niki, Manuel Gomez Rodriguez, Bernhard Schölkopf, Krikamol Muandet, and Isabel Valera. (2020). “Fair Decisions Despite Imperfect Predictions.” _AISTATS_, PMLR 108:277–287.**  
https://proceedings.mlr.press/v108/kilbertus20a.html

<a id="r74"></a>**[R74] Ensign, Danielle, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger, and Suresh Venkatasubramanian. (2018). “Runaway Feedback Loops in Predictive Policing.” _FAT*_, PMLR 81:160–171.**  
https://proceedings.mlr.press/v81/ensign18a.html

<a id="r75"></a>**[R75] Wilensky, Uri, and William Rand. (2015). _An Introduction to Agent-Based Modeling: Modeling Natural, Social, and Engineered Complex Systems with NetLogo_. MIT Press.**  
https://mitpress.mit.edu/9780262731898/an-introduction-to-agent-based-modeling/

<a id="r76"></a>**[R76] Grimm, Volker, et al. (2020). “The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism.” _Journal of Artificial Societies and Social Simulation_ 23(2).**  
https://doi.org/10.18564/jasss.4259

<a id="r77"></a>**[R77] Fudenberg, Drew, and David K. Levine. (1998). _The Theory of Learning in Games_. MIT Press.**  
https://mitpress.mit.edu/9780262529242/the-theory-of-learning-in-games/

<a id="r78"></a>**[R78] Schmit, Sven, and Carlos Riquelme. (2018). “Human Interaction with Recommendation Systems.” _AISTATS_, PMLR 84:862–870.**  
https://proceedings.mlr.press/v84/schmit18a.html

<a id="r79"></a>**[R79] Liu, Lydia T., Sarah Dean, Esther Rolf, Max Simchowitz, and Moritz Hardt. (2018). “Delayed Impact of Fair Machine Learning.” _ICML_, PMLR 80:3150–3158.**  
https://proceedings.mlr.press/v80/liu18c.html

## AI-agent feedback

<a id="r81"></a>**[R81] Pan, Alexander, Erik Jones, Meena Jagadeesan, and Jacob Steinhardt. (2024). “Feedback Loops With Language Models Drive In-Context Reward Hacking.” _ICML_, PMLR 235:39154–39200.**  
https://proceedings.mlr.press/v235/pan24d.html

---

## Additional useful readings from the original bibliography

The following works deepen themes developed above even where they are not required in the curriculum:

- Goodhart, Charles A. E. (1984). _Monetary Theory and Practice: The UK Experience_. Macmillan.
- Ericsson, Neil R., and John S. Irons, eds. (1995). _Testing Exogeneity_. Oxford University Press.
- Hoover, Kevin D. (1994). “Econometrics as Observation: The Lucas Critique and the Nature of Econometric Inference.” _Journal of Economic Methodology_ 1(1): 65–80.
- Campbell, Donald T. (1988). _Methodology and Epistemology for Social Science: Selected Papers_. University of Chicago Press.
- Nichols, Sharon L., and David C. Berliner. (2007). _Collateral Damage: How High-Stakes Testing Corrupts America’s Schools_. Harvard Education Press.
- Muller, Jerry Z. (2018). _The Tyranny of Metrics_. Princeton University Press.
- Azariadis, Costas. (1981). “Self-Fulfilling Prophecies.” _Journal of Economic Theory_ 25(3): 380–396.
- Romanos, George D. (1973). “Reflexive Predictions.” _Philosophy of Science_ 40(1): 97–109.
- Kopec, Matthew. (2011). “A More Fulfilling (and Frustrating) Take on Reflexive Predictions.” _Philosophy of Science_ 78(5): 1249–1260.
- MacKenzie, Donald. (2004). “The Big, Bad Wolf and the Rational Market: Portfolio Insurance, the 1987 Crash and the Performativity of Economics.” _Economy and Society_ 33(3): 303–334.
- MacKenzie, Donald, Fabian Muniesa, and Lucia Siu, eds. (2007). _Do Economists Make Markets? On the Performativity of Economics_. Princeton University Press.
- Bell, Graham. (1982). _The Masterpiece of Nature: The Evolution and Genetics of Sexuality_. University of California Press.
- Goodfellow, Ian J., Jonathon Shlens, and Christian Szegedy. (2015). “Explaining and Harnessing Adversarial Examples.” _ICLR_. https://arxiv.org/abs/1412.6572
- Levitt, Steven D., and John A. List. (2011). “Was There Really a Hawthorne Effect at the Hawthorne Plant?” _American Economic Journal: Applied Economics_ 3(1): 224–238. https://doi.org/10.1257/app.3.1.224
- Myerson, Roger B., and Mark A. Satterthwaite. (1983). “Efficient Mechanisms for Bilateral Trading.” _Journal of Economic Theory_ 29(2): 265–281. https://doi.org/10.1016/0022-0531(83)90048-0

---

# Closing Principle

The literatures in this guide converge on a common warning but also point toward a constructive research program.

The warning is:

> **Pre-deployment predictive validity does not guarantee post-deployment validity when the model affects decisions, observations, incentives, institutions, or population dynamics.**

The constructive program is:

> **Model deployment as part of the system. Represent the response mechanism explicitly. Distinguish prediction from decision. Treat observation as potentially endogenous. Analyze repeated dynamics rather than only one-step effects. Validate interventions prospectively where possible. Evaluate equilibrium and long-run system value, not only predictive accuracy.**

In compact form:

$$
\boxed{
\text{Model}
\rightarrow
\text{Decision}
\rightarrow
\text{Adaptive Response}
\rightarrow
\text{Observation}
\rightarrow
\text{Learning}
\rightarrow
\text{Model}
}
$$

The core research question is not merely **whether a model predicts the system**. It is:

> **What system does repeated use of the model create, and how should that coupled model-system process be designed, learned, validated, and governed?**
