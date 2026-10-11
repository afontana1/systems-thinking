# Signal Processing Learning Path
## From mathematical foundations to DSP, FFTs, filtering, and spectral estimation

**Target background:** advanced undergraduate / first-year graduate level  
**Assumed background:** strong mathematics, econometrics, statistics, and machine learning  
**Primary goal:** build a rigorous understanding of signals and systems, time and frequency domains, Fourier analysis, the DFT/FFT, digital filters, and statistical spectral analysis.

---

## The four core books

This learning path uses four books, but **not** as four cover-to-cover reads.

1. **Alan V. Oppenheim, Alan S. Willsky, with S. Hamid Nawab — _Signals and Systems_**
   - Role: establish the signals-and-systems language.
   - Use selectively.
   - Main topics: LTI systems, convolution, complex exponentials, Fourier representations, sampling, Laplace transforms, z-transforms.

2. **Alan V. Oppenheim and Ronald W. Schafer — _Discrete-Time Signal Processing_, 3rd ed.**
   - Role: the main DSP textbook.
   - This is the book to study most carefully.
   - Main topics: discrete-time systems, DTFT, sampling, DFT, FFT, FIR/IIR filters, frequency response.

3. **Richard G. Lyons — _Understanding Digital Signal Processing_, 3rd ed.**
   - Role: intuition, implementation, and engineering interpretation.
   - Use as a companion to Oppenheim & Schafer rather than as the primary theoretical text.

4. **Petre Stoica and Randolph L. Moses — _Spectral Analysis of Signals_**
   - Role: statistical and parametric spectral analysis.
   - This is where DSP connects especially strongly to econometrics and time-series statistics.
   - Main topics: power spectra, periodograms, AR/MA/ARMA spectral models, line spectra, model-based spectral estimation.

The overall path is:

> **Phase 0 prerequisites → Signals & Systems → Discrete-Time DSP → Practical FFT/filter intuition → Spectral estimation → Time-frequency analysis / applications**

---

# Phase 0 — Prerequisites and mathematical refresh

You probably do **not** need a semester of prerequisite study. Given a graduate econometrics / ML background, the goal of Phase 0 is to identify and patch a few DSP-specific gaps.

A good target is **1–3 weeks**, depending on how familiar complex numbers, difference equations, and Fourier analysis already feel.

The most important prerequisite is not advanced mathematics. It is becoming fluent in the particular mathematical language used by signal processing.

---

## 0.1 Complex numbers and complex exponentials

This is the first thing to review if it is not already automatic.

You should be comfortable with

$$
z = a + jb
$$

and polar form

$$
z = re^{j\theta}.
$$

Euler's identity should feel completely natural:

$$
e^{j\theta} = \cos\theta + j\sin\theta.
$$

From this,

$$
\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}
$$

and

$$
\sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}.
$$

You should also be comfortable with complex conjugation,

$$
z^* = a-jb,
$$

magnitude,

$$
|z| = \sqrt{zz^*},
$$

and phase,

$$
\arg z.
$$

### Why this matters

In signal processing, complex exponentials are not merely a calculation trick. They are the natural coordinates of linear time-invariant systems.

A sinusoid can be represented using exponentials, and an LTI system acts particularly simply on

$$
e^{j\omega t}
$$

or

$$
e^{j\omega n}.
$$

That observation is one of the foundations of Fourier analysis.

### Sources to consult

**Primary free review:**

- MIT OpenCourseWare — **18.03SC Differential Equations**, lecture material on **Complex Arithmetic and Euler's Formula**.
  - https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/

**For a more geometric treatment:**

- Tristan Needham — **_Visual Complex Analysis_**
  - Oxford University Press.
  - Focus on the opening material on complex arithmetic and geometric interpretation.
  - You do **not** need the whole book for DSP.

**If you want a conventional course-level reference:**

- MIT OpenCourseWare — **18.04 Complex Variables with Applications**
  - https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
  - The lecture notes on complex algebra and the complex plane are more than enough for this prerequisite.

### Exit criterion

You should be able to manipulate

