# Annotated Bibliography: Models Embedded in Adaptive Systems

The literature below concerns a common problem:

> **A model, metric, prediction, or policy may change the system it describes, invalidating the relationships on which it was based.**

The relevant disciplines use different vocabularies because they emphasize different mechanisms. Economists focus on changing expectations and incentives; sociologists on constitutive classifications and institutions; machine-learning researchers on deployment-induced distribution shift; system dynamicists on feedback; and evolutionary biologists on selection and coevolution.

This is a **selective research bibliography**, organized around the most important conceptual traditions rather than an exhaustive list.

---

## I. The Lucas Critique and Policy-Regime Dependence

### Orientation

The Lucas Critique concerns the failure of historically estimated behavioral relationships to remain stable after a policy-regime change. Its defining mechanism is not merely that an intervention has side effects, but that agents revise their decisions because the rules and their expectations have changed.

### Foundational work

**Lucas, Robert E., Jr. 1976. “Econometric Policy Evaluation: A Critique.” _Carnegie-Rochester Conference Series on Public Policy_ 1: 19–46.**

The foundational statement. Lucas argues that parameters estimated from historical aggregate data need not be invariant under policy changes because individuals’ decision rules depend on expected policy. A model that forecasts a new regime while retaining behavioral equations from the old regime can therefore give systematically misleading results. This is the essential starting point for understanding policy-dependent data-generating processes.

**Sargent, Thomas J., and Neil Wallace. 1975. “Rational Expectations, the Optimal Monetary Instrument, and the Optimal Money Supply Rule.” _Journal of Political Economy_ 83 (2): 241–254.**

An early rational-expectations analysis showing that policy outcomes depend on how private agents understand the monetary regime. It complements Lucas by making explicit why anticipated and unanticipated policy may have different effects.

**Sargent, Thomas J., and Neil Wallace. 1976. “Rational Expectations and the Theory of Economic Policy.” _Journal of Monetary Economics_ 2 (2): 169–183.**

Develops the consequences of rational expectations for policy analysis. Particularly useful for seeing how the Lucas problem becomes an equilibrium problem: policy rules, expectations, and private behavior must be solved jointly.

**Kydland, Finn E., and Edward C. Prescott. 1977. “Rules Rather than Discretion: The Inconsistency of Optimal Plans.” _Journal of Political Economy_ 85 (3): 473–491.**

Shows that a policy considered optimal before private actors respond may no longer be optimal afterward. Anticipating this, agents adjust their behavior in advance. The paper extends the Lucas insight from parameter instability to the strategic credibility of policy.

### Assessment and extensions

**Ericsson, Neil R., and John S. Irons, eds. 1995. _Testing Exogeneity_. Oxford University Press. See especially Ericsson, “The Lucas Critique in Practice.”**

Examines whether the Lucas Critique is empirically consequential and how policy invariance might be tested. Ericsson emphasizes that Lucas identified a possible failure of econometric models, not a proof that every reduced-form relation necessarily changes after every intervention.

**Hoover, Kevin D. 1994. “Econometrics as Observation: The Lucas Critique and the Nature of Econometric Inference.” _Journal of Economic Methodology_ 1 (1): 65–80.**

A methodological interpretation of Lucas. Hoover asks what can actually be learned from observational macroeconomic relationships and whether “deep parameters” are as directly recoverable as the structural modeling program sometimes assumes.

**Lawson, Tony. 1995. “The ‘Lucas Critique’: A Generalisation.” _Cambridge Journal of Economics_ 19 (2): 257–276.**

One of the most directly relevant works for the broader question. Lawson argues that Lucas’s observation can be generalized: interventions may alter the social structures and causal mechanisms that generated the original regularities. This moves beyond rational expectations toward a general critique of invariant social-scientific laws.

### Applications

This literature is most developed in monetary and fiscal policy, structural econometrics, labor supply, taxation, and macroeconomic forecasting. The recurring methodological response is to seek models based on preferences, technologies, constraints, information, and explicit policy rules rather than purely historical aggregate correlations.

---

## II. Goodhart’s Law and Proxy Failure Under Optimization

### Orientation

Goodhart’s Law concerns a proxy that is useful while it is merely observed but becomes unreliable once it is deliberately optimized. The intervention acts directly on the measured indicator, often separating it from the underlying objective.

### Foundational work

**Goodhart, Charles A. E. 1975. “Problems of Monetary Management: The U.K. Experience.” In _Papers in Monetary Economics_, vol. 1. Reserve Bank of Australia.**

Goodhart’s original context was monetary policy. Once a monetary aggregate was selected for control, financial institutions and market participants adapted, weakening the empirical relationship that had made the aggregate useful in the first place. The original formulation is therefore closely related to the Lucas Critique, although Goodhart emphasizes control through indicators.

