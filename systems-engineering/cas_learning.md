# Complex Adaptive Systems from a Systems Engineering Perspective

**Learning guide — current through September 2026**

<a id="purpose"></a>
## Purpose of this guide

This guide is a structured curriculum for a technically experienced reader with a background in software, data, analytics, engineering, or systems architecture who wants to understand **complex adaptive systems (CAS) from a systems engineering perspective** and develop toward research-level competence.

It is organized around a central systems-engineering question:

> **How do we design, architect, govern, operate, assure, and improve systems whose behavior cannot be completely predicted or centrally controlled?**

The guide treats CAS-in-systems-engineering not as one tidy discipline, but as an interdisciplinary zone spanning systems science, complex systems, engineering systems, system-of-systems engineering, sociotechnical systems, cybernetics, network science, simulation, resilience engineering, safety science, governance, decision making under deep uncertainty, model-based systems engineering, and systems practice.

The objective is not merely to accumulate readings. By the end of the curriculum, you should be able to:

1. distinguish major forms and mechanisms of complexity;
2. explain how systems engineering changes when systems are open, adaptive, multi-actor, and only partly controllable;
3. select modeling and intervention methods based on the structure of a problem rather than methodological preference;
4. build and critique system dynamics, agent-based, network, architecture, uncertainty, and safety models;
5. reason about architecture, governance, resilience, adaptation, and lifecycle value under deep uncertainty;
6. distinguish what conventional systems engineering can represent well from what requires complexity-oriented extensions;
7. evaluate claims made from computational models and mixed-method systems research;
8. design a defensible research study on a complex engineered or sociotechnical system; and
9. produce a capstone analysis that compares multiple lenses on the same real system.

The current-practice snapshot is updated through **September 2026**. It incorporates ISO/IEC/IEEE 15288:2023, the INCOSE Systems Engineering Handbook Fifth Edition, SEBoK v2.14, and the final adoption of SysML v2.

---

<a id="toc"></a>
# Table of Contents

