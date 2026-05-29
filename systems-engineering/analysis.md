# The "V" Diagram

A good way to read the **systems engineering V** is as a sequence of increasingly concrete definition activities on the left, realization at the bottom, and increasing evidence / assurance on the right. Standard references describe life-cycle stages spanning **conception, development, production/utilization/support, and retirement**, while verification and validation cut across the lifecycle. ([SEBoK][1])

Below is a **phase-by-phase map** of the analyses, models, simulations, and especially the kinds of methods commonly drawn from **operations research (OR)** and **industrial engineering (IE)**. I am using a practical V-model structure, aligned with common SE lifecycle descriptions in INCOSE, SEBoK, and NASA, even though exact labels vary by industry. ([INCOSE][2])

# Table of contents

* [Problem / opportunity / mission analysis](#problem-opportunity-mission-analysis)
* [Feasibility & concept exploration](#feasibility-concept-exploration)
* [Stakeholder needs / ConOps (Concept of Operations)](#stakeholder-needs-conops-concept-of-operations)
* [System requirements definition](#system-requirements-definition)
* [Architecture / high-level design](#architecture-high-level-design)
* [Subsystem / detailed design](#subsystem-detailed-design)
* [Implementation / build / procure](#implementation-build-procure)
* [Unit / component verification](#unit-component-verification)
* [Integration & integration verification](#integration-integration-verification)
* [System verification](#system-verification)
* [System validation / transition](#system-validation-transition)
* [Operations & support](#operations-support)
* [Retirement / disposal](#retirement-disposal)
* [Cross-cutting analyses that apply across the whole V](#cross-cutting-analyses-that-apply-across-the-whole-v)
* [The most common OR / IE methods by V-diagram zone](#the-most-common-or-ie-methods-by-v-diagram-zone)
* [A compact master checklist by phase](#a-compact-master-checklist-by-phase)
* [Caveat](#caveat)

# Problem / opportunity / mission analysis

Purpose: decide whether a system intervention is warranted, and what mission or business problem matters.

## Typical analyses

* Mission analysis
* Problem framing / root-cause analysis
* Needs analysis
* Stakeholder analysis
* Current-state (“as-is”) process analysis
* Capability analysis
* Gap analysis
* Baseline performance analysis
* Demand / workload characterization
* External environment and context analysis
* Market / policy / threat analysis
* High-level risk and opportunity analysis

## OR / IE analyses commonly used

* Process mapping and value-stream analysis
* Bottleneck analysis
* Capacity analysis
* Queueing analysis (rough-order)
* Throughput analysis
* Work sampling / time study (for existing operations)
* Forecasting (demand, arrivals, usage)
* Benchmarking / comparative performance analysis
* Pareto analysis of incidents, defects, delays, or cost drivers
* Constraint analysis / theory of constraints

## Models and simulations

* As-is workflow models
* High-level process flow models
* Context diagrams
* Mission thread / scenario models
* Influence diagrams / causal loop sketches
* Simple discrete-event models of current operations
* Top-down spreadsheet models for workload, utilization, and cost

## Typical outputs

* Problem statement
* Capability gaps
* Baseline KPIs
* Candidate intervention areas
* Initial measures of effectiveness (MOEs)

# Feasibility & concept exploration

Purpose: identify viable concepts and select a preferred direction before committing to detailed requirements.

NASA’s concept phases explicitly emphasize developing a baseline concept and demonstrating feasibility before moving deeper into design. ([NASA][3])

## Typical analyses

* Feasibility analysis (technical, operational, economic, schedule)
* Analysis of alternatives (AoA)
* Trade-space / trade-off analysis
* Cost-benefit analysis
* Business case analysis
* Technology maturity / readiness analysis
* Preliminary lifecycle cost analysis
* Initial safety, security, and regulatory analysis
* Make / buy / partner analysis
* Sensitivity and uncertainty analysis
* Preliminary supportability and sustainment analysis

## OR / IE analyses commonly used

* Multi-criteria decision analysis (MCDA)
* Weighted scoring / utility analysis
* Decision trees / expected value analysis
* Cost estimation / parametric estimating
* Learning-curve analysis (where relevant)
* Sensitivity analysis
* Scenario analysis
* Monte Carlo simulation for cost/schedule/risk
* Capacity and resource feasibility checks
* Network and location analysis (if logistics/distribution matters)
* Optimization of concept parameters under constraints

## Models and simulations

* Candidate concept models
* Trade curves
* Parametric performance models
* Discrete-event simulation (alternative concepts)
* System dynamics models (policy / demand / feedback effects)
* Early digital mockups / MBSE conceptual models
* Probabilistic cost and schedule models
* Rough-order reliability / availability models

## Typical outputs

* Preferred concept
* Feasibility findings
* Decision rationale
* Top risks and assumptions
* Entry basis for requirements definition

# Stakeholder needs / ConOps (Concept of Operations)

Purpose: define how the system will be used and what outcomes constitute operational success.

ConOps is commonly used to check that requirements and concepts reflect intended use and operational reality. ([essp.larc.nasa.gov][4])

## Typical analyses

* Operational analysis
* Use-case analysis
* User journey / operational thread analysis
* Mission effectiveness analysis
* Human factors and workload analysis
* Functional user needs analysis
* Stakeholder priority and conflict analysis
* Operational constraints analysis
* Failure / degraded-mode operational analysis
* Interoperability-in-use analysis

## OR / IE analyses commonly used

* Workload analysis
* Staffing analysis
* Queueing / wait-time analysis for user-facing operations
* Resource allocation analysis
* Shift / coverage analysis
* Facility flow or movement analysis
* Human-in-the-loop task allocation
* Service-level analysis
* Preliminary ergonomic analysis
* Demand segmentation

## Models and simulations

* ConOps / OpsCon models
* Swimlane diagrams
* Operational scenarios and mission threads
* Event sequence models
* Service blueprints
* Agent-based models (when operator behavior matters)
* Simulations of operating tempo, arrivals, and response times

## Typical outputs

* ConOps
* Operational scenarios
* User classes / roles
* Preliminary acceptance conditions
* Candidate operational performance measures

# System requirements definition

Purpose: convert needs and operational expectations into a disciplined, testable set of requirements.

## Typical analyses

* Requirements analysis
* Requirements decomposition
* Requirements quality analysis (clarity, completeness, verifiability)
* Functional analysis
* Performance analysis
* Constraint analysis
* Interface requirements analysis
* Allocation analysis (high level)
* Requirements conflict / consistency analysis
* Traceability analysis
* Verification method analysis (how each requirement will later be verified)

## OR / IE analyses commonly used

* Target-setting from baselines and forecasts
* Capacity requirements analysis
* Throughput / cycle-time target derivation
* Reliability / availability target allocation
* Service-level target analysis
* Tolerance and variability analysis
* Resource envelope analysis
* Statistical characterization of demand and loads
* Quality function deployment (QFD)-type translation methods
* Risk-based prioritization of requirements

## Models and simulations

* Requirements models (textual + MBSE)
* Functional decomposition trees
* Functional flow block diagrams
* N2 / interface matrices
* Context and boundary models
* Performance envelope models
* Traceability matrices
* Preliminary state models / mode models

## Typical outputs

* Validated system requirements baseline
* Verification cross-reference basis
* Performance thresholds and objectives
* Interface requirement set

# Architecture / high-level design

Purpose: choose the system structure that best satisfies requirements and enables downstream design.

## Typical analyses

* Functional allocation analysis
* Logical architecture analysis
* Physical architecture trade studies
* Interface analysis
* Partitioning / modularity analysis
* Redundancy and fault-tolerance analysis
* Interoperability and standards analysis
* Security architecture analysis
* Safety architecture analysis
* Scalability analysis
* Maintainability / supportability-by-architecture analysis

## OR / IE analyses commonly used

* Network flow analysis
* Reliability block modeling at architectural level
* Allocation / assignment models
* Optimization of resource placement
* Facility layout or topology optimization
* Inventory positioning concepts (if logistics support is central)
* Redundancy optimization
* Decision analysis for centralized vs distributed structures
* Capacity balancing across architectural nodes

## Models and simulations

* Logical architecture models
* Physical block diagrams
* Interface control concepts
* N2 matrices / DSMs (design structure matrices)
* State-machine / mode-transition models
* Reliability block diagrams
* Fault trees (preliminary)
* Network models
* High-level performance and latency simulations
* MBSE architecture views

## Typical outputs

* Selected system architecture
* Allocation baseline
* High-risk interfaces
* Architectural drivers and constraints

# Subsystem / detailed design

Purpose: refine the architecture into implementable subsystem and component definitions.

## Typical analyses

* Detailed functional allocation
* Detailed interface analysis
* Tolerance / stack-up analysis
* Design-for-manufacture / design-for-assembly (DFM/DFA)
* Design-for-testability
* Design-for-reliability / maintainability
* Preliminary FMEA / FMECA
* Thermal / structural / electrical / software performance analyses (domain-specific)
* Configuration analysis
* Detailed human factors analysis
* Supplier / sourcing analysis

## OR / IE analyses commonly used

* Line balancing (for products/processes with assembly)
* Process capability analysis
* Statistical tolerance analysis
* Time-and-motion study for service or manual tasks
* Workstation design and ergonomic analysis
* Resource loading analysis
* Scheduling analysis for detailed work packages
* Inventory / replenishment planning assumptions for parts
* Design-to-cost allocation
* Optimization of subsystem parameter settings

## Models and simulations

* Detailed design models / CAD / SysML / software design models
* Failure modes models
* Detailed queueing or transaction models
* Process plans and routing models
* Testability models / observability-controllability models
* Finite element / domain engineering simulations (where applicable)
* Detailed reliability / maintainability models
* Digital twins / digital thread elements (if used)

## Typical outputs

* Detailed design packages
* Detailed interface definitions
* Parts / software / process specifications
* Unit verification basis

# Implementation / build / procure

Purpose: realize the designed elements through manufacturing, coding, procurement, or configuration.

NASA describes implementation as the phase where detailed design is completed and products are fabricated, assembled, integrated, and tested for deployment. ([NASA][5])

## Typical analyses

* Production planning analysis
* Capacity planning
* Procurement and supplier analysis
* Make/buy execution analysis
* Quality planning
* Process validation analysis
* Work instruction and standard work analysis
* Cost and schedule control analysis
* Yield / scrap / rework analysis
* Industrialization / ramp-up analysis

## OR / IE analyses commonly used

* Master production scheduling
* Material requirements planning (MRP)-type analysis
* Inventory policy analysis
* EOQ / reorder policy analysis
* Lot sizing
* Job-shop / flow-shop scheduling
* Critical path / PERT/CPM
* Resource leveling
* Statistical process control (SPC)
* Process capability (Cp/Cpk)
* Learning-curve analysis
* Supply chain risk analysis
* Facility layout and material handling analysis

## Models and simulations

* Production system models
* Scheduling network models
* Capacity / utilization models
* Discrete-event simulation of assembly, coding, test, or deployment pipelines
* Supply chain network models
* Quality control charts and process capability models
* Cost performance / earned value models

## Typical outputs

* Realized components/subsystems
* Production readiness evidence
* Process baselines
* Supplier readiness / manufacturing readiness evidence

# Unit / component verification

Purpose: verify each lowest-level element against its specified requirements.

Verification is a lifecycle-wide activity, but in the V it appears explicitly on the right side as evidence that specified requirements have been met. ([SEBoK][6])

## Typical analyses

* Test readiness analysis
* Verification procedure analysis
* Measurement system analysis
* Statistical acceptance analysis
* Defect analysis
* Root-cause analysis of failures
* Margin analysis
* Repeatability / reproducibility analysis

## OR / IE analyses commonly used

* Design of experiments (DOE)
* Measurement system analysis (gage R&R, if applicable)
* Acceptance sampling
* Hypothesis testing
* Confidence interval estimation
* Reliability demonstration test planning
* Weibull / life-data analysis
* SPC on unit-level characteristics
* Yield analysis
* Defect Pareto analysis

## Models and simulations

* Test models and test benches
* Verification cross-reference matrix (unit level)
* Statistical quality models
* Reliability growth and life models
* Simulation-based expected-results models
* Calibration and measurement uncertainty models

## Typical outputs

* Unit verification results
* Nonconformance reports
* Corrective actions
* Verified component baseline

# Integration & integration verification

Purpose: progressively combine system elements and confirm interfaces and interactions work as intended.

## Typical analyses

* Integration sequencing analysis
* Interface verification analysis
* Compatibility analysis
* Configuration consistency analysis
* Defect clustering and integration issue analysis
* Dependency analysis
* Incremental risk analysis
* Integration resource and test environment analysis

## OR / IE analyses commonly used

* Network / dependency analysis
* Critical path analysis for integration sequence
* Queueing/resource analysis for shared labs or test stands
* Optimization of integration order to reduce risk or rework
* Fault isolation analysis
* Bayesian updating of risk as evidence accumulates
* Bottleneck analysis in integration/test pipelines

## Models and simulations

* Interface matrices
* Dependency graphs
* Integration sequence models
* Emulators / stubs / hardware-in-the-loop or software-in-the-loop models
* Discrete-event simulation of integration flows
* Fault-injection simulation
* Digital integration environments

## Typical outputs

* Integrated subsystems
* Verified interfaces
* Updated risk / defect profile
* Integration evidence by build increment


# System verification

Purpose: show the fully integrated system meets the **specified system requirements**.

SEBoK distinguishes verification as demonstrating the system fulfills specified requirements; it is performed in parallel with lifecycle activities and is not limited to a single test event. ([SEBoK][6])

## Typical analyses

* Requirements compliance analysis
* Test coverage analysis
* Verification closure analysis
* Statistical performance analysis
* Environmental qualification analysis
* Reliability / availability verification analysis
* Safety requirement verification
* Security control verification
* Margin and robustness analysis
* Defect leakage analysis

## OR / IE analyses commonly used

* Statistical hypothesis testing against requirements
* Confidence / reliability demonstration
* Availability modeling and verification
* Test sample size determination
* DOE for performance envelopes
* Variability and robustness analysis
* Sensitivity analysis
* Control charting / trend analysis during qualification
* Queueing / throughput verification in operationally representative loads

## Models and simulations

* Verification cross-reference matrix (system level)
* Qualification test models
* Reliability block diagrams and Markov models
* Load / performance test simulations
* Stress / endurance simulation
* Digital twin comparisons to measured data
* Statistical compliance models

## Typical outputs

* Verification report
* Requirement-by-requirement objective evidence
* Residual noncompliances / waivers
* System ready for validation / transition


# System validation / transition

Purpose: show the system fulfills its **intended use in the intended operational environment** and can be transitioned to users.

SEBoK defines validation as building confidence that the system can accomplish its intended use, goals, and objectives. ([SEBoK][7])

## Typical analyses

* Operational validation analysis
* User acceptance analysis
* Mission effectiveness analysis in representative conditions
* Human performance / usability validation
* Transition readiness analysis
* Training effectiveness analysis
* Deployment and cutover analysis
* Organizational readiness analysis
* Benefit realization analysis
* Post-deployment risk analysis

## OR / IE analyses commonly used

* Pilot / trial analysis
* Before-vs-after performance comparison
* Service level and wait-time validation
* Staffing sufficiency analysis
* Adoption / throughput ramp analysis
* Experimental / quasi-experimental assessment of improvement
* Cost-to-serve validation
* Queueing and workload validation under actual demand
* Decision analysis on rollout sequencing

## Models and simulations

* Operational test scenarios
* Field trial / pilot models
* Training and staffing models
* Rollout / cutover simulations
* Scenario-based mission models
* Agent-based models of user-system interaction (if appropriate)

## Typical outputs

* Validation evidence
* User acceptance
* Transition / deployment authorization
* Initial operational capability (where applicable)


# Operations & support

Purpose: sustain performance, control cost, and improve the system in service.

Lifecycle references explicitly include utilization/support after development and production. ([SEBoK][1])

## Typical analyses

* Operations performance analysis
* Reliability, availability, maintainability (RAM) analysis
* Failure trend analysis
* Root-cause / corrective action analysis
* Maintenance optimization
* Spares and inventory analysis
* Workforce and shift analysis
* Capacity / demand rebalancing
* Service quality analysis
* Cost of operations analysis
* Configuration and change impact analysis
* Obsolescence analysis
* Continuous improvement / Lean / Six Sigma analyses

## OR / IE analyses commonly used

* Queueing analysis for service systems / support desks / repair depots
* Inventory optimization for spare parts
* Preventive vs corrective maintenance optimization
* Reliability-centered maintenance (RCM)-type analysis
* Renewal / replacement analysis
* Scheduling and dispatch optimization
* Facility location / routing (if field support matters)
* Control charts and process capability in operations
* Forecasting for demand, failures, and consumables
* Simulation of support systems and repair loops
* Markov / semi-Markov availability models
* Cost and productivity analysis
* Lean waste analysis
* Value-stream analysis
* Throughput and utilization balancing

## Models and simulations

* Reliability growth / degradation models
* Repairable system models
* Spare parts simulation
* Maintenance queue simulations
* Workforce scheduling models
* Capacity and service network models
* Operational dashboards / control systems
* Digital twin for condition monitoring and predictive maintenance

## Typical outputs

* Operational performance trends
* Maintenance and sustainment plans
* Improvement backlog
* Updated lifecycle cost outlook
* Decisions on upgrade, redesign, or replacement


# Retirement / disposal

Purpose: safely and economically remove, replace, repurpose, or decommission the system.

Lifecycle standards commonly include retirement/disposal as a formal stage. ([SEBoK][1])

## Typical analyses

* Retirement feasibility and timing analysis
* Replacement analysis
* Decommissioning planning
* Disposal / environmental compliance analysis
* Data migration / archival analysis
* Asset recovery / salvage analysis
* Transition-to-successor analysis
* End-of-life risk analysis
* Workforce transition analysis

## OR / IE analyses commonly used

* Replacement timing / economic life analysis
* Net present value of retire-vs-extend decisions
* Capacity transition planning
* Inventory depletion / runout analysis
* Reverse logistics analysis
* Resource scheduling for shutdown
* Cost-risk trade-offs for phased vs immediate retirement

## Models and simulations

* Decommissioning schedules
* Reverse supply chain models
* Cutover / migration simulations
* Cost and salvage models
* Risk models for phased shutdown

## Typical outputs

* Retirement decision package
* Decommissioning plan
* Disposal / archival evidence
* Lessons learned into next lifecycle


# Cross-cutting analyses that apply across the whole V

Some analyses are not confined to one phase; they appear continuously, with different depth and fidelity.

## Risk, uncertainty, and decision analysis

* Risk identification and ranking
* Monte Carlo risk analysis
* Sensitivity analysis
* Assumptions analysis
* Decision analysis under uncertainty
* Opportunity analysis

## Cost and schedule analysis

* ROM estimates early, bottom-up later
* Lifecycle cost analysis
* Schedule network analysis
* Earned value / cost performance analysis
* Resource loading and leveling

## Quality and variation analysis

* SPC
* Process capability
* DOE
* Acceptance sampling
* Root-cause analysis
* Reliability growth

## Safety, security, resilience

* Preliminary hazard analysis → detailed hazard analysis
* Fault tree analysis
* FMEA / FMECA
* Security threat modeling
* Resilience and continuity analysis

## Modeling and simulation

A 2025 NASA modeling handbook notes that modeling supports SE work products across SE processes, reflecting the cross-cutting nature of models throughout the lifecycle. ([NASA Standards][8])

Common model classes:

* Descriptive models (requirements, structure, interfaces)
* Behavioral models (states, sequences, scenarios)
* Analytical models (cost, performance, reliability)
* Simulation models (discrete-event, agent-based, system dynamics, Monte Carlo)
* Statistical models (quality, reliability, forecasting)
* Optimization models (resource allocation, scheduling, inventory, routing)


# The most common OR / IE methods by V-diagram zone

## Left side of the V (definition side)

Most common:

* Forecasting
* MCDA / trade studies
* Optimization
* Queueing and capacity analysis
* Process analysis
* Facility / network analysis
* Cost estimation
* Decision analysis
* Scenario analysis
* Monte Carlo

## Bottom of the V (realization side)

Most common:

* Scheduling
* Resource leveling
* Inventory / supply analysis
* SPC / process capability
* Production system simulation
* Learning curves
* Yield / scrap / rework analysis

## Right side of the V (assurance side)

Most common:

* DOE
* Statistical test design
* Reliability demonstration
* Hypothesis testing
* Acceptance sampling
* Defect and root-cause analysis
* Test coverage analysis
* Operational performance validation

## In-service / sustainment

Most common:

* Maintenance optimization
* Spare parts optimization
* Queueing for support operations
* Reliability / availability / renewal models
* Continuous improvement / Lean / Six Sigma
* Replacement analysis



# A compact master checklist by phase

If you want the broadest possible checklist, a typical V-model program may touch these major analysis families:

* Mission / need / stakeholder / context analysis
* Capability and gap analysis
* ConOps and operational scenario analysis
* AoA and trade-space analysis
* Technical / operational / economic / schedule feasibility
* Requirements, functional, interface, and allocation analysis
* Architecture, modularity, interoperability, and resilience analysis
* Detailed design, tolerance, manufacturability, maintainability, and testability analysis
* Production, supply, scheduling, capacity, and quality analysis
* Unit, integration, system verification analysis
* Operational validation and transition readiness analysis
* RAM, maintenance, spares, and lifecycle cost analysis
* Retirement, replacement, reverse logistics, and disposal analysis


# Caveat

The **exact mix** depends on the domain:

* **Defense / aerospace**: heavier on mission effectiveness, AoA, safety, reliability, readiness, and formal validation.
* **Industrial systems / manufacturing**: heavier on process capability, line balance, scheduling, inventory, and maintainability.
* **Digital / software-intensive systems**: heavier on workload, latency, capacity, security, resilience, deployment, and service operations.
* **Infrastructure / logistics systems**: heavier on network flow, facility location, routing, asset lifecycle, and demand modeling.


[1]: https://sebokwiki.org/wiki/Life_Cycle_Stages? "Life Cycle Stages"
[2]: https://www.incose.org/docs/default-source/default-document-library/systems-engineering-guidebookisbn-9780692091807bb88028572db67488e78ff000036190a.pdf?sfvrsn=365365c7_0& "Systems Engineering Guidebook"
[3]: https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/? "SEH 3.0 NASA Program/Project Life Cycle"
[4]: https://essp.larc.nasa.gov/EVI-6/pdf_files/NASA_SystemsEngineeringHandbookRev2.pdf? "NASA Systems Engineering Handbook Rev 2 i"
[5]: https://www.nasa.gov/reference/system-engineering-handbook-appendix/? "System Engineering Handbook: Appendix"
[6]: https://sebokwiki.org/wiki/System_Verification? "System Verification"
[7]: https://sebokwiki.org/wiki/System_Validation? "System Validation"
[8]: https://standards.nasa.gov/system/files/tmp/2025-03-12-NASA-HDBK-1009A.pdf? "2025-03-12-NASA-HDBK-1009A.pdf"