**Goodhart, Charles A. E. 1984. _Monetary Theory and Practice: The UK Experience_. Macmillan.**

Collects and develops Goodhart’s monetary-policy arguments. Useful for understanding that the law did not originate as a generic slogan about metrics but as an observation about financial innovation and endogenous reactions to monetary control.

### Modern taxonomy

**Manheim, David, and Scott Garrabrant. 2019. “Categorizing Variants of Goodhart’s Law.” _arXiv:1803.04585_.**

The clearest modern taxonomy. The authors distinguish:

- **regressional Goodhart**, caused by selecting extreme values of a noisy proxy;
- **extremal Goodhart**, caused by optimizing outside the domain where the proxy was reliable;
- **causal Goodhart**, caused by intervening on a correlate rather than the true causal objective;
- **adversarial Goodhart**, caused by agents actively gaming the proxy.

The paper is valuable because these mechanisms require different remedies. Better measurement may help regressional failure but not necessarily strategic manipulation.

**Strathern, Marilyn. 1997. “‘Improving Ratings’: Audit in the British University System.” _European Review_ 5 (3): 305–321.**

A major anthropological statement of the broader maxim, commonly paraphrased as “when a measure becomes a target, it ceases to be a good measure.” Strathern applies it to academic auditing, showing how evaluation systems reorganize the activity they purport merely to assess.

### Applications and syntheses

**Muller, Jerry Z. 2018. _The Tyranny of Metrics_. Princeton University Press.**

A wide-ranging synthesis covering education, medicine, policing, business, universities, and public administration. More synthetic than technical, but especially useful for comparing institutional consequences of metric fixation.

**Power, Michael. 1997. _The Audit Society: Rituals of Verification_. Oxford University Press.**

Studies how auditing and verification practices reshape organizations. The book explains why organizations often optimize visible, auditable processes rather than substantive outcomes.

**Espeland, Wendy Nelson, and Michael Sauder. 2007. “Rankings and Reactivity: How Public Measures Recreate Social Worlds.” _American Journal of Sociology_ 113 (1): 1–40.**

A major empirical study of law-school rankings. It shows how rankings alter resource allocation, admissions strategy, organizational identity, and participants’ perceptions. It links Goodhart-type gaming to the sociology of reactivity: measures do not merely become less accurate; they reorganize institutions.

---

## III. Campbell’s Law and Corruption Pressures in Social Indicators

### Orientation

Campbell’s Law is closely related to Goodhart’s Law but places more emphasis on institutional stakes, corruption pressures, and the degradation of the activity being evaluated.

### Foundational work

**Campbell, Donald T. 1976. _Assessing the Impact of Planned Social Change_. Occasional Paper Series no. 8, Public Affairs Center, Dartmouth College. Reprinted 1979 in _Evaluation and Program Planning_ 2 (1): 67–90.**

Campbell argues that the greater the role of a quantitative indicator in social decision-making, the greater the pressure to corrupt the indicator and distort the processes it is supposed to monitor. He discusses educational testing, program evaluation, and the political difficulties of preserving valid evidence when careers and institutions depend on measured results.

**Campbell, Donald T. 1988. _Methodology and Epistemology for Social Science: Selected Papers_. Edited by E. Samuel Overman. University of Chicago Press.**

Places Campbell’s Law within his broader work on quasi-experimentation, institutional learning, and the “experimenting society.” Campbell did not reject measurement; he sought plural, revisable evaluation systems less susceptible to centralized manipulation.

### Applications

**Nichols, Sharon L., and David C. Berliner. 2007. _Collateral Damage: How High-Stakes Testing Corrupts America’s Schools_. Harvard Education Press.**

Applies Campbell’s logic to high-stakes educational testing. It documents teaching to the test, curriculum narrowing, exclusion of low-performing students, and other adaptations that raise measured performance without necessarily improving education.

**Jacob, Brian A., and Steven D. Levitt. 2003. “Rotten Apples: An Investigation of the Prevalence and Predictors of Teacher Cheating.” _Quarterly Journal of Economics_ 118 (3): 843–877.**

An empirical study of teacher cheating under high-stakes testing. It is a particularly clean example of indicator pressure producing strategically altered data.

**Bevan, Gwyn, and Christopher Hood. 2006. “What’s Measured Is What Matters: Targets and Gaming in the English Public Health Care System.” _Public Administration_ 84 (3): 517–538.**

Examines target-based governance in healthcare. It distinguishes several forms of gaming and shows how centrally imposed targets can improve some measured dimensions while displacing effort or manipulating reported performance elsewhere.

### Relation to Goodhart