$$
Ae^{j(\omega n+\phi)}
$$

without translating it into sine and cosine every time.

---

## 0.2 Linear algebra

You likely already know almost everything needed here.

Review only if necessary:

- vector spaces
- orthogonality
- projections
- eigenvalues and eigenvectors
- diagonalization
- Hermitian matrices
- positive-semidefinite matrices
- quadratic forms
- complex inner products

For complex vectors, remember that the natural inner product uses a conjugate transpose:

$$
\langle x,y\rangle = x^H y.
$$

A matrix is Hermitian when

$$
A = A^H.
$$

### Why this matters

There is a powerful linear-algebraic interpretation of Fourier analysis:

> The Fourier transform is a change of representation into a basis in which many important linear operators become simple.

For finite signals, the DFT can be written as a matrix transformation:

$$
X = Fx.
$$

The inverse transform is then

$$
x = F^{-1}X.
$$

Up to normalization, the DFT matrix is unitary.

This viewpoint will connect naturally to PCA, eigendecompositions, kernels, and linear operators from ML.

### Sources to consult

**Primary source:**

- Gilbert Strang — MIT OpenCourseWare **18.06 Linear Algebra**
  - https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

Focus on:

- vector spaces
- orthogonality
- eigenvalues/eigenvectors
- symmetric matrices
- positive-definite matrices

If those are already routine, skip this review.

### Exit criterion

You should understand why diagonalizing a linear operator makes repeated application of that operator easier to understand.

That intuition becomes important when Fourier modes appear as eigenfunctions of LTI systems.

---

## 0.3 Infinite sums, geometric series, and basic calculus

You do not need advanced real analysis.

You should be comfortable with geometric sums such as

$$
\sum_{n=0}^{\infty} ar^n
=
\frac{a}{1-r},
\qquad |r|<1.
$$

For finite sums,

$$
\sum_{n=0}^{N-1} r^n
=
\frac{1-r^N}{1-r}.
$$

You should also be comfortable differentiating and integrating exponentials and sinusoids.

For example,

$$
\frac{d}{dt} e^{j\omega t}
=
j\omega e^{j\omega t}.
$$

### Why this matters

Geometric sums occur constantly in:

- Fourier transforms
- z-transforms
- filter derivations
- frequency responses
- AR processes
- poles and zeros

### Sources to consult

If needed, use:

- MIT OpenCourseWare — **18.01SC Single Variable Calculus**
  - https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/

For most mathematically experienced readers, a brief review of geometric series is sufficient.

---

## 0.4 Difference equations and linear recurrences

This is particularly important.

You should be comfortable with recurrences such as

$$
y[n] = ay[n-1] + bx[n].
$$

For a homogeneous recurrence,

$$
y[n] = ay[n-1],
$$

the solution has the form

$$
y[n] = Ca^n.
$$

Higher-order recurrences lead to characteristic polynomials.

For example,

$$
y[n] - a_1y[n-1] - a_2y[n-2] = x[n].
$$

### Why this matters

A digital filter is often literally a difference equation.

For example,

$$
y[n]=0.9y[n-1]+0.1x[n]
$$

is simultaneously:

- a recurrence relation,
- a causal linear system,
- an IIR digital filter,
- a simple dynamical system.

From an econometrics viewpoint, this should feel very close to autoregressive modeling.

### Sources to consult

**Best bridge resource:**

- MIT OpenCourseWare — **6.003 Signals and Systems**
  - https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/

Use the early material on:

- difference equations
- system representations
- discrete-time signals
- system functions

You can also review the difference-equation material in Oppenheim & Willsky directly.

### Exit criterion

Given a first- or second-order linear recurrence, you should be able to reason about its solution and stability.

---

## 0.5 Probability, random variables, and stochastic processes

Given your econometrics background, this will probably be the easiest prerequisite.

You should already know:

- expectation
- variance
- covariance
- conditional expectation
- Gaussian random variables
- covariance matrices
- stationary processes
- white noise
- AR, MA, and ARMA models

For a process

$$
x_t,
$$

its autocovariance is

