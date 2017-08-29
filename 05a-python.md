≈ß# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are sequences of values, where the values can be any type, and they are indexed by integers. The main difference between tuples and lists is that lists are mutable while tuples are not. Being immutable or hashable allows tuples to be used as keys in dictionaries, because keys must always correspond to the same hash value in order for their corresponding values to be looked up correctly.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are sequences of values and are mutable. Key differences are that sets are unordered, contain no duplicates, and can only contain immutable elements as values. For example, if I wanted to store the prime factorization of a number, I would use a list because I might need duplicates. If I wanted to store all of the triangular numbers, I would use a set to eliminate duplicates. Finding an element in a set is faster than in a list. This is because when a set is created, each element is hashed to a unique number, so when checking for an element the program just has to check if that element's hash value already exists.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is an anonymous function, and is defined without a name. The syntax of a lambda function is "lambda arguments: expression." For example, the lines
```python
squared = lambda x: x**2
print(squared(5))
```
>> would print 25.
Lambda functions are used when you only need a quick function for a short time. They can be used as arguments in other functions. For example, a lambda function can be used as an argument to the ```map()``` function, which takes in a function and a list, and applies the function to each item in the list. The following code maps every number in the list to its square, and prints ```[1,4,9,16,25,36]```.
```python
oldlist = [1,2,3,4,5,6]
newlist = list(map(lambda x: x**2, oldlist))
print(newlist)
```
>> As the key argument to the ```sorted()``` function, ```sorted()``` will sort a list by the values returned by the key. Here is an example:
```python
mylist = [(1,10,12),(7,5,3),(3,8,20),(8,6,4)]
newlist = sorted(mylist, key=lambda x: x[1])
print(newlist)
```
>> The above would print ```[(7,5,3),(8,6,4),(3,8,20),(1,10,12)]``` because the key tells it to sort by the second value of each item in the list.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is the ability in python to create and manipulate lists in a very intuitive way. It allows you to reduce the following code to a single line:
```python
squares = []
for i in range(11):
    squares.append(i**2)
print(squares)
# OR
squares2 = [i**2 for i in range(11)]
print(squares2)
# both print [0,1,4,9,16,25,36,49,64,81,100]
```
>> The function `map()` applies a function to each item in a list and returns that list. The equivalent of the above using `map()` would be:
```python
squares3 = list(map(lambda x: x**2, list(range(11))))
```
>> Now, if I wanted a list of only the odd perfect squares, I could use the following list comprehension:
```python
oddsquares = [i for i in squares if (i % 2 == 1)]
```
>> The above can also be done using the `filter()` function, which creates a list of elements that satisfy a given function from another list. We can find the odd squares using `filter()`:
```python
oddsquares2 = list(filter(lambda x: (x % 2 == 1), squares))
```
>> Set comprehension works similarly; below we create a set of the odd squares:
```python
oddsquares3 = {i for i in squares if (i % 2 == 1)}
```
>> The biggest difference is that this set is unordered; when I print `oddsquares3` I get `{1,9,81,49,25}`. With dictionary comprehension, I can easily build a dictionary where the keys are the squares and the values are whether the squares are odd:
```python
squaresdict = {x: x % 2 == 1 for x in squares}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