Goodhart’s Law is often framed as a statistical failure of proxies. Campbell’s Law highlights the **political and organizational mechanism**: rewards and punishments create incentives to manipulate both the metric and the underlying practice.

---

## IV. Self-Fulfilling Prophecies, Reflexive Predictions, and Expectation Feedback

### Orientation

This tradition asks how beliefs or publicly disseminated forecasts causally influence whether the forecast comes true. Unlike Goodhart, no explicit optimization target is required. The mechanism may be coordination, panic, stigma, confidence, or preventive action.

### Foundational sociology

**Merton, Robert K. 1948. “The Self-Fulfilling Prophecy.” _Antioch Review_ 8 (2): 193–210.**

Merton defines a self-fulfilling prophecy as an initially false understanding of a situation that evokes behavior making the belief true. His central examples include bank runs and racial prejudice. The concept captures positive feedback from belief to behavior to apparent confirmation.

**Thomas, William I., and Dorothy Swaine Thomas. 1928. _The Child in America: Behavior Problems and Programs_. Knopf.**

The source of the “Thomas theorem”: when people define situations as real, those definitions are real in their consequences. This is a foundational precursor to Merton.

### Formal and empirical development

**Schelling, Thomas C. 1960. _The Strategy of Conflict_. Harvard University Press.**

Shows how expectations can coordinate actors on one among several possible equilibria. Focal points, commitments, and anticipated reactions explain how collectively held beliefs can organize real outcomes without any centralized enforcement.

**Diamond, Douglas W., and Philip H. Dybvig. 1983. “Bank Runs, Deposit Insurance, and Liquidity.” _Journal of Political Economy_ 91 (3): 401–419.**

A canonical formal model of self-fulfilling bank runs. Depositors’ expectations about others’ withdrawals can select between a stable and a crisis equilibrium.

**Azariadis, Costas. 1981. “Self-Fulfilling Prophecies.” _Journal of Economic Theory_ 25 (3): 380–396.**

Develops self-fulfilling equilibrium dynamics in macroeconomics. Useful for understanding “sunspot” equilibria in which beliefs not anchored in fundamentals can nevertheless coordinate economically consequential behavior.

### Philosophy of prediction

**Buck, Roger C. 1963. “Reflexive Predictions.” _Philosophy of Science_ 30 (4): 359–369.**

A foundational philosophical treatment of predictions whose accuracy can be changed by their dissemination and uptake. Buck asks whether such predictions create a special methodological problem for social science.

**Romanos, George D. 1973. “Reflexive Predictions.” _Philosophy of Science_ 40 (1): 97–109.**

Refines and critiques earlier formulations, attempting to distinguish reflexive predictions from ordinary causal effects of information.

**Kopec, Matthew. 2011. “A More Fulfilling (and Frustrating) Take on Reflexive Predictions.” _Philosophy of Science_ 78 (5): 1249–1260.**

Argues that the methodological difficulties are more serious than the earlier literature acknowledged, especially where forecasters cannot know how audiences will interpret or respond to the prediction.

### Applications

Important application domains include financial panics, inflation expectations, electoral bandwagon and underdog effects, teacher expectations of students, racial stereotyping, medical prognosis, and public-risk warnings. The same forecast may be self-fulfilling in one setting and self-defeating in another.

---

## V. Reflexivity in Economics and Finance

### Orientation

Reflexivity describes a two-way connection between participants’ representations of reality and the reality those representations help produce. It is broader than self-fulfilling prophecy because the feedback may continue recursively rather than terminate once a prediction is confirmed.

### Major texts

**Soros, George. 1987. _The Alchemy of Finance_. Simon & Schuster.**

Soros’s central statement. He distinguishes a “cognitive function,” through which participants try to understand the world, from a “participating function,” through which their decisions change it. In markets, beliefs affect prices, collateral, credit, investment, and business performance, which then alter beliefs.

**Soros, George. 2013. “Fallibility, Reflexivity, and the Human Uncertainty Principle.” _Journal of Economic Methodology_ 20 (4): 309–329.**

A more concise and academically framed exposition. Soros argues that social situations involving thinking participants cannot be treated in the same way as phenomena wholly independent of observers.

**Arthur, W. Brian. 1994. _Increasing Returns and Path Dependence in the Economy_. University of Michigan Press.**

Shows how positive feedback, coordination, and increasing returns can lock economies into paths that are partly produced by expectations and early contingent events.

**Arthur, W. Brian. 2015. “Complexity and the Economy.” _Oxford Review of Economic Policy_ 31 (2): 199–211.**

Presents the economy as an evolving system in which agents continually react to patterns partly created by their own reactions. This is a useful bridge between financial reflexivity and complexity economics.

### Applications

