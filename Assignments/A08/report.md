# Implementation Process

The implementation process mostly consists of manipulating data (using loops often) and then just returning it with FastAPI. FastAPI does make creating the endpoints and documentation very easy, just needing a decoration and a return statement.

# Challenges Faced

To save programming time, I used other functions inside new ones, such as using countries() and then looping through those countries to do a max_deaths. (thus looping through the entire dataset squared times just for one api call :P ) The result of choices such as these, is that my API is extremely slow, so much that it can slow down development. Other than that, no major difficulties were encountered during implementation. If I was doing this for work I would've made different choices in regards to performance, especially with the size of the data set.