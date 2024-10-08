# Documenting Data Analysis

In the presentation supported by this book I want to introduce you to the **power** of using computers to analyze and visualize data. Spreadsheets are great for budgeting but they are difficult to use when data gets "big." And **big data** is here to stay. **Biology** and **chemistry** are rapidly becoming data-intensive fields. The tools to command all this data reside in specialized tools like "***R***" and general-purpose languages like ***Python***.

Most science students have never really commanded a computer. Apps command you, not the other way around. Learning to **interpret and adapt** a computer program for your own purposes is an essential skill in science. 

The goal of our program is to explore **chemistry**, not computer science. I will not be teaching **programming**. We will use programs that have been written and adapt them as needed. Along the way the basics of commanding a computer with written instructions will be revealed to you. 

## In a Nutshell

The presentation will start with an argument that you can **plot with *python* tools** just as effectively as in Microsoft excel. Then we will digress to plead that you never commit one of Excels greatest sins, using the smoothed line to connect data points. One of the most important ideas in data analysis is correct **propagation of experimental error**. You will be introduced to the **uncertainties package** in *Python* that will handle your errors for you. Finally we will explore using *Python* plotting tools and the uncertainties package to analyze kinetic data using the Erying equation. At every step the **self-documenting** nature of *Python* code will be emphasized.

## Steal it All

We will use *Python* only as a **tool**. This book is intended to provide some basic **examples** of *Python* code for performing **calculations and visualizing data**. All code for the demonstrations in this presentation is already written for you. Steal it from me; steal it from the internet; give your code to friends. Always **give credit** where credit is due. Examine, play with, and **steal the code** in the interactive notebooks linked below. To learn, you must first imitate. Later, you will inovate. The journey from here to there is up to you.

## Notebooks for the Presentation

The python notebooks described below contain all the code and documentation for the plots and data sets used in the presentation. Steal it run with it. 

## Part 1: Quick Examples of *Python*

This notebook provides some simple examples of data analysis in *Python*. We will use the example of the Michaelis-Menten plot to highlight the dangers in linearization for data analysis.

>**Title**: [Part 1: Quick Examples *Python*](01_PlotBasics.ipynb) <br>
>**Tools**: *Python* math operators, *NumPy*, *SciPy*, *matplotlib*  <br>
>**Skills**: Basic math operations and math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Accessing physical constants in *SciPy*. Data analysis tools in *SciPy*. Simple data visualization using *matplotlib*.

## Part 2: Please Don't Use "Smooth Lines"

Some data is not meant to be fit to a mathematical model. How should these data sets be presented? Quite often a simple plot with points connected by lines will do. Just don't chose the "smooth line" option. Along the way we will explore some of the smooth line options available via *Python* and spline functions. And we will then make a promise to never use them.