$$
\gamma(k)
=
\operatorname{Cov}(x_t,x_{t-k}).
$$

For a zero-mean wide-sense stationary process, the autocorrelation can be written as

$$
R_x[k]
=
E[x[n]x^*[n-k]].
$$

### Sources to consult

You probably do not need a full probability review.

If you want a signal-processing-oriented stochastic-process reference:

- MIT OpenCourseWare — **6.432 Stochastic Processes, Detection, and Estimation**
  - https://ocw.mit.edu/courses/6-432-stochastic-processes-detection-and-estimation-spring-2004/

For a more general probability/process review:

- MIT OpenCourseWare — **6.262 Discrete Stochastic Processes**
  - https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/

Do **not** work through either entire course before beginning DSP. Use them as references when a stochastic-process concept becomes unfamiliar.

### Exit criterion

You should be comfortable viewing

$$
x[n]
$$

as a realization of an underlying stochastic process rather than merely as a deterministic array of numbers.

---

## 0.6 The prerequisite that deserves the most attention: convolution

Convolution will appear almost immediately.

For discrete-time signals,

$$
y[n]
=
(x*h)[n]
=
\sum_{k=-\infty}^{\infty}
x[k]h[n-k].
$$

For continuous-time signals,

$$
y(t)
=
(x*h)(t)
=
\int_{-\infty}^{\infty}
x(\tau)h(t-\tau)\,d\tau.
$$

### Why it matters

For an LTI system,

$$
y = x*h.
$$

The impulse response

$$
h
$$

completely characterizes the system.

Then Fourier analysis gives the extraordinary simplification

$$
Y(\omega)=X(\omega)H(\omega).
$$

So:

> convolution in the time domain becomes multiplication in the frequency domain.

This is one of the central ideas of the entire subject.

### Source to consult

Use:

- MIT OpenCourseWare — **6.003 Signals and Systems**
- Oppenheim & Willsky — sections on LTI systems and convolution

Do several convolution exercises by hand.

### Phase 0 coding exercise

Implement discrete convolution yourself:

```python
def convolve_manual(x, h):
    ...
```

Do not call `numpy.convolve` until your own implementation works.

Then compare your output to NumPy.

---

# Phase 1 — Signals and systems

## Primary resource

**Oppenheim & Willsky — _Signals and Systems_**

Companion:

- MIT OpenCourseWare **6.003 Signals and Systems**
- https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/

### Time allocation

Approximately **2–4 weeks**.

Do not aim to read the entire book.

---

## 1.1 Signals

Become comfortable distinguishing:

- continuous time

$$
x(t)
$$

- discrete time

$$
x[n]
$$

- deterministic signals
- stochastic signals
- periodic signals
- finite-energy signals
- finite-power signals

Learn the unit impulse:

$$
\delta[n].
$$

Any discrete-time sequence can be represented as

$$
x[n]
=
\sum_{k=-\infty}^{\infty}
x[k]\delta[n-k].
$$

This identity is what makes the impulse response so important.

---

## 1.2 Linear time-invariant systems

Understand:

- linearity
- time invariance
- causality
- memory
- stability

An LTI system is completely described by its impulse response:

$$
h[n].
$$

Its output is

$$
y[n]
=
\sum_k x[k]h[n-k].
$$

---

## 1.3 Complex exponentials as eigenfunctions

This deserves special attention.

Suppose the input is

$$
x[n]=e^{j\omega n}.
$$

For an LTI system,

$$
y[n]
=
H(e^{j\omega})e^{j\omega n}.
$$

The output has the **same frequency**.

Only its amplitude and phase change.

Therefore complex exponentials are eigenfunctions of LTI systems.

This fact is the conceptual foundation of frequency response.

---

## 1.4 Fourier series and Fourier transforms

Study:

- Fourier series
- continuous-time Fourier transform
- discrete-time Fourier transform
- frequency response

The Fourier transform decomposes a signal into complex exponentials.

Conceptually,

$$
\text{signal}
=
\text{weighted combination of frequency components}.
$$

---

