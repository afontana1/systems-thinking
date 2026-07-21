# The Systems Engineering V: Analyses, Methods, and Evidence

The systems engineering **V** is best understood as a relationship between definition and evidence, not as a rigid one-pass sequence. The left side progressively defines the problem, intended use, requirements, architecture, and detailed design. The bottom realizes the solution. The right side integrates the realized elements and accumulates objective evidence that the solution was built correctly and is suitable for its intended use. Operations, support, change, and retirement extend beyond the development V and feed new information back into it. ([SEBoK][1])

This handbook separates two ideas that are often mixed together:

1. **Where an analysis is used in the V.** The phase map explains the decision being made, the required fidelity, and the evidence expected at each point.
2. **What the analysis actually is.** The consolidated catalog explains each recurring analysis once: its purpose, justification, method, inputs, outputs, what it reveals, limitations, and links to other analyses.

An analysis may appear in several phases without being a different analysis. For example, capacity analysis begins as a rough feasibility check, becomes a quantitative requirement-setting tool, supports architecture sizing, is verified under representative load, and continues during operations. Later phase sections therefore link back to the same authoritative method description rather than redefining it.

## Table of contents

* [The Systems Engineering V: Analyses, Methods, and Evidence](#the-systems-engineering-v-analyses-methods-and-evidence)
* [Part I — How to use analyses across the V](#part-i--how-to-use-analyses-across-the-v)
    * [1. Interpreting analysis maturity across the lifecycle](#1-interpreting-analysis-maturity-across-the-lifecycle)
    * [2. Minimum analysis discipline](#2-minimum-analysis-discipline)
    * [3. Problem, opportunity, and mission analysis](#3-problem-opportunity-and-mission-analysis)
    * [4. Feasibility and concept exploration](#4-feasibility-and-concept-exploration)
    * [5. Stakeholder needs and Concept of Operations](#5-stakeholder-needs-and-concept-of-operations)
    * [6. System requirements definition](#6-system-requirements-definition)
    * [7. Architecture and high-level design](#7-architecture-and-high-level-design)
    * [8. Subsystem and detailed design](#8-subsystem-and-detailed-design)
    * [9. Implementation, build, procure, and configure](#9-implementation-build-procure-and-configure)
    * [10. Unit and component verification](#10-unit-and-component-verification)
    * [11. Integration and integration verification](#11-integration-and-integration-verification)
    * [12. System verification](#12-system-verification)
    * [13. System validation and transition](#13-system-validation-and-transition)
    * [14. Operations, support, improvement, and evolution](#14-operations-support-improvement-and-evolution)
    * [15. Retirement, disposal, replacement, and knowledge transfer](#15-retirement-disposal-replacement-and-knowledge-transfer)
* [Part II — Consolidated analysis-method catalog](#part-ii--consolidated-analysis-method-catalog)
    * [16. Mission, needs, capability, and gap analysis](#16-mission-needs-capability-and-gap-analysis)
    * [17. Stakeholder, context, and boundary analysis](#17-stakeholder-context-and-boundary-analysis)
    * [18. Current-state process, value-stream, and bottleneck analysis](#18-current-state-process-value-stream-and-bottleneck-analysis)
    * [19. Root-cause, Pareto, and causal analysis](#19-root-cause-pareto-and-causal-analysis)
    * [20. Demand, workload, and forecasting analysis](#20-demand-workload-and-forecasting-analysis)
    * [21. Capacity, throughput, utilization, and constraint analysis](#21-capacity-throughput-utilization-and-constraint-analysis)
    * [22. Queueing and waiting-time analysis](#22-queueing-and-waiting-time-analysis)
    * [23. Feasibility analysis](#23-feasibility-analysis)
    * [24. Analysis of alternatives, trade-space, and multi-criteria decision analysis](#24-analysis-of-alternatives-trade-space-and-multi-criteria-decision-analysis)
    * [25. Cost-benefit, business-case, and lifecycle-cost analysis](#25-cost-benefit-business-case-and-lifecycle-cost-analysis)
    * [26. Risk, opportunity, uncertainty, sensitivity, and Monte Carlo analysis](#26-risk-opportunity-uncertainty-sensitivity-and-monte-carlo-analysis)
    * [27. Functional analysis and allocation](#27-functional-analysis-and-allocation)
    * [28. Requirements analysis, quality, allocation, and traceability](#28-requirements-analysis-quality-allocation-and-traceability)
    * [29. Interface, dependency, and integration analysis](#29-interface-dependency-and-integration-analysis)
    * [30. Performance budgeting, margins, and robustness analysis](#30-performance-budgeting-margins-and-robustness-analysis)
    * [31. Reliability, availability, maintainability, and supportability analysis](#31-reliability-availability-maintainability-and-supportability-analysis)
    * [32. FMEA and FMECA](#32-fmea-and-fmeca)
    * [33. Fault-tree, event-tree, hazard, and safety-control analysis](#33-fault-tree-event-tree-hazard-and-safety-control-analysis)
    * [34. Security threat, vulnerability, and resilience analysis](#34-security-threat-vulnerability-and-resilience-analysis)
    * [35. Human factors, workload, staffing, and human-system integration analysis](#35-human-factors-workload-staffing-and-human-system-integration-analysis)
    * [36. Discrete-event, agent-based, system-dynamics, and hybrid simulation](#36-discrete-event-agent-based-system-dynamics-and-hybrid-simulation)
    * [37. Optimization, allocation, scheduling, routing, and network analysis](#37-optimization-allocation-scheduling-routing-and-network-analysis)
    * [38. Inventory, spare-parts, supply-network, and logistics analysis](#38-inventory-spare-parts-supply-network-and-logistics-analysis)
    * [39. Statistical process control, process capability, and measurement-system analysis](#39-statistical-process-control-process-capability-and-measurement-system-analysis)
    * [40. Design of experiments, hypothesis testing, and statistical verification](#40-design-of-experiments-hypothesis-testing-and-statistical-verification)
    * [41. Reliability demonstration, life-data, and accelerated-testing analysis](#41-reliability-demonstration-life-data-and-accelerated-testing-analysis)
    * [42. Verification planning, coverage, evidence sufficiency, and closure analysis](#42-verification-planning-coverage-evidence-sufficiency-and-closure-analysis)
    * [43. Validation, operational evaluation, pilot, and benefit-realization analysis](#43-validation-operational-evaluation-pilot-and-benefit-realization-analysis)
    * [44. Maintenance, replacement, and renewal analysis](#44-maintenance-replacement-and-renewal-analysis)
    * [45. Lean, Six Sigma, continuous-improvement, and productivity analysis](#45-lean-six-sigma-continuous-improvement-and-productivity-analysis)
    * [46. Retirement, reverse-logistics, data-disposition, and transition analysis](#46-retirement-reverse-logistics-data-disposition-and-transition-analysis)
* [Part III — Cross-reference guides](#part-iii--cross-reference-guides)
    * [47. Analysis families by V phase](#47-analysis-families-by-v-phase)
    * [48. Selecting an analysis by engineering question](#48-selecting-an-analysis-by-engineering-question)
    * [49. Standard analysis report template](#49-standard-analysis-report-template)
    * [50. Domain tailoring](#50-domain-tailoring)
    * [51. Final principles](#51-final-principles)

---

# Part I — How to use analyses across the V

## 1. Interpreting analysis maturity across the lifecycle

The same named analysis should become more rigorous as uncertainty decreases and the cost of error increases. Early analyses are often comparative and order-of-magnitude: they identify dominant drivers, eliminate infeasible concepts, and expose missing information. Later analyses use controlled baselines, validated models, measured data, explicit uncertainty, configuration control, and documented acceptance criteria.

| Maturity | Typical question | Appropriate evidence | Common mistake |
| --- | --- | --- | --- |
| Exploratory | What might work, and what could dominate the decision? | Scenarios, ranges, simple models, expert judgment | Presenting rough estimates as predictions |
| Comparative | Which alternative is preferable and why? | Common assumptions, normalized criteria, sensitivity results | Comparing alternatives with inconsistent baselines |
| Allocative | What targets and budgets should each element receive? | Traceable requirements, budgets, margins, allocation rationale | Allocating targets without feasibility evidence |
| Predictive | Will the design meet its requirements? | Calibrated analytical or simulation models, uncertainty bounds | Ignoring model-form uncertainty |
| Confirmatory | Did the realized system meet the requirement? | Controlled tests, inspections, analyses, demonstrations | Treating model output alone as sufficient evidence |
| Operational | Is the fielded system still effective, affordable, and safe? | Observed performance, trends, incidents, maintenance and cost data | Failing to update assumptions with field evidence |

## 2. Minimum analysis discipline

Every consequential analysis should state the decision it supports, the system boundary, the baseline or alternatives being compared, the assumptions, data sources, model form, uncertainty treatment, acceptance or decision criteria, configuration/version, reviewer, and residual limitations. A numerical result without this context is not decision evidence; it is only a number.

A practical analysis record should answer:

* What decision, requirement, risk, or claim is being supported?
* What is included and excluded from the system boundary?
* What data, assumptions, and scenarios drive the result?
* Why is the selected method suitable?
* How was the model checked, calibrated, or validated?
* How sensitive is the conclusion to uncertainty?
* What result would change the decision?
* What follow-on work is required?

---

# 3. Problem, opportunity, and mission analysis

**Purpose.** Decide whether intervention is warranted, define the outcome that matters, and distinguish symptoms from the underlying mission or business problem.

**Analyses most often used.**

* [Mission, needs, capability, and gap analysis](#16-mission-needs-capability-and-gap-analysis)
* [Stakeholder, context, and boundary analysis](#17-stakeholder-context-and-boundary-analysis)
* [Current-state process, value-stream, and bottleneck analysis](#18-current-state-process-value-stream-and-bottleneck-analysis)
* [Root-cause, Pareto, and causal analysis](#19-root-cause-pareto-and-causal-analysis)
* [Mission, needs, capability, and gap analysis](#16-mission-needs-capability-and-gap-analysis)
* [Demand and workload](#20-demand-workload-and-forecasting-analysis), [capacity](#21-capacity-throughput-utilization-and-constraint-analysis), and [queueing](#22-queueing-and-waiting-time-analysis)
* Baseline cost and performance analysis
* [Risk, opportunity, uncertainty, sensitivity, and Monte Carlo analysis](#26-risk-opportunity-uncertainty-sensitivity-and-monte-carlo-analysis)

**How the analyses are used here.** Methods are deliberately broad and low-cost. Use ranges, scenarios, direct observation, interviews, existing operational data, and simple process or workload models. The aim is not to select a design; it is to establish a defensible problem boundary and show that the observed shortfall is real, material, and addressable.

**Expected outputs and evidence.**

* Approved problem or opportunity statement
* System-of-interest boundary and context
* Stakeholder map and concern set
* Current-state workflow and baseline measures
* Capability gaps and initial measures of effectiveness
* Assumption, issue, risk, and data-quality log

# 4. Feasibility and concept exploration

**Purpose.** Generate credible solution concepts, eliminate infeasible options, and justify a preferred direction before detailed requirements and design commitments make change expensive.

**Analyses most often used.**

* [Feasibility analysis](#23-feasibility-analysis)
* [Analysis of alternatives, trade-space, and MCDA](#24-analysis-of-alternatives-trade-space-and-multi-criteria-decision-analysis)
* [Analysis of alternatives, trade-space, and MCDA](#24-analysis-of-alternatives-trade-space-and-multi-criteria-decision-analysis)
* [Cost-benefit, business-case, and lifecycle-cost analysis](#25-cost-benefit-business-case-and-lifecycle-cost-analysis)
* Technology readiness and maturity assessment
* [Risk, uncertainty, sensitivity, and Monte Carlo analysis](#26-risk-opportunity-uncertainty-sensitivity-and-monte-carlo-analysis)
* Make-buy-partner analysis
* Preliminary safety, security, reliability, supportability, and regulatory analysis

**How the analyses are used here.** Use a common set of scenarios and assumptions for all alternatives. Model only enough detail to discriminate among concepts. Explore ranges rather than single-point predictions, identify Pareto-efficient alternatives, and test whether the recommendation survives changes in weights, costs, demand, performance assumptions, and risk.

**Expected outputs and evidence.**

* Concept descriptions and common evaluation baseline
* Feasibility findings and eliminated alternatives
* Trade-space and sensitivity results
* Preferred concept with decision rationale
* Initial lifecycle cost, schedule, and risk ranges
* Key technology, policy, and evidence maturation plans

# 5. Stakeholder needs and Concept of Operations

**Purpose.** Describe how people and organizations will use the future system, under what conditions, and what observable outcomes will constitute operational success.

**Analyses most often used.**

* [Mission and needs analysis](#16-mission-needs-capability-and-gap-analysis) and [functional analysis](#27-functional-analysis-and-allocation)
* Use-case and scenario analysis
* [Human factors, workload, staffing, and human-system integration analysis](#35-human-factors-workload-staffing-and-human-system-integration-analysis)
* [Demand](#20-demand-workload-and-forecasting-analysis), [capacity](#21-capacity-throughput-utilization-and-constraint-analysis), and [queueing](#22-queueing-and-waiting-time-analysis)
* Interoperability-in-use analysis
* Degraded-mode and contingency analysis
* Stakeholder priority and conflict analysis

**How the analyses are used here.** Develop normal, peak, degraded, emergency, maintenance, and recovery scenarios. Allocate activities to humans, organizations, automation, and external systems. Quantify operating tempo, arrivals, workload, decision time, resource contention, and environmental constraints wherever these affect feasibility or acceptance.

**Expected outputs and evidence.**

* ConOps or OpsCon
* Operational scenarios and mission threads
* User, operator, maintainer, and support roles
* Operational states and degraded modes
* Candidate measures of effectiveness and acceptance conditions
* Operational data and workload assumptions

# 6. System requirements definition

**Purpose.** Translate stakeholder needs and operational scenarios into necessary, feasible, unambiguous, traceable, and verifiable requirements.

**Analyses most often used.**

* [Requirements analysis, quality, allocation, and traceability](#28-requirements-analysis-quality-allocation-and-traceability)
* [Functional analysis and allocation](#27-functional-analysis-and-allocation) and [performance budgeting](#30-performance-budgeting-margins-and-robustness-analysis)
* [Interface, dependency, and integration analysis](#29-interface-dependency-and-integration-analysis)
* Capacity, throughput, latency, reliability, availability, and service-level target setting
* Constraint and resource-envelope analysis
* [Requirements analysis, quality, allocation, and traceability](#28-requirements-analysis-quality-allocation-and-traceability)
* [Verification planning, coverage, evidence sufficiency, and closure analysis](#42-verification-planning-coverage-evidence-sufficiency-and-closure-analysis)
* Risk-based prioritization and QFD

**How the analyses are used here.** Derive requirements from scenarios, hazards, interfaces, regulations, and quantitative analyses rather than from preference. Express required conditions and measurable outcomes without prematurely prescribing design. Check each requirement for necessity, singularity, feasibility, verifiability, assumptions, source, and downstream allocation.

**Expected outputs and evidence.**

* Baselined stakeholder and system requirements
* Measures, thresholds, objectives, tolerances, and margins
* Interface requirements and external constraints
* Bidirectional traceability
* Verification cross-reference basis
* Unresolved conflicts, assumptions, and feasibility risks

# 7. Architecture and high-level design

**Purpose.** Select and justify a logical and physical structure that can satisfy the requirements with acceptable performance, risk, cost, adaptability, and lifecycle burden.

**Analyses most often used.**

* [Functional analysis and allocation](#27-functional-analysis-and-allocation)
* [Analysis of alternatives, trade-space, and MCDA](#24-analysis-of-alternatives-trade-space-and-multi-criteria-decision-analysis)
* [Interface, dependency, and integration analysis](#29-interface-dependency-and-integration-analysis)
* [Capacity analysis](#21-capacity-throughput-utilization-and-constraint-analysis) and [optimization/network analysis](#37-optimization-allocation-scheduling-routing-and-network-analysis)
* [RAM and supportability analysis](#31-reliability-availability-maintainability-and-supportability-analysis)
* [Safety analysis](#33-fault-tree-event-tree-hazard-and-safety-control-analysis) and [security/resilience analysis](#34-security-threat-vulnerability-and-resilience-analysis)
* Maintainability, supportability, modularity, and scalability analysis
* [Simulation](#36-discrete-event-agent-based-system-dynamics-and-hybrid-simulation) and [optimization](#37-optimization-allocation-scheduling-routing-and-network-analysis)

**How the analyses are used here.** Compare architectural alternatives with consistent missions, loads, and requirements. Allocate functions, performance budgets, resources, failure containment, and verification responsibilities. Analyze interfaces and dependencies early because they drive integration risk. Preserve margins and document architecture decisions and rejected alternatives.

**Expected outputs and evidence.**

* Selected logical and physical architecture
* Function-to-element allocation baseline
* Interface and dependency baseline
* Performance, resource, reliability, and safety budgets
* Architecture decision records and trade results
* High-risk interfaces, technologies, and verification needs

# 8. Subsystem and detailed design

**Purpose.** Refine the architecture into buildable, procurable, configurable, maintainable, and testable components and processes.

**Analyses most often used.**

* Detailed performance and domain analyses
* [Performance budgeting, margins, and robustness analysis](#30-performance-budgeting-margins-and-robustness-analysis)
* [FMEA/FMECA](#32-fmea-and-fmeca), [safety analysis](#33-fault-tree-event-tree-hazard-and-safety-control-analysis), and [security analysis](#34-security-threat-vulnerability-and-resilience-analysis)
* Design for manufacture, assembly, test, reliability, maintainability, and human use
* [SPC, process capability, and measurement-system analysis](#39-statistical-process-control-process-capability-and-measurement-system-analysis)
* Detailed resource loading, scheduling, and cost allocation
* Supplier, sourcing, and configuration analysis
* [Design of experiments](#40-design-of-experiments-hypothesis-testing-and-statistical-verification) and [optimization](#37-optimization-allocation-scheduling-routing-and-network-analysis)

**How the analyses are used here.** Use higher-fidelity models tied to controlled design baselines. Close budgets at component level, quantify tolerance and interaction effects, identify failure modes, and design observability, controllability, diagnostics, access, test points, and production processes into the solution rather than adding them later.

**Expected outputs and evidence.**

* Detailed design and interface packages
* Component specifications and tolerances
* Updated failure, hazard, threat, and control analyses
* Manufacturing, software, service, and test process definitions
* Unit verification procedures and expected-result models
* Released configuration baseline

# 9. Implementation, build, procure, and configure

**Purpose.** Realize the defined elements repeatably while controlling variation, supplier performance, schedule, cost, quality, and configuration.

**Analyses most often used.**

* Production and service-process planning
* [Capacity analysis](#21-capacity-throughput-utilization-and-constraint-analysis) and [optimization/scheduling](#37-optimization-allocation-scheduling-routing-and-network-analysis)
* [Inventory, spare-parts, supply-network, and logistics analysis](#38-inventory-spare-parts-supply-network-and-logistics-analysis)
* [SPC, process capability, and measurement-system analysis](#39-statistical-process-control-process-capability-and-measurement-system-analysis)
* Yield, scrap, rework, defect, and learning-curve analysis
* Supplier readiness and incoming-quality analysis
* Cost, schedule, and earned-value analysis
* Process validation and configuration audits

**How the analyses are used here.** Model the realization system as carefully as the product when throughput, quality, or ramp-up matters. Establish standard work and process controls, confirm measurement capability, qualify special processes, analyze bottlenecks, and ensure that every realized item remains traceable to approved configuration and evidence.

**Expected outputs and evidence.**

* Conforming realized components or configured services
* Qualified suppliers and validated processes
* Production and deployment readiness evidence
* Yield, capability, throughput, and schedule status
* Nonconformance and corrective-action records
* As-built and as-configured baselines

# 10. Unit and component verification

**Purpose.** Demonstrate that each lowest-level realized element satisfies its allocated requirements before integration obscures defects and makes diagnosis expensive.

**Analyses most often used.**

* Test readiness and procedure analysis
* [SPC, process capability, and measurement-system analysis](#39-statistical-process-control-process-capability-and-measurement-system-analysis)
* [Design of experiments and statistical verification](#40-design-of-experiments-hypothesis-testing-and-statistical-verification)
* Acceptance sampling and statistical compliance analysis
* [Reliability demonstration, life-data, and accelerated-testing analysis](#41-reliability-demonstration-life-data-and-accelerated-testing-analysis)
* Defect Pareto and root-cause analysis
* Margin, robustness, and failure-injection analysis

**How the analyses are used here.** Verify against the controlled requirement and configuration, not against design intent or informal expectations. Establish traceability, calibrated instrumentation, environmental conditions, sample size, decision rules, uncertainty, and handling of anomalies before testing. Preserve raw evidence and configuration metadata.

**Expected outputs and evidence.**

* Requirement-linked unit evidence
* Test and analysis reports
* Calibrated measurement and uncertainty records
* Nonconformances, failure analyses, and corrective actions
* Verified component baseline and integration release status

# 11. Integration and integration verification

**Purpose.** Combine elements in a risk-informed sequence and confirm that interfaces, interactions, timing, data, controls, and emergent behaviors work as intended.

**Analyses most often used.**

* [Interface, dependency, and integration analysis](#29-interface-dependency-and-integration-analysis)
* Interface compatibility and contract verification
* Configuration consistency analysis
* Shared-lab and test-resource capacity analysis
* Fault isolation and diagnostic analysis
* Defect clustering, rework, and bottleneck analysis
* Incremental risk updating and evidence closure

**How the analyses are used here.** Integrate around risk, not convenience alone. Address volatile, novel, high-coupling, safety-critical, and low-observability interfaces early. Use emulators, stubs, software-in-the-loop, hardware-in-the-loop, and incremental builds where they accelerate learning. Recheck assumptions as real components replace models.

**Expected outputs and evidence.**

* Verified interfaces and integrated increments
* Integration evidence and anomaly history
* Updated dependency, configuration, and risk status
* Fault-isolation and diagnostic evidence
* Release basis for system-level verification

# 12. System verification

**Purpose.** Provide objective evidence that the fully integrated system satisfies the specified system requirements.

**Analyses most often used.**

* [Verification planning, coverage, evidence sufficiency, and closure analysis](#42-verification-planning-coverage-evidence-sufficiency-and-closure-analysis)
* [Verification planning, coverage, evidence sufficiency, and closure analysis](#42-verification-planning-coverage-evidence-sufficiency-and-closure-analysis)
* Statistical performance and robustness analysis
* Environmental qualification
* Reliability, availability, safety, security, and resilience verification
* Load, stress, endurance, and failure-recovery analysis
* Waiver, deviation, and residual-risk analysis

**How the analyses are used here.** Use the verification method selected when the requirement was defined unless an approved change is justified. Test representative boundaries, loads, modes, interfaces, and environments—not only nominal points. Combine test, demonstration, inspection, and validated analysis where appropriate, while maintaining requirement-level traceability.

**Expected outputs and evidence.**

* Requirement-by-requirement objective evidence
* Verification report and closure status
* Qualification and compliance evidence
* Residual noncompliances, waivers, and limitations
* Validated technical performance baseline
* Readiness basis for validation and transition

# 13. System validation and transition

**Purpose.** Build confidence that the system accomplishes its intended use in its actual or representative operational environment and that users and supporting organizations can adopt it successfully.

**Analyses most often used.**

* [Validation, operational evaluation, pilot, and benefit-realization analysis](#43-validation-operational-evaluation-pilot-and-benefit-realization-analysis)
* User acceptance, usability, and human-performance analysis
* [Validation, operational evaluation, pilot, and benefit-realization analysis](#43-validation-operational-evaluation-pilot-and-benefit-realization-analysis)
* Staffing, training, support, and organizational readiness analysis
* Deployment, migration, rollout, and cutover analysis
* Benefit-realization and cost-to-serve analysis
* Post-deployment risk and contingency analysis

**How the analyses are used here.** Validation uses stakeholder outcomes and operational scenarios rather than merely repeating requirement tests. Include representative users, workloads, environments, interfaces, policies, support arrangements, and degraded conditions. Distinguish technical readiness from organizational readiness and from benefit realization.

**Expected outputs and evidence.**

* Validation and user-acceptance evidence
* Transition or deployment authorization
* Training, staffing, support, and cutover readiness
* Operational limitations and residual risks
* Initial operational capability or equivalent acceptance
* Post-deployment measurement and learning plan

# 14. Operations, support, improvement, and evolution

**Purpose.** Sustain mission effectiveness, safety, service, affordability, and adaptability while learning from actual use.

**Analyses most often used.**

* [SPC, process capability, and measurement-system analysis](#39-statistical-process-control-process-capability-and-measurement-system-analysis)
* [RAM and supportability analysis](#31-reliability-availability-maintainability-and-supportability-analysis)
* [Maintenance and replacement](#44-maintenance-replacement-and-renewal-analysis) and [spares/logistics](#38-inventory-spare-parts-supply-network-and-logistics-analysis)
* Demand forecasting, capacity, queueing, staffing, routing, and dispatch analysis
* Incident, defect, root-cause, and corrective-action analysis
* Lifecycle cost and cost-to-serve analysis
* Configuration, change-impact, obsolescence, and technical-debt analysis
* [Lean, Six Sigma, continuous-improvement, and productivity analysis](#45-lean-six-sigma-continuous-improvement-and-productivity-analysis)

**How the analyses are used here.** Replace assumed demand, failure, repair, and usage distributions with observed data. Monitor leading and lagging indicators, distinguish common-cause from special-cause variation, and update maintenance, inventory, staffing, and capacity policies. Feed systemic issues back into requirements, architecture, and design baselines.

**Expected outputs and evidence.**

* Operational performance and reliability trends
* Maintenance, spares, staffing, and capacity policies
* Improvement and modernization backlog
* Updated lifecycle cost and risk outlook
* Change proposals and refreshed baselines
* Evidence for upgrade, redesign, or replacement

# 15. Retirement, disposal, replacement, and knowledge transfer

**Purpose.** Remove, replace, repurpose, archive, or dispose of the system without creating unacceptable mission, safety, security, environmental, legal, or continuity risk.

**Analyses most often used.**

* [Maintenance, replacement, and renewal analysis](#44-maintenance-replacement-and-renewal-analysis)
* [Maintenance, replacement, and renewal analysis](#44-maintenance-replacement-and-renewal-analysis)
* Transition capacity and cutover analysis
* Data migration, retention, and archival analysis
* [Retirement, reverse-logistics, data-disposition, and transition analysis](#46-retirement-reverse-logistics-data-disposition-and-transition-analysis)
* Inventory depletion and supplier-exit analysis
* Environmental, safety, security, and compliance analysis
* Workforce and knowledge-transfer analysis

**How the analyses are used here.** Treat retirement as a system transition, not merely a shutdown. Identify dependent users and systems, retained obligations, hazardous materials, sensitive data, residual interfaces, support commitments, and successor capacity. Model phased and immediate options and preserve evidence and lessons needed by successor systems.

**Expected outputs and evidence.**

* Retirement or replacement decision package
* Decommissioning, migration, disposal, and archival plans
* Continuity and rollback provisions
* Asset, data, and compliance disposition evidence
* Lessons learned and transferred knowledge
* Closed configuration and contract obligations

---

# Part II — Consolidated analysis-method catalog

The following sections are the authoritative descriptions of recurring analysis families. Phase sections should reference these methods and specify the required fidelity rather than restating the method.

# 16. Mission, needs, capability, and gap analysis

**Purpose.** Establish why a system intervention may be needed, what outcomes matter, and what capability shortfall prevents those outcomes.

**Why it is justified.** Without a clear mission and gap, a program can optimize a solution to the wrong problem. This analysis provides the logical chain from strategic intent to observable deficiency and creates the basis for measures of effectiveness.

**How to perform it.**

1. Define the mission or business outcome and the affected stakeholders.
2. Describe the current operating context and system boundary.
3. Identify required capabilities and current capability levels.
4. Compare required and current performance using evidence and scenarios.
5. Separate root capability gaps from symptoms, local inefficiencies, and proposed solutions.
6. Prioritize gaps by mission consequence, urgency, reach, and tractability.

**What it reveals.** It reveals whether the problem is real and material, which stakeholders experience it, where the performance shortfall occurs, and whether a new system is necessary or whether policy, process, training, staffing, or existing assets could close the gap.

**Typical inputs.**

* Mission outcomes and strategic objectives
* Operational evidence and baseline measures
* Stakeholder concerns
* Current and required capability descriptions
* Constraints, threats, policies, and assumptions

**Typical outputs and decisions supported.**

* Problem or opportunity statement
* Capability map and gap register
* Initial measures of effectiveness
* Scope boundary and intervention hypotheses

**Important limitations and misuse risks.** Use this analysis during mission framing and revisit it when operational evidence, strategy, threats, technology, or policy changes. Avoid embedding a preferred solution in the need statement.

# 17. Stakeholder, context, and boundary analysis

**Purpose.** Identify who has interests in the system, what surrounds it, which interactions cross its boundary, and which concerns the architecture must address.

**Why it is justified.** Many failures originate outside the designed product: unclear ownership, omitted users, unmanaged external systems, conflicting incentives, or hidden regulatory and environmental constraints. Boundary clarity prevents unowned interfaces and invalid assumptions.

**How to perform it.**

1. Identify users, operators, maintainers, owners, acquirers, regulators, suppliers, affected communities, and external-system owners.
2. Elicit each stakeholder’s decisions, concerns, constraints, success criteria, and authority.
3. Draw the system-of-interest boundary and external entities.
4. Catalog flows of information, material, energy, money, commands, and responsibility.
5. Record assumptions about external behavior and identify who validates them.
6. Map concerns to viewpoints, requirements, analyses, and evidence.

**What it reveals.** It reveals omitted stakeholders, conflicting objectives, external dependencies, ownership gaps, trust boundaries, environmental constraints, and interfaces that require agreements rather than only technical design.

**Typical inputs.**

* Strategy, contracts, regulations, organization charts
* Interviews and operational observation
* Existing context diagrams and interface documents
* Known external systems and environments

**Typical outputs and decisions supported.**

* Stakeholder and concern register
* Context and boundary diagrams
* External-interface inventory
* Assumption and dependency log

**Important limitations and misuse risks.** Perform early, but maintain continuously. A boundary change is an architecture change and should trigger impact analysis.

# 18. Current-state process, value-stream, and bottleneck analysis

**Purpose.** Understand how work is currently performed, where time and resources are consumed, and which constraints limit flow or value delivery.

**Why it is justified.** Proposed systems often automate non-value-added work or move a bottleneck rather than remove it. Direct analysis of the current process provides the baseline needed to justify change and quantify improvement.

**How to perform it.**

1. Select an end-to-end value stream and define start and finish conditions.
2. Observe actual work rather than relying only on procedures.
3. Map activities, handoffs, queues, rework loops, information flows, decision points, and delays.
4. Measure processing time, waiting time, work in process, yield, demand, staffing, and variability.
5. Identify the constraining resource or policy and test whether it shifts under different demand.
6. Develop improvement hypotheses and predict system-level effects.

**What it reveals.** It reveals hidden queues, rework, excessive handoffs, non-value-added activity, policy constraints, uneven workload, local optimization, and the difference between touch time and elapsed time.

**Typical inputs.**

* Transaction or work-order histories
* Observation, interviews, work sampling, and time studies
* Process procedures and layouts
* Demand, staffing, defect, and delay data

**Typical outputs and decisions supported.**

* As-is process or value-stream map
* Baseline cycle-time and flow-efficiency measures
* Bottleneck and waste findings
* Candidate future-state interventions

**Important limitations and misuse risks.** Use before specifying automation or capacity. Validate the map with the people who perform and receive the work.

# 19. Root-cause, Pareto, and causal analysis

**Purpose.** Move from observed symptoms to plausible underlying mechanisms and identify which causes merit action.

**Why it is justified.** Correcting the most visible symptom can suppress evidence while leaving the system vulnerable. Root-cause analysis creates a causal explanation that can be tested and supports corrective action at the appropriate level.

**How to perform it.**

1. Define the problem precisely: what, where, when, magnitude, and affected conditions.
2. Stratify data by time, product, user, environment, supplier, mode, or other relevant factors.
3. Use Pareto analysis to focus on dominant categories without assuming the largest category is the root cause.
4. Develop causal hypotheses using event timelines, five-whys, fishbone diagrams, fault trees, or causal graphs.
5. Test hypotheses against evidence, counterexamples, and controlled experiments where possible.
6. Select corrective actions that break or control the causal path and define recurrence measures.

**What it reveals.** It reveals concentration of losses, causal chains, common contributors, latent organizational or design conditions, and whether different symptoms share a common mechanism.

**Typical inputs.**

* Incident, defect, delay, cost, or failure records
* Configuration and environmental data
* Interviews, logs, and physical evidence
* Process and architecture models

**Typical outputs and decisions supported.**

* Problem definition and causal model
* Verified or ranked root causes
* Corrective and preventive actions
* Effectiveness-monitoring plan

**Important limitations and misuse risks.** Do not declare a root cause solely because a team reached the fifth “why.” Causal claims require evidence and should distinguish proximate, contributing, and systemic causes.

# 20. Demand, workload, and forecasting analysis

**Purpose.** Characterize how much work, traffic, material, or service demand the system must handle and how that demand varies over time and scenario.

**Why it is justified.** Capacity, staffing, inventory, reliability, and performance conclusions are only as credible as the demand assumptions that drive them. Average demand alone usually hides peaks and variability that create failure.

**How to perform it.**

1. Define demand units, arrival processes, customer or mission classes, geography, time horizon, and scenarios.
2. Clean and stratify historical data; identify trend, seasonality, intermittency, censoring, and structural breaks.
3. Select simple benchmark forecasts before complex models.
4. Estimate distributions, peaks, correlations, and uncertainty—not only point forecasts.
5. Validate forecasts using holdout periods and decision-relevant error measures.
6. Create planning scenarios for growth, shocks, policy changes, and rare but consequential missions.

**What it reveals.** It reveals growth and seasonality, peak-to-average ratios, demand segmentation, uncertainty bands, correlated loads, intermittent demand, and the scenarios that dominate sizing or service risk.

**Typical inputs.**

* Historical arrivals, transactions, usage, failures, or consumption
* Mission plans and market or policy drivers
* Expert scenarios and external constraints

**Typical outputs and decisions supported.**

* Demand model and forecast ranges
* Peak and design-load scenarios
* Input distributions for capacity, queueing, inventory, and simulation
* Forecast error and update plan

**Important limitations and misuse risks.** Use rolling updates. Do not choose a forecasting method solely by statistical fit; choose it based on the decision horizon, data-generating process, and cost of errors.

# 21. Capacity, throughput, utilization, and constraint analysis

**Purpose.** Determine how much work a system can process, which resources constrain it, and what margin exists under expected and adverse demand.

**Why it is justified.** Insufficient capacity causes delay, overload, failure, and loss of mission effectiveness; excessive capacity can create unnecessary cost and complexity. This analysis connects demand to resource sizing and performance requirements.

**How to perform it.**

1. Define the flow unit and the end-to-end process or network.
2. Estimate effective capacity for each resource, accounting for setup, downtime, mix, yield, maintenance, and human constraints.
3. Compute throughput, utilization, work in process, cycle time, and capacity margin by scenario.
4. Identify the active constraint and recognize that it can move as demand mix or design changes.
5. Evaluate alternatives such as added resources, pooling, buffering, scheduling, process redesign, or demand shaping.
6. Stress test peak, degraded, maintenance, and recovery conditions.

**What it reveals.** It reveals bottlenecks, hidden capacity losses, imbalance among resources, insufficient surge margin, sensitivity to product mix, and whether adding capacity at one point merely moves the constraint.

**Typical inputs.**

* Demand and routing data
* Resource calendars, service or processing times, yields, setup and downtime
* Operating policies and priority rules
* Architecture or process network

**Typical outputs and decisions supported.**

* Capacity model and resource requirements
* Constraint and utilization profile
* Throughput and cycle-time predictions
* Capacity margin and expansion triggers

**Important limitations and misuse risks.** Capacity is not simply the theoretical rate of the slowest machine. Use effective capacity and account for variability, dependencies, and shared resources.

# 22. Queueing and waiting-time analysis

**Purpose.** Estimate delay, congestion, work in process, abandonment, and service levels when variable demand competes for finite resources.

**Why it is justified.** Even when average capacity exceeds average demand, variability can produce long and nonlinear delays as utilization approaches saturation. Queueing analysis explains why “almost fully utilized” resources can provide poor service.

**How to perform it.**

1. Define arrivals, service processes, number of servers, queue discipline, priorities, capacities, routing, abandonment, and time dependence.
2. Check whether simple analytical queue models are appropriate; otherwise use numerical or discrete-event simulation.
3. Estimate utilization, expected and percentile waiting time, queue length, time in system, probability of delay, and service-level attainment.
4. Test pooling, segmentation, appointment, priority, staffing, buffer, and demand-shaping policies.
5. Validate against observed queue behavior and distributions.

**What it reveals.** It reveals nonlinear congestion, the value of pooled resources, effects of variability and priorities, required staffing or buffers, and why local utilization targets may conflict with end-to-end responsiveness.

**Typical inputs.**

* Arrival timestamps and classifications
* Service-time and routing distributions
* Staffing schedules and queue rules
* Abandonment, blocking, and rework behavior

**Typical outputs and decisions supported.**

* Queue model and service-level predictions
* Staffing or resource recommendations
* Delay and congestion risk under scenarios
* Inputs to ConOps, requirements, and validation

**Important limitations and misuse risks.** Avoid relying only on averages or steady-state formulas when demand is time-varying, queues are networked, or failures and priorities are important.

# 23. Feasibility analysis

**Purpose.** Determine whether a concept can plausibly be delivered and operated within technical, operational, economic, schedule, legal, and resource constraints.

**Why it is justified.** A concept can be attractive in one dimension yet impossible as a whole. Feasibility analysis provides an early integrated challenge before detailed work creates sunk-cost pressure.

**How to perform it.**

1. Define the concept and success criteria at a comparable level of detail.
2. Assess technical performance and technology maturity.
3. Assess operational fit, human use, external interfaces, and organizational change.
4. Estimate cost, schedule, resources, supply, facilities, and support needs.
5. Identify regulatory, safety, security, environmental, and contractual constraints.
6. Test key assumptions with prototypes, experiments, supplier evidence, or focused models.
7. Classify findings as feasible, feasible with conditions, unresolved, or infeasible.

**What it reveals.** It reveals hard constraints, missing enabling capabilities, immature technologies, unrealistic schedules, unaffordable lifecycle burdens, external approvals, and assumptions that require evidence before commitment.

**Typical inputs.**

* Concept descriptions and operational scenarios
* Rough requirements and performance targets
* Technology and supplier evidence
* Cost, schedule, resource, and regulatory information

**Typical outputs and decisions supported.**

* Integrated feasibility assessment
* Conditions and evidence needed to proceed
* Eliminated concepts and rationale
* Risk-reduction plan

**Important limitations and misuse risks.** Feasibility is not proof of desirability, and desirability is not proof of feasibility. Keep the judgment multidimensional.

# 24. Analysis of alternatives, trade-space, and multi-criteria decision analysis

**Purpose.** Compare credible alternatives across competing objectives and document why one option, portfolio, or architecture is preferred.

**Why it is justified.** Complex systems rarely have a single metric or dominant solution. A transparent trade process prevents implicit preferences from masquerading as technical necessity and makes value judgments visible to decision-makers.

**How to perform it.**

1. Define the decision, alternatives, constraints, stakeholders, scenarios, and evaluation criteria.
2. Screen infeasible alternatives using hard constraints.
3. Normalize performance measures and distinguish value functions from raw measures.
4. Estimate cost, schedule, performance, risk, adaptability, and lifecycle effects using common assumptions.
5. Identify dominance and Pareto-efficient alternatives before applying weights.
6. Apply MCDA, utility, or decision analysis where value tradeoffs are necessary.
7. Perform sensitivity to weights, scores, uncertainty, and scenarios.
8. Document rationale, dissent, limitations, and conditions that would reverse the decision.

**What it reveals.** It reveals dominated alternatives, key tradeoffs, Pareto fronts, criteria that drive the decision, robustness of the recommendation, value conflicts, and where additional information would be most useful.

**Typical inputs.**

* Alternative definitions and common scenarios
* Evaluation criteria and stakeholder value judgments
* Performance, cost, schedule, risk, and uncertainty estimates
* Constraints and policy assumptions

**Typical outputs and decisions supported.**

* Trade matrix and trade-space visualizations
* Sensitivity and robustness results
* Preferred alternative and decision rationale
* Rejected alternatives and reversal conditions

**Important limitations and misuse risks.** Weighted scoring can hide poor assumptions behind arithmetic. Use it only after defining measures and value functions clearly, and always test sensitivity.

# 25. Cost-benefit, business-case, and lifecycle-cost analysis

**Purpose.** Estimate and compare the total economic consequences of alternatives across acquisition, implementation, operation, support, risk, and retirement.

**Why it is justified.** Acquisition cost alone can favor designs that are expensive to operate, maintain, secure, upgrade, or retire. Lifecycle analysis aligns the decision horizon with the consequences of the decision.

**How to perform it.**

1. Define perspective, time horizon, baseline, alternatives, currency basis, discounting, and treatment of inflation.
2. Build a cost breakdown structure and identify recurring, nonrecurring, direct, indirect, contingency, and risk costs.
3. Estimate benefits in measurable operational, financial, risk, or mission terms without forcing all benefits into money when that is not credible.
4. Model timing, uncertainty, learning, utilization, maintenance, replacement, and residual value.
5. Calculate present value and relevant comparative measures.
6. Perform sensitivity and break-even analysis on dominant assumptions.

**What it reveals.** It reveals cost drivers, downstream ownership burden, break-even conditions, affordability peaks, cost-risk exposure, and whether benefits depend on unrealistic adoption or performance assumptions.

**Typical inputs.**

* Work breakdown and architecture
* Resource quantities and rates
* Schedule, demand, reliability, maintenance, staffing, and support assumptions
* Benefit measures and baseline performance

**Typical outputs and decisions supported.**

* Lifecycle cost estimate and range
* Cash-flow and affordability profile
* Cost-benefit or business-case comparison
* Sensitivity, break-even, and cost-risk results

**Important limitations and misuse risks.** Do not present uncertain long-range costs as precise. Separate estimate uncertainty from known but unpriced scope and from risk events.

# 26. Risk, opportunity, uncertainty, sensitivity, and Monte Carlo analysis

**Purpose.** Characterize uncertain outcomes, identify dominant drivers, and support decisions that remain acceptable across plausible futures.

**Why it is justified.** Single-point estimates conceal uncertainty and can create false confidence. Explicit uncertainty analysis shows the probability and consequence of missing objectives and helps target risk reduction.

**How to perform it.**

1. Define uncertain variables, risk events, dependencies, scenarios, and outcome measures.
2. Distinguish aleatory variability, epistemic uncertainty, model-form uncertainty, and ambiguity.
3. Assign ranges or distributions based on evidence and document rationale.
4. Build deterministic relationships and dependency structures.
5. Run sensitivity analysis to identify dominant inputs.
6. Use Monte Carlo or other propagation methods when combined uncertainty matters.
7. Compare mitigation, contingency, margin, and information-gathering options.
8. Communicate distributions, percentiles, exceedance probabilities, and limitations.

**What it reveals.** It reveals probability of cost or schedule overrun, performance shortfall, dominant uncertainties, correlated risks, tail exposure, value of margin, and where new evidence would most reduce decision uncertainty.

**Typical inputs.**

* Deterministic cost, schedule, performance, or reliability model
* Input ranges, distributions, correlations, and risk events
* Historical data and expert judgment
* Decision thresholds and risk tolerances

**Typical outputs and decisions supported.**

* Outcome distributions and confidence ranges
* Sensitivity rankings and tornado charts
* Risk exposure and mitigation priorities
* Contingency and margin recommendations

**Important limitations and misuse risks.** Monte Carlo does not repair a poor model. Results are conditional on structure, distributions, and dependencies; validate these and disclose weak evidence.

# 27. Functional analysis and allocation

**Purpose.** Define what transformations and behaviors the system must perform and allocate them to hardware, software, people, services, procedures, or external systems.

**Why it is justified.** Jumping directly from needs to components can lock in familiar solutions and leave functions missing, duplicated, or assigned to unsuitable performers. Functional analysis preserves solution flexibility and exposes interfaces.

**How to perform it.**

1. Define top-level functions from operational scenarios and requirements.
2. Decompose functions to a level useful for architecture and verification.
3. Specify inputs, outputs, controls, triggers, resources, states, timing, and performance.
4. Model sequence, concurrency, alternatives, and degraded behavior.
5. Allocate functions to candidate performers and evaluate workload, technology, safety, security, and lifecycle implications.
6. Trace functions to needs, requirements, interfaces, risks, and verification cases.

**What it reveals.** It reveals missing and duplicated functions, unsuitable human-automation allocation, functional dependencies, data and interface needs, timing conflicts, and requirements with no realization path.

**Typical inputs.**

* Operational scenarios and requirements
* Context and interface information
* Technology and human-performance constraints
* Architecture alternatives

**Typical outputs and decisions supported.**

* Functional hierarchy and behavior models
* Function-to-performer allocations
* Functional interfaces and performance budgets
* Traceability and verification implications

**Important limitations and misuse risks.** Functional decomposition should serve decisions and traceability, not become an arbitrary tree. Preserve end-to-end scenarios so decomposition does not lose system behavior.

# 28. Requirements analysis, quality, allocation, and traceability

**Purpose.** Create and maintain a coherent set of necessary, feasible, measurable, and verifiable requirements linked to their sources and realization evidence.

**Why it is justified.** Requirements are contractual and technical claims about what must be true. Poor requirements transfer ambiguity downstream, where it becomes expensive design churn, unverifiable acceptance, and stakeholder dispute.

**How to perform it.**

1. Identify source needs, scenarios, regulations, hazards, interfaces, and analysis results.
2. Write requirements with a clear subject, required action or quality, conditions, and measurable criterion.
3. Check necessity, singularity, clarity, feasibility, consistency, solution neutrality, and verifiability.
4. Derive quantitative targets using performance, capacity, reliability, safety, and cost analyses.
5. Allocate requirements and budgets to elements and interfaces.
6. Define verification method, level, environment, and evidence.
7. Maintain bidirectional traceability and conduct change-impact analysis.

**What it reveals.** It reveals contradictions, gaps, gold plating, unverifiable language, hidden assumptions, infeasible targets, orphan requirements, unallocated requirements, and tests without an authoritative requirement.

**Typical inputs.**

* Stakeholder needs and ConOps
* Architecture and analysis results
* Standards, regulations, contracts, and hazards
* Interface agreements

**Typical outputs and decisions supported.**

* Requirements baseline
* Allocation and traceability structure
* Verification cross-reference matrix
* Conflict, assumption, and change-impact records

**Important limitations and misuse risks.** Traceability should support reasoning and change impact, not merely produce a dense matrix. Every link should have a defined semantic meaning.

# 29. Interface, dependency, and integration analysis

**Purpose.** Identify, specify, govern, and verify interactions among system elements and external entities, including the dependencies that determine integration risk.

**Why it is justified.** Interfaces are where independently designed elements meet and where assumptions conflict. They are a dominant source of defects, schedule delay, security exposure, and emergent behavior.

**How to perform it.**

1. Inventory external and internal interfaces and assign ownership on both sides.
2. Specify exchanged information, material, energy, forces, commands, timing, protocols, units, tolerances, errors, security, and lifecycle states.
3. Use interface matrices, N-squared diagrams, DSMs, sequence models, and dependency graphs.
4. Identify coupling, cycles, volatility, criticality, and low-observability interactions.
5. Plan interface control, versioning, compatibility, emulation, integration sequence, and verification.
6. Analyze failure propagation and recovery across boundaries.

**What it reveals.** It reveals missing ownership, inconsistent assumptions, high-coupling clusters, cyclic dependencies, risky integration order, protocol and semantic mismatches, failure propagation paths, and hidden external dependencies.

**Typical inputs.**

* Architecture and functional allocations
* Interface control information
* Behavior and timing models
* Supplier and external-system agreements

**Typical outputs and decisions supported.**

* Interface specifications and ownership matrix
* Dependency and integration-risk model
* Integration sequence and test strategy
* Compatibility and change-control rules

**Important limitations and misuse risks.** An interface is more than a connector or API. Include semantics, timing, failure behavior, physical constraints, security, configuration, and operational responsibility.

# 30. Performance budgeting, margins, and robustness analysis

**Purpose.** Translate system-level performance objectives into allocated budgets and demonstrate that the design can meet them with adequate margin under variation and uncertainty.

**Why it is justified.** Performance is emergent from interacting elements. Without explicit budgets, local designs can each appear compliant while the system misses mass, power, latency, accuracy, thermal, bandwidth, reliability, or cost targets.

**How to perform it.**

1. Define system measures, conditions, thresholds, objectives, and acceptance rules.
2. Develop equations or simulations that connect element properties to system performance.
3. Allocate budgets to subsystems and interfaces with rationale.
4. Track predicted values, uncertainty, reserve, and margin consistently.
5. Analyze worst case, statistical variation, sensitivities, and interactions.
6. Rebalance allocations as design evidence improves and control changes to the budget.

**What it reveals.** It reveals dominant contributors, insufficient margin, coupled budgets, sensitivity to tolerances, unrealistic allocations, and where design changes or requirements relief are needed.

**Typical inputs.**

* System requirements and scenarios
* Architecture and component predictions
* Tolerance, environmental, and uncertainty data
* Measured test results as they become available

**Typical outputs and decisions supported.**

* Controlled performance budgets
* Margin and sensitivity reports
* Allocation changes and design actions
* Verification predictions and acceptance basis

**Important limitations and misuse risks.** Define margin conventions explicitly; organizations often calculate margin differently. Avoid double counting reserve or mixing nominal, worst-case, and percentile values.

# 31. Reliability, availability, maintainability, and supportability analysis

**Purpose.** Predict and improve the probability that the system performs when required, can be restored within required time, and can be supported throughout its lifecycle.

**Why it is justified.** High nominal performance is irrelevant if the system is frequently unavailable, difficult to diagnose, slow to repair, or dependent on unavailable skills and spares. RAM and supportability connect design to operational readiness.

**How to perform it.**

1. Define mission profiles, success criteria, failure states, repair concepts, logistics delay, and operating environment.
2. Develop reliability block diagrams, fault trees, Markov or repairable-system models as appropriate.
3. Estimate failure and repair distributions using analogous data, tests, physics, and expert judgment.
4. Allocate reliability and maintainability targets.
5. Analyze redundancy, common-cause failure, diagnostics, coverage, access, staffing, spares, and maintenance policy.
6. Plan demonstrations and update models with field data.

**What it reveals.** It reveals single points of failure, dominant failure modes, insufficient diagnostic coverage, sensitivity to repair and logistics delay, required spares and maintenance resources, and whether redundancy actually improves availability.

**Typical inputs.**

* Mission and duty-cycle profiles
* Architecture and failure-mode data
* Repair procedures, staffing, logistics, and spare-part data
* Test and operational failure histories

**Typical outputs and decisions supported.**

* Reliability and availability predictions
* Allocated RAM requirements
* Maintenance and support concept
* Demonstration plan and readiness risks

**Important limitations and misuse risks.** Do not equate component reliability with system availability. Include repair, logistics, software recovery, common-cause failure, human response, and operational dependencies.

# 32. FMEA and FMECA

**Purpose.** Systematically identify how functions, components, processes, or human actions can fail, the effects of those failures, and the controls that prevent or detect them.

**Why it is justified.** FMEA provides structured coverage of credible failure modes before they appear in operation. FMECA adds criticality to focus design and verification effort.

**How to perform it.**

1. Define scope, level, functions, operating modes, and interfaces.
2. For each item or function, identify failure modes, local effects, next-higher effects, end effects, causes, existing prevention and detection controls.
3. Assess severity, occurrence, detectability, or a domain-specific criticality method.
4. Identify compensating provisions, diagnostics, maintenance actions, design changes, and verification needs.
5. Track actions to closure and update after design, test, supplier, or field changes.

**What it reveals.** It reveals weak diagnostics, hidden dependencies, maintenance-induced failures, common controls relied upon by many hazards, failure modes without detection, and elements whose failures dominate mission or safety consequences.

**Typical inputs.**

* Functions, architecture, schematics, interfaces, processes, and procedures
* Failure data and analogous systems
* Operating modes and environmental conditions

**Typical outputs and decisions supported.**

* FMEA/FMECA worksheet
* Critical failure-mode list
* Derived requirements and design actions
* Diagnostic, maintenance, and test recommendations

**Important limitations and misuse risks.** Ranking numbers should not replace engineering judgment. High-severity items may require action regardless of calculated priority, and common-cause interactions may need other methods.

# 33. Fault-tree, event-tree, hazard, and safety-control analysis

**Purpose.** Explain how combinations of failures, conditions, and control actions can produce unacceptable losses and identify effective prevention and mitigation barriers.

**Why it is justified.** Safety and mission loss often result from interactions rather than a single component failure. Top-down and scenario-based analyses complement bottom-up FMEA and support defensible safety requirements and assurance claims.

**How to perform it.**

1. Define losses, hazards, top events, initiating events, and system boundaries.
2. Construct fault trees for combinations of causes and event trees for consequence sequences where appropriate.
3. Use hazard analyses or control-structure methods such as STPA for unsafe interactions and inadequate control.
4. Identify prevention, detection, mitigation, containment, and recovery barriers.
5. Assess independence, common cause, human and software contribution, and barrier effectiveness.
6. Derive requirements, design constraints, procedures, and verification evidence.

**What it reveals.** It reveals minimal cut sets, dominant accident sequences, barrier dependencies, unsafe control actions, missing feedback, common-cause vulnerabilities, and residual risk requiring authority acceptance.

**Typical inputs.**

* Architecture, functions, states, interfaces, and operational scenarios
* Failure data, environmental conditions, procedures, and human actions
* Regulatory and organizational risk criteria

**Typical outputs and decisions supported.**

* Hazard log and causal models
* Safety requirements and controls
* Verification and assurance evidence needs
* Residual-risk and acceptance record

**Important limitations and misuse risks.** Quantification can be useful but should not create false precision when causal completeness and dependence assumptions are uncertain.

# 34. Security threat, vulnerability, and resilience analysis

**Purpose.** Identify assets, adversaries, attack surfaces, trust boundaries, vulnerabilities, and controls, and evaluate the system’s ability to resist, detect, contain, recover, and adapt.

**Why it is justified.** Security is an emergent property of technology, people, supply chain, operations, and governance. Adding controls late can conflict with safety, usability, performance, and maintainability.

**How to perform it.**

1. Identify critical assets, missions, data, privileges, and safety consequences.
2. Define threat actors, capabilities, intent, access, and plausible abuse cases.
3. Model trust boundaries, data flows, attack surfaces, dependencies, and attack paths.
4. Assess vulnerabilities and control effectiveness across prevention, detection, response, and recovery.
5. Analyze degraded and compromised modes, resilience objectives, and recovery priorities.
6. Prioritize treatments by mission consequence, exploitability, exposure, and uncertainty; plan verification and monitoring.

**What it reveals.** It reveals concentration of privilege, insecure dependencies, exploitable interfaces, weak detection, cascading compromise, recovery gaps, supply-chain exposure, and conflicts between security and other system qualities.

**Typical inputs.**

* Architecture, data flows, interfaces, identities, and deployment model
* Threat intelligence and vulnerability evidence
* Operational scenarios, safety consequences, and recovery requirements

**Typical outputs and decisions supported.**

* Threat model and attack-path analysis
* Security and resilience requirements
* Control architecture and verification plan
* Residual-risk and monitoring plan

**Important limitations and misuse risks.** A checklist alone is not a threat model. Analyze the actual system, adversary, mission, and dependency structure, and update continuously as threats and configurations change.

# 35. Human factors, workload, staffing, and human-system integration analysis

**Purpose.** Design the combined human-technical system so people can perceive, decide, act, coordinate, recover, maintain, and learn within realistic capability and workload limits.

**Why it is justified.** Humans are not interchangeable resources or error sources. Poor allocation, interfaces, procedures, staffing, and organizational design can defeat otherwise sound technology.

**How to perform it.**

1. Identify user populations, roles, abilities, constraints, environments, and consequences of error.
2. Model tasks, decisions, information needs, handoffs, workload, timing, situation awareness, and teamwork.
3. Allocate functions between humans and automation based on comparative strengths, failure behavior, and accountability.
4. Analyze staffing levels, shifts, fatigue, training, accessibility, maintainability, and emergency tasks.
5. Prototype and evaluate interfaces with representative users and scenarios.
6. Validate performance under nominal, peak, degraded, and recovery conditions.

**What it reveals.** It reveals overload and underload, mode confusion, poor feedback, excessive memory and coordination demands, staffing gaps, training burden, accessibility barriers, and automation that is difficult to supervise or recover.

**Typical inputs.**

* Operational scenarios and task descriptions
* User characteristics and environmental data
* Interface prototypes and system behavior
* Demand, timing, error, and staffing information

**Typical outputs and decisions supported.**

* Human-system function allocations
* Task, workload, and staffing models
* Interface and procedure requirements
* Usability and human-performance evidence

**Important limitations and misuse risks.** Average task time is insufficient. Include variability, interruption, fatigue, rare emergencies, teamwork, and the cognitive work required to diagnose unexpected conditions.

# 36. Discrete-event, agent-based, system-dynamics, and hybrid simulation

**Purpose.** Experiment with system behavior over time when interactions, variability, feedback, adaptation, or emergent effects make static calculations inadequate.

**Why it is justified.** Simulation can expose consequences before committing to physical systems or disruptive operational trials. Different paradigms answer different questions and should not be selected merely because a tool is available.

**How to perform it.**

1. Define the decision, system boundary, outcomes, scenarios, and required fidelity.
2. Choose discrete-event simulation for queues, resources, routing, and event timing; agent-based simulation for heterogeneous autonomous actors; system dynamics for aggregate feedback and accumulation; hybrid approaches when these interact.
3. Develop conceptual models and input distributions before coding.
4. Verify implementation and validate behavior against data, theory, and stakeholder expectations.
5. Design experiments, replications, warm-up, run length, and random seeds appropriately.
6. Analyze uncertainty and sensitivity and document limitations.

**What it reveals.** It reveals congestion, resource contention, transient behavior, feedback loops, policy resistance, emergent patterns, threshold effects, and performance distributions that simple averages or closed-form models miss.

**Typical inputs.**

* Process, architecture, behavior, and policy models
* Demand, service, failure, routing, and decision data
* Scenarios and experimental factors

**Typical outputs and decisions supported.**

* Executable model and verification/validation record
* Scenario and experiment results
* Performance distributions and trade insights
* Recommendations and model limitations

**Important limitations and misuse risks.** Animation is not validation. A visually convincing model can still be wrong; maintain a conceptual model, evidence trail, and independent checks.

# 37. Optimization, allocation, scheduling, routing, and network analysis

**Purpose.** Find resource assignments, designs, schedules, routes, locations, or policies that best satisfy an objective subject to constraints.

**Why it is justified.** Complex allocation decisions contain interactions that intuition handles poorly. Optimization makes objectives and constraints explicit and can identify better or provably bounded solutions.

**How to perform it.**

1. Define decision variables, objective functions, constraints, time horizon, uncertainty, and feasibility rules.
2. Choose an appropriate formulation: linear, integer, nonlinear, dynamic, stochastic, robust, network, or heuristic.
3. Validate that the mathematical objective represents stakeholder value and does not omit critical constraints.
4. Solve and inspect feasibility, shadow prices, binding constraints, and alternative optima.
5. Stress test with scenarios, uncertainty, and implementation constraints.
6. Translate the solution into an executable policy and monitor performance.

**What it reveals.** It reveals binding constraints, resource scarcity, opportunity costs, better allocations, scheduling conflicts, network bottlenecks, sensitivity to assumptions, and the value of additional capacity or flexibility.

**Typical inputs.**

* Demand and resource data
* Costs, durations, capacities, precedence, geography, and policy constraints
* Architecture or process network
* Decision objectives and service requirements

**Typical outputs and decisions supported.**

* Recommended allocation, schedule, route, location, or design
* Objective value and constraint status
* Sensitivity and scenario results
* Implementation rules and exceptions

**Important limitations and misuse risks.** An optimal solution to the wrong objective is harmful. Include operational practicality, robustness, fairness, safety, and change cost rather than optimizing a narrow proxy.

# 38. Inventory, spare-parts, supply-network, and logistics analysis

**Purpose.** Determine what material or spares to hold, where to hold them, when to replenish, and how supply uncertainty affects production and operational availability.

**Why it is justified.** Inventory ties up cost but protects against uncertain demand, lead time, failure, and disruption. Too little inventory causes downtime; too much masks process problems and creates obsolescence.

**How to perform it.**

1. Classify items by criticality, demand pattern, value, lead time, substitutability, and repairability.
2. Estimate demand and lead-time distributions, including intermittent failures and common-cause events.
3. Define service, availability, downtime, and cost objectives.
4. Evaluate reorder points, order quantities, base-stock, multi-echelon, repairable-item, pooling, cannibalization, and emergency policies.
5. Model supplier capacity, disruption, obsolescence, shelf life, and transportation.
6. Validate policies with simulation when networks and repair loops are complex.

**What it reveals.** It reveals items that dominate downtime or cost, insufficient lead-time protection, excess and obsolete stock, value of pooling, supplier concentration risk, and tradeoffs between inventory, repair capacity, and availability.

**Typical inputs.**

* Demand or failure history
* Lead times, costs, repair times, and service targets
* Network locations, suppliers, and transportation
* Criticality and substitution rules

**Typical outputs and decisions supported.**

* Inventory and replenishment policies
* Spares and repair-capacity recommendations
* Service and downtime risk
* Supply-network and obsolescence actions

**Important limitations and misuse risks.** Classical EOQ assumptions rarely hold for critical spares. Use service and availability consequences, intermittency, repair loops, and multi-echelon dependencies.

# 39. Statistical process control, process capability, and measurement-system analysis

**Purpose.** Determine whether a process is stable, whether it can meet specification consistently, and whether the measurement system can distinguish real variation from measurement error.

**Why it is justified.** Inspection alone does not create quality. Stable and capable processes prevent defects, while inadequate measurement systems can hide problems or create false alarms.

**How to perform it.**

1. Define the characteristic, specification, sampling plan, subgroup logic, and measurement method.
2. Conduct measurement-system analysis, including bias, linearity, stability, repeatability, and reproducibility where applicable.
3. Use control charts suited to the data and process to distinguish common-cause and special-cause variation.
4. Investigate and remove special causes before calculating capability.
5. Estimate capability using appropriate distributional and stability assumptions.
6. Implement reaction plans and monitor after process changes.

**What it reveals.** It reveals instability, shifts, trends, excessive measurement error, within- versus between-process variation, inability to meet tolerance, and whether improvement requires control or redesign.

**Typical inputs.**

* Process measurements and timestamps
* Specification limits and operational tolerances
* Measurement equipment, operators, and procedures
* Process conditions and lot information

**Typical outputs and decisions supported.**

* Measurement-system study
* Control charts and reaction plan
* Capability indices and distribution assessment
* Process-improvement and acceptance decisions

**Important limitations and misuse risks.** Specification limits are not control limits. Capability indices are misleading for unstable processes or inappropriate distribution assumptions.

# 40. Design of experiments, hypothesis testing, and statistical verification

**Purpose.** Efficiently determine how factors affect outcomes and make evidence-based conclusions about compliance, differences, interactions, and robustness.

**Why it is justified.** One-factor-at-a-time testing misses interactions and wastes test resources. Informal comparison can mistake noise for effect. Designed experiments and statistical inference improve learning and evidence strength.

**How to perform it.**

1. State the engineering question, response variables, factors, ranges, nuisance variables, and decision criteria.
2. Select experimental design, randomization, blocking, replication, and sample size based on effect size and risk.
3. Confirm measurement capability and control configuration and environment.
4. Execute according to a preplanned protocol and preserve raw data.
5. Analyze effects, interactions, residuals, uncertainty, and practical—not only statistical—significance.
6. Confirm important findings and translate them into design settings, margins, requirements, or evidence.

**What it reveals.** It reveals influential factors, interactions, nonlinearities, robust settings, uncertainty in performance, and whether observed differences or compliance claims are supported by adequate evidence.

**Typical inputs.**

* Factors and response definitions
* Expected variability and effect sizes
* Test resources, configurations, and constraints
* Acceptance risks and confidence requirements

**Typical outputs and decisions supported.**

* Experimental design and analysis
* Effect and interaction estimates
* Compliance or comparison conclusion
* Recommended settings and follow-on tests

**Important limitations and misuse risks.** A p-value is not the probability that a requirement is true. State effect size, uncertainty, assumptions, power, and practical significance.

# 41. Reliability demonstration, life-data, and accelerated-testing analysis

**Purpose.** Use test or field data to estimate lifetime behavior or demonstrate reliability with stated confidence.

**Why it is justified.** Reliability requirements concern a population and time horizon, while tests observe finite samples for limited time. Statistical planning is necessary to connect evidence to the claim.

**How to perform it.**

1. Define failure, mission profile, censoring rules, confidence, reliability metric, and decision risks.
2. Select binomial, exponential, Weibull, degradation, accelerated-life, or repairable-system methods as appropriate.
3. Determine units, test duration, stresses, and stopping rules.
4. Check acceleration assumptions and failure-mode consistency.
5. Analyze censored data, confidence bounds, trends, and failure modes.
6. Update design and reliability models and plan growth testing where failures occur.

**What it reveals.** It reveals achieved reliability bounds, life distributions, wear-out behavior, infant mortality, dominant failure modes, stress sensitivity, and whether the test has enough information to support the claim.

**Typical inputs.**

* Reliability requirement and mission profile
* Test durations, stresses, failures, and censoring
* Failure-analysis results and environmental conditions

**Typical outputs and decisions supported.**

* Reliability estimate and confidence bounds
* Demonstration decision
* Life or degradation model
* Corrective-action and growth plan

**Important limitations and misuse risks.** Zero failures does not prove perfection. The inference depends on total exposure, assumed distribution, confidence, and relevance of test stresses to use conditions.

# 42. Verification planning, coverage, evidence sufficiency, and closure analysis

**Purpose.** Plan and assess whether every requirement and critical claim has suitable, credible, configuration-controlled evidence.

**Why it is justified.** Programs can execute many tests yet leave important requirements unverified, use the wrong environment, or produce evidence that cannot be traced to the delivered configuration.

**How to perform it.**

1. For every requirement, define verification level, method, configuration, environment, procedure, success criterion, and evidence owner.
2. Identify dependencies, shared evidence, prerequisite calibrations, and required models.
3. Analyze coverage across requirements, functions, interfaces, states, modes, environments, hazards, and boundaries.
4. Assess evidence quality, anomalies, deviations, waivers, and model validity.
5. Track closure and perform independent review of high-consequence claims.

**What it reveals.** It reveals orphan requirements, duplicated or missing tests, untested modes and interfaces, weak model evidence, configuration mismatches, insufficient environments, and claims dependent on unresolved anomalies.

**Typical inputs.**

* Requirements baseline and traceability
* Verification procedures, reports, models, and raw evidence
* Configuration and anomaly records
* Qualification and regulatory criteria

**Typical outputs and decisions supported.**

* Verification cross-reference matrix
* Coverage and closure status
* Evidence-sufficiency findings
* Residual noncompliance and waiver record

**Important limitations and misuse risks.** Verification is not synonymous with test. Inspection, demonstration, and analysis can be valid, but the chosen method must be capable of proving the specific requirement.

# 43. Validation, operational evaluation, pilot, and benefit-realization analysis

**Purpose.** Determine whether the delivered system solves the intended problem and creates acceptable outcomes in representative use.

**Why it is justified.** A fully verified system can still be operationally ineffective, unusable, unaffordable, or rejected. Validation reconnects the realized system to the original mission and stakeholder need.

**How to perform it.**

1. Restate intended outcomes, users, environments, scenarios, and baseline.
2. Design operational trials, pilots, simulations, or comparative evaluations with representative conditions.
3. Measure mission effectiveness, user performance, service, safety, workload, adoption, support burden, and unintended consequences.
4. Use before-after, controlled, quasi-experimental, or longitudinal methods where causal benefit claims matter.
5. Assess transition readiness, training, staffing, data, policy, and organizational change.
6. Define post-deployment monitoring and benefit realization.

**What it reveals.** It reveals mismatch between requirements and real need, usability and adoption barriers, operational workarounds, insufficient support, unexpected interactions, and whether promised benefits appear under actual demand.

**Typical inputs.**

* ConOps, stakeholder needs, and measures of effectiveness
* Verified system and representative configuration
* Operational baseline and scenarios
* Users, organizations, and support arrangements

**Typical outputs and decisions supported.**

* Validation and acceptance evidence
* Operational limitations and transition actions
* Benefit-realization assessment
* Post-deployment monitoring plan

**Important limitations and misuse risks.** Do not validate only with expert users in ideal conditions. Include representative diversity, workload, disruptions, and organizational constraints.

# 44. Maintenance, replacement, and renewal analysis

**Purpose.** Choose inspection, preventive maintenance, condition-based maintenance, repair, overhaul, and replacement policies that balance availability, risk, and lifecycle cost.

**Why it is justified.** Too much maintenance wastes resources and can induce failures; too little increases downtime and hazard. Replacement decisions require comparing future costs and risks rather than sunk costs.

**How to perform it.**

1. Define failure and degradation behavior, consequences, detectability, repair options, and operating context.
2. Estimate age-, usage-, or condition-dependent risk and maintenance effectiveness.
3. Compare corrective, preventive, condition-based, reliability-centered, and redesign options.
4. Model downtime, labor, spares, access, logistics, and opportunity cost.
5. Optimize intervals or thresholds and test sensitivity.
6. Monitor outcomes and update policies with field evidence.

**What it reveals.** It reveals whether failures are age-related, which tasks are effective, optimal intervention timing, value of monitoring, tradeoffs among spares and repair capacity, and when replacement dominates continued support.

**Typical inputs.**

* Failure, inspection, degradation, and maintenance history
* Costs, downtime consequences, labor, spares, and logistics
* Asset condition and mission profile
* Safety and regulatory obligations

**Typical outputs and decisions supported.**

* Maintenance and inspection policy
* Replacement or overhaul timing
* Resource and spare requirements
* Expected availability, risk, and cost

**Important limitations and misuse risks.** Preventive replacement is not automatically beneficial. It works best when failure risk increases with age or use and the intervention actually restores condition.

# 45. Lean, Six Sigma, continuous-improvement, and productivity analysis

**Purpose.** Improve flow, quality, cost, and responsiveness by reducing waste, controlling variation, and redesigning work around stakeholder value.

**Why it is justified.** Operational systems drift, demand changes, and local workarounds accumulate. Structured improvement turns field evidence into controlled learning rather than episodic cost cutting.

**How to perform it.**

1. Define customer or mission value and the performance problem.
2. Measure baseline flow, quality, demand, workload, cost, and variation.
3. Map the value stream and analyze causes, constraints, and variation.
4. Design countermeasures using flow, pull, mistake-proofing, standard work, visual control, automation, and variation reduction.
5. Pilot changes and evaluate effects statistically and operationally.
6. Control the improved process, update standards, and monitor unintended consequences.

**What it reveals.** It reveals waste, rework, overprocessing, delay, unstable processes, uneven workload, unnecessary inventory, poor handoffs, and opportunities to improve without major capital investment.

**Typical inputs.**

* Operational performance and quality data
* Value-stream and process observations
* Stakeholder needs and service criteria
* Cost and workload information

**Typical outputs and decisions supported.**

* Improved process design
* Measured improvement and control plan
* Updated standard work and metrics
* Further improvement backlog

**Important limitations and misuse risks.** Do not use Lean as a synonym for staff reduction or Six Sigma as a template exercise. Improvement must preserve safety, resilience, learning capacity, and stakeholder value.

# 46. Retirement, reverse-logistics, data-disposition, and transition analysis

**Purpose.** Plan the safe and economical withdrawal of systems, assets, data, contracts, skills, and support while maintaining continuity and compliance.

**Why it is justified.** Retirement creates new interfaces and risks: orphaned data, unsupported dependencies, hazardous materials, stranded inventory, knowledge loss, and insufficient successor capacity.

**How to perform it.**

1. Inventory assets, data, users, interfaces, contracts, licenses, suppliers, hazardous materials, and legal obligations.
2. Identify successor capabilities and transition dependencies.
3. Compare phased, parallel, immediate, repurpose, sell, salvage, archive, and disposal options.
4. Model capacity, cutover, rollback, inventory runout, reverse logistics, cost, and risk.
5. Define data migration, retention, destruction, and evidence requirements.
6. Transfer knowledge and close configuration, security, safety, environmental, and contractual obligations.

**What it reveals.** It reveals hidden dependencies, continuity gaps, residual access and data risk, inventory liabilities, stranded support obligations, successor capacity shortfalls, and optimal transition timing.

**Typical inputs.**

* Asset and configuration records
* Dependency and interface inventories
* Successor plans and capacity
* Contracts, regulations, data, environmental, and safety requirements

**Typical outputs and decisions supported.**

* Retirement decision and transition plan
* Disposition and archival records
* Continuity, rollback, and risk controls
* Lessons learned and knowledge-transfer evidence

**Important limitations and misuse risks.** Do not wait until the system is obsolete to begin. Design for data portability, modular replacement, safe disposal, and knowledge preservation during development.

---

# Part III — Cross-reference guides

# 47. Analysis families by V phase

| Analysis family | Early definition | Requirements and architecture | Detailed design and realization | Verification and validation | Operations and retirement |
| --- | --- | --- | --- | --- | --- |
| Mission, needs, capability, and gap | Primary | Trace rationale | Revisit on major change | Validation basis | Benefits and replacement basis |
| Stakeholder, context, and boundary | Primary | Interface and concern basis | Supplier and deployment updates | Representative-user and environment basis | Evolving ecosystem and retirement dependencies |
| Process, value stream, root cause | Baseline problem | Inform functional and architecture choices | Design production/service processes | Analyze defects and transition | Continuous improvement |
| Demand, capacity, and queueing | Baseline and rough sizing | Set targets and size architecture | Size resources and processes | Verify and validate load/service | Forecast and rebalance |
| Feasibility and alternatives | Primary selection | Architecture trades | Local design trades | Waiver or recovery decisions | Upgrade/replace trades |
| Cost and lifecycle economics | Business case | Budget and affordability | Design-to-cost and production control | Cost of compliance and transition | Cost-to-serve and replacement |
| Risk, uncertainty, sensitivity, Monte Carlo | Initial exposure | Margins and robust architecture | Parameter and supplier risk | Confidence and residual risk | Operational and retirement risk |
| Functional, requirements, allocation, traceability | Needs translation | Primary | Detailed allocation | Evidence closure | Change impact |
| Interface and integration | External context | Primary architecture concern | Detailed contracts | Integration and system evidence | Change and decommission dependencies |
| Performance budgets and robustness | Feasibility ranges | Primary allocation | Close budgets | Confirm margins | Monitor degradation and growth |
| RAM and supportability | Rough concepts | Allocate and architect | Detailed design and support planning | Demonstrate | Optimize maintenance and replacement |
| Safety, security, resilience | Initial hazards/threats | Derive controls and architecture | Detailed implementation | Verify controls and validate recovery | Monitor and safely retire |
| Human factors and staffing | User and work context | Allocate functions and derive needs | Detailed interface and procedure design | Usability and operational validation | Workforce and workload optimization |
| Simulation and optimization | Explore concepts | Size and choose architecture | Tune design and processes | Design tests and evaluate scenarios | Optimize operations and transition |
| Quality, DOE, statistical evidence | Baseline variation where available | Plan evidence | Control realization | Primary evidence methods | Process monitoring and improvement |
| Inventory and logistics | Rough support feasibility | Support architecture | Provisioning and supply planning | Deployment readiness | Spares and reverse logistics |

# 48. Selecting an analysis by engineering question

| Engineering question | Primary analysis families |
| --- | --- |
| Are we solving the right problem? | Mission, needs, capability, gap, stakeholder, context, root-cause analysis |
| How much demand must the system handle? | Demand forecasting, capacity, queueing, scenario, and simulation analysis |
| Which concept or architecture should we choose? | Feasibility, analysis of alternatives, trade-space, MCDA, lifecycle cost, risk and sensitivity analysis |
| What must the system do? | Operational scenario, functional analysis, requirements analysis, allocation and traceability |
| Will the architecture meet performance targets? | Performance budgets, capacity, network, simulation, optimization, reliability and robustness analysis |
| What can fail or cause harm? | FMEA/FMECA, fault tree, event tree, hazard, threat, resilience and human factors analysis |
| Can people operate and support it? | Human factors, workload, staffing, maintainability, supportability, training and validation analysis |
| Can we build or deploy it repeatably? | Process capability, SPC, measurement analysis, capacity, scheduling, supply and inventory analysis |
| How should we test it? | Verification planning, coverage, DOE, statistical test design, reliability demonstration and measurement uncertainty |
| Does it work in real use? | Validation, operational evaluation, pilot, before-after and benefit-realization analysis |
| How should we sustain or replace it? | RAM, maintenance, spares, forecasting, queueing, lifecycle cost, renewal and replacement analysis |
| How do we retire it safely? | Retirement, transition, reverse logistics, data disposition, continuity and risk analysis |

# 49. Standard analysis report template

A reusable analysis report or model record can use the following structure:

* **Decision and claim:** Decision, requirement, risk, or assurance claim supported.
* **Scope and boundary:** System, lifecycle, scenarios, organizations, interfaces, and exclusions.
* **Baseline and alternatives:** Controlled configurations and options compared.
* **Measures and criteria:** Outcome measures, thresholds, objectives, utility, and acceptance rules.
* **Method justification:** Why the selected analytical, statistical, simulation, or optimization method is suitable.
* **Inputs and provenance:** Data sources, versions, sampling, quality, preprocessing, and expert judgments.
* **Assumptions and uncertainty:** Ranges, distributions, correlations, model-form limits, and unresolved issues.
* **Model and calculations:** Equations, logic, algorithms, implementation, and configuration.
* **Verification and validation:** Checks that the model was implemented correctly and is sufficiently representative for the decision.
* **Results:** Central estimates, ranges, distributions, scenarios, and visualizations.
* **Sensitivity and robustness:** Drivers, reversal conditions, margins, and alternative interpretations.
* **Conclusion and recommendation:** Decision rationale tied directly to evidence and criteria.
* **Limitations and residual risk:** What the analysis cannot establish and what remains uncertain.
* **Actions and traceability:** Requirements, design changes, tests, risks, owners, dates, and affected baselines.

# 50. Domain tailoring

* **Defense and aerospace:** emphasize mission effectiveness, environmental qualification, safety, reliability, readiness, assurance, interoperability, configuration control, and formal evidence.
* **Manufacturing and industrial systems:** emphasize process design, line balance, capacity, quality, supply, maintainability, human work, production readiness, and statistical control.
* **Software-intensive and digital services:** emphasize workload, latency, availability, data, security, resilience, deployment, observability, change frequency, service levels, and operational recovery.
* **Infrastructure, logistics, and transportation:** emphasize demand, network flow, facility location, routing, capacity expansion, asset management, safety, disruption, and long lifecycle economics.
* **Healthcare and other high-consequence services:** emphasize human factors, workflow, queueing, safety, privacy, equity, clinical or professional governance, and validation in representative practice.

# 51. Final principles

1. Start with the decision and claim, not with a favored tool.
2. Use the least-complex method that is credible for the consequence of the decision.
3. Reuse one controlled analysis model across phases when possible, increasing fidelity and replacing assumptions with evidence.
4. Preserve common scenarios and baselines so alternatives remain comparable.
5. Quantify uncertainty and state what could reverse the conclusion.
6. Validate models for their intended decision; no model is universally valid.
7. Trace analysis results into requirements, architecture decisions, risks, verification, and operational policies.
8. Treat human, organizational, safety, security, support, and retirement consequences as system properties, not afterthoughts.
9. Update analyses when configuration, demand, environment, evidence, or stakeholder values change.
10. Prefer a transparent, reviewable argument over false numerical precision.

---

## References

[1]: https://sebokwiki.org/wiki/Life_Cycle_Stages "Life Cycle Stages"
[2]: https://www.incose.org/docs/default-source/default-document-library/systems-engineering-guidebookisbn-9780692091807bb88028572db67488e78ff000036190a.pdf?sfvrsn=365365c7_0& "Systems Engineering Guidebook"
[3]: https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/ "NASA Program/Project Life Cycle"
[4]: https://essp.larc.nasa.gov/EVI-6/pdf_files/NASA_SystemsEngineeringHandbookRev2.pdf "NASA Systems Engineering Handbook Rev 2"
[5]: https://www.nasa.gov/reference/system-engineering-handbook-appendix/ "NASA Systems Engineering Handbook Appendix"
[6]: https://sebokwiki.org/wiki/System_Verification "System Verification"
[7]: https://sebokwiki.org/wiki/System_Validation "System Validation"
[8]: https://standards.nasa.gov/system/files/tmp/2025-03-12-NASA-HDBK-1009A.pdf "NASA-HDBK-1009A"
