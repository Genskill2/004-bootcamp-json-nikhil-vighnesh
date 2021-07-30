# Introduction

(This is a translation of a problem found here
http://eloquentjavascript.net/04_data.html into Python)

Scott is a boy who automatically transforms into a squirrel on some
nights for unexplained reasons. He visited doctor Van Helsing who
suggested that he keep track of all the things he does on a regular
basis in a journal so that he can identify which activity is most
correlated with the transformation.

The journal is saved as a file called [journal.json](journal.json)
which has multiple entries like this one for each day of the month for
3 months. A total of 91 entries.

    {
      "events": [
        "carrot",
        "exercise",
        "weekend"
      ],
      "squirrel": false
    }

This indicates that, for this day, Scott ate carrots, he exercised,
and it was the weekend. He did not turn into a squirrel on that
day. There will be similar entries for each of the 91 days.

This file was then submitted to the doctor who analysed it to find out
which event is most correlated (positively or negatively) with the
transformation into the squirrel.

# Mathematical background

[Correlation](https://en.wikipedia.org/wiki/Correlation_and_dependence)
is a mathematically calculated value that represents how related two
values are. Consider two variables `X` and `Y`. For simplicity, let's
assume that the variables can take on only two values (True and
False). The correlation (denoted by `corr(X,Y)`), can vary between -1
to +1. If it's -1, it means that the two variables are perfectly
negatively correlated meaning that if `X` is True, `Y` will be
False. If it's +1, they're perfectly positively correlated. If `X`
is True, `Y` will also True. If the correlation is `0`, it means that
if `X` is True, there's equal probability that `Y` can be True or
False. 


## Formula

The correlation is usually denoted by ϕ. 


      ϕ = (n₁₁ * n₀₀ - n₁₀ * n₀₁) / sqrt(n₁₊ * n₀₊ * n₊₁ * n₊₀)


Here, The subscripts of n indicate the values of the two variables whose
correlations we're calculating. Let's call them x and y.


     n₁₁ is the number of times x and y were both True
     n₀₀ is the number of times x and y were both False
     n₁₀ is the number of times x was True but y was False
     n₀₁ is the number of times x was False but y was True
     
     n₁₊ is the number of times x was True regardless of the value of y
     n₀₊ is the number of times x was False regardless of the value of y
     n₊₁ is the number of times y was True regardless of the value of x
     n₊₀ is the number of times y was False regardless of the value of x


### Example

Consider the value for the two variables `X` and `Y`. 

      | X | Y |
      |---+---|
      | T | T |
      | T | F |
      | T | T |
      | F | T |
      | F | T |
      | T | F |
      | F | F |


     n₁₁  - number of times X and Y were both True         2
     n₀₀  - number of times X and Y were both False        1
     n₁₀  - number of times X was True but Y was False     2
     n₀₁  - number of times X was False but Y was True     2
     
     n₁₊  - number of times X was True regardless of the value of Y       4
     n₀₊  - number of times X was False regardless of the value of Y      3
     n₊₁  - number of times Y was True regardless of the value of X       4
     n₊₀  - number of times Y was False regardless of the value of X      3


Calculating the correlation like so

      ϕ = (n₁₁ * n₀₀ - n₁₀ * n₀₁) / sqrt(n₁₊ * n₀₊ * n₊₁ * n₊₀)
        = (2 * 1 - 2 * 2) / sqrt(4*3*4*3)
        = (2 - 4) / sqrt(144)
        = -2 / 12
        = -0.1667
  
This means that there's a slight negative correlation. If `X` is
True there's a slight chance that `Y` is False. If `X` were a social
event like "festival coming up", and `Y` were an event like "supply of
clothes reducing", then you can make a reasonable assumption that if
the festival is coming up, there's a slight chance of supply of
clothes reducing. This doesn't suggest that `X` causes `Y`
(correlation is not causation). It only suggests that they're
correlated. 


# Exercises

There are several event (e.g. `carrot`) which we need to find the
correlations with `squirrel` event. Then we can find out which event
is most correlated with the `squirrel` event and then let Scott know
what to do or not do. 

Implement the following functions in the provided `correlation.py` file.


1. Write a function called `load_journal` which will load the journal
   file using the `json` module and returns the parsed data. It will
   take the name of the file to parse as input and return a list of
   dictionaries (which is what the actual journal file contains).

1. Write a function called `compute_phi` which will take 2 inputs, the
   name of a file that you can pass to the `load_journal` function
   mentioned above and an event (e.g. `"carrot"`). It should return
   the correlation of the `"carrot"` event and the `squirrel` event.
   
1. Write a function called `compute_correlations` which will take the
   filename of the journal (`journal.json`) as input. It will first
   call `load_journal` to load the file. Then it will go through the
   contents of the file and call `compute_phi` for each event and
   finally return a dictionary whose keys are the various events in
   the journal and the values will be the correlations of the event
   and `squirrel`. 

1. Write a function called `diagnose` which will take the name of the
   journal file (`journal.json`) and use `compute_correlations` and
   return the event that's most highly positively and most highly
   negatively correlated with the `squirrel` event.

*Do not modify any files except `correlation.py`*. If you do, your
grading will fail.

# Diagnosis

What would you recommend to Scott to prevent transforming into a squirrel?
    