## 1.5 Sampling

Understand how a continuous signal becomes a sequence:

$$
x[n] = x(nT_s).
$$

The sampling frequency is

$$
f_s=\frac{1}{T_s}.
$$

Do not merely memorize Nyquist. Learn why sampling creates replicated spectra.

### Phase 1 milestone

You should be able to explain, mathematically:

> Why does a moving-average smoother remove rapidly varying components of a signal?

---

# Phase 2 — Core discrete-time signal processing

## Primary book

**Oppenheim & Schafer — _Discrete-Time Signal Processing_, 3rd ed.**

Publisher overview:

- Pearson describes the book as a treatment of discrete-time linear systems, filtering, sampling, and discrete-time Fourier analysis.

### Time allocation

Approximately **6–10 weeks**.

This is the center of the learning path.

---

## 2.1 Discrete-time LTI systems

Deepen your understanding of:

- convolution
- difference equations
- causal systems
- stability
- impulse response

Connect recurrences directly to filters.

For example,

$$
y[n]
=
0.8y[n-1]
+
0.2x[n]
$$

is a recursive low-pass filter.

---

## 2.2 The DTFT

Study the discrete-time Fourier transform:

$$
X(e^{j\omega})
=
\sum_{n=-\infty}^{\infty}
x[n]e^{-j\omega n}.
$$

The inverse relation is

$$
x[n]
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
X(e^{j\omega})e^{j\omega n}\,d\omega.
$$

Important ideas:

- periodicity in frequency
- magnitude
- phase
- convolution theorem
- modulation
- time shifts
- frequency shifts

The central relationship is

$$
y[n]=x[n]*h[n]
$$

which becomes

$$
Y(e^{j\omega})
=
X(e^{j\omega})H(e^{j\omega}).
$$

---

## 2.3 Sampling and aliasing

Study this carefully.

Suppose a sinusoid is sampled:

$$
x(t)=\cos(2\pi f_0t).
$$

Sampling at

$$
f_s
$$

produces

$$
x[n]
=
\cos\left(2\pi\frac{f_0}{f_s}n\right).
$$

Discrete-time frequencies differing by integer multiples of

$$
2\pi
$$

are indistinguishable.

This is the mathematical origin of aliasing.

The familiar condition

$$
f_s > 2f_{\max}
$$

is a consequence of keeping repeated spectral copies from overlapping.

### Coding exercise

Generate sinusoids above and below the Nyquist frequency and sample them.

Demonstrate that two different continuous frequencies can generate the same discrete sequence.

---

## 2.4 The DFT

For a finite sequence of length

$$
N,
$$

the DFT is

$$
X[k]
=
\sum_{n=0}^{N-1}
x[n]
e^{-j2\pi kn/N}.
$$

The inverse DFT is

$$
x[n]
=
\frac{1}{N}
\sum_{k=0}^{N-1}
X[k]
e^{j2\pi kn/N}.
$$

You should understand the distinction between:

- Fourier series
- Fourier transform
- DTFT
- DFT
- FFT

The key distinction:

> The **DFT** is a mathematical transformation.  
> The **FFT** is a family of algorithms for computing the DFT efficiently.

---

## 2.5 Matrix view of the DFT

Write

$$
X = Fx.
$$

where

$$
F_{kn}
=
e^{-j2\pi kn/N}.
$$

This connects the DFT to linear algebra.

With appropriate normalization,

$$
F^HF=I.
$$

Think of the DFT as expressing a vector in a Fourier basis.

This interpretation should fit naturally with your ML background.

---

## 2.6 FFT

A direct DFT costs approximately

$$
O(N^2).
$$

The FFT exploits algebraic structure to reduce this to roughly

$$
O(N\log N).
$$

You do not need to memorize every FFT architecture.

Understand at least one radix-2 Cooley–Tukey decomposition.

The important idea is that a length-

$$
N
$$

DFT can be decomposed into smaller DFTs of the even- and odd-indexed samples.

### Coding exercise

Implement:

1. a naive DFT,
2. a radix-2 FFT,
3. timing comparisons against `numpy.fft.fft`.

Plot computation time against

$$
N.
$$

---

# Phase 3 — Filtering and engineering intuition

## Primary theoretical source

**Oppenheim & Schafer**

## Companion

**Richard G. Lyons — _Understanding Digital Signal Processing_, 3rd ed.**

Use Lyons whenever the formal treatment starts to feel detached from the behavior of actual signals.

---

## 3.1 FIR filters

A finite impulse response filter has

$$
y[n]
=
\sum_{k=0}^{M}
b_kx[n-k].
$$

Its transfer function is

$$
H(z)
=
\sum_{k=0}^{M}
b_kz^{-k}.
$$

Study:

- moving averages
- smoothing
- linear phase
- delay
- window-based FIR design

---

## 3.2 IIR filters

An IIR filter may have the form

$$
y[n]
=
\sum_{k=0}^{M}b_kx[n-k]
-
\sum_{k=1}^{P}a_ky[n-k].
$$

Its transfer function is

$$
H(z)
=
\frac{\sum_{k=0}^{M}b_kz^{-k}}
{1+\sum_{k=1}^{P}a_kz^{-k}}.
$$

Study:

- poles
- zeros
- stability
- resonance
- recursive filters

This should connect strongly to ARMA models.

---

## 3.3 Frequency response

Evaluate the transfer function on the unit circle:

$$
z=e^{j\omega}.
$$

Then

$$
H(e^{j\omega})
$$

describes how the system acts on each frequency.

Magnitude response:

$$
|H(e^{j\omega})|.
$$

Phase response:

$$
\arg H(e^{j\omega}).
$$

Study:

- low-pass
- high-pass
- band-pass
- notch filters

---

## 3.4 How to use Lyons

Do not read Lyons cover to cover before continuing.

Use it as a companion for:

- DFT intuition
- FFT implementation
- spectral leakage
- windowing
- FIR filters
- IIR filters
- quadrature / I-Q signals
- Hilbert transforms

A productive pattern is:

1. read the formal treatment in Oppenheim & Schafer,
2. work one derivation,
3. read Lyons on the same topic,
4. implement it,
5. inspect plots.

---

# Phase 4 — Finite data, FFT interpretation, and spectral leakage

Spend approximately **2 weeks** here before moving deeply into statistical spectral analysis.

This phase prevents a common mistake:

> treating an FFT as though it reveals a perfect, objective list of frequencies contained in the underlying process.

In reality you observe a finite record.

Suppose

$$
x[n]
=
\sin(2\pi f_1n/f_s)
+
0.5\sin(2\pi f_2n/f_s)
+
\epsilon[n].
$$

Compute the FFT and vary:

- sample rate
- observation duration
- number of samples
- noise variance
- signal frequencies
- FFT length
- window functions

---

## 4.1 Frequency resolution

With

$$
N
$$

samples at sampling frequency

$$
f_s,
$$

FFT-bin spacing is

$$
\Delta f
=
\frac{f_s}{N}.
$$

This is not the same thing as saying every frequency can be perfectly resolved at that spacing, but it is a crucial first relationship.

---

## 4.2 Spectral leakage

A finite observation is equivalent to multiplying an infinite signal by a window.

In time:

$$
x_w[n]
=
x[n]w[n].
$$

Multiplication in time corresponds to convolution in frequency.

Therefore a window changes the observed spectrum.

Compare:

- rectangular window
- Hann window
- Hamming window

Study the tradeoff between:

- main-lobe width
- side-lobe suppression
- amplitude accuracy
- frequency resolution

---

## 4.3 Zero padding

Zero padding may create a denser-looking FFT:

$$
N_{\text{FFT}} > N.
$$

But zero padding does **not** create new information.

It interpolates the sampled frequency-domain representation.

This distinction is worth understanding deeply.

---

## Phase 4 project

Construct a two-tone signal where one frequency lies exactly on an FFT bin and another lies between bins.

Compare spectra under several windows.

Then explain:

1. why leakage occurs,
2. why the peak changes shape,
3. why zero padding makes the graph smoother without increasing the information content.

