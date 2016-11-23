# Hiring Homework

## Anagrams

Backstory – imagine for a moment that I’m an online entrepreneur who has the great idea to create a website which will serve up anagrams for customers. It’s going to be so great and attract so many customers that I’ll make a fortune serving ads on the site but I don’t have a lot of capital to get going and I want to make sure that I can run the site efficiently on very few resources.

Assignment – demonstrate to me with a command line/console application that you can process the attached dictionary of valid English words in such a way as to quickly determine all the anagrams of given inputs.

I expect to enter this at the command line:

`C:\>anagrams dictionary.txt cats capers`

And get the following output:
```
Anagrams for "cats":
        acts
        cast
        cats
        scat

Anagrams for "capers":
        capers
        escarp
        pacers
        parsec
        recaps
        scrape
        spacer
```
I’m not too worried about error handling around the dictionary file because we can make sure it is correctly formatted. I’m also not too worried about “bad input” because I think we can easily filter it out. I mostly want to see the implementation of the algorithm to process the dictionary and return anagrams of test input.

A free version of Visual Studio 2015 (Visual Studio Community) is available [here](https://www.visualstudio.com/vs-2015-product-editions). It supports C++, Python, and C# development as well as F# and node.js/JavaScript. Please provide a .sln file and the supporting files to build and execute your proof-of-concept application.

Please solicit additional information if further specification is necessary.

## Priority Queue

Please create a generic priority queue in your favorite language.  Specifications for required and optional functionality can be found below.  If any requirements are unclear, please feel free to reach out and ask for clarification.

Code a generic Priority Queue
*	Priority is UInts
*	Number of priorities bound by the limits of UInts
*	Higher priorities are returned first
*	Items within a given priority will be returned in FIFO order.
*	Support the Enqueue, Dequeue and Count methods

Problem focus
*	Solve for performance
*	Write unit tests that validate the items are returned in the order expected.

Extra Credit:
*	Make thread safe
*	Write a Count(unit priority) method. 