>**Title**: [Part 2: Please Don't Use "Smooth Lines"](02-CubicSpline.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Pandas*  <br>
>**Skills**: Importing data from a csv file using the *Pandas* library. Basic math operations and math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Simple data visualization using *matplotlib*. Data interpolation using fits to spline function in the `SciPy.interpolate` sublibrary

## Part 3: Uncertainty and Confidence Intervals

The Erying plot is a classic way to explore how *Python* tools can assist in analysis. Experimental data is often known only to within a range that defines it prescission. This experimental error will be reflected in parameters calculated from the mathematical model used in the analysis. The error will be transmitted through any calculation using these values. If we use the uncertainty of the parameters to calculate the prescission of the predicted results of the model then we will have the confidence interval across the range of experimental data. This can be plotted as well to provide a visual indication of the experimental error within the model.

Error propagation can get complicated. But we will use a set of tools provided by the *Uncertainties* library to handle all of this automatically. We will also use a robust and extremely computationaly expensive method to obtain a more "real-world" estimate of the confidence interval. 

>**Title**: [Part 3: The Eyring Equation and Experimental Error](03-Eyring_Exercises_Intro.md) 

### Part 3A: A Simple Data Analysis

This notebook will plot a 5-point Erying plot and determine the $\Delta H^\ddagger$ and $\Delta S^\ddagger$ for the reaction. The standard deviations for the parameters will be examined and used to calculate the confidence interval for the rate constant at a given temperature. The ```scipy.stats.linregress()``` tool will be demonstrated along with the ```matplotlib.pyplot``` library for plotting. Along the way we will learn the correct way to use the *uncertainties* module in our calculations.

>**Title**: [Part 3A: A Simple Data Analysis](03A-Eyring_Exercises_1_simple.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Uncertainties.ufloat*, *Uncertainties.unumpy*  <br>
>**Skills**: Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Simple data visualization using *matplotlib*. Data interpolation using linear regression with `SciPy.stats.linregress()`. Creating uncertain values with `Uncertainties.ufloat()`. The consequences of strongly correlated errors in fit parameters (covariance) and ways to deal with this effect.


### Part 3B: Curve Fitting and Covariance

The ```scipy.optimize``` sublibrary provides a better set of tools for fitting data to models and interfacing with the *uncertainties* package.  We will be using ```scipy.optimize.curvefit()``` in this exercise and using the covariance matrix returned by that function to create ufloat values that reflect the coupling between errors in fit parameters.

>**Title**: [Part 3B: Curve Fitting and Covariance](03B-Eyring_Exercises_2_curvefit.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Uncertainties.correlated_values*, , *Uncertainties.unumpy*  <br>
>**Skills**: Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Data visualization using *matplotlib*. Using `SciPy.optimize.curve_fit()` to fit data to arbitrary mathematical models. Creating uncertain values with `Uncertainties.correlated_values()`. Propagating error and determining confidence intervals

### Part 3C: Using LMFit

The *lmfit* library provides another set of tools for handling data and interfacing with the *uncertainties* package. It has many built-in tools for analyzing and visualizing the curve fit. It returns ufloat values for fit parameters directly that already contain information on any covariance.

>**Title**: [Part 3C: Using LMFit](03C-Eyring_Exercises_3_LMfit.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Uncertainties*, *LMFit*  <br>
>**Skills**: Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Data visualization using *matplotlib*. Using *LMFit* to fit data to arbitrary mathematical models and plot data. Propagating error and determining confidence intervals


### Part 3D: Reading Data

This notebook will read in data from a text file. Creating data files for your experimental data will allow you to use a notebook to analyze a new set of data by changing the file name and nothing else. This will enable your data analysis notebook to be more versatile. This notebook is almost identical to Part 3B except that the data is read from a file rather than entered directly. Here we use the full dfata set from the publication and can see the result of increasing data on prescission.

>**Title**: [Part 3D: Reading Data](03D-Eyring_Exercises_4_pandas.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Pandas*, *Uncertainties*  <br>
>**Skills**: Importing data from a csv file using the *Pandas* library. Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Data visualization using *matplotlib*. Using `SciPy.optimize.curve_fit()` to fit data to arbitrary mathematical models. Creating uncertain values with `Uncertainties.correlated_values()`. Propagating error and determining confidence intervals


### Part 3E: Bootstrapping Confidence Intervals

The confidence intervals produced by ```lmfit``` or by using the covariance matrix from ```curve_fit``` follow typical rules for error propagation and present a range that is symmetrical above and below any value. This is the common $a \pm b$ way of presenting error. However, the confidence range may not be symmetrical (this is especially true sparse data sets.) One way to express this is to use more sophisticated error propagation tools in $python$ such as ```soerp``` or ```mcerp```. We won't be exploring those here. In this notebook we will use a robust but inefficient method for determining the confidence interval for a data set and generate a confidence band on a plot that reflects the "real world" error in your data. This method is called "bootstrapping."  

>**Title**: [Part 3E: Bootstrapping Confidence Intervals](03E-Eyring_Exercises_5_Bootstrap.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Pandas*, *Uncertainties*  <br>
>**Skills**: Importing data from a csv file using the *Pandas* library. Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Data visualization using *matplotlib*. 

### Part 3F: Final Plots

Three blocks of code that determine the thermodynamic parameters and confidence intervals (CI) for the Erying plot three different ways: using `scipy.optimize.curve_fit` and using the standard deviation to establish the CI; using `lmfit` and the confidence interval is determined by the CI algorithm of `lmfit` (explained [here](https://lmfit.github.io/lmfit-py/confidence.html)); and using the bootstrap method.

>**Title**: [Part 3F: Final Plots](03F_Final_Plots.ipynb) <br>
>**Tools**: *NumPy*, *SciPy*, *matplotlib*, *Pandas*, *Uncertainties*  <br>
>**Skills**: Importing data from a csv file using the *Pandas* library. Math functions using the tools of *NumPy*. Math with *NumPy* arrays, formatting numbers in f-strings. Data visualization using *matplotlib* and *lmfit*. Using `SciPy.optimize.curve_fit` to fit data to arbitrary mathematical models. Creating uncertain values with `Uncertainties.correlated_values`. Propagating error and determining confidence intervals




## Part 4: Pick a Style

Journals often have a specific style for plots. In a thesis, you should use the same style for all plots. In this notebook we will explore styling plots using many option available in the ```matplotlib.pyplot``` library. Once you get a style you like in a notebook, you never need to change. I haven't changed my style since 1985, that why I look so good.

>**Title**: [Part 4: Styling Plots"](04-Styling.ipynb) <br>
>**Tools**: *matplotlib* <br>
>**Skills**: Applying style files to plots. using standard styles and styles provided by journals.

## Notes and References

This is a **Juptyter-book** that was built from a set of **interactive *Python* Jupyter notebooks**. The original notebook for any given chapter can be obtained using the **download link** at the top of the page.


The Ouroboros with benzene image was accessed at https://commons.wikimedia.org/wiki/File:Ouroboros-benzene.svg on June 24, 2022. It is licensed under the Creative Commons license CC BY-SA 