The reflexivity approach is particularly relevant to asset bubbles, collateral cycles, exchange-rate crises, credit booms, venture-capital narratives, and markets in which higher valuations improve the financing and apparent fundamentals of the valued asset.

---

## VI. Performativity of Economics and Models

### Orientation

Performativity makes a stronger claim than “people react to forecasts.” Economic theories, formulas, categories, and technical devices may become part of the infrastructure through which markets are constituted. Models can therefore help make economic activity resemble the model.

### Foundational works

**Callon, Michel, ed. 1998. _The Laws of the Markets_. Blackwell.**

The foundational collection for the performativity program in economic sociology. Callon argues that economics does not merely describe an independently existing economy; economic knowledge, calculative devices, accounting systems, and market technologies help organize and stabilize concrete markets.

**Barnes, Barry. 1983. “Social Life as Bootstrapped Induction.” _Sociology_ 17 (4): 524–545.**

Develops the idea that social classifications can become self-validating because people organize conduct around collectively sustained categories. Barnes’s work is an important precursor to what is sometimes called “Barnesian performativity.”

### Canonical empirical studies

**MacKenzie, Donald, and Yuval Millo. 2003. “Constructing a Market, Performing Theory: The Historical Sociology of a Financial Derivatives Exchange.” _American Journal of Sociology_ 109 (1): 107–145.**

A landmark study of the Chicago Board Options Exchange. The authors show how financial economics helped legitimate, organize, and technically equip options markets. Option-pricing theory did not simply predict prices; its formulas, assumptions, and trading practices became components of the market.

**MacKenzie, Donald. 2006. _An Engine, Not a Camera: How Financial Models Shape Markets_. MIT Press.**

The major book-length treatment. MacKenzie distinguishes different forms of performativity, including cases where model use makes markets conform more closely to theory and cases of “counterperformativity,” where use of a model undermines its own assumptions.

**MacKenzie, Donald. 2004. “The Big, Bad Wolf and the Rational Market: Portfolio Insurance, the 1987 Crash and the Performativity of Economics.” _Economy and Society_ 33 (3): 303–334.**

An application to portfolio insurance and the 1987 stock-market crash. It illustrates counterperformativity: widespread use of a trading strategy based on a model may contribute to price dynamics that invalidate the model’s assumptions.

**MacKenzie, Donald, Fabian Muniesa, and Lucia Siu, eds. 2007. _Do Economists Make Markets? On the Performativity of Economics_. Princeton University Press.**

A broad collection of empirical and conceptual studies. It is useful for assessing the scope and limits of the performativity thesis beyond option pricing.

### Distinctive contribution

Where Lucas worries that intervention makes a model **less predictively invariant**, performativity also considers cases where adoption makes a model **more descriptively accurate** by reshaping institutions around it.

---

## VII. Performative Prediction in Machine Learning

### Orientation

Performative prediction formalizes the situation in which deploying a predictive model changes the distribution of future data. It is the clearest contemporary mathematical formulation of the general embedded-model problem.

### Foundational work

**Perdomo, Juan C., Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. 2020. “Performative Prediction.” In _Proceedings of the 37th International Conference on Machine Learning_, 7599–7609.**

Introduces a formal framework in which model parameters induce a distribution over future observations. The paper distinguishes ordinary empirical-risk minimization from performative risk and defines **performative stability**, where retraining on the distribution induced by a deployed model reproduces the same model. It also shows that stability and optimality need not coincide.

**Mendler-Dünner, Celestine, Juan C. Perdomo, Tijana Zrnic, and Moritz Hardt. 2020. “Stochastic Optimization for Performative Prediction.” _Advances in Neural Information Processing Systems_ 33.**

Studies how frequently a model should be redeployed when deployment changes the environment. It distinguishes parameter updating from actual deployment and analyzes “greedy” versus “lazy” deployment policies.

### Extensions

**Brown, Gavin, Shlomi Hod, and Iden Kalemaj. 2022. “Performative Prediction in a Stateful World.” _Proceedings of AISTATS_.**

Extends the basic framework to environments with memory. Current distributions depend not only on the current model but also on previous system states, making the problem closer to dynamic control.

**Jagadeesan, Meena, Tijana Zrnic, and Celestine Mendler-Dünner. 2022. “Regret Minimization with Performative Feedback.” In _Proceedings of ICML_.**

Frames repeated model deployment as an online-learning problem. It asks how decision-makers can learn effectively when their own past actions alter the data they subsequently observe.

**Hardt, Moritz, and Celestine Mendler-Dünner. 2023. “Performative Prediction: Past and Future.”**

A conceptual survey linking learning, steering, equilibrium, causal inference, and platform power. It is a useful entry point after Perdomo et al.

### Applications