1. [Part I — The Central Framing](#part-i)
   1. [What systems engineering is doing with CAS](#central-framing)
   2. [A vocabulary that prevents conceptual slippage](#taxonomy)
   3. [Forms of complexity](#forms-of-complexity)
   4. [Core engineering questions](#core-questions)
   5. [Key tensions to carry throughout the curriculum](#tensions)
2. [Part II — Systems Science and Complexity Foundations](#part-ii)
   1. [Systems thinking, cybernetics, and design](#systems-foundations)
   2. [Core CAS mechanisms](#cas-mechanisms)
   3. [Multiscale organization and near-decomposability](#multiscale)
   4. [Networks and interdependence](#network-foundations)
   5. [Adaptation, learning, evolution, and co-evolution](#adaptation)
3. [Part III — Systems Engineering Perspectives on Complexity](#part-iii)
   1. [Baseline professional systems engineering](#baseline-se)
   2. [Engineering systems and sociotechnical systems](#engineering-systems)
   3. [System-of-systems engineering](#sose)
   4. [Systems practice, soft systems, and critical systems thinking](#systems-practice)
   5. [Governance and institutions](#governance)
   6. [Safety, resilience, and high reliability](#safety-resilience)
   7. [Mission engineering and human systems integration](#mission-hsi)
   8. [MBSE and digital engineering](#mbse)
4. [Part IV — The Methods Toolkit](#part-iv)
   1. [Method selection as a first-class skill](#method-selection)
   2. [System dynamics](#system-dynamics)
   3. [Agent-based modeling](#abm)
   4. [Network science](#network-science)
   5. [Nonlinear dynamics and tipping behavior](#nonlinear-dynamics)
   6. [DSM and structural architecture analysis](#dsm)
   7. [Uncertainty quantification and sensitivity analysis](#uq)
   8. [Decision making under deep uncertainty](#dmdu)
   9. [Safety and resilience analysis](#safety-methods)
   10. [MBSE as an integration environment](#mbse-method)
   11. [Multimethod and mixed-method inquiry](#multimethod)
5. [Part V — Research Methodology for Complex Engineered Systems](#part-v)
   1. [From interesting model to defensible research claim](#research-claims)
   2. [Verification, validation, calibration, and evaluation](#vv)
   3. [Experimental design for simulation](#simulation-experiments)
   4. [Evidence, causality, and triangulation](#evidence)
   5. [Reproducibility and model documentation](#reproducibility)
   6. [Ethics and intervention](#ethics)
6. [Part VI — The Phased Curriculum](#part-vi)
   1. [Module 0 — Establish the baseline systems-engineering frame](#module-0)
   2. [Module 1 — Learn systems science, cybernetics, and the science of design](#module-1)
   3. [Module 2 — Learn the mechanisms of complex adaptive systems](#module-2)
   4. [Module 3 — Connect complexity science to systems engineering](#module-3)
   5. [Module 4 — Learn sociotechnical problem framing and systems practice](#module-4)
   6. [Module 5 — Learn systems of systems, governance, and mission thinking](#module-5)
   7. [Module 6 — Build the computational modeling toolkit](#module-6)
   8. [Module 7 — Architect under uncertainty and deep uncertainty](#module-7)
   9. [Module 8 — Study safety, resilience, and operational adaptation](#module-8)
   10. [Module 9 — Integrate with MBSE and digital engineering](#module-9)
   11. [Module 10 — Learn research design, validation, and reproducibility](#module-10)
   12. [Module 11 — Synthesis and capstone](#module-11)
7. [Part VII — Recurring Reference Systems](#part-vii)
8. [Part VIII — Questions to Carry While Reading and Modeling](#part-viii)
9. [Part IX — Branches by Research Interest](#part-ix)
10. [Part X — Capstone Structure](#part-x)
11. [Part XI — Maintaining a Living View of the Field](#part-xi)
12. [Part XII — References](#references)

---

<a id="part-i"></a>
# Part I — The Central Framing

<a id="central-framing"></a>
## 1. What systems engineering is doing with CAS

From a systems engineering perspective, complex adaptive systems are important because engineers increasingly work with systems that are:

- open rather than cleanly bounded;
- nonlinear rather than proportionate;
- multi-actor rather than centrally owned;
- adaptive rather than behaviorally fixed;
- coupled across technical, human, organizational, and institutional layers;
- distributed across multiple scales;
- evolving after deployment;
- embedded in environments that themselves change in response to the system; and
- capable of producing system-level behavior that no individual component owner fully intended.

Examples include critical infrastructure, digital platforms, healthcare delivery, transportation networks, military and emergency-response missions, global supply systems, autonomous and cyber-physical ecosystems, financial infrastructure, large software/data platforms, and inter-organizational systems of systems.

Traditional systems engineering remains necessary for these systems, but it is often insufficient when interpreted as strongly reductionist, centrally controlled, requirements-complete, and optimized around a stable future. The challenge shifts from finding a single final design to maintaining useful capability over time under changing conditions and partial control.

The systems-engineering problem is therefore not only:

> **Why did this emergent behavior occur?**

It is also:

> **What can we responsibly design, constrain, enable, monitor, adapt, govern, or learn so that system-level outcomes remain acceptable despite irreducible uncertainty and distributed agency?**

That is the core intellectual identity of this guide: **intervention under irreducible complexity**.

A useful consequence follows. Complexity is not an excuse for vagueness. The job is to identify *which mechanisms of complexity matter for the decision at hand*, choose representations that preserve those mechanisms, and design interventions that are robust to what cannot be predicted.

<a id="taxonomy"></a>
## 2. A vocabulary that prevents conceptual slippage

These categories overlap but should not be treated as synonyms.

| Term | Working definition for this guide | Primary engineering implication |
|---|---|---|
| **Complicated system** | Many parts or intricate structure, but decomposition and prediction remain sufficiently effective | Decomposition, interface management, verification, optimization |
| **Complex system** | Interactions produce system-level behavior that is difficult to infer from parts alone | Interaction structure, feedback, nonlinearities, emergence |
| **Complex adaptive system (CAS)** | A complex system in which agents or subsystems modify behavior through adaptation, learning, selection, or evolution | Behavior can change in response to the intervention itself |
| **Complex engineered system** | An engineered system with meaningful complex-system behavior | Design must address interaction-driven behavior, not only component correctness |
| **Sociotechnical system** | Technical and human/social/organizational elements jointly constitute the system | Human behavior, incentives, institutions, and technology must be modeled together |
| **System of systems (SoS)** | Constituent systems retain meaningful operational and/or managerial independence while collaborating to create higher-level capability | Authority, architecture, interoperability, incentives, governance, evolution |
| **Enterprise system** | Organization, processes, technology, incentives, governance, and environment considered systemically | Transformation and design cannot be reduced to the technical architecture |
| **Mission system** | A mission or capability is treated as the system of interest, often spanning multiple systems and organizations | Architecture is organized around outcomes/capabilities rather than product boundaries |
| **Platform/ecosystem** | Multiple autonomous participants interact through shared technical and institutional structures | Rules, APIs, standards, incentives, network effects, governance |

Two cautions follow.

**First**, not every SoS is meaningfully adaptive, and not every CAS is a SoS. A swarm of simple adaptive agents may be a CAS without managerial independence; a federation of independently managed systems may be an SoS even if constituent behavior changes slowly.

**Second**, “complexity” can describe the system, the environment, the stakeholder situation, the modeling problem, or the observer’s epistemic limitations. Good research states which meaning is intended.

<a id="forms-of-complexity"></a>
## 3. Forms of complexity

Instead of treating complexity as one scalar quantity, classify what makes the engineering task difficult.

### 3.1 Structural complexity

Many elements, dense coupling, dependency cycles, multilayer architecture, or highly heterogeneous components.

Typical methods:
- architecture models;
- DSM;
- graph/network analysis;
- modularity analysis;
- interface analysis.

### 3.2 Dynamic complexity

Behavior arises from feedback, delays, accumulations, nonlinearity, oscillation, instability, or path dependence.

Typical methods:
- system dynamics;
- nonlinear dynamics;
- time-series analysis;
- simulation.

### 3.3 Adaptive complexity

Agents change strategies, rules, connections, goals, or internal models as experience accumulates.

Typical methods:
- agent-based modeling;
- learning/evolutionary models;
- repeated-game models;
- adaptive control and online experimentation.

### 3.4 Network/interdependence complexity

Failure, information, influence, or resources propagate through dependency networks or interacting layers.

Typical methods:
- network science;
- cascading-failure models;
- multilayer/interdependent network models;
- percolation and diffusion models.

### 3.5 Organizational and governance complexity

Authority, incentives, ownership, standards, incentives, and decision rights are distributed.

Typical methods:
- institutional analysis;
- stakeholder analysis;
- SoS governance models;
- mechanism/incentive analysis;
- organizational network analysis.

### 3.6 Goal and value complexity

Stakeholders disagree about objectives, tradeoffs, legitimate boundaries, or definitions of success.

Typical methods:
- soft systems methodology;
- critical systems practice;
- participatory modeling;
- multi-criteria decision analysis;
- value-focused thinking.

### 3.7 Uncertainty complexity

Uncertainty may be probabilistic, epistemic, structural, scenario-based, or deep enough that actors disagree about models, probabilities, or values.

Typical methods:
- uncertainty quantification;
- global sensitivity analysis;
- scenario discovery;
- Robust Decision Making;
- Dynamic Adaptive Policy Pathways;
- real options/flexibility.

### 3.8 Lifecycle and evolutionary complexity

The system changes as technology, users, organizations, adversaries, regulations, and neighboring systems evolve.

Typical methods:
- evolutionary architecture;
- staged commitment;
- modularity;
- upgrade pathways;
- technical-debt analysis;
- adaptive roadmaps.

The practical lesson is simple: **different complexity mechanisms imply different useful abstractions**. A network model cannot substitute for a governance model merely because both are “complexity methods.”

<a id="core-questions"></a>
## 4. Core engineering questions

The rest of the guide can be read as attempts to answer a recurring set of questions.

### 4.1 Characterization

- What makes this system complex rather than merely complicated?
- Which complexity mechanisms dominate the decision?
- At what spatial, organizational, temporal, or abstraction scales do they occur?
- Is the complexity in the system, the environment, the stakeholder situation, or the modeler’s knowledge?

### 4.2 Emergence

- Which system-level outcomes arise from local interactions?
- Which emergent behaviors are functional, neutral, hazardous, or value-conflicted?
- What local rules, interfaces, feedbacks, incentives, or constraints shape those outcomes?
- Can emergence be anticipated, bounded, detected, exploited, or contained?

### 4.3 Architecture

- Which dependencies should be tight and which should be loose?
- Where do modularity and interface standards create optionality?
- When does efficiency create hidden fragility?
- Which architectural decisions should remain reversible?

### 4.4 Adaptation

- What adapts: components, users, organizations, policies, algorithms, adversaries, or the whole ecosystem?
- What information drives adaptation?
- How quickly can the system adapt relative to environmental change?
- Does local adaptation improve or degrade system-level outcomes?

### 4.5 Control and governance

- Who has decision rights?
- Which behaviors can be controlled directly and which can only be influenced?
- What information is locally available versus centrally available?
- Are standards, incentives, protocols, contracts, or shared models more appropriate than command-and-control?

### 4.6 Uncertainty

- Which uncertainties can be represented probabilistically?
- Which assumptions are disputed or structurally uncertain?
- Where would a point forecast create false precision?
- What strategy performs acceptably across many plausible futures?
- What should be monitored so the strategy can change later?

### 4.7 Safety and resilience

- What must never happen?
- What control constraints are required for safety?
- How do pressures and adaptations migrate operations toward unsafe boundaries?
- What capacity is available to absorb, recover, stretch, reconfigure, and learn?

### 4.8 Evidence and learning

- What observations would falsify the model?
- Which results are explanatory, predictive, exploratory, or normative?
- How do we learn after deployment without creating unacceptable risk?
- How should the model change as the real system changes?

<a id="tensions"></a>
## 5. Key tensions to carry throughout the curriculum

A mature understanding of complex systems engineering comes from learning to reason across tensions rather than adopting one slogan.

| Tension | Question to ask |
|---|---|
| Prediction vs. exploration | Do we need a forecast, or do we need to understand the consequences of assumptions? |
| Optimization vs. robustness | Is peak performance in one future more valuable than acceptable performance across many futures? |
| Control vs. influence | Does the engineer actually possess authority over the relevant actors? |
| Requirements vs. evolving intent | Which needs can be stabilized and which will evolve? |
| Top-down architecture vs. bottom-up emergence | Which structures must be imposed and which behaviors should be allowed to self-organize? |
| Efficiency vs. resilience | What slack, diversity, redundancy, or spare capacity is worth preserving? |
| Modularity vs. tightly coupled performance | Where does decoupling reduce propagation risk, and where does integration enable essential capability? |
| Standardization vs. diversity | Does standardization reduce coordination burden or create correlated failure modes? |
| Stability vs. adaptability | How much change can be tolerated without loss of identity or safety? |
| Model fidelity vs. decision usefulness | Is a more detailed model actually better for the decision? |
| Quantitative model vs. stakeholder interpretation | Is the limiting problem computational or fundamentally about contested meaning and values? |
| Technical boundary vs. sociotechnical boundary | What important behavior disappears if humans, organizations, or institutions are treated as “external”? |

---
<a id="part-ii"></a>
# Part II — Systems Science and Complexity Foundations

<a id="systems-foundations"></a>
## 6. Systems thinking, cybernetics, and the science of design

A systems engineer working on CAS should understand the intellectual lineages that predate modern complexity science. These traditions give you concepts for purpose, feedback, control, hierarchy, boundary choice, observer dependence, and intervention.

### 6.1 General systems and hierarchy

Herbert Simon is particularly important because he connects **complexity, hierarchy, near-decomposability, bounded rationality, and design**. His essay *The Architecture of Complexity* [R09](#r09) and *The Sciences of the Artificial* [R10](#r10) provide a bridge between complex-systems reasoning and engineering design.

Key ideas to learn:
- hierarchical and nearly decomposable organization;
- interfaces as mechanisms that reduce coordination burden;
- bounded rationality and satisficing;
- artificial systems as objects of scientific study;
- design as transformation from existing situations to preferred ones.

### 6.2 Cybernetics

W. Ross Ashby's *An Introduction to Cybernetics* [R11](#r11) introduces ideas that remain surprisingly current for complex engineered systems:

- feedback;
- regulation;
- state and transformation;
- requisite variety;
- homeostasis;
- constraints on control.

A key engineering lesson from requisite variety is that **a regulator must possess enough behavioral variety to cope with the variety of disturbances that matter**. This provides a principled reason why overly centralized control can fail in rich environments: information and response variety may not exist at the center at the right time or resolution.

### 6.3 Problem framing traditions

Not all complexity is dynamic or computational. In many real systems, the first challenge is that stakeholders do not agree on the problem definition, boundary, purpose, or success criteria.

Peter Checkland's Soft Systems Methodology (SSM) [R12](#r12) is useful when the problem situation itself is contested. Michael C. Jackson's Critical Systems Practice [R13](#r13) adds an explicit multimethodological intervention framework and asks the practitioner to match methods to the problem situation rather than treating one methodology as universally sufficient.

These traditions should be learned alongside—not after—formal modeling, because a mathematically elegant model of the wrong boundary can be less useful than a simpler model built from better problem structuring.

<a id="cas-mechanisms"></a>
## 7. Core CAS mechanisms

The term CAS becomes useful only when it refers to mechanisms rather than atmosphere. The following mechanisms should become part of your working vocabulary.

### 7.1 Nonlinearity

Output is not proportionate to input. Small changes can have negligible effects in one regime and large effects in another. Superposition fails.

Engineering relevance:
- margins can disappear suddenly;
- local optimizations interact;
- risk cannot always be extrapolated linearly from nominal operation.

### 7.2 Feedback

**Reinforcing feedback** amplifies change; **balancing feedback** counteracts it. When multiple loops operate with delays, the resulting behavior can include overshoot, oscillation, lock-in, instability, and counterintuitive policy response.

System dynamics is the primary methodology in this guide for learning feedback-dominant explanations [R19](#r19).

### 7.3 Emergence

Macro-level patterns arise from interactions among lower-level elements. A useful engineering treatment distinguishes:
- emergence that is surprising only because the observer lacks a convenient aggregate model;
- emergence that requires simulation to derive from local rules;
- system-level properties whose meaning exists only at the macro level, such as congestion, market liquidity, mission effectiveness, organizational culture, or resilience.

The important engineering question is not whether emergence is mysterious. It is **which local structures and rules generate the macro behavior, and which of those are legitimate intervention points**.

### 7.4 Self-organization

Order can arise without a central designer specifying the final global configuration. Self-organization may be desirable—such as load balancing or distributed coordination—or hazardous—such as herding, unsafe workarounds, or correlated failure.

Do not equate self-organization with optimality. A self-organized state can be stable and still be undesirable.

### 7.5 Adaptation and learning

Agents update behavior based on feedback, experience, incentives, imitation, learning algorithms, or selection. Adaptation matters because the system may respond to your intervention in ways that invalidate the assumptions behind the intervention.

Examples:
- users route around controls;
- attackers change tactics;
- organizations create workarounds;
- software services change load-shaping behavior;
- markets alter strategies;
- machine-learning policies update online.

### 7.6 Path dependence and lock-in

Current options depend on historical sequence. Positive feedback, switching costs, network effects, sunk investments, standards, institutional routines, and learning curves can make an initially contingent choice difficult to reverse.

Engineering implication: architecture decisions can create **option value or option foreclosure** long before consequences become visible.

### 7.7 Thresholds and tipping behavior

Systems can change regime when control parameters cross thresholds. Near critical transitions, local linear intuition may be unreliable. The relevant methods include nonlinear dynamics, bifurcation analysis, network percolation, and simulation.

### 7.8 Heterogeneity

Different actors have different goals, capabilities, beliefs, constraints, network positions, and adaptation rates. Aggregating heterogeneous agents into a representative average can erase the mechanism producing the behavior of interest.

### 7.9 Co-evolution

The system changes the environment while the environment changes the system. Platform operators affect participant strategies; participants affect platform rules. Infrastructure investment reshapes demand; demand reshapes infrastructure planning. Security defenses alter attacker behavior, which then changes defensive priorities.

### 7.10 Robust-yet-fragile behavior

Designed systems may become highly robust to anticipated disturbances while becoming vulnerable to unanticipated conditions. Carlson and Doyle's Highly Optimized Tolerance work [R36](#r36) is a useful counterweight to the simplistic idea that more optimization always means better engineering.

<a id="multiscale"></a>
## 8. Multiscale organization and near-decomposability

Complex systems operate at multiple scales simultaneously:
- component;
- subsystem;
- organization;
- enterprise;
- ecosystem;
- geographic region;
- seconds, days, years, and decades.

A behavior that appears random at one scale may be structured at another. A local intervention can improve one subsystem while degrading another. Likewise, a governance structure that works for low-frequency strategic coordination may fail for millisecond operational control.

Questions to learn to ask:
- At what scale does the disturbance occur?
- At what scale is information available?
- At what scale can action be taken?
- At what scale is performance evaluated?
- Are these scales aligned?

Bar-Yam's multiscale complexity work is useful here, as is Simon's near-decomposability. Together they motivate an important design heuristic:

> **Match coordination and control to the scale at which relevant information and action exist.**

This is not a universal argument for decentralization. It is an argument against assuming that one control scale is sufficient.

<a id="network-foundations"></a>
## 9. Networks and interdependence

Many engineered systems are simultaneously several networks:

- physical connectivity;
- information flow;
- dependency;
- organizational communication;
- ownership;
- control authority;
- software calls;
- supply relationships;
- financial relationships.

A learner should become comfortable with:
- degree and degree distributions;
- path length;
- clustering;
- centrality;
- communities;
- assortativity;
- motifs;
- small-world structure;
- scale-free claims and their limitations;
- diffusion and contagion;
- percolation;
- synchronization;
- cascading failure;
- multilayer and interdependent networks.

Newman's *Networks* [R22](#r22) is the main technical reference. Barabási's freely available *Network Science* [R23](#r23) is a good companion. Buldyrev et al. [R24](#r24) is important because engineered infrastructures are often not one network but **interdependent networks**, where a failure in one layer can recursively disable another.

Network models are powerful but easy to misuse. A graph captures relationships; it does not automatically capture the causal mechanism operating over those relationships. Always ask what edges mean and what dynamics run on the graph.

<a id="adaptation"></a>
## 10. Adaptation, learning, evolution, and co-evolution

John Holland's CAS work [R08A](#r08a) is valuable for understanding adaptation through rules, selection, aggregation, tags, and building blocks. Miller and Page [R08](#r08) provide a computationally oriented introduction to adaptive social systems.

Distinguish at least four mechanisms:

### 10.1 Behavioral adaptation

An agent changes an action based on observations or rewards.

### 10.2 Learning

The agent changes an internal representation, policy, belief, or model that influences future behavior.

### 10.3 Selection

Population composition changes because some strategies, designs, organizations, or components persist more successfully than others.

### 10.4 Structural evolution

The topology or architecture itself changes: links form or disappear, modules are replaced, standards evolve, firms enter/exit, teams reorganize.

A serious CAS analysis should state **what adapts, through what mechanism, on what timescale, using what information, and according to what objective or selection pressure**.

---

<a id="part-iii"></a>
# Part III — Systems Engineering Perspectives on Complexity

<a id="baseline-se"></a>
## 11. Baseline professional systems engineering

Before learning how complexity changes systems engineering, establish a clear comparator for conventional practice.

### 11.1 ISO/IEC/IEEE 15288:2023

ISO/IEC/IEEE 15288:2023 [R01](#r01) defines a common framework for system life-cycle processes. It explicitly applies to systems of interest, system elements, and systems of systems and allows iterative, concurrent, and recursive application.

Study it to understand:
- stakeholder needs and requirements;
- system requirements;
- architecture and design definition;
- implementation, integration, verification, transition, validation, operation, maintenance, and disposal;
- technical management processes;
- lifecycle thinking.

Do **not** study it as if it were a predictive theory of complex systems. Use it as the baseline process framework against which complexity-oriented methods can be positioned.

### 11.2 INCOSE Systems Engineering Handbook Fifth Edition

The INCOSE Handbook Fifth Edition [R02](#r02) is a state-of-good-practice professional reference aligned with ISO/IEC/IEEE 15288:2023. Use it to understand the vocabulary and process assumptions of mainstream systems engineering.

Carry one question throughout the guide:

> Which SE processes remain valid as written, which require iteration or reinterpretation, and which need complementary methods when the system is adaptive, distributed, deeply uncertain, or sociotechnical?

### 11.3 SEBoK as a living reference

SEBoK should be treated as a recurring reference rather than a one-time reading. Version 2.14, released in May 2026, refreshed the Systems Science knowledge area and strengthened coverage of complexity and structure [R03](#r03).

Use SEBoK to maintain vocabulary, trace concepts to primary references, and stay connected to professional systems-engineering practice.

<a id="engineering-systems"></a>
## 12. Engineering systems and sociotechnical systems

The engineering-systems tradition treats large engineered systems as inseparable combinations of:

- technical artifacts;
- people;
- organizations;
- institutions;
- regulation;
- markets;
- incentives;
- operating procedures;
- users;
- infrastructure;
- lifecycle evolution.

De Weck, Roos, and Magee's *Engineering Systems* [R16](#r16) is a strong foundational text. This perspective is especially useful for transportation, energy, healthcare, communications, digital infrastructure, enterprise systems, and platform ecosystems.

The key move is a boundary move:

> **Do not treat the social or institutional layer as merely an external disturbance if it helps produce the system's behavior.**

This does not mean every model must contain everything. It means the analyst must justify exclusions.

<a id="sose"></a>
## 13. System-of-systems engineering

SoSE is one of the clearest professional homes for complexity-oriented systems engineering because it starts from limited central authority.

Maier's classic paper [R17](#r17) emphasizes characteristics such as operational and managerial independence and makes architecture and communication standards central to SoS design. The Jamshidi edited volume [R18](#r18) contains important work from the SoSE community, including Boardman, Sauser, Gorod, Dahmann, and others.

Core SoSE concerns:
- constituent autonomy;
- evolutionary development;
- managerial independence;
- capability emergence;
- interoperability;
- negotiated architecture;
- governance;
- federated decision making;
- asynchronous lifecycles;
- changing constituent membership.

A useful contrast is:

**Traditional system:** engineer has substantial authority over decomposition and interfaces.

**System of systems:** engineer may influence interfaces, incentives, standards, information, and coordination while constituent owners retain their own missions and roadmaps.

This makes SoSE directly relevant to cloud ecosystems, data-sharing federations, government programs, supply networks, autonomous fleets, and cross-organizational mission systems.

<a id="systems-practice"></a>
## 14. Systems practice, soft systems, and critical systems thinking

Hitchins and Gharajedaghi provide an important starting point for a broader **problem-framing and intervention** track.

### 14.1 Soft Systems Methodology

Use SSM [R12](#r12) when:
- the problem is not agreed upon;
- stakeholders hold incompatible worldviews;
- system boundaries are contested;
- measures of success differ;
- intervention itself changes perceptions and relationships.

### 14.2 Critical Systems Practice

Jackson's Critical Systems Practice [R13](#r13) argues for multimethodology and an intervention cycle summarized as **EPIC**:
- Explore;
- Produce an intervention strategy;
- Intervene;
- Check.

This is extremely compatible with CAS-oriented engineering because it does not assume that one representation or one methodology is sufficient.

### 14.3 Gharajedaghi and interactive design

Gharajedaghi [R14](#r14) is especially useful for purposeful organizational systems, pluralism, interactive design, and business/enterprise architecture.

### 14.4 Hitchins

Hitchins remains valuable for advanced systems thinking and practical framing of large interconnected problems. Read him after gaining enough formal modeling experience to connect qualitative systems practice with technical architecture and simulation.

<a id="governance"></a>
## 15. Governance and institutions

Complex systems engineering often fails if governance is treated as an afterthought. In distributed systems, **the governance architecture may be as important as the technical architecture**.

Study:
- decision rights;
- incentives;
- standards;
- protocols;
- contracts;
- information disclosure;
- accountability;
- conflict resolution;
- subsidiarity;
- polycentric governance;
- commons problems;
- platform rules;
- entry/exit conditions;
- compliance and enforcement;
- institutional adaptation.

Ostrom's *Governing the Commons* [R35](#r35) is useful because it provides an empirical alternative to assuming that coordination requires either a single central authority or purely market mechanisms.

For software/data/platform systems, translate these ideas into:
- API governance;
- schema and protocol standards;
- access rights;
- data stewardship;
- shared-service ownership;
- service-level commitments;
- ecosystem participation rules;
- platform moderation and incentive structures.

Governance should be modeled as a design variable rather than a contextual footnote.

<a id="safety-resilience"></a>
## 16. Safety, resilience, and high reliability

These traditions answer different questions and should not be collapsed.

### 16.1 Reliability

How consistently does a system perform a specified function under stated conditions?

### 16.2 Robustness

How insensitive is performance to a specified class of perturbations or parameter variation?

### 16.3 Safety

How are unacceptable losses prevented, including losses arising from interaction and inadequate control rather than simple component failure?

### 16.4 Resilience

How does the system sustain or recover valued capability under disturbance and surprise? Woods [R34](#r34) distinguishes several meanings, including rebound, robustness, graceful extensibility, and sustained adaptability.

### 16.5 High reliability

How do organizations operating hazardous systems maintain reliable performance despite uncertainty and operational pressure? Weick and Sutcliffe [R33](#r33) provide an organizational perspective through high-reliability organizing.

### 16.6 Systems-theoretic safety

Leveson's STAMP/STPA framework [R31](#r31) models safety as a control problem in complex sociotechnical systems. Instead of assuming accidents are adequately explained as linear chains of component failures, it asks whether safety constraints are enforced across a control structure.

### 16.7 Rasmussen's dynamic risk model

Rasmussen [R32](#r32) is essential for understanding how organizational, regulatory, managerial, and operational pressures interact. This work makes adaptation itself part of safety analysis: actors locally optimize under pressure and can collectively migrate toward unsafe boundaries.

### 16.8 Resilience engineering

Hollnagel, Woods, and Leveson [R33A](#r33a) shift attention toward how systems adapt successfully as well as how they fail.

A mature curriculum should compare these perspectives rather than pick one vocabulary.

<a id="mission-hsi"></a>
## 17. Mission engineering and human systems integration

Two contemporary practices extend the sociotechnical perspective.

### 17.1 Mission engineering

Mission engineering treats mission outcomes/capabilities as the system of interest, frequently crossing organizational and system boundaries. It is useful when no single platform or product can be optimized independently to produce the desired outcome.

Questions:
- What mission threads create capability?
- Which systems and organizations participate?
- Which dependencies are critical?
- Which mission effects are emergent from coordination?
- Where are alternatives, substitutions, and graceful degradation possible?

### 17.2 Human Systems Integration (HSI)

HSI treats human, organizational, and technical elements as an integrated design problem across the lifecycle [R39](#r39). This is important because “the human” should not be modeled only as operator error or a requirement source.

Relevant topics:
- human factors and ergonomics;
- staffing and workforce;
- training;
- workload;
- human-machine teaming;
- organizational design;
- usability;
- safety;
- automation and function allocation;
- cognitive work.

<a id="mbse"></a>
## 18. MBSE and digital engineering

MBSE is important, but it should be positioned correctly.

> **MBSE is primarily a modeling and information-integration paradigm for systems engineering; it is not by itself a theory of complexity.**

MBSE is strong at:
- architecture representation;
- requirements relationships;
- behavior and interfaces;
- traceability;
- configuration;
- shared semantics;
- analysis integration;
- digital continuity.

But a system model can be formally consistent and still fail to represent adaptation, emergence, political authority, nonlinear feedback, or deep uncertainty.

The useful question is therefore:

> Which aspects of the CAS can be represented directly in the system model, and which require linked simulation, data analysis, participatory models, or uncertainty methods?

SysML v2 reached final adoption in 2025 and introduces improved semantics, textual and graphical syntax, and API-based interoperability [R04](#r04). For this curriculum, SysML v2 matters not because notation solves complexity, but because it makes **model integration and composability** increasingly central to digital engineering.

---
<a id="part-iv"></a>
# Part IV — The Methods Toolkit

<a id="method-selection"></a>
## 19. Method selection as a first-class skill

The objective is not to become loyal to one methodology. It is to learn how to select and combine methods based on the causal and decision structure of the problem.

Use this template whenever you encounter a method:

1. **Question** — What decision or explanation is the method intended to support?
2. **Representation** — What objects, relationships, states, behaviors, and boundaries does it encode?
3. **Mechanism** — What causal process is assumed to generate outcomes?
4. **Assumptions** — What is held fixed or simplified?
5. **Data** — What observations or judgments are required?
6. **Analysis** — What operations are performed on the representation?
7. **Output** — What kind of claim is produced: descriptive, explanatory, predictive, exploratory, prescriptive?
8. **Validation** — What evidence supports trusting the result for the intended use?
9. **Failure modes** — In what situations does the method systematically mislead?
10. **Complementary methods** — What important dimensions are omitted and need another lens?

A compact selection map:

| Dominant issue | Good starting methods |
|---|---|
| Feedback, delays, accumulation | System dynamics |
| Heterogeneous adaptive actors | Agent-based modeling |
| Connectivity, propagation, topology | Network science |
| Stability, regimes, thresholds | Nonlinear dynamics / bifurcation analysis |
| Static dependency and architecture | DSM / architecture models |
| Requirements, traceability, interfaces | MBSE / SysML |
| Parameter and model uncertainty | UQ / sensitivity analysis |
| Deeply uncertain futures | RDM / DAPP / exploratory modeling |
| Safety constraints and control flaws | STPA / systems-theoretic safety |
| Contested problem framing | SSM / critical systems practice |
| Distributed ownership and authority | SoSE / governance / institutional analysis |
| Organizational adaptation under pressure | Rasmussen / resilience engineering / HRO |

No table can replace judgment, but it prevents the common mistake of choosing a method because it is familiar rather than because it preserves the mechanisms that matter.

<a id="system-dynamics"></a>
## 20. System dynamics

System dynamics (SD) is especially useful when system behavior is dominated by **feedback, accumulation, delays, nonlinear responses, and endogenous structure**. Sterman's *Business Dynamics* [R19](#r19) is the core reference.

### Learn

- causal-loop diagrams;
- reinforcing and balancing loops;
- stocks and flows;
- delays;
- dimensional consistency;
- reference modes;
- equilibrium and transient behavior;
- feedback dominance;
- path dependence;
- policy resistance;
- calibration and sensitivity analysis.

### Use SD when

- aggregate behavior is more important than individual identity;
- feedback mechanisms are central;
- quantities accumulate over time;
- policies have delayed or counterintuitive effects;
- you want to explain dynamic behavior through endogenous structure.

### Be cautious when

- heterogeneity among agents is the mechanism of interest;
- network topology determines who interacts with whom;
- discrete choices and local rules dominate;
- adaptive agents substantially change strategies.

### Exercise

Build a stock-and-flow model of technical debt in a software platform. Include feature pressure, development capacity, defect generation, rework, architecture degradation, and productivity. Identify at least one reinforcing and one balancing loop. Then test a policy that appears beneficial in the short term but creates a long-term side effect.

### Artifact

A model diagram, assumptions table, behavior-over-time plots, sensitivity analysis, and a two-page explanation of the dominant feedback structure.

<a id="abm"></a>
## 21. Agent-based modeling

Agent-based modeling (ABM) is useful when macro behavior emerges from **heterogeneous agents interacting locally and adapting over time**. Wilensky and Rand [R20](#r20) provide a hands-on introduction applicable to natural, social, and engineered systems.

### Learn

- agents and state variables;
- environments;
- interaction rules;
- scheduling;
- local information;
- heterogeneity;
- learning/adaptation;
- stochasticity;
- networks of interaction;
- initialization;
- parameter sweeps;
- emergent macro metrics;
- verification and validation;
- replication.

### Use ABM when

- individual differences matter;
- local interactions generate macro outcomes;
- actors adapt;
- topology or spatial location matters;
- representative-agent assumptions erase critical mechanisms.

### Be cautious when

- agent rules are selected because they “look plausible” but lack empirical basis;
- the model contains many free parameters and weak validation;
- emergent behavior is treated as evidence merely because it is interesting;
- the model is too complicated to understand causally.

### Documentation

Use the ODD protocol [R21](#r21) to document the model's overview, design concepts, and details. Treat documentation as part of model design, not an afterthought.

### Exercise

Implement a simple coordination or service-selection ecosystem in which software services/teams choose dependencies based on performance, cost, and prior reliability. Observe whether concentration, lock-in, or cascades emerge as local adaptation proceeds.

### Artifact

Code, ODD documentation, parameter experiment plan, replication results, and a short statement distinguishing what the model demonstrates from what it does **not** demonstrate.

<a id="network-science"></a>
## 22. Network science

Network science is the primary toolkit for reasoning about **relational structure**. Newman's *Networks* [R22](#r22) is the technical reference; Barabási [R23](#r23) is an accessible companion.

### Learn structural concepts

- nodes and edges;
- directed/undirected and weighted networks;
- degree;
- centrality;
- clustering;
- shortest paths;
- connected components;
- communities;
- assortativity;
- motifs;
- core-periphery structure;
- multilayer networks.

### Learn dynamics on networks

- diffusion;
- contagion;
- epidemics;
- threshold models;
- synchronization;
- percolation;
- cascading failure;
- load redistribution.

### Engineering applications

- software/service dependencies;
- supply networks;
- organizational communication;
- infrastructure interdependence;
- fault propagation;
- design-task networks;
- information flow;
- collaboration networks;
- command and control.

### Critical caution

Do not assume that a node with high centrality is necessarily the best intervention point. Centrality is a family of structural measures, not a causal theory. Connect topology to an explicit dynamical mechanism.

### Interdependent networks

Buldyrev et al. [R24](#r24) is an important reminder that robustness results from single networks may reverse when multiple networks depend on one another.

### Exercise

Construct two network views of the same software platform:
1. service-call dependencies;
2. team ownership/coordination dependencies.

Compare structural bottlenecks. Identify places where the technical and organizational structures are misaligned.

<a id="nonlinear-dynamics"></a>
## 23. Nonlinear dynamics and tipping behavior

A systems engineer does not need to become a dynamical-systems theorist, but should understand enough nonlinear dynamics to recognize when linear intuition is unsafe.

### Learn

- state space;
- equilibrium;
- local stability;
- phase portraits;
- eigenvalue intuition;
- attractors;
- limit cycles;
- bifurcations;
- hysteresis;
- multiple stable states;
- chaos at an introductory level;
- sensitivity to initial conditions;
- thresholds and regime shifts.

Strogatz [R25](#r25) is an excellent foundation.

### Why this matters

Many engineering decisions implicitly assume that small parameter changes produce small outcome changes. Near a bifurcation or threshold, that assumption fails.

### Exercise

Choose a simple nonlinear model—capacity/congestion, resource depletion, epidemic spread, or feedback control. Vary a control parameter and identify qualitatively different regimes. Explain what an operator would need to monitor to detect proximity to a regime transition.

<a id="dsm"></a>
## 24. DSM and structural architecture analysis

Design Structure Matrix (DSM) methods are among the most practical techniques in the guide for exposing structural coupling. Eppinger and Browning [R26](#r26) is the main reference.

### Learn

- component DSMs;
- task/process DSMs;
- team/organization DSMs;
- clustering;
- sequencing;
- tearing;
- dependency cycles;
- propagation paths;
- multi-domain matrices.

### Use DSM when

- you need a compact representation of dependencies;
- architecture and coupling matter;
- iteration/rework cycles matter;
- you want to compare product, process, and organization structure.

### Limitation

DSM is primarily a **structural representation**. It does not automatically model adaptation, nonlinear dynamics, or stakeholder values. Use it with simulation or network dynamics when those matter.

### Exercise

Build a DSM for a data platform containing data products, pipelines, schemas, teams, and deployment dependencies. Cluster it and identify architecture boundaries that reduce coordination burden without destroying necessary integration.

<a id="uq"></a>
## 25. Uncertainty quantification and sensitivity analysis

Complexity and uncertainty are related but not identical. A complex model can have well-characterized parameter uncertainty; a simple model can face deep structural uncertainty.

### Distinguish

- **aleatory uncertainty** — variability treated as stochastic;
- **epistemic uncertainty** — incomplete knowledge;
- **parameter uncertainty** — unknown parameter values;
- **structural/model uncertainty** — uncertainty about equations, rules, mechanisms, or boundaries;
- **scenario uncertainty** — alternative external conditions;
- **deep uncertainty** — key parties do not know or agree on models, probability distributions, or valuation of outcomes.

### Learn

- Monte Carlo simulation;
- local sensitivity;
- global sensitivity;
- screening;
- uncertainty propagation;
- scenario analysis;
- ensemble analysis;
- robustness metrics;
- assumption testing.

Saltelli et al. [R27](#r27) is a useful reference for global sensitivity analysis.

### Engineering rule

Do not run Monte Carlo over uncertain parameters while silently fixing uncertain model structure. The resulting numerical precision can obscure the larger uncertainty.

<a id="dmdu"></a>
## 26. Decision making under deep uncertainty

When the future cannot be represented credibly by a single probability distribution, the objective changes from “optimize for the forecast” to **stress-test strategies across plausible futures and design adaptation pathways**.

### 26.1 Robust Decision Making (RDM)

RDM [R29](#r29) uses computation to explore many plausible futures, identify the conditions under which a strategy fails, and search for strategies that remain acceptable across a broad range of conditions.

Key ideas:
- exploratory modeling;
- vulnerability analysis;
- scenario discovery;
- robustness rather than expected-value optimality;
- adaptive strategies.

### 26.2 Dynamic Adaptive Policy Pathways (DAPP)

DAPP [R30](#r30) organizes decisions into pathways over time. A near-term action is selected, but alternative future actions are preserved. Monitoring reveals when an existing pathway approaches an adaptation tipping point and a change is required.

Key ideas:
- adaptation tipping points;
- pathways;
- signposts;
- triggers;
- sequencing;
- option preservation.

### 26.3 Flexibility in engineering design

De Neufville and Scholtes [R28](#r28) provide a design-oriented complement: embed flexibility so systems can change configuration as uncertainty resolves.

### Exercise

Take a long-lived platform or infrastructure architecture. Define 4–6 deeply uncertain drivers. Compare:
- a fixed “best estimate” design;
- a robust design;
- an adaptive design with monitoring triggers.

Explain where option value comes from and what must be instrumented to exercise the option.

<a id="safety-methods"></a>
## 27. Safety and resilience analysis

Safety and resilience require more than conventional component reliability analysis when failures emerge from interaction, software, organizational behavior, or inadequate control.

### 27.1 STPA / STAMP

Leveson [R31](#r31) reframes safety around control constraints.

Learn:
- losses;
- hazards;
- safety constraints;
- control structure;
- unsafe control actions;
- causal scenarios.

Use it when hazardous outcomes can occur without any single component “failing” in a conventional sense.

### 27.2 Rasmussen-style system analysis

Map actors across levels—regulators, executives, management, planners, operators—and examine:
- constraints;
- incentives;
- information;
- performance pressures;
- adaptation;
- boundary migration.

### 27.3 Resilience analysis

Assess capabilities to:
- anticipate;
- monitor;
- respond;
- recover;
- stretch capacity;
- reconfigure;
- learn.

Woods' distinctions [R34](#r34) help avoid using “resilience” as a vague synonym for reliability.

### Exercise

Choose a software incident, infrastructure outage, or operational accident. Analyze it twice:
1. as a component failure chain;
2. as a system control/adaptation problem.

Compare what interventions become visible under each representation.

<a id="mbse-method"></a>
## 28. MBSE as an integration environment

Treat MBSE as the environment in which system knowledge can be structured and linked—not the only model.

A mature digital engineering workflow may connect:
- requirements and stakeholder needs;
- architecture models;
- SysML behavior;
- DSM/network representations;
- executable simulations;
- physics models;
- agent-based models;
- system dynamics models;
- safety analyses;
- test evidence;
- operational telemetry;
- uncertainty analyses.

A useful research question is **semantic alignment**: when two models use the same term—“capacity,” “availability,” “agent,” “service,” “failure”—do they actually mean the same thing?

SysML v2 [R04](#r04) makes APIs, textual notation, and formalized semantics more prominent, which should make model transformation and co-simulation increasingly important topics for complexity-oriented SE research.

### Exercise

Create a conceptual integration map showing how one system architecture model would exchange information with:
- an ABM;
- a network model;
- a safety model;
- an uncertainty analysis.

Identify ownership of each parameter and metric.

<a id="multimethod"></a>
## 29. Multimethod and mixed-method inquiry

Some complex-system questions cannot be answered credibly with one method.

A multimethod study might combine:
- interviews to identify decision rules;
- event logs to estimate interaction patterns;
- network analysis to identify structural dependencies;
- ABM to explore adaptive behavior;
- system dynamics to model strategic feedback;
- STPA to identify hazardous control structures;
- RDM to stress-test interventions;
- workshops to interpret results with stakeholders.

The challenge is not merely combining methods. It is maintaining clarity about what each method contributes and avoiding contradictions hidden by incompatible assumptions.

Use a **method integration table**:

| Method | Purpose | Boundary | Core variables | Time scale | Evidence source | Output passed to other methods |
|---|---|---|---|---|---|---|
| Example: network model | identify propagation structure | services | calls/dependencies | minutes–months | telemetry/config | candidate critical nodes |
| Example: ABM | explore adaptation | teams/services | policies/choices | days–years | interviews/logs | distribution of architectures |

---

<a id="part-v"></a>
# Part V — Research Methodology for Complex Engineered Systems

<a id="research-claims"></a>
## 30. From interesting model to defensible research claim

Complex-systems modeling makes it easy to produce interesting patterns. Research requires a stronger standard.

Every study should state:

1. **Decision/research question** — What exactly is being asked?
2. **System of interest** — What is inside/outside the boundary?
3. **Claim type** — Description, explanation, prediction, exploration, design evaluation, or prescription?
4. **Mechanism** — What process is hypothesized to produce the outcome?
5. **Representation** — Why does the model preserve the necessary mechanism?
6. **Evidence** — What observations support assumptions and outputs?
7. **Alternatives** — What rival explanations/models exist?
8. **Uncertainty** — Which conclusions are sensitive to uncertain assumptions?
9. **Scope conditions** — Where should the result not be generalized?
10. **Decision relevance** — What action changes if the conclusion is accepted?

One of the most important habits to develop is asking:

> **What evidence would cause me to reject or substantially revise this model?**

If the answer is “nothing,” the model is functioning as a narrative rather than an empirical research object.

<a id="vv"></a>
## 31. Verification, validation, calibration, and evaluation

Use these terms carefully.

### Verification

Did we implement the intended model correctly?

Examples:
- code tests;
- conservation checks;
- limiting cases;
- dimensional checks;
- independent reimplementation;
- deterministic seed tests.

### Validation

Is the model adequate for its intended purpose relative to evidence?

Potential evidence:
- historical behavior;
- cross-sectional patterns;
- qualitative process evidence;
- expert elicitation;
- withheld data;
- known extreme cases;
- intervention outcomes.

### Calibration

What parameter values make the model sufficiently consistent with observations?

Calibration is not validation. A flexible model can fit historical data and still represent the wrong mechanism.

### Evaluation

Does the model support the decision it was built for?

A model can be scientifically imperfect but useful for robust decision exploration if its uncertainties are exposed. Conversely, a highly detailed model can be decision-useless if its output depends on unobservable assumptions.

<a id="simulation-experiments"></a>
## 32. Experimental design for simulation

Treat computational simulation as experimentation.

Learn to design:
- parameter sweeps;
- factorial experiments;
- Latin hypercube or space-filling designs;
- stochastic replications;
- convergence checks;
- variance decomposition;
- global sensitivity;
- response surfaces;
- scenario ensembles;
- adversarial stress tests.

For stochastic models, report distributions and uncertainty rather than single trajectories.

For high-dimensional models, do not vary one parameter at a time and infer independence unless the model structure justifies it.

<a id="evidence"></a>
## 33. Evidence, causality, and triangulation

Simulation is not automatically causal evidence about the real world. It demonstrates consequences of assumptions encoded in the model.

Strengthen claims using triangulation:
- observational data;
- natural experiments;
- experiments or A/B tests where feasible;
- interviews;
- archival records;
- incident reports;
- comparative cases;
- model ensembles;
- competing causal structures.

Distinguish:
- **model causality** — X causes Y inside the specified model;
- **empirical causality** — evidence supports X causing Y in the real system;
- **decision robustness** — the proposed action remains acceptable even if causal uncertainty is unresolved.

This distinction is especially important in CAS research because equifinality—multiple mechanisms producing similar macro patterns—is common.

<a id="reproducibility"></a>
## 34. Reproducibility and model documentation

For computational research, preserve:
- source code;
- dependencies/environment;
- model version;
- input data provenance;
- random seeds or seed-generation process;
- experiment configuration;
- analysis notebooks/scripts;
- assumptions;
- model diagrams;
- units;
- parameter definitions;
- output definitions.

For ABM, use ODD [R21](#r21) as a baseline documentation protocol.

For cross-model research, maintain a data dictionary and semantic mapping across tools.

For qualitative work, document:
- sampling;
- interview protocols;
- coding approach;
- decision trail;
- researcher interpretation.

Reproducibility does not mean another researcher must obtain an identical real-world outcome. It means they can reconstruct what you did and understand how conclusions arose.

<a id="ethics"></a>
## 35. Ethics and intervention

Complex systems engineering is intervention-oriented, which means the analyst must consider second-order consequences.

Ask:
- Who benefits from the intervention?
- Who bears risk and cost?
- Which stakeholders are missing from the model?
- Could optimization move risk elsewhere in the system?
- Does monitoring required for adaptive control create privacy or autonomy concerns?
- Could a governance mechanism create perverse incentives?
- Could standardization produce systemic monoculture?
- Could resilience for one actor reduce resilience for another?
- Are there irreversible interventions that should be staged or tested first?

For adaptive systems, also consider strategic response: publication or implementation of a policy can change the behavior it was based on.

---
<a id="part-vi"></a>
# Part VI — The Phased Curriculum

The modules below transform the guide from a reading list into a learning program. Each module contains:

- **Learning objective** — what capability you are building;
- **Core concepts** — what you should understand;
- **Required readings** — the minimum serious path;
- **Selective/deep readings** — useful extensions;
- **Exercise** — something to do, not merely read;
- **Artifact** — a reusable product of your learning;
- **Mastery check** — evidence that you can move on.

A reasonable part-time pace is roughly one substantial module every two to four weeks, but the sequencing matters more than calendar duration.

<a id="module-0"></a>
## Module 0 — Establish the baseline systems-engineering frame

### Learning objective

Build a precise understanding of mainstream systems engineering so you can later distinguish where complexity-oriented extensions genuinely add something.

### Core concepts

- system of interest;
- stakeholder needs;
- requirements;
- architecture;
- design definition;
- interfaces;
- verification vs. validation;
- lifecycle processes;
- technical management;
- risk and decision management;
- configuration and information management;
- recursive/iterative application of SE processes.

### Required readings

1. **ISO/IEC/IEEE 15288:2023** — overview and life-cycle process structure [R01](#r01).
2. **INCOSE Systems Engineering Handbook, Fifth Edition** — focus on lifecycle processes, systems thinking, architecture, risk, V&V, and technical leadership [R02](#r02).
3. **SEBoK** — use the current systems engineering and systems science overview material [R03](#r03).

### Selective/deep readings

- SEBoK material on emergence, complexity, systems of systems, systems thinking, and lifecycle models.
- ISO/IEC/IEEE architecture standards if architecture becomes a major specialization.

### Exercise

Choose one system you know well—a data platform, cloud service ecosystem, enterprise analytics platform, transportation service, or infrastructure system. Describe it using conventional SE language:

- stakeholders;
- system boundary;
- operational context;
- functions;
- interfaces;
- requirements;
- architecture;
- V&V approach;
- lifecycle.

Then write a second page titled **“Where the conventional representation becomes uncomfortable.”** Identify adaptation, contested goals, changing boundaries, distributed authority, unmodeled feedback, and uncertainties that do not fit neatly.

### Artifact

A 4–6 page baseline system description plus a “complexity gap” memo.

### Mastery check

You can explain the mainstream SE process without caricaturing it as purely waterfall or purely reductionist, and you can identify specific—not rhetorical—places where additional complexity methods are needed.

---

<a id="module-1"></a>
## Module 1 — Learn systems science, cybernetics, and the science of design

### Learning objective

Develop the conceptual foundations needed to reason about wholes, feedback, hierarchy, regulation, purpose, boundaries, and design.

### Core concepts

- system/environment boundary;
- open systems;
- hierarchy;
- near-decomposability;
- feedback;
- regulation;
- requisite variety;
- bounded rationality;
- purpose and goals;
- design as transformation;
- observer/problem framing.

### Required readings

1. Herbert Simon, **“The Architecture of Complexity”** [R09](#r09).
2. Herbert Simon, **The Sciences of the Artificial**, especially chapters on complexity and design [R10](#r10).
3. W. Ross Ashby, selected chapters from **An Introduction to Cybernetics** [R11](#r11).

### Selective/deep readings

- Gharajedaghi, **Systems Thinking: Managing Chaos and Complexity** [R14](#r14).
- Checkland and Scholes, **Soft Systems Methodology in Action** [R12](#r12).
- Selected cybernetics/management cybernetics material if governance and organizational control become central.

### Exercise

Take your Module 0 system and identify:
- nested levels;
- nearly decomposable subsystems;
- feedback loops;
- information required for regulation;
- sources of environmental variety;
- where the regulator lacks requisite variety.

Then identify one design decision that reduces effective complexity by creating a stable interface or modular boundary.

### Artifact

A systems map and a 2–3 page memo connecting Simon/Ashby concepts to an engineering architecture.

### Mastery check

You can explain why hierarchy and modularity can make complex systems manageable without claiming they eliminate complexity, and you can use requisite variety as more than a slogan.

---

<a id="module-2"></a>
## Module 2 — Learn the mechanisms of complex adaptive systems

### Learning objective

Replace vague complexity language with a mechanism-level understanding of nonlinear, adaptive, emergent behavior.

### Core concepts

- nonlinearity;
- emergence;
- self-organization;
- feedback;
- heterogeneity;
- adaptation;
- learning;
- selection;
- evolution;
- co-evolution;
- path dependence;
- network effects;
- tipping and regime shifts;
- multiscale behavior;
- robust-yet-fragile behavior.

### Required readings

1. Melanie Mitchell, **Complexity: A Guided Tour** [R07](#r07).
2. John H. Miller and Scott E. Page, **Complex Adaptive Systems** [R08](#r08).
3. John Holland, **Hidden Order** — selected chapters [R08A](#r08a).

### Selective/deep readings

- Braha, Minai, and Bar-Yam, eds., **Complex Engineered Systems** [R15](#r15).
- Carlson and Doyle on Highly Optimized Tolerance [R36](#r36).
- Bar-Yam's multiscale engineering work in *Complex Engineered Systems*.

### Exercise

Build a “mechanism dictionary.” For each of 12 mechanisms, include:
- definition;
- minimal example;
- engineering example;
- observable signature;
- modeling method;
- plausible intervention;
- common misconception.

Then select one real system and identify which three mechanisms you believe dominate. State what evidence would change your mind.

### Artifact

A 10–15 page CAS mechanism notebook that can later become a research reference.

### Mastery check

You can hear the sentence “this is a complex system” and immediately ask **“complex in what way, generated by which mechanisms, at what scale?”**

---

<a id="module-3"></a>
## Module 3 — Connect complexity science to systems engineering

### Learning objective

Understand how systems-engineering researchers translate general complexity ideas into engineering questions about architecture, intervention, governance, and lifecycle performance.

### Core concepts

- complex systems vs. complex engineered systems;
- objective and subjective complexity;
- emergence in engineering;
- intervention under incomplete control;
- complexity and architecture;
- complexity across lifecycle stages;
- engineering under uncertainty;
- self-organization as an engineering choice.

### Required readings

1. **INCOSE, A Complexity Primer for Systems Engineers** [R05](#r05).
2. Sarah Sheard and Ali Mostashari, **“Principles of Complex Systems for Systems Engineering”** [R06](#r06).
3. Braha, Minai, and Bar-Yam, eds., **Complex Engineered Systems: Science Meets Technology** — introduction plus selected chapters [R15](#r15).
4. De Weck, Roos, and Magee, **Engineering Systems** [R16](#r16).

### Selective/deep readings

- SEBoK, **Emergence and Complexity** [R03A](#r03a).
- William B. Rouse on complex engineered, organizational, and natural systems.
- Dan Braha's engineering-network work.
- Bar-Yam on multiscale analysis and evolutionary engineering.

### Exercise

Write a comparative analysis of three systems:
1. a complicated but relatively stable engineered product;
2. a complex engineered system;
3. a complex adaptive sociotechnical system.

For each, compare:
- ownership;
- adaptivity;
- predictability;
- requirements stability;
- interface stability;
- governance;
- useful modeling methods;
- suitable intervention style.

### Artifact

A 6–8 page field-positioning essay: **“What changes in systems engineering when the system is complex and adaptive?”**

### Mastery check

You can distinguish a genuine complexity-oriented engineering problem from a merely large or complicated engineering problem and explain why that distinction changes methodology.

---

<a id="module-4"></a>
## Module 4 — Learn sociotechnical problem framing and systems practice

### Learning objective

Develop the ability to work on problems where the system boundary, objectives, and even the definition of the problem are disputed.

### Core concepts

- problem situation vs. formulated problem;
- stakeholder worldview;
- purposeful systems;
- multiple perspectives;
- boundary critique;
- soft vs. hard systems approaches;
- intervention strategy;
- multimethodology;
- participatory modeling;
- organizational/institutional context.

### Required readings

1. Checkland and Scholes, **Soft Systems Methodology in Action** — selected chapters [R12](#r12).
2. Michael C. Jackson, **Critical Systems Practice** material, beginning with the EPIC framework [R13](#r13).
3. Gharajedaghi, **Systems Thinking** — selected chapters [R14](#r14).

### Selective/deep readings

- Derek Hitchins on advanced systems thinking and management.
- Critical Systems Heuristics for boundary critique.
- Participatory systems modeling literature relevant to your domain.

### Exercise

Choose a sociotechnical issue with genuine stakeholder disagreement—for example platform data governance, observability/privacy tradeoffs, AI-assisted operations, or shared infrastructure prioritization.

Create:
- stakeholder map;
- alternative system boundaries;
- competing definitions of success;
- rich-picture or equivalent qualitative map;
- three candidate intervention framings.

Then explain why a purely optimization-based formulation would prematurely close the problem.

### Artifact

A problem-framing dossier and workshop-ready system map.

### Mastery check

You can distinguish **uncertainty about the answer** from **disagreement about what question should be answered**.

---

<a id="module-5"></a>
## Module 5 — Learn systems of systems, governance, and mission thinking

### Learning objective

Learn how engineering changes when authority, ownership, and lifecycle decisions are distributed among semi-autonomous actors.

### Core concepts

- operational independence;
- managerial independence;
- evolutionary development;
- emergent capability;
- constituent-system autonomy;
- interoperability;
- negotiated architecture;
- standards;
- protocols;
- federation;
- decision rights;
- governance;
- mission threads;
- polycentric coordination.

### Required readings

1. Mark Maier, **“Architecting Principles for Systems-of-Systems”** [R17](#r17).
2. Selected chapters from Jamshidi, ed., **System of Systems Engineering: Innovations for the 21st Century** [R18](#r18).
3. Elinor Ostrom, **Governing the Commons** — selected chapters on self-governance and institutional design [R35](#r35).

### Selective/deep readings

- Boardman, Sauser, and Gorod on SoS management and systemigrams.
- Judith Dahmann and SoSE practice literature.
- Mission engineering guides and current INCOSE/DoD materials [R38](#r38).
- Platform governance and standards literature for software/data ecosystems.

### Exercise

Model a federated data ecosystem or multi-team software platform as a system of systems.

Identify:
- constituent systems;
- owners;
- local objectives;
- shared mission/capability;
- interfaces;
- standards;
- incentives;
- decision rights;
- conflicts;
- upgrade/lifecycle mismatch;
- governance mechanisms.

Then design two governance architectures:
1. more centralized;
2. more polycentric/federated.

Compare likely benefits, failure modes, and information requirements.

### Artifact

A SoS systemigram or equivalent context model plus a governance architecture memo.

### Mastery check

You no longer assume “the system owner” exists. You can state precisely who controls what and which outcomes require coordination rather than command.

---
<a id="module-6"></a>
## Module 6 — Build the computational modeling toolkit

### Learning objective

Become capable of choosing and constructing models that preserve the dominant mechanisms of a complex engineered system.

This module is intentionally broader and more technical than the others. It should be treated as a laboratory sequence rather than a single reading block.

### Core concepts

- feedback and stocks/flows;
- heterogeneous agents;
- networks and propagation;
- nonlinear dynamics;
- architecture/dependency matrices;
- stochastic simulation;
- experimental design;
- model comparison;
- sensitivity analysis.

### Track A — System dynamics

**Required:** Sterman, *Business Dynamics* [R19](#r19).

Focus on:
- modeling process;
- causal loops;
- stocks/flows;
- delays;
- path dependence;
- model testing.

**Build:** a feedback model of technical debt, capacity, demand, resilience investment, or organizational staffing.

### Track B — Agent-based modeling

**Required:** Wilensky and Rand [R20](#r20); ODD protocol [R21](#r21).

Focus on:
- agent rules;
- heterogeneity;
- local interaction;
- adaptation;
- stochastic experiments;
- validation.

**Build:** an adaptive coordination, platform, market, routing, or organizational model.

### Track C — Network science

**Required:** Newman [R22](#r22); selected Barabási chapters [R23](#r23).

Focus on:
- structural metrics;
- communities;
- centrality;
- diffusion;
- robustness;
- interdependent networks.

**Build:** a dependency/organizational/infrastructure network and simulate one propagation process on it.

### Track D — Nonlinear dynamics

**Required:** selected Strogatz chapters [R25](#r25).

Focus on:
- stability;
- equilibria;
- bifurcations;
- multiple regimes;
- oscillation;
- tipping.

**Build:** a small model with at least one qualitative regime change.

### Track E — Architecture / DSM

**Required:** Eppinger and Browning [R26](#r26).

Focus on:
- clustering;
- dependency cycles;
- sequencing;
- multidomain architecture.

**Build:** DSM for your recurring reference system.

### Integration exercise

Represent the **same system** using at least three methods. For each representation, answer:

- What becomes visible?
- What disappears?
- What is treated as endogenous?
- What intervention does this method naturally suggest?
- Which conclusions conflict with another method?

### Artifact

A small portfolio containing at least three executable or analyzable models plus a comparative methods memo.

### Mastery check

You can justify model choice from the mechanism and decision question, not from personal tool preference.

---

<a id="module-7"></a>
## Module 7 — Architect under uncertainty and deep uncertainty

### Learning objective

Learn to design systems that preserve value when forecasts are unreliable and assumptions may change.

### Core concepts

- uncertainty taxonomy;
- robustness;
- flexibility;
- optionality;
- staged commitment;
- real options logic;
- architecture evolvability;
- scenario discovery;
- exploratory modeling;
- adaptive pathways;
- signposts and triggers;
- robust-yet-fragile design.

### Required readings

1. De Neufville and Scholtes, **Flexibility in Engineering Design** [R28](#r28).
2. Lempert, **Robust Decision Making** overview [R29](#r29).
3. Haasnoot et al., **Dynamic Adaptive Policy Pathways** [R30](#r30).
4. Carlson and Doyle, **Highly Optimized Tolerance** [R36](#r36).

### Selective/deep readings

- RAND material on exploratory modeling and scenario discovery.
- Real-options literature in engineering systems.
- Robust optimization where uncertainty can be represented mathematically with credible uncertainty sets.
- Resilient/evolvable architecture research from MIT and INCOSE communities.

### Exercise

Take a long-lived architecture decision with substantial uncertainty—for example:
- data storage architecture;
- cloud/vendor strategy;
- infrastructure capacity expansion;
- interoperability standard;
- fleet architecture;
- communications network.

Define:
- irreversible decisions;
- reversible decisions;
- uncertainties;
- candidate options;
- signposts;
- trigger thresholds;
- adaptation actions.

Construct at least three pathways and identify when each becomes preferable.

### Artifact

An adaptive architecture roadmap containing options, signposts, triggers, and decision points.

### Mastery check

You can explain why “better forecasting” is sometimes the wrong response to uncertainty and can design a strategy that learns and adapts as information arrives.

---

<a id="module-8"></a>
## Module 8 — Study safety, resilience, and operational adaptation

### Learning objective

Understand how complex sociotechnical systems fail, succeed, adapt under pressure, and sustain capability near operational boundaries.

### Core concepts

- accidents as interaction/control problems;
- hazards and losses;
- safety constraints;
- unsafe control actions;
- organizational pressure;
- drift and boundary migration;
- work-as-imagined vs. work-as-done;
- graceful extensibility;
- adaptation;
- high-reliability organizing;
- robust-yet-fragile behavior.

### Required readings

1. Nancy Leveson, **Engineering a Safer World** [R31](#r31).
2. Jens Rasmussen, **“Risk Management in a Dynamic Society”** [R32](#r32).
3. Hollnagel, Woods, and Leveson, eds., **Resilience Engineering: Concepts and Precepts** — selected chapters [R33A](#r33a).
4. David Woods, **“Four Concepts for Resilience…”** [R34](#r34).
5. Weick and Sutcliffe, **Managing the Unexpected** — selected chapters [R33](#r33).

### Exercise

Select a documented outage, accident, security incident, or operational failure. Build four interpretations:

1. component failure / fault-chain view;
2. STPA control-structure view;
3. Rasmussen pressure/adaptation view;
4. resilience/HRO view.

Identify interventions uniquely visible under each lens.

Then distinguish interventions aimed at:
- prevention;
- robustness;
- detection;
- containment;
- graceful degradation;
- recovery;
- adaptation;
- organizational learning.

### Artifact

A comparative incident analysis and redesigned control/resilience architecture.

### Mastery check

You can distinguish reliability, robustness, safety, and resilience without treating them as synonyms, and you can explain how normal local adaptation can contribute to system-level risk.

---

<a id="module-9"></a>
## Module 9 — Integrate with MBSE and digital engineering

### Learning objective

Learn how complexity-oriented models can participate in a coherent engineering information environment.

### Core concepts

- system models vs. simulation models;
- semantics;
- traceability;
- architecture;
- requirements;
- model interfaces;
- co-simulation;
- executable architecture;
- digital thread;
- operational data feedback;
- model lifecycle/configuration;
- uncertainty provenance.

### Required readings

1. Current SysML v2 overview/specification materials [R04](#r04).
2. Relevant INCOSE Handbook / SEBoK MBSE material [R02](#r02), [R03](#r03).
3. Review your DSM, network, ABM, SD, and safety models from prior modules.

### Selective/deep readings

- model transformation and FMI/co-simulation literature;
- digital engineering measurement frameworks;
- architecture framework literature relevant to your domain;
- semantic interoperability and knowledge-graph approaches.

### Exercise

Design a **model federation** for your recurring system.

Define:
- authoritative model for architecture;
- authoritative source for requirements;
- external simulations;
- shared parameters;
- units;
- assumptions;
- experiment configuration;
- outputs returned to the system model;
- operational data used for recalibration;
- configuration/version strategy.

### Artifact

A model-integration architecture and data/semantic contract.

### Mastery check

You can explain what MBSE contributes to CAS engineering and what it does not replace. You can also define how multiple analytical models could remain traceable to architecture and decisions.

---

<a id="module-10"></a>
## Module 10 — Learn research design, validation, and reproducibility

### Learning objective

Develop from “model builder” into a researcher capable of making defensible claims about complex engineered systems.

### Core concepts

- research question and claim type;
- conceptual model;
- construct validity;
- verification;
- validation;
- calibration;
- parameter identifiability;
- sensitivity;
- uncertainty;
- simulation experiment design;
- triangulation;
- replication;
- reproducibility;
- case study and mixed methods;
- scope conditions.

### Required readings

1. Revisit model testing/validation chapters in Sterman [R19](#r19).
2. Revisit ABM verification, validation, and replication in Wilensky and Rand [R20](#r20).
3. ODD protocol [R21](#r21).
4. Selected global sensitivity material from Saltelli et al. [R27](#r27).

### Selective/deep readings

- literature on validation of simulation models in your chosen domain;
- design of experiments for stochastic simulation;
- case-study research methods;
- causal inference methods if empirical causal claims are central;
- uncertainty quantification and Bayesian calibration if mathematically appropriate.

### Exercise

Take one model from Module 6 and write a research protocol before running new experiments.

Specify:
- research question;
- hypotheses or exploratory questions;
- model purpose;
- assumptions;
- calibration data;
- validation data;
- experiment design;
- sensitivity plan;
- falsification/update criteria;
- reporting plan;
- reproducibility package.

Then execute the study.

### Artifact

A mini research paper plus reproducibility package.

### Mastery check

You can state exactly what your model supports claiming and can identify where uncertainty, calibration, or structural assumptions weaken the conclusion.

---

<a id="module-11"></a>
## Module 11 — Synthesis and capstone

### Learning objective

Demonstrate that you can analyze and intervene in a complex engineered sociotechnical system using multiple perspectives without collapsing them into one model.

### Required task

Choose one substantive system and produce a research-grade systems analysis using at least:

1. one structural method — DSM, architecture model, or network analysis;
2. one dynamic/adaptive method — system dynamics, ABM, or nonlinear dynamics;
3. one uncertainty/adaptation method — RDM, DAPP, flexibility, or robust analysis;
4. one sociotechnical/governance or safety lens — SSM, institutional analysis, STPA, Rasmussen, resilience engineering, or SoSE governance.

### Required capstone questions

- What is the system of interest, and who contests that boundary?
- Which complexity mechanisms dominate?
- What adapts and at what rate?
- Where does authority reside?
- What is predictable and what is not?
- What system-level behavior is emergent?
- What dependencies create propagation or fragility?
- Which requirements or objectives are stable, and which evolve?
- What interventions are reversible?
- Which futures make the preferred intervention fail?
- What should be monitored after intervention?
- What evidence would cause you to revise the model or intervention?

### Artifact

A capstone package containing:
- 25–40 page report;
- architecture/system maps;
- models and code;
- uncertainty/sensitivity analysis;
- intervention roadmap;
- governance/safety implications;
- limitations;
- reproducibility appendix.

### Mastery check

You can defend why each method is present, explain contradictions among models, and translate the analysis into an intervention strategy that explicitly accounts for uncertainty, adaptation, governance, and learning.

---
<a id="part-vii"></a>
# Part VII — Recurring Reference Systems

The curriculum becomes more coherent if you repeatedly analyze the same one or two systems through different lenses. This lets you see what each method reveals and hides.

## 36. Reference System A — Modern software/data/platform ecosystem

A strong reference system for a reader with software/data experience is a large platform composed of:

- user-facing products;
- APIs;
- data stores;
- pipelines;
- shared infrastructure;
- internal platform services;
- external vendors;
- multiple product and platform teams;
- security/compliance functions;
- changing workloads;
- organizational incentives;
- standards and governance.

### Analyze it repeatedly as

**Conventional SE:** needs, interfaces, architecture, V&V.

**DSM:** service/team/data dependencies and coupling.

**Network science:** propagation, criticality, communities, organizational/technical congruence.

**System dynamics:** technical debt, capacity, demand, staffing, rework, reliability investment.

**ABM:** team/service selection, local optimization, adoption of standards, platform competition.

**SoS:** autonomous teams/services/vendors with different roadmaps and owners.

**Governance:** API standards, data ownership, access policy, shared-service decision rights.

**STPA:** unsafe control actions in deployment, automation, access, or incident response.

**DMDU:** vendor lock-in, architecture evolution, scaling, regulation, AI-driven change.

**MBSE/digital engineering:** traceability among architecture, requirements, simulations, and telemetry.

## 37. Reference System B — Interdependent critical infrastructure

Choose a system involving at least two coupled infrastructures, such as:

- electricity + telecommunications;
- transportation + energy;
- water + power;
- cloud infrastructure + financial/payment services;
- emergency services + communications + transportation.

### Analyze it repeatedly as

- multilayer/interdependent network;
- SoS with distributed owners;
- mission architecture;
- resilience system;
- deep-uncertainty planning problem;
- governance/institutional problem;
- nonlinear demand/capacity system;
- safety/control structure.

These two reference systems prevent the curriculum from becoming a sequence of disconnected theories.

---

<a id="part-viii"></a>
# Part VIII — Questions to Carry While Reading and Modeling

Use these questions as a standing research checklist.

## 38. Ontology and boundary

- What does the author/model treat as the system?
- What is excluded as “environment”?
- Would including organizations, incentives, or institutions change the explanation?
- Is the chosen level of aggregation hiding the relevant mechanism?

## 39. Complexity mechanism

- Is complexity structural, dynamic, adaptive, organizational, goal-related, or uncertain?
- What creates the nonlinearity?
- What feedback loops dominate?
- What is emergent and from what local interactions?
- What changes endogenously?

## 40. Agency and adaptation

- Which actors make decisions?
- What do they know?
- What are they optimizing or satisficing?
- How do they learn?
- Can they strategically respond to the intervention?
- Are their goals aligned?

## 41. Architecture and control

- Where is authority centralized?
- Where is it distributed?
- What is controlled directly versus influenced indirectly?
- What information does the controller need?
- Does the controller possess sufficient variety and response speed?
- Which interfaces enable coordination?

## 42. Uncertainty

- Which variables have meaningful probability distributions?
- Which uncertainties are structural?
- Which future conditions are deeply uncertain?
- Which decisions are irreversible?
- What options can be preserved?
- What signposts could reveal that assumptions are failing?

## 43. Evidence

- What empirical observations support the model?
- Is the result calibrated, validated, or merely illustrative?
- What would falsify the proposed mechanism?
- Are multiple mechanisms capable of reproducing the same macro behavior?
- Is the model being used outside its validated scope?

## 44. Intervention

- Is the intervention model optimization, control, constraint, incentive, modularity, flexibility, governance, redundancy, experimentation, or adaptation?
- Who implements it?
- Who can resist or route around it?
- What new feedback loops will it create?
- Does it shift risk to another actor or scale?
- How reversible is it?

## 45. Learning

- What will be measured after deployment?
- How will the model be updated?
- What trigger causes intervention adaptation or redesign?
- How do we distinguish temporary noise from structural change?

---

<a id="part-ix"></a>
# Part IX — Branches by Research Interest

After completing Modules 0–6, branch more deeply according to the problems you want to study.

## 46. Branch A — Architecture, software, and digital ecosystems

Prioritize:
- DSM and architecture networks;
- Dan Braha and engineering networks;
- platform/ecosystem governance;
- modularity and near-decomposability;
- MBSE/SysML v2;
- technical debt and architecture evolution;
- reliability/resilience of distributed software;
- organizational/technical network congruence;
- real options and architecture flexibility.

Suggested research questions:
- How does dependency topology affect software-system fragility?
- How do team boundaries and architecture boundaries co-evolve?
- When does standardization improve ecosystem coordination versus create correlated failure?
- Which platform interfaces preserve future option value?

## 47. Branch B — Enterprise, organization, and governance

Prioritize:
- Rouse;
- Gharajedaghi;
- Checkland;
- Jackson;
- Ostrom;
- system dynamics;
- organizational network analysis;
- SoS governance;
- institutional adaptation;
- HRO/resilience engineering.

Suggested research questions:
- How do local incentives produce undesirable system-level outcomes?
- Which governance structures support adaptation without fragmentation?
- How do organizations migrate toward operational risk under performance pressure?
- How do decision rights affect learning and resilience?

## 48. Branch C — Infrastructure, resilience, and deep uncertainty

Prioritize:
- network cascades;
- nonlinear dynamics;
- system dynamics;
- RDM and DAPP;
- de Neufville and Scholtes;
- resilience engineering;
- mission engineering;
- SoSE;
- scenario discovery;
- interdependent infrastructure.

Suggested research questions:
- Which architectures remain viable across climate, demand, technology, and policy uncertainty?
- What indicators should trigger infrastructure adaptation?
- How do coupled infrastructures create systemic failure pathways?
- Which investments create flexibility rather than lock-in?

## 49. Branch D — Safety-critical sociotechnical systems

Prioritize:
- Leveson;
- Rasmussen;
- Woods/Hollnagel;
- HSI;
- human-machine teaming;
- control theory/cybernetics;
- organizational adaptation;
- incident data and qualitative field methods.

Suggested research questions:
- How do automation and human adaptation change control-loop safety?
- How should safety constraints evolve in adaptive systems?
- What creates graceful extensibility at operational limits?
- How do local workarounds become system-level hazards or resilience resources?

## 50. Branch E — Autonomous, AI-enabled, and adaptive cyber-physical systems

Prioritize:
- ABM;
- multi-agent systems;
- control and cybernetics;
- assurance of adaptive systems;
- human-machine teaming;
- STPA;
- online monitoring;
- runtime assurance;
- simulation-based testing;
- governance and accountability.

Suggested research questions:
- What should be constrained versus learned?
- How can emergent multi-agent behavior be bounded?
- What monitoring is required when behavior changes after deployment?
- How can assurance cases remain valid as models/policies evolve?

---

<a id="part-x"></a>
# Part X — Capstone Structure

A strong capstone should look less like “apply four techniques” and more like a coherent research argument.

## 51. Recommended report structure

### 1. Problem statement

Define the decision, system, stakeholders, and why conventional bounded analysis is insufficient.

### 2. Complexity diagnosis

Identify the dominant complexity mechanisms and scales. Explain why each matters.

### 3. Competing system framings

Show at least two plausible boundaries or stakeholder perspectives.

### 4. Architecture and dependency model

Represent key components, organizations, interfaces, and dependencies.

### 5. Dynamic/adaptive model

Build and justify the mechanism-level simulation.

### 6. Evidence and validation

Describe data, expert evidence, calibration, validation tests, and uncertainty.

### 7. Failure/vulnerability exploration

Identify where the system fails, becomes brittle, or enters unacceptable regimes.

### 8. Intervention alternatives

Include architectural, operational, governance, and adaptive options—not only parameter tuning.

### 9. Deep-uncertainty analysis

Stress-test alternatives across plausible futures and identify vulnerabilities.

### 10. Adaptation strategy

Define signposts, triggers, reversible actions, and future options.

### 11. Safety/resilience/governance implications

Assess second-order effects, control constraints, decision rights, and distribution of risk.

### 12. Conclusions and scope conditions

State what the evidence supports, what remains unresolved, and what would change the recommendation.

## 52. Capstone quality criteria

A strong capstone:
- makes system boundaries explicit;
- identifies mechanisms rather than merely calling the system complex;
- uses methods because they fit the question;
- shows how models complement or disagree;
- exposes uncertainty rather than burying it;
- validates important assumptions;
- distinguishes exploratory from predictive claims;
- treats governance and humans as part of the system when relevant;
- proposes reversible/adaptive interventions where uncertainty is deep;
- provides a monitoring and learning strategy.

---

<a id="part-xi"></a>
# Part XI — Maintaining a Living View of the Field

This field is too interdisciplinary and fast-moving for a static bibliography to remain complete. Maintain the guide as a living research map.

## 53. Professional anchors to revisit annually

### SEBoK

SEBoK is especially useful for tracking changes in systems science, complexity, SoS, architecture, and professional systems-engineering terminology. As of September 2026, SEBoK v2.14 is the current release; it was published in May 2026 and included a substantial refresh of the Systems Science knowledge area [R03](#r03).

### INCOSE technical products and working groups

Monitor:
- Complex Systems Working Group;
- Systems of Systems Working Group;
- Resilient Systems Working Group;
- Human Systems Integration Working Group;
- Systems Science Working Group;
- Model-Based Systems Engineering / digital engineering activities;
- Agile Systems Engineering;
- relevant symposium proceedings.

### Standards

Track updates to:
- ISO/IEC/IEEE 15288;
- architecture description standards;
- SoS guidance;
- model-based systems-engineering standards;
- SysML.

### Mission engineering

Mission engineering continues to evolve as a practice for linking missions, architectures, systems of systems, models, data, and operational outcomes [R38](#r38). It is a useful area to watch because it forces SE to operate above individual product boundaries.

### SysML v2 ecosystem

SysML v2 reached final adoption in July 2025 [R04](#r04). Over the next several years, watch tool interoperability, APIs, model libraries, simulation integration, and migration from SysML v1.x.

## 54. Maintain a literature matrix

Do not maintain only a bibliography. Maintain a spreadsheet or knowledge base with fields such as:

- citation;
- school/tradition;
- system type;
- complexity mechanism;
- method;
- unit of analysis;
- scale;
- intervention type;
- empirical domain;
- assumptions;
- evidence type;
- validation method;
- software/tool;
- key contribution;
- limitations;
- related papers;
- your notes.

This turns reading into a cumulative map rather than a pile of summaries.

## 55. Recommended reading workflow

For every substantial paper/book chapter:

1. Write the research question in one sentence.
2. State the assumed system boundary.
3. Name the complexity mechanism.
4. Identify the method and representation.
5. Identify the intervention model.
6. Record the empirical evidence.
7. State the strongest claim supported.
8. State one important limitation.
9. Translate it to one of your reference systems.
10. Record one research question it creates.

## 56. Suggested overall ordering

If you want a concise default route through this expanded guide:

1. ISO/INCOSE/SEBoK baseline.
2. Simon + Ashby.
3. Mitchell + Miller/Page.
4. INCOSE Complexity Primer + Sheard/Mostashari.
5. Engineering Systems + Complex Engineered Systems.
6. Maier/SoSE + governance.
7. Sterman + ABM + network science + DSM.
8. De Neufville + RDM + DAPP.
9. Leveson + Rasmussen + resilience engineering.
10. MBSE/SysML v2 integration.
11. Research-methodology module.
12. Capstone.

This ordering moves from **baseline → concepts → engineering perspectives → methods → intervention under uncertainty → assurance → integration → research**.

---

<a id="references"></a>
# Part XII — References

The references below include foundational literature and current professional sources used throughout this guide. Links are provided where a stable publisher, standards-body, professional-society, DOI, or open-access page is available.

## A. Current systems-engineering standards, bodies of knowledge, and professional references

<a id="r01"></a>
**[R01] ISO/IEC/IEEE. (2023). _ISO/IEC/IEEE 15288:2023 — Systems and software engineering — System life cycle processes._**  
https://www.iso.org/standard/81702.html

<a id="r02"></a>
**[R02] INCOSE. (2023). _INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities_, 5th ed.**  
INCOSE describes the handbook as a state-of-good-practice reference aligned with ISO/IEC/IEEE 15288:2023.  
https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/

<a id="r03"></a>
**[R03] Systems Engineering Body of Knowledge (SEBoK). (2026). _SEBoK Version 2.14._**  
Released 18 May 2026; includes a major refresh of the Systems Science knowledge area.  
https://sebokwiki.org/wiki/Version_2.14

<a id="r03a"></a>
**[R03A] SEBoK. (2026). _Emergence and Complexity._**  
https://sebokwiki.org/wiki/Emergence_and_Complexity

<a id="r04"></a>
**[R04] Object Management Group. (2025). _SysML Version 2.0 — Final Adoption._**  
OMG approved final adoption of SysML v2, KerML 1.0, and the SysML API and Services specification in July 2025.  
https://www.omg.org/news/releases/pr2025/07-21-25.htm

<a id="r05"></a>
**[R05] INCOSE Complex Systems Working Group. (2015; revised 2021). _A Complexity Primer for Systems Engineers._**  
https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=COMPPRIME

<a id="r05a"></a>
**[R05A] INCOSE Systems of Systems Working Group. _Systems of Systems Working Group._**  
https://www.incose.org/group/systems-of-systems-working-group/

## B. Complexity science, systems science, cybernetics, and design

<a id="r06"></a>
**[R06] Sheard, S. A., & Mostashari, A. (2009). “Principles of Complex Systems for Systems Engineering.” _Systems Engineering_, 12(4), 295–311.**  
https://doi.org/10.1002/sys.20124

<a id="r07"></a>
**[R07] Mitchell, M. (2009). _Complexity: A Guided Tour._ Oxford University Press.**  
https://doi.org/10.1093/oso/9780195124415.001.0001

<a id="r08"></a>
**[R08] Miller, J. H., & Page, S. E. (2007). _Complex Adaptive Systems: An Introduction to Computational Models of Social Life._ Princeton University Press.**  
https://www.jstor.org/stable/j.ctt7s3kx

<a id="r08a"></a>
**[R08A] Holland, J. H. (1995). _Hidden Order: How Adaptation Builds Complexity._ Basic Books.**  
https://books.google.com/books/about/Hidden_Order.html?id=jQHvAAAAMAAJ

<a id="r09"></a>
**[R09] Simon, H. A. (1962). “The Architecture of Complexity.” _Proceedings of the American Philosophical Society_, 106(6), 467–482.**  
https://www.jstor.org/stable/985254

<a id="r10"></a>
**[R10] Simon, H. A. (1996). _The Sciences of the Artificial_, 3rd ed. MIT Press.**  
https://mitpress.mit.edu/9780262264495/the-sciences-of-the-artificial/

<a id="r11"></a>
**[R11] Ashby, W. R. (1956). _An Introduction to Cybernetics._ Chapman & Hall / Wiley.**  
Open scan/metadata: https://www.biodiversitylibrary.org/item/26977

<a id="r12"></a>
**[R12] Checkland, P., & Scholes, J. (1999). _Soft Systems Methodology in Action: Includes a 30-Year Retrospective._ Wiley.**  
https://www.wiley-vch.de/en/areas-interest/finance-economics-law/soft-systems-methodology-in-action-978-0-471-98605-8

<a id="r13"></a>
**[R13] Jackson, M. C. (2020). “Critical Systems Practice 1: Explore—Starting a Multimethodological Intervention.” _Systems Research and Behavioral Science_, 37(5), 839–858.**  
https://doi.org/10.1002/sres.2746

<a id="r14"></a>
**[R14] Gharajedaghi, J. (2011). _Systems Thinking: Managing Chaos and Complexity: A Platform for Designing Business Architecture_, 3rd ed. Elsevier.**  
https://shop.elsevier.com/books/systems-thinking/gharajedaghi/978-0-12-385915-0

## C. Complex engineered systems, engineering systems, and systems of systems

<a id="r15"></a>
**[R15] Braha, D., Minai, A. A., & Bar-Yam, Y. (Eds.). (2006). _Complex Engineered Systems: Science Meets Technology._ Springer.**  
https://doi.org/10.1007/3-540-32834-3

<a id="r16"></a>
**[R16] de Weck, O. L., Roos, D., & Magee, C. L. (2011). _Engineering Systems: Meeting Human Needs in a Complex Technological World._ MIT Press.**  
https://doi.org/10.7551/mitpress/8799.001.0001

<a id="r17"></a>
**[R17] Maier, M. W. (1998). “Architecting Principles for Systems-of-Systems.” _Systems Engineering_, 1(4), 267–284.**  
https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D

<a id="r18"></a>
**[R18] Jamshidi, M. (Ed.). (2009). _System of Systems Engineering: Innovations for the 21st Century._ Wiley.**  
https://doi.org/10.1002/9780470403501

> **Bibliographic note:** the Wiley volume at DOI 10.1002/9780470403501 is edited by **Mo Jamshidi**. Boardman, Sauser, Gorod, Dahmann, and other important SoSE researchers contribute within this literature; their work remains central to the curriculum.

## D. Modeling and computational methods

<a id="r19"></a>
**[R19] Sterman, J. D. (2000). _Business Dynamics: Systems Thinking and Modeling for a Complex World._ McGraw-Hill.**  
https://www.mheducation.com/highered/product/Business-Dynamics-Sterman.html

<a id="r20"></a>
**[R20] Wilensky, U., & Rand, W. (2015). _An Introduction to Agent-Based Modeling: Modeling Natural, Social, and Engineered Complex Systems with NetLogo._ MIT Press.**  
https://mitpress.mit.edu/9780262731898/an-introduction-to-agent-based-modeling/

<a id="r21"></a>
**[R21] Grimm, V., Railsback, S. F., Vincenot, C. E., et al. (2020). “The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism.” _Journal of Artificial Societies and Social Simulation_, 23(2), 7.**  
https://doi.org/10.18564/jasss.4259

<a id="r22"></a>
**[R22] Newman, M. (2018). _Networks_, 2nd ed. Oxford University Press.**  
https://doi.org/10.1093/oso/9780198805090.001.0001

<a id="r23"></a>
**[R23] Barabási, A.-L. _Network Science._**  
Open online textbook: https://networksciencebook.com/

<a id="r24"></a>
**[R24] Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). “Catastrophic Cascade of Failures in Interdependent Networks.” _Nature_, 464, 1025–1028.**  
https://doi.org/10.1038/nature08932

<a id="r25"></a>
**[R25] Strogatz, S. H. (2018). _Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering_, 2nd ed. CRC Press.**  
https://books.google.com/books/about/Nonlinear_Dynamics_and_Chaos.html?id=A0paDwAAQBAJ

<a id="r26"></a>
**[R26] Eppinger, S. D., & Browning, T. R. (2012). _Design Structure Matrix Methods and Applications._ MIT Press.**  
https://doi.org/10.7551/mitpress/8896.001.0001

<a id="r27"></a>
**[R27] Saltelli, A., Ratto, M., Andres, T., et al. (2008). _Global Sensitivity Analysis: The Primer._ Wiley.**  
https://uat.store.wiley.com/en-us/global-sensitivity-analysis-the-primer-p-9780470725177

## E. Uncertainty, flexibility, and adaptive decision making

<a id="r28"></a>
**[R28] de Neufville, R., & Scholtes, S. (2011). _Flexibility in Engineering Design._ MIT Press.**  
https://mitpress.mit.edu/9780262016230/flexibility-in-engineering-design/

<a id="r29"></a>
**[R29] Lempert, R. J. (2019). “Robust Decision Making (RDM).” In _Decision Making under Deep Uncertainty_. Springer.**  
https://doi.org/10.1007/978-3-030-05252-2_2

<a id="r30"></a>
**[R30] Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). “Dynamic Adaptive Policy Pathways: A Method for Crafting Robust Decisions for a Deeply Uncertain World.” _Global Environmental Change_, 23(2), 485–498.**  
https://doi.org/10.1016/j.gloenvcha.2012.12.006

## F. Safety, resilience, reliability, and robust-yet-fragile systems

<a id="r31"></a>
**[R31] Leveson, N. G. (2012). _Engineering a Safer World: Systems Thinking Applied to Safety._ MIT Press.**  
https://mitpress.mit.edu/9780262297301/engineering-a-safer-world/

<a id="r32"></a>
**[R32] Rasmussen, J. (1997). “Risk Management in a Dynamic Society: A Modelling Problem.” _Safety Science_, 27(2–3), 183–213.**  
https://doi.org/10.1016/S0925-7535(97)00052-0

<a id="r33"></a>
**[R33] Weick, K. E., & Sutcliffe, K. M. (2015). _Managing the Unexpected: Sustained Performance in a Complex World_, 3rd ed. Wiley.**  
https://doi.org/10.1002/9781119175834

<a id="r33a"></a>
**[R33A] Hollnagel, E., Woods, D. D., & Leveson, N. (Eds.). (2006). _Resilience Engineering: Concepts and Precepts._ Ashgate.**  
Bibliographic overview: https://psnet.ahrq.gov/issue/resilience-engineering-concepts-and-precepts

<a id="r34"></a>
**[R34] Woods, D. D. (2015). “Four Concepts for Resilience and the Implications for the Future of Resilience Engineering.” _Reliability Engineering & System Safety_, 141, 5–9.**  
https://doi.org/10.1016/j.ress.2015.03.018

<a id="r36"></a>
**[R36] Carlson, J. M., & Doyle, J. (2000). “Highly Optimized Tolerance: Robustness and Design in Complex Systems.” _Physical Review Letters_, 84(11), 2529–2532.**  
https://doi.org/10.1103/PhysRevLett.84.2529

## G. Governance, institutions, mission, and human systems

<a id="r35"></a>
**[R35] Ostrom, E. (1990). _Governing the Commons: The Evolution of Institutions for Collective Action._ Cambridge University Press.**  
https://doi.org/10.1017/CBO9780511807763

<a id="r38"></a>
**[R38] Office of the Under Secretary of Defense for Research and Engineering. (2023). _Mission Engineering Guide, Version 2.0._**  
https://ac.cto.mil/mission-engineering/

<a id="r38a"></a>
**[R38A] INCOSE. (2024). _Mission Engineering — Extending Systems of Systems Engineering to Mission._**  
https://www.incose.org/resource/mission-engineering-extending-systems-of-systems-engineering-to-mission/

<a id="r39"></a>
**[R39] INCOSE Human Systems Integration Working Group. (2023). _Human Systems Integration: Volume 1 / HSI Primer._**  
https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=HUMANSYSINTV1

<a id="r40"></a>
**[R40] INCOSE. (2024). _Systems Engineering Agility Primer._**  
https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=SYSENGAGIPRIM

## H. Recommended additional researchers and literature streams

These are not all required for the core curriculum, but they are important expansion directions.

### Dan Braha

Read for engineering networks, product-development networks, problem-solving dynamics, bottlenecks, and structural sources of robustness/fragility. Start with [R15] and follow cited work.

### Yaneer Bar-Yam

Read for multiscale complexity, limits of centralized control, evolutionary engineering, and matching system complexity to environmental complexity. Start with his chapter in [R15].

### William B. Rouse

Read for enterprises, organizational transformation, decision support, healthcare systems, and complex engineered/organizational systems.

### Richard de Neufville and the flexibility stream

Read [R28] and related real-options literature for architecture and infrastructure under uncertainty.

### Boardman, Sauser, Gorod, Dahmann, and the SoSE community

Use [R18], current INCOSE SoS Working Group resources [R05A], and associated papers for autonomy, governance, systemigrams, acknowledged systems of systems, and evolutionary development.

### Derek Hitchins

Read for advanced systems thinking, systems practice, and engineering/management of highly interconnected systems.

### Jamshid Gharajedaghi

Read [R14] for purposeful systems, interactive design, enterprise architecture, and organizational complexity.

### Nancy Leveson, Jens Rasmussen, David Woods, Erik Hollnagel

Read [R31]–[R34] as a connected safety/resilience lineage rather than isolated texts.

### John Doyle / robust-yet-fragile systems

Read [R36] and related work on complexity and robustness for a control/design-oriented view of why highly optimized systems can acquire distinctive fragilities.

---

# Closing Guidance

The most important lesson of the curriculum is not that conventional systems engineering is obsolete, nor that complex systems cannot be engineered.

It is that **engineering changes when prediction, authority, stable requirements, and decomposability are limited**.

In those settings, competent practice requires several simultaneous abilities:

- decompose where decomposition is valid;
- preserve interaction effects where decomposition destroys the mechanism;
- model feedback and adaptation;
- understand networks and propagation;
- distinguish uncertainty from deep uncertainty;
- design architectures with flexibility and options;
- treat governance and institutions as part of the engineering problem;
- design for safety and resilience rather than nominal performance alone;
- integrate multiple models without pretending they are equivalent;
- validate claims and expose uncertainty;
- intervene incrementally where possible;
- monitor and learn after deployment.

The mature systems engineer is therefore not trying to eliminate all complexity. The goal is to determine **which complexity must be understood, which can be structured, which can be absorbed, which can be governed, which can be exploited, and which must remain the subject of ongoing learning**.

That is the perspective from which complex adaptive systems become an engineering discipline rather than merely an interesting description of the world.