---

# Phase 5 — Statistical spectral analysis

## Primary book

**Petre Stoica and Randolph L. Moses — _Spectral Analysis of Signals_**

A copy is made available by Petre Stoica through his Uppsala University site:

- https://user.it.uu.se/~ps/SAS-new.pdf

The book is especially appropriate here because it treats both classical and modern spectral estimation, including nonparametric methods, rational spectra, and line spectra.

### Time allocation

Approximately **4–8 weeks** for a first pass.

---

## 5.1 Autocorrelation and power spectral density

For a wide-sense stationary process,

$$
R_x[k]
=
E[x[n]x^*[n-k]].
$$

The power spectral density is the Fourier transform of the autocorrelation sequence:

$$
S_x(e^{j\omega})
=
\sum_{k=-\infty}^{\infty}
R_x[k]e^{-j\omega k}.
$$

Conversely,

$$
R_x[k]
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
S_x(e^{j\omega})e^{j\omega k}\,d\omega.
$$

This is the Wiener–Khinchin relationship.

For someone trained in econometrics, this is a major conceptual bridge:

> dependence across lags and distribution of power across frequencies are two representations of the same second-order structure.

---

## 5.2 The periodogram

For a finite record,

$$
x[0],\ldots,x[N-1],
$$

a basic spectral estimate is proportional to

$$
\left|X[k]\right|^2.
$$

The periodogram might be written schematically as

$$
\hat S_x(\omega)
=
\frac{1}{N}
\left|
\sum_{n=0}^{N-1}
x[n]e^{-j\omega n}
\right|^2.
$$

Study:

- expectation
- bias
- variance
- inconsistency of the raw periodogram
- smoothing
- averaging

This is where spectral analysis becomes explicitly an estimation problem.

---

## 5.3 Welch-type spectral estimation

Divide a time series into overlapping segments, window each segment, compute periodograms, and average them.

The important tradeoff is:

> reduced variance in exchange for reduced frequency resolution.

Implement Welch's method and compare it with a raw periodogram.

---

# Phase 6 — AR, MA, and ARMA models as filters

This is likely to be the point where your econometrics background creates the largest payoff.

Consider an AR(1):

$$
x_t
=
\phi x_{t-1}
+
\epsilon_t.
$$

Using the lag operator,

$$
(1-\phi L)x_t
=
\epsilon_t.
$$

Therefore,

$$
x_t
=
\frac{1}{1-\phi L}
\epsilon_t.
$$

DSP interprets this as white noise passed through a linear filter.

The corresponding transfer function is

$$
H(z)
=
\frac{1}{1-\phi z^{-1}}.
$$

On the unit circle,

$$
H(e^{j\omega})
=
\frac{1}{1-\phi e^{-j\omega}}.
$$

If the innovation variance is

$$
\sigma_\epsilon^2,
$$

then the spectral density is proportional to

$$
S_x(\omega)
=
\sigma_\epsilon^2
\left|
H(e^{j\omega})
\right|^2.
$$

Therefore,

$$
S_x(\omega)
=
\frac{\sigma_\epsilon^2}
{|1-\phi e^{-j\omega}|^2}.
$$

Now several vocabularies become one:

| Econometrics | Signal processing |
|---|---|
| lag polynomial | filter polynomial |
| AR model | all-pole filter |
| MA model | FIR / moving-average filter |
| ARMA model | rational transfer function |
| stationarity | pole/stability condition |
| autocovariance | correlation structure |
| spectral density | distribution of variance/power by frequency |

This is the conceptual bridge you should exploit aggressively.

---

# Phase 7 — Parametric spectral estimation

Continue with Stoica & Moses.

Study:

- AR spectral estimation
- MA spectral estimation
- ARMA spectral estimation
- Yule–Walker methods
- covariance methods
- model-order selection
- line-spectrum estimation

At this point the central question is no longer:

> "How do I compute an FFT?"

It becomes:

> "Given a finite noisy realization, what can I infer about the spectral structure of the underlying process?"