Applications include recommendation systems, credit scoring, hiring, predictive policing, education, healthcare, navigation, content moderation, and political targeting. In each case, model outputs influence decisions that affect the population on which the next version of the model is trained.

---

## VIII. Strategic Classification and Gaming

### Orientation

Strategic classification is a special case of performative prediction in which individuals knowingly alter observable features in response to a classifier. The environment changes because classified agents are strategic.

### Foundational work

**Hardt, Moritz, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters. 2016. “Strategic Classification.” In _Proceedings of the 2016 ACM Conference on Innovations in Theoretical Computer Science_, 111–122.**

Formalizes classification as a game between a decision-maker and an individual who can modify features at a cost. The paper studies classifiers that remain accurate with respect to individuals’ underlying characteristics despite gaming.

**Brückner, Michael, and Tobias Scheffer. 2011. “Stackelberg Games for Adversarial Prediction Problems.” In _Proceedings of KDD_, 547–555.**

An early game-theoretic approach to prediction when an adversary responds to the learned rule. The learner commits to a model and the adversary optimizes against it.

**Dalvi, Nilesh, Pedro Domingos, Sumit Sanghai, and Deepak Verma. 2004. “Adversarial Classification.” In _Proceedings of KDD_, 99–108.**

A foundational treatment of classification under feature manipulation, originally motivated by spam and fraud detection.

### Causal and social extensions

**Milli, Smitha, John Miller, Anca D. Dragan, and Moritz Hardt. 2019. “The Social Cost of Strategic Classification.” In _Proceedings of FAT*_.**

Shows that making a classifier robust to gaming does not automatically make it socially desirable. Strategic adaptation may impose substantial costs on individuals, especially when changing observable features does not improve the underlying outcome.

**Kleinberg, Jon, and Manish Raghavan. 2020. “How Do Classifiers Induce Agents to Invest Effort Strategically?” _ACM Transactions on Economics and Computation_ 8 (4).**

Distinguishes socially valuable improvement from superficial gaming. A classifier can encourage productive investment when the features rewarded are causally connected to genuine qualification.

### Applications

Examples include résumé keywords, search-engine optimization, credit profiles, school admissions, insurance declarations, tax reporting, fraud detection, spam filters, and content-moderation evasion.

---

## IX. Policy Resistance and System Dynamics

### Orientation

System dynamics studies interventions that activate feedback loops, delays, compensating responses, and unintended consequences. Unlike Lucas, adaptive response need not involve rational expectations; it may arise from organizational routines, resource constraints, physical accumulation, or decentralized behavior.

### Foundational works

**Forrester, Jay W. 1961. _Industrial Dynamics_. MIT Press.**

Introduces system dynamics as a method for modeling stocks, flows, delays, and feedback in organizations and industrial systems.

**Forrester, Jay W. 1969. _Urban Dynamics_. MIT Press.**

Applies system dynamics to urban policy. The controversial models illustrate how apparently beneficial interventions can have delayed or countervailing effects through housing, employment, migration, and public services.

**Forrester, Jay W. 1971. “Counterintuitive Behavior of Social Systems.” _Theory and Decision_ 2: 109–140.**

A classic statement that complex social systems often respond to policy in unexpected, ineffective, or harmful ways because policymakers focus on immediate symptoms and neglect feedback structure.

### Major synthesis

**Sterman, John D. 2000. _Business Dynamics: Systems Thinking and Modeling for a Complex World_. Irwin/McGraw-Hill.**

The standard comprehensive text. It develops causal-loop diagrams, stock-and-flow models, delays, nonlinearities, behavioral decision rules, and model testing.

**Sterman, John D. 2006. “Learning from Evidence in a Complex World.” _American Journal of Public Health_ 96 (3): 505–514.**

Defines policy resistance as the tendency of interventions to be defeated by the system’s response. Sterman emphasizes that so-called side effects are not outside the system; they are effects produced through feedback loops omitted from the decision-maker’s mental model.

**Sterman, John D. 2002. “All Models Are Wrong: Reflections on Becoming a Systems Scientist.” _System Dynamics Review_ 18 (4): 501–531.**

A methodological essay emphasizing model boundaries, endogenous explanations, learning, and the risks of treating feedback from other actors as exogenous disturbance.

### Applications

System-dynamics studies have examined induced traffic demand, public health, obesity, epidemics, fisheries, climate policy, drug enforcement, housing, supply chains, energy transitions, and organizational growth.

---

## X. Evolutionary Response and the Red Queen

### Orientation

Evolutionary analogues show that Lucas-type instability does not require conscious strategy. An intervention changes selection pressures, causing a population’s composition or traits to evolve. The data-generating process changes through differential survival and reproduction.

### Red Queen theory

