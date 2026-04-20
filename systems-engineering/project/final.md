# Table of Contents

1. [Introduction](#1-introduction)
    1. [Background](#11-background)
    2. [Problem](#12-problem)
    3. [Need](#13-need)
        1. [Formal Needs Statement](#131-formal-needs-statement)
    4. [Job to Be Done](#14-job-to-be-done)
    5. [Future Success](#15-future-success)

2. [Current Situation](#2-current-situation)
    1. [Current Systems and Operations](#21-current-systems-and-operations)
        1. [Human Actors](#211-human-actors)
        2. [Technologies and Tools Currently Used](#212-technologies-and-tools-currently-used)
        3. [Typical Characteristics of the Current system](#213-typical-characteristics-of-the-current-system)
        4. [Typical Current Operational Flow](#214-typical-current-operational-flow)
    2. [Deficiencies / Opportunities](#22-deficiencies--opportunities)

3. [Stakeholder Analysis](#3-stakeholder-analysis)
    1. [Stakeholder Identification and Analysis](#31-stakeholder-identification-and-analysis)
        1. [Active Stakeholders](#311-active-stakeholders)
        2. [Passive Stakeholders](#312-passive-stakeholders)
    2. [Stakeholder Requirements](#32-stakeholder-requirements)
        1. [Capabilities](#321-capabilities)
        2. [Characteristics](#322-characteristics)

4. [Acceptance Criteria](#4-acceptance-criteria)
    1. [Defined Acceptance Criteria](#41-defined-acceptance-criteria)

5. [Concept for the Proposed System](#5-concept-for-the-proposed-system)
    1. [Concept Generation](#51-concept-generation)
        1. [CONOPS](#511-conops)
    2. [Concept Selection](#52-concept-selection)
        1. [Pugh Matrix](#521-pugh-matrix)
    3. [System Context](#53-system-context)
    4. ["To Be" Operational Scenarios](#54-to-be-operational-scenarios)
    5. [Use Case Model](#55-use-case-model)
    6. [Use Case Specifications](#56-use-case-specifications)
        1. [Sequence Diagram](#561-sequence-diagram)
    7. [QFD Analysis](#57-qfd-analysis)
    8. [System Requirements](#58-system-requirements)
    9. [Functional and Physical Architecture](#59-functional-and-physical-architecture)
        1. [Input/Output Matrices](#591-inputoutput-matrices)
        2. [First Level Decomposition](#592-first-level-decomposition)
        3. [IDEF0 Model](#593-idef0-model)
    10. [Risk Assessment](#510-risk-assessment)
        1. [Technical Performance Measures](#5101-technical-performance-measures)

6. [Reflection](#6-reflection)

7. [Conclusion](#7-conclusion)

8. [References](#8-references)

9. [Appendices](#9-appendices)
    1. [Supporting Diagrams](#91-supporting-diagrams)
    2. [QFD Matrix](#92-qfd-matrix)
    3. [Use Case Details](#93-use-case-details)
    4. [Risk Management Plan](#94-risk-management-plan)

---

# 1. Introduction

## 1.1 Background

Agricultural producers in California’s Central Valley operate in an environment shaped by recurring water scarcity, variable rainfall, rising groundwater pumping costs, increasing energy costs, and uncertainty related to water allocation policies and regulatory oversight. At the same time, growers must continue to protect crop health, maintain yield, and operate within practical constraints such as labor availability, irrigation infrastructure capacity, and field-level variability in soil and crop conditions.

Irrigation decisions are therefore no longer simple timing decisions. They require balancing agronomic, economic, environmental, and operational factors across multiple fields over time. In many farming operations, these decisions are still made using a combination of grower experience, static schedules, spreadsheets, disconnected sensor tools, controller interfaces, and manual field observation. While these methods can work, they are difficult to scale and often do not provide integrated support for timely, optimized decision-making under uncertainty.

## 1.2 Problem

Current irrigation planning and execution methods do not adequately support growers and irrigation managers in determining when, where, and how much to irrigate under changing and uncertain conditions. Relevant information is often fragmented across weather data, soil moisture readings, pump records, field observations, water delivery constraints, and cost considerations. As a result, irrigation scheduling is frequently reactive, inconsistent, and dependent on individual judgment rather than supported by structured system-level analysis.

This creates several risks. Water may be over-applied, increasing waste and pumping cost. Water may also be under-applied, stressing crops and reducing yield or quality. Limited water resources may not be allocated to the highest-priority fields at the right time. Managers may also struggle to justify or document decisions in the face of operational, financial, or regulatory pressure.

The challenge is sufficiently complex that it cannot be addressed well through a single calculation or isolated manual process. It involves multiple data sources, multiple stakeholders, competing objectives, and repeated decisions over time.

## 1.3 Need

Central Valley growers and irrigation managers need a better way to make field-level irrigation decisions under uncertain and changing conditions. They need support that helps them integrate agronomic, environmental, operational, and economic information so they can decide when irrigation should occur, how much water should be applied, and how to prioritize irrigation actions when water, energy, or pumping capacity is constrained.

That need suggests the value of a software-intensive decision-support system that can gather inputs, analyze constraints, generate recommendations, and support human decision-making across changing conditions.

The system should help users:

- determine when irrigation should occur
- determine how much water should be applied
- prioritize irrigation actions when water or pumping capacity is constrained
- adapt recommendations when weather, water supply, or field conditions change
- document decisions and outcomes for operational review and accountability

There is a well-defined paying customer for such a system. The most likely sponsor or customer would be a farm owner, agricultural enterprise, vineyard operator, orchard operator, irrigation management company, or large grower organization that bears the cost of water use inefficiency, pumping energy, and crop-performance loss. In some cases, irrigation districts, water agencies, or agricultural service providers could also serve as sponsors if the system were positioned as a regional efficiency or advisory platform.

Likely users include growers, irrigation managers, farm operations managers, field supervisors, and possibly agronomists or crop advisors. The envisioned system would interact with weather data services, soil moisture sensors, irrigation controllers, pump or flow monitoring systems, farm records, and possibly utility pricing data or water allocation records.

### 1.3.1 Formal Needs Statement

California Central Valley growers and irrigation managers operate under increasing pressure from water scarcity, variable rainfall, rising pumping and energy costs, and uncertainty in water supply and regulation. Current irrigation planning methods rely on fragmented data, manual coordination, and experience-based judgment, which can lead to inefficient water use, inconsistent scheduling, and difficulty adapting to changing conditions. These challenges are sufficiently complex to require a software-intensive system that integrates environmental, agronomic, operational, and cost information to support field-level irrigation decisions. The need is supported by a clear customer base, including farms and agricultural operations that directly bear the financial and operational consequences of poor irrigation decisions. A successful solution would enable users to create adaptive, explainable, and efficient irrigation schedules that reduce waste, manage cost, and improve resilience under uncertainty. Multiple conceptual solutions are possible, including decision-support dashboards, optimization tools, and semi-automated irrigation control systems.

## 1.4 Job to Be Done

The primary job to be done is to enable growers and irrigation managers to make timely, defensible irrigation decisions that deliver sufficient water to crops while minimizing waste, pumping cost, and exposure to water-supply uncertainty. This job exists independently of any specific software solution because farms must continuously decide when, where, and how much to irrigate in order to sustain crop performance and manage limited water resources.

This job is persistent and well-defined because growers already must decide when and how much to irrigate; the decision must happen regardless of whether a software solution exists. Poor decisions have direct cost, water-use, and yield consequences. The problem is recurring, operational, and high-stakes.

## 1.5 Future Success

A successful future state would be one in which irrigation decisions are no longer based primarily on disconnected tools and informal judgment, but instead are supported by a unified system that provides timely, explainable, and operationally feasible recommendations.

Success would look like:

- irrigation schedules are generated at the field or zone level using current and forecasted conditions
- users can quickly understand why the system is recommending a specific irrigation action
- water use becomes more efficient without harming crop health or yield
- pumping is reduced or shifted more intelligently when cost is high
- scarce water is allocated more deliberately during shortage conditions
- managers can track decisions, changes, and outcomes over time
- the farm operation becomes more resilient to uncertainty in rainfall, supply, and regulation

# 2. Current Situation

## 2.1 Current Systems and Operations

In the current situation, irrigation decisions are often made using a mix of human judgment, manual coordination, and partially connected tools. Typical decision inputs include grower experience, fixed irrigation calendars, manual field inspection, weather reports, pump and flow records, spreadsheets or handwritten logs, recommendations from agronomists or irrigation consultants, and data from disconnected tools such as soil moisture sensors, weather stations, or controller systems.

In many operations, irrigation planning and execution do not occur through a single integrated system. Instead, the current operational environment is a patchwork of spreadsheets, handwritten records, weather applications, sensor dashboards, irrigation controllers, and direct communication with field crews. Scheduling decisions are therefore often made manually and revised reactively as conditions change.

The typical process involves assessing field conditions, estimating water demand, checking operational and resource constraints, scheduling irrigation by field or block, executing the plan through pumps and valves or automated controllers, and monitoring outcomes through field inspection and later adjustments.

#### 2.1.1 Human Actors

The current irrigation decision environment involves several human actors, each with a distinct role in planning, approving, executing, or responding to irrigation activity. The grower or farm owner is often the primary decision-maker or the person ultimately accountable for crop performance, water use, and operating cost. In some operations, that person makes irrigation decisions directly; in others, authority is shared with or delegated to an irrigation manager. The irrigation manager typically plays the central operational role by interpreting conditions across fields, balancing resource constraints, and translating priorities into an irrigation schedule. Field supervisors may help coordinate labor, verify field conditions, and communicate changing needs or problems from the field to management. Equipment operators are responsible for implementing the plan by running pumps, opening or closing valves, adjusting controller settings, and ensuring that irrigation equipment is functioning as intended. Agronomists or crop advisors may also influence decisions by providing recommendations based on crop condition, soil behavior, weather patterns, or production goals. In addition, external stakeholders such as water districts or regulators can shape operations by imposing delivery schedules, reporting requirements, allocation limits, or compliance constraints that must be considered during planning and execution.

#### 2.1.2 Technologies and Tools Currently Used

The technologies and tools currently used in many irrigation operations are often practical and familiar, but they are not always well integrated. Manual valve and pump controls are still common, especially in operations where physical infrastructure has developed over time and automation is partial rather than comprehensive. Irrigation controllers or timers may be used to automate portions of watering activity, but they often operate independently from broader planning tools or decision logic. Spreadsheets and paper logs remain common for tracking schedules, water use, observations, and operational notes, particularly because they are flexible and easy for local staff to modify. Weather apps or local forecasts are frequently consulted to anticipate heat, rainfall, or evapotranspiration-related conditions, while standalone soil moisture sensors provide additional field-specific information where they are installed. Larger operations may also use SCADA systems or pump-monitoring tools to track equipment status, flows, and runtime, but these systems are often focused on equipment oversight rather than integrated irrigation decision support. Communication between managers and field crews often relies on phone calls or text messages, which are useful for immediate coordination but may not create a durable or structured decision record. Accounting records and utility bills may later be used to review pumping cost, but this information is often analyzed after the fact rather than incorporated directly into daily irrigation planning.

### 2.1.3 Typical Characteristics of the Current System

Taken together, the current system is typically characterized by fragmentation, human dependence, and limited analytical integration. Information relevant to irrigation decisions is often spread across multiple sources, including field observations, controller settings, weather forecasts, sensor dashboards, utility records, and verbal communication, with no single system bringing those inputs together in a unified way. 

As a result, decision quality depends heavily on the experience and judgment of individual growers or irrigation managers, whose intuition may be strong but difficult to scale, transfer, or standardize across time and personnel. Real-time optimization is usually limited, meaning that even when useful data exists, it may not be processed quickly or systematically enough to support dynamic adjustments. Decisions are often made at the field level and sometimes at the block level, but not always at the finer irrigation-zone level where more precise control could improve outcomes. 

The system is also frequently reactive, with adjustments made after crop stress, runoff, overwatering, or delivery problems are observed rather than prevented in advance. Most importantly, there is often weak integration between agronomic considerations, operational realities, and economic constraints, making it difficult to consistently choose irrigation actions that are simultaneously good for crop health, resource efficiency, and overall farm performance.

### 2.1.4 Typical Current Operational Flow

| Step | Current Operation |
|---|---|
| 1. Assess conditions | Grower or irrigation manager reviews recent weather, looks at field conditions, checks soil visually or via sensors if available, and considers crop growth stage. |
| 2. Estimate need | Water demand is estimated based on experience, past schedules, crop type, recent temperatures, and expected rainfall. |
| 3. Check constraints | Labor availability, pump capacity, water allotments, irrigation district deliveries, energy cost, and equipment limitations are considered. |
| 4. Create schedule | A daily or weekly irrigation plan is created for each field or block, often manually. |
| 5. Execute irrigation | Workers run pumps, valves, pivots, drip systems, or set controller programs. |
| 6. Monitor results | The team checks whether irrigation occurred as intended and watches for signs of plant stress, runoff, or overwatering. |
| 7. Adjust | The next schedule is adjusted based on observed conditions, supply changes, or weather shifts. |


## 2.2 Deficiencies and Opportunities

Current irrigation planning is often manual, fragmented, and heavily dependent on experience rather than integrated analysis. Data relevant to irrigation decisions is spread across multiple sources, and scheduling is often reactive or based on fixed routines that do not adapt well to weather, soil, crop stage, cost, or water-supply constraints.

1. Irrigation decisions rely too heavily on individual judgment

   Many farms depend on the experience of growers or irrigation managers to decide when and how much to water. That experience is valuable, but it can also make decision-making inconsistent, hard to scale, and vulnerable when knowledgeable personnel are unavailable. Watering decisions may vary from person to person, may not be documented clearly, and may be difficult to repeat consistently across seasons, fields, or staff.

2. Data is fragmented across multiple tools and people

   Relevant information is often spread across weather apps, soil sensors, controller interfaces, pump records, spreadsheets, handwritten notes, and verbal communication with crews. These pieces are rarely integrated into one decision-support view. Managers must mentally combine multiple data sources, which increases effort, slows decisions, and raises the risk that important information will be overlooked.

3. Scheduling is often reactive instead of proactive

   Current practice often adjusts irrigation after visible signs of stress, changing weather, supply disruption, or unexpected operational issues appear. Even where planning exists, it may be based on fixed routines rather than dynamic conditions. Fields may be overwatered or underwatered before corrections are made, reducing efficiency and potentially affecting crop quality or yield.

4. Fixed schedules do not adapt well to changing conditions

   Many irrigation schedules are based on habit, historical practice, or generalized assumptions. However, actual water needs can change with temperature, crop growth stage, recent irrigation, rainfall, and soil variation. Water is not always applied in the right amount or at the right time, which can create waste, stress plants, and increase pumping costs.

5. Current systems may not account well for resource constraints

   Even when crop water needs are understood, decisions must also reflect real constraints such as limited water allocation, well output, pump capacity, labor availability, and electricity cost. The resulting schedule may be agronomically reasonable but operationally inefficient or financially costly.

6. Limited support for uncertainty and risk

   Water availability can change due to drought, rainfall variability, delivery restrictions, groundwater limitations, or regulatory changes. Most current practices do not provide structured support for making irrigation decisions under uncertain future conditions. Managers may be forced to make high-stakes decisions without clear visibility into tradeoffs, contingency plans, or likely outcomes.

7. Poor traceability and justification of decisions

   When decisions are made informally, it can be difficult to explain why a certain field was irrigated, why another was deferred, or why water use changed over time. This makes management review, performance improvement, and possible compliance or reporting tasks harder.

8. Difficulty prioritizing across multiple fields or zones

   When water, pumping capacity, or labor is limited, managers need to decide which fields or irrigation zones should receive water first. Current methods may not support systematic prioritization. Resources may be allocated inefficiently, especially during shortage conditions.


### 2.2.1 Opportunities for Improvement

These deficiencies create a clear opportunity for an integrated software-based precision irrigation scheduling system. Such a system could combine environmental, agronomic, and operational data into a unified decision-support platform and generate adaptive irrigation recommendations for each field or zone. By helping users determine when, where, and how much to irrigate under changing conditions, the system could improve water-use efficiency, reduce pumping cost, support better prioritization under scarcity, and increase the consistency and traceability of irrigation decisions.

1. Integrate relevant irrigation data into one platform

   A software system could combine weather forecasts, crop data, soil moisture readings, irrigation history, field-zone information, and operational constraints into one view. This will reduce mental workload and improve decision quality by making relevant information easier to access and interpret.

2. Provide decision support for optimal irrigation scheduling

   Instead of relying only on intuition or fixed calendars, the system could recommend irrigation timing and quantity for each field or zone based on current and forecasted conditions. This will improve water-use efficiency while maintaining crop health.

3. Adapt recommendations dynamically as conditions change

   The system could update schedules when weather forecasts shift, rainfall occurs, pumps fail, water allocations change, or sensor readings indicate unusual conditions. This will enable more proactive and resilient irrigation planning.

4. Balance agronomic, operational, and economic factors

   The software could account not just for plant water needs, but also for pumping costs, energy timing, equipment limitations, and water availability. A system can potentially support decisions that are both agronomically sound and operationally realistic.

5. Help prioritize water use under scarcity

   When water is limited, the system could rank fields or zones based on urgency, crop sensitivity, expected impact, or management priorities. A system will improve outcomes during shortage periods and make tradeoffs more explicit.

6. Increase consistency and transparency of decisions

   A structured system can document assumptions, recommendations, actions, and changes over time. This makes decisions easier to explain, evaluate, and improve across seasons.

7. Reduce waste and avoid unnecessary pumping expense

   By applying water more precisely and only when needed, the system could reduce over-irrigation and support more efficient pump usage. A system can help lower operating cost while conserving water.

8. Create a foundation for future automation or compliance support

   Even if the initial concept is a recommendation system rather than a control system, it could later connect to irrigation controllers, reporting tools, or regulatory documentation workflows. A recommendation system can provide long-term extensibility beyond basic scheduling.

# 3. Stakeholder Analysis

## 3.1 Stakeholder Identification and Analysis

The proposed precision irrigation scheduling system has both active and passive stakeholders. Active stakeholders are those who directly interact with, operate, configure, maintain, or make decisions with the system or depend on it to perform operational decisions. These include the grower or farm owner, irrigation manager, farm operations manager, field supervisor, irrigation crew lead, agronomist, and system support personnel. These stakeholders use the system to plan irrigation, review recommendations, allocate resources, execute field activities, and monitor performance.

Passive stakeholders are affected by the system’s outcomes but do not directly operate it. These include water districts, regulators, utility providers, local communities, consumers, environmental interests, and business stakeholders. Their interests relate to efficient water use, sustainability, cost control, agricultural reliability, and reduced environmental impact.


### 3.1.1 Active Stakeholders


| Stakeholder                                    | Why they are active                                                                         | Main interest in the system                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Grower / Farm Owner**                        | May use the system to review schedules, approve actions, and monitor performance            | Lower water use, protect yield, reduce cost, improve farm profitability         |
| **Irrigation Manager**                         | Primary day-to-day user who creates, adjusts, or executes irrigation plans using the system | Accurate recommendations, easy scheduling, better prioritization under scarcity |
| **Farm Operations Manager**                    | Uses the system to coordinate labor, equipment, and field activities                        | Operational efficiency, resource coordination, fewer disruptions                |
| **Field Supervisor / Irrigation Crew Lead**    | Uses schedule outputs to carry out watering tasks in the field                              | Clear instructions, realistic schedules, fewer manual errors                    |
| **Agronomist / Crop Advisor**                  | May review recommendations and provide crop-specific input                                  | Maintain crop health, align irrigation with agronomic best practice             |
| **System Administrator / IT Support**          | Configures users, integrations, permissions, and system availability                        | Reliability, maintainability, secure access                                     |
| **Data Analyst / Farm Management Staff**       | May review historical reports, water-use trends, and performance data                       | Better reporting, trend analysis, management insight                            |
| **Maintenance Technician / Equipment Manager** | Uses system outputs or alerts related to pumps, valves, or sensors                          | Early warning of issues, reduced downtime, easier troubleshooting               |


### 3.1.2 Passive Stakeholders

| Stakeholder                                          | Why they are passive                                                                         | Main interest in the system                                             |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Farm Workers**                                     | Affected by scheduling decisions and work allocation, but may not directly use the system    | Predictable workload, clear operations, safe working conditions         |
| **Water District / Irrigation District**             | Affected by how efficiently water is used and how demand is managed                          | Efficient allocation, reduced waste, better demand predictability       |
| **Groundwater Sustainability Agencies / Regulators** | Concerned with water use, conservation, and compliance outcomes rather than direct operation | Better water stewardship, reduced overuse, possible compliance support  |
| **Utility Providers / Energy Suppliers**             | Indirectly affected by pumping demand and time-of-use consumption                            | More predictable demand, off-peak usage patterns                        |
| **Local Communities**                                | Impacted by regional water sustainability and agricultural stability                         | Sustainable water use, economic stability, environmental responsibility |
| **Consumers / Produce Buyers**                       | Do not use the system, but may be affected by crop quality, yield stability, and price       | Reliable agricultural output, crop quality                              |
| **Environmental Interests / Ecosystems**             | Affected by groundwater withdrawal, runoff, and water-use efficiency                         | Reduced waste, less environmental stress                                |
| **Investors / Business Partners**                    | Interested in profitability and operational resilience, not daily system use                 | Lower risk, better efficiency, better business performance              |


## 3.2 Stakeholder Requirements

### 3.2.1 Capabilities

### 3.2.2 Characteristics

# 4. Acceptance Criteria

## 4.1 Defined Acceptance Criteria

# 5. Concept for the Proposed System

## 5.1 Concept Generation

### 5.1.1 CONOPS

## 5.2 Concept Selection

### 5.2.1 Pugh Matrix

## 5.3 System Context

## 5.4 "To Be" Operational Scenarios

## 5.5 Use Case Model

## 5.6 Use Case Specifications

### 5.6.1 Sequence Diagram

## 5.7 QFD Analysis

## 5.8 System Requirements

| Requirement Number | System Requirement | Traceability | Verification |
|---|---|---|---|
| SR-001 | The system shall... | Stakeholder / Use Case / QFD / Acceptance Criteria | Test / Analysis / Inspection / Demonstration |
| SR-002 | The system shall... |  |  |
| SR-003 | The system shall... |  |  |
| SR-004 | The system shall... |  |  |
| SR-005 | The system shall... |  |  |
| SR-006 | The system shall... |  |  |
| SR-007 | The system shall... |  |  |
| SR-008 | The system shall... |  |  |
| SR-009 | The system shall... |  |  |
| SR-010 | The system shall... |  |  |

## 5.9 Functional and Physical Architecture

### 5.9.1 Input/Output Matrices

### 5.9.2 First Level Decomposition

### 5.9.3 IDEF0 Model

## 5.10 Risk Assessment

### 5.10.1 Technical Performance Measures

# 6. Reflection

# 7. Conclusion

# 8. References

# 9. Appendices

## 9.1 Supporting Diagrams

## 9.2 QFD Matrix

## 9.3 Use Case Details

## 9.4 Risk Management Plan