That is fundamentally a statistical estimation problem.

Your existing background in:

- bias/variance
- likelihood
- identification
- asymptotics
- model selection
- regularization

should transfer directly.

---

# Phase 8 — Time-frequency analysis

Ordinary Fourier analysis answers something like:

> Which frequencies are represented in this observation?

But many signals are nonstationary.

Examples include:

- ECG
- EEG
- speech
- music
- vibration
- radar
- seismic signals

A heart's behavior changes over time, so one often wants both temporal and spectral localization.

---

## 8.1 Short-time Fourier transform

The short-time Fourier transform applies a localized window:

$$
X(\tau,\omega)
=
\sum_n
x[n]w[n-\tau]e^{-j\omega n}.
$$

Instead of one spectrum for the whole record, you obtain spectra at different times.

The magnitude-squared STFT gives a spectrogram-like representation:

$$
|X(\tau,\omega)|^2.
$$

Study the time-frequency resolution tradeoff:

- narrow window → better temporal localization
- wide window → better frequency resolution

---

## 8.2 Wavelets

After STFTs, learn the basic motivation for wavelets.

Unlike a fixed-width Fourier window, wavelets naturally operate at multiple scales.

This makes them useful when high-frequency events are short-lived while low-frequency structure evolves more slowly.

Do not start here. Wavelets make much more sense after the Fourier/FFT/filtering foundation is strong.

---

# Phase 9 — Biomedical-signal capstone

Since the original motivation was a hospital monitor, use ECG as a capstone project.

A possible pipeline:

1. load a public ECG recording,
2. inspect the raw time-domain signal,
3. determine the sampling rate,
4. plot its FFT,
5. estimate its power spectral density,
6. identify mains interference if present,
7. design a notch or band-pass filter,
8. examine the filter's frequency response,
9. apply it to the ECG,
10. detect QRS complexes,
11. estimate R–R intervals,
12. construct an instantaneous or windowed heart-rate series,
13. examine heart-rate variability in time and frequency domains.

A typical signal path looks conceptually like:

$$
\text{electrode voltage}
\rightarrow
\text{sampling}
\rightarrow
\text{digital filtering}
\rightarrow
\text{feature detection}
\rightarrow
\text{physiological estimates}.
$$

This ties together essentially the entire learning path.

---

# Suggested 20-week schedule

| Weeks | Main topic | Primary resource |
|---|---|---|
| 1–2 | Phase 0 review: complex numbers, convolution, recurrences | MIT 18.03 / 18.04 / 6.003 |
| 3–4 | Signals, LTI systems, convolution | Oppenheim & Willsky + MIT 6.003 |
| 5 | Complex exponentials and Fourier representations | Oppenheim & Willsky |
| 6 | Sampling and aliasing | Oppenheim & Willsky / Oppenheim & Schafer |
| 7–8 | DTFT and frequency response | Oppenheim & Schafer |
| 9–10 | DFT | Oppenheim & Schafer + Lyons |
| 11 | FFT | Oppenheim & Schafer + Lyons |
| 12–13 | FIR/IIR filters, poles and zeros | Oppenheim & Schafer + Lyons |
| 14 | Windowing, leakage, finite records | Lyons + experiments |
| 15 | PSD and autocorrelation | Stoica & Moses |
| 16 | Periodogram and Welch methods | Stoica & Moses |
| 17–18 | AR/MA/ARMA spectral models | Stoica & Moses |
| 19 | Parametric spectral estimation | Stoica & Moses |
| 20 | STFT + ECG capstone | implementation/project |

Treat this as a guide rather than a rigid schedule.

---

# Recommended coding environment

Python is sufficient.

Core packages:

```text
numpy
scipy
matplotlib
pandas
```

Particularly useful modules include:

```python
numpy.fft
scipy.signal
```

But for learning, deliberately implement several objects from scratch first:

- convolution
- naive DFT
- radix-2 FFT
- moving-average FIR filter
- simple recursive IIR filter
- periodogram
- autocorrelation estimator

Then compare your implementation with NumPy/SciPy.

---