**Van Valen, Leigh. 1973. “A New Evolutionary Law.” _Evolutionary Theory_ 1: 1–30.**

Introduces the Red Queen hypothesis in the context of extinction patterns. Van Valen proposes that the effective environment of a lineage continually deteriorates because other organisms are also evolving. Adaptation may therefore be necessary simply to maintain relative fitness.

**Bell, Graham. 1982. _The Masterpiece of Nature: The Evolution and Genetics of Sexuality_. University of California Press.**

Develops a microevolutionary Red Queen account of sexual reproduction, especially under changing parasite pressures.

**Brockhurst, Michael A., et al. 2014. “Running with the Red Queen: The Role of Biotic Conflicts in Evolution.” _Proceedings of the Royal Society B_ 281.**

A review of antagonistic coevolution among hosts, parasites, predators, prey, and competitors. It clarifies empirical predictions and modern uses of the Red Queen hypothesis.

### Intervention-driven evolution

**Palumbi, Stephen R. 2001. _The Evolution Explosion: How Humans Cause Rapid Evolutionary Change_. W. W. Norton.**

A broad account of human-induced selection through antibiotics, pesticides, harvesting, and habitat change.

**Hendry, Andrew P., Kiyoko M. Gotanda, and Erik I. Svensson. 2017. “Human Influences on Evolution, and the Ecological and Societal Consequences.” _Philosophical Transactions of the Royal Society B_ 372.**

Surveys anthropogenic evolutionary change and its feedback into ecological and social outcomes.

### Relation to Lucas

Lucas emphasizes **within-agent behavioral adaptation** under changed expectations. Evolutionary models emphasize **population adaptation** under changed selection. Both reject forecasts that assume the pre-intervention response mechanism will remain fixed.

---

## XI. Adversarial Adaptation and Cybersecurity

### Orientation

Security systems are paradigmatic embedded models because targets actively inspect, evade, and exploit defenses. What looks statistically stable before deployment can disappear once adversaries learn the rule.

### Core works

**Dalvi, Nilesh, et al. 2004. “Adversarial Classification.” In _Proceedings of KDD_, 99–108.**

Introduces a decision-theoretic framework for classification where malicious actors optimally modify inputs to evade detection.

**Lowd, Daniel, and Christopher Meek. 2005. “Adversarial Learning.” In _Proceedings of KDD_, 641–647.**

Studies how adversaries can infer and circumvent a classifier through query access. It makes explicit that secrecy and adaptation are part of the model environment.

**Barreno, Marco, Blaine Nelson, Russell Sears, Anthony D. Joseph, and J. D. Tygar. 2006. “Can Machine Learning Be Secure?” In _Proceedings of the ACM Symposium on Information, Computer and Communications Security_.**

Provides an influential taxonomy of attacks on machine-learning systems, including causative versus exploratory attacks and attacks on integrity versus availability.

**Biggio, Battista, and Fabio Roli. 2018. “Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning.” _Pattern Recognition_ 84: 317–331.**

A historical review connecting cybersecurity, pattern recognition, and adversarial examples.

**Goodfellow, Ian J., Jonathon Shlens, and Christian Szegedy. 2015. “Explaining and Harnessing Adversarial Examples.” In _International Conference on Learning Representations_.**

Establishes the modern adversarial-example literature, although its mechanism differs somewhat from strategic social adaptation: inputs are deliberately constructed to exploit model geometry.

### General lesson

A defensive model changes the attacker’s optimization problem. Evaluation against a static historical distribution can therefore substantially overstate real-world performance.

---

## XII. The Hawthorne Effect and Reactivity to Observation

### Orientation

The Hawthorne effect is a narrower claim: research participants may change behavior because they know they are being observed or studied.

### Historical sources

**Roethlisberger, F. J., and William J. Dickson. 1939. _Management and the Worker_. Harvard University Press.**

The major report associated with the Western Electric Hawthorne studies. It describes experiments concerning working conditions, social relations, supervision, and productivity.

**Mayo, Elton. 1933. _The Human Problems of an Industrial Civilization_. Macmillan.**

Interprets the Hawthorne research as evidence for the importance of social organization, attention, and informal groups at work.

### Critical reassessment

**McCambridge, Jim, John Witton, and Diana R. Elbourne. 2014. “Systematic Review of the Hawthorne Effect: New Concepts Are Needed to Study Research Participation Effects.” _Journal of Clinical Epidemiology_ 67 (3): 267–277.**

A systematic review finding substantial conceptual ambiguity and heterogeneous evidence. It recommends treating research-participation effects as a family of possible mechanisms rather than a single universal effect.

**Levitt, Steven D., and John A. List. 2011. “Was There Really a Hawthorne Effect at the Hawthorne Plant? An Analysis of the Original Illumination Experiments.” _American Economic Journal: Applied Economics_ 3 (1): 224–238.**