# The five ideas to master

If you finish this path with these ideas deeply internalized, you will have the core DSP mental model.

## 1. LTI systems are convolution operators

$$
y[n]
=
x[n]*h[n].
$$

---

## 2. Complex exponentials are eigenfunctions of LTI systems

$$
e^{j\omega n}
\rightarrow
H(e^{j\omega})e^{j\omega n}.
$$

---

## 3. Fourier transformation converts convolution into multiplication

$$
x*h
\quad\longleftrightarrow\quad
XH.
$$

This is why frequency-domain analysis is so powerful.

---

## 4. Sampling changes the spectral representation

Sampling creates repeated spectral structure and can produce aliasing.

The Nyquist condition is not merely a rule of thumb; it emerges from this frequency-domain geometry.

---

## 5. An FFT of finite data is not "the true spectrum"

You observe a finite, noisy sample.

Windowing, record length, sampling frequency, noise, model assumptions, and estimator choice all affect what you see.

That is why the progression

$$
\text{Fourier transform}
\rightarrow
\text{DFT/FFT}
\rightarrow
\text{periodogram}
\rightarrow
\text{spectral estimation}
$$

is so important.

---

# Recommended order of the four books

## Book 1 — Oppenheim & Willsky

Use selectively.

Goal:

> acquire the signals-and-systems conceptual language.

Move on once you understand:

- LTI systems
- convolution
- complex exponentials
- Fourier representations
- sampling
- basic z-transform intuition

---

## Book 2 — Oppenheim & Schafer

This is the book to study seriously.

Goal:

> understand discrete-time DSP mathematically.

Spend most of your textbook time here.

---

## Book 3 — Lyons

Read in parallel with Book 2.

Goal:

> turn the mathematics into engineering intuition.

Use it when you want to know what a DSP phenomenon actually looks like in sampled data.

---

## Book 4 — Stoica & Moses

Read after the DFT/FFT/filtering foundation is stable.

Goal:

> turn spectral analysis into a statistical inference problem.

This book should be especially natural after graduate econometrics.

---

# Reference links

## Core books

- Alan V. Oppenheim and Ronald W. Schafer, **_Discrete-Time Signal Processing_, 3rd ed.**  
  Pearson:  
  https://www.pearson.com/subject-catalog/p/discrete-time-signal-processing/P200000003226/9780137549771

- Richard G. Lyons, **_Understanding Digital Signal Processing_, 3rd ed.**  
  Pearson:  
  https://www.pearson.com/en-us/subject-catalog/p/understanding-digital-signal-processing/P200000000443

- Petre Stoica and Randolph L. Moses, **_Spectral Analysis of Signals_**  
  Author-hosted copy:  
  https://user.it.uu.se/~ps/SAS-new.pdf

## Free prerequisite / companion courses

- MIT OCW **6.003 Signals and Systems**  
  https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/

- MIT OCW **18.06 Linear Algebra** — Gilbert Strang  
  https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

- MIT OCW **18.04 Complex Variables with Applications**  
  https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/

- MIT OCW **18.03SC Differential Equations**  
  https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/

- MIT OCW **6.262 Discrete Stochastic Processes**  
  https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/

- MIT OCW **6.432 Stochastic Processes, Detection, and Estimation**  
  https://ocw.mit.edu/courses/6-432-stochastic-processes-detection-and-estimation-spring-2004/

---

# Final recommendation

Given a strong econometrics/ML background, do **not** spend months rebuilding prerequisites.

Use Phase 0 diagnostically.

The highest-value path is:

$$
\boxed{
\text{6.003 / Oppenheim-Willsky}
\rightarrow
\text{Oppenheim-Schafer}
\rightarrow
\text{Lyons alongside}
\rightarrow
\text{Stoica-Moses}
}
$$

The deepest connection to your existing knowledge will appear when you recognize that an ARMA process can be viewed as a linear filter driven by white noise, and that its autocovariance and spectral density are dual descriptions of the same second-order stochastic structure.

Once that clicks, econometric time-series analysis and signal processing stop looking like separate subjects.