Reanalyzes the original data and finds less support for the standard textbook story than commonly assumed.

**Mannevuo, Mona. 2018. “The Riddle of Adaptation: Revisiting the Hawthorne Studies.” _Sociology_ 52 (6): 1228–1243.**

Reconstructs the studies historically and emphasizes adaptation, experimental management, and the social relations of the research setting.

### Relation to the broader family

The Hawthorne effect concerns **observation-induced behavior change**, not necessarily changed policy, strategic gaming, or institutional performativity. It is therefore a genuine relative of Lucas but not a synonym.

---

## XIII. Mechanism Design as a Constructive Response

### Orientation

Mechanism design is not principally a critique. It is a response to the problem of adaptive agents: design the rules while explicitly anticipating strategic behavior, private information, and equilibrium responses.

### Foundations

**Hurwicz, Leonid. 1960. “Optimality and Informational Efficiency in Resource Allocation Processes.” In _Mathematical Methods in the Social Sciences_, edited by Kenneth Arrow, Samuel Karlin, and Patrick Suppes. Stanford University Press.**

An early foundation of mechanism design. Hurwicz treats institutions as communication and decision systems constrained by decentralized information.

**Hurwicz, Leonid. 1972. “On Informationally Decentralized Systems.” In _Decision and Organization_, edited by C. B. McGuire and Roy Radner. North-Holland.**

Develops incentive compatibility and the informational constraints faced by institutional designers.

**Gibbard, Allan. 1973. “Manipulation of Voting Schemes: A General Result.” _Econometrica_ 41 (4): 587–601.**

Shows that broad classes of voting mechanisms are manipulable. This is a central impossibility result for designing rules when participants respond strategically.

**Satterthwaite, Mark A. 1975. “Strategy-Proofness and Arrow’s Conditions.” _Journal of Economic Theory_ 10 (2): 187–217.**

Independently establishes the voting-manipulation result now known as the Gibbard–Satterthwaite theorem.

**Myerson, Roger B. 1981. “Optimal Auction Design.” _Mathematics of Operations Research_ 6 (1): 58–73.**

A foundational analysis of revenue-optimal auctions under private information.

**Myerson, Roger B., and Mark A. Satterthwaite. 1983. “Efficient Mechanisms for Bilateral Trading.” _Journal of Economic Theory_ 29 (2): 265–281.**

Shows that under standard assumptions no mechanism can simultaneously achieve efficiency, incentive compatibility, individual rationality, and budget balance in bilateral trade.

**Maskin, Eric. 1999. “Nash Equilibrium and Welfare Optimality.” _Review of Economic Studies_ 66 (1): 23–38.**

A foundational work in implementation theory, asking when desired social-choice rules can be realized as equilibria of a designed game.

### Applications

Mechanism design has informed spectrum auctions, procurement, school assignment, kidney exchange, matching markets, online advertising, platform design, voting rules, taxation, and financial regulation.

### Limits

Mechanism design internalizes strategic response, but only relative to a specified model of preferences, information, rationality, and available actions. Agents may learn differently, develop unforeseen strategies, form coalitions, or alter institutions outside the modeled game. It solves a Lucas-type problem only to the extent that the response model is itself structurally adequate.

---

# Overarching Themes

## 1. The Distinction Between Observation and Intervention

All of these traditions reject the inference:

\[
P(Y\mid X=x)
\quad\Rightarrow\quad
P(Y\mid do(X=x)).
\]

A historical association does not by itself identify the result of actively changing \(X\). The intervention may alter expectations, incentives, population composition, institutional practices, or causal pathways.

Lucas emphasizes this for policy regimes. Goodhart emphasizes it for metrics. Evolutionary biology emphasizes it for selection pressures.

## 2. Endogenous Distribution Shift

In conventional prediction, the future data distribution is treated as external to the model. Here it depends on the model or decision:

\[
D_{t+1}=F(D_t,M_t,A_t,R_t),
\]

where \(M_t\) is the model, \(A_t\) the action taken from it, and \(R_t\) the system’s response.

This is explicit in performative prediction, implicit in Lucas, and expressed as feedback structure in system dynamics.

## 3. Several Distinct Adaptive Mechanisms

The system may change through:

- **expectation revision** — Lucas, rational expectations;
- **strategic gaming** — Goodhart, Campbell, strategic classification;
- **coordination on beliefs** — self-fulfilling prophecy;
- **institutional reconstruction** — performativity;
- **dynamic compensation** — policy resistance;
- **selection and reproduction** — evolutionary adaptation;
- **reciprocal strategic competition** — adversarial learning and Red Queen dynamics;
- **reactivity to observation** — Hawthorne effects.

These mechanisms should not be collapsed into one vague idea. They imply different modeling and policy responses.

## 4. Positive and Negative Reflexivity

Deployment can weaken a model, but it need not.

**Self-defeating effects:**  
A traffic forecast diverts drivers and prevents the predicted congestion.

**Self-fulfilling effects:**  
A bank-failure forecast triggers withdrawals and causes failure.

**Performative convergence:**  
A pricing model becomes a market convention, causing prices to conform more closely to it.

**Oscillation or instability:**  
Repeated adaptation by models and agents prevents convergence.

Thus “the model changes the system” does not specify the direction of change.

## 5. Models Can Be Descriptive, Strategic, and Infrastructural

A model may enter the system in at least three ways:

1. **As information:** people hear a forecast and respond.
2. **As a rule:** institutions allocate rewards or penalties using it.
3. **As infrastructure:** software, accounting systems, contracts, and market procedures instantiate its categories.

Lucas and Merton focus mainly on the first two. Performativity research gives special attention to the third.

## 6. Invariance Is the Central Methodological Objective

A robust model needs relationships that survive the intervention being considered. Different fields pursue this goal differently:

- structural economics seeks policy-invariant preferences, technologies, and constraints;
- causal inference seeks interventionally stable causal mechanisms;
- mechanism design models equilibrium response to rules;
- system dynamics models feedback and delays;
- robust machine learning anticipates gaming and distribution shift;
- evolutionary medicine models selection generated by treatment.

The shared challenge is to identify **what remains stable while agents and environments adapt**.

## 7. Adaptation Can Occur at Multiple Levels

Responses may occur within individuals, between agents, inside organizations, across institutions, or over generations.

For example, a hospital target can produce:

- clinicians changing treatment decisions;
- administrators changing coding;
- patients changing where they seek care;
- regulators changing targets;
- firms developing new services around the metric.

A model that captures only one level can still fail through adaptation at another.

## 8. Reflexivity Complicates Model Validation

Ordinary validation asks whether a model predicts held-out observations. Embedded-model validation must also ask:

- What happens after the model becomes known?
- What actions are taken because of it?
- Who benefits from manipulating it?
- Does it change the meaning of its features or labels?
- Does retraining amplify an earlier intervention?
- Are observed outcomes evidence of accuracy, or products of the model itself?

This is why retrospective predictive accuracy may be a poor guide to deployment performance.

---

# Comparative Map

| Tradition | What enters the system? | Main response mechanism | Typical failure |
|---|---|---|---|
| Lucas Critique | Policy regime | Expectations and optimization | Coefficients change |
| Goodhart’s Law | Metric target | Proxy optimization | Proxy detaches from goal |
| Campbell’s Law | High-stakes indicator | Gaming and institutional corruption | Activity and data are distorted |
| Self-fulfilling prophecy | Belief or forecast | Coordination and behavioral response | Prediction creates outcome |
| Reflexivity | Participants’ beliefs | Recursive belief–reality feedback | Boom, bust, or path dependence |
| Performativity | Theory and calculative device | Institutional construction | Model remakes the market |
| Performative prediction | Deployed predictor | Decision-induced distribution shift | Training distribution becomes obsolete |
| Strategic classification | Decision rule | Feature manipulation | Inputs lose their original meaning |
| Policy resistance | Intervention | Feedback and compensating response | Policy is weakened or reversed |
| Red Queen | Adaptation by others | Coevolution | No lasting relative advantage |
| Evolutionary response | Treatment or selection pressure | Differential survival and reproduction | Intervention selects resistance |
| Hawthorne effect | Observation | Participant reactivity | Study behavior differs from ordinary behavior |
| Mechanism design | Institutional rules | Equilibrium strategy | Design succeeds or fails under incentive constraints |

---

# Suggested Reading Sequence

1. **Lucas (1976)** for policy-regime dependence.
2. **Campbell (1976/1979)** and **Manheim and Garrabrant (2019)** for metric corruption and proxy failure.
3. **Merton (1948)** and **Buck (1963)** for belief-mediated prediction.
4. **Callon (1998)** and **MacKenzie and Millo (2003)** for models as constitutive infrastructure.
5. **Sterman (2006)** for general feedback and policy resistance.
6. **Perdomo et al. (2020)** for a modern mathematical framework.
7. **Van Valen (1973)** for adaptation without conscious anticipation.
8. **Hurwicz, Maskin, and Myerson** for the constructive institutional-design response.

Taken together, these literatures support a general methodological principle:

> **In a complex adaptive system, a model’s deployment is an intervention. Its validity must therefore be evaluated in the post-deployment system it helps create, not only against the pre-deployment data from which it was learned.**
