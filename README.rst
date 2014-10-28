==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #10
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-27T09:00:00-0400
:Due-Date: 2014-11-03T09:00:00-0400

Overview
========

This exercise will have you interacting with several files. You'll create a
series of functions that will correlate two data sources then write your output
to a report.

Task 01: Reading a CSV
======================

The goal of this particular exercise is to open and read a CSV file found on
the local filesystem. You'll be creating a function that takes a filename
as a string then returning a summarized version of the data.

The particular data we'll be analyzing is one-month of NYC Restaurant
Inspection data. You'll be returning a boro-average score.

Specifications
--------------

#.  Create a file named ``boroughs.py``

#.  Recreate the following grading scale as a dictionary with float values:

    .. table:: Grades

        ====== =====
        Letter Value
        ====== =====
        A      100%
        B      90%
        C      80%
        D      70%
        F      60%
        ====== =====

#.  Give a quick look at ``inspection_results.csv`` to get a sense of the data
    with which we'll be working.

#.  Create a function named ``get_score_summary()``

    #.  ``get_score_summary()`` takes exactly 1 argument, a string which
        represents the filename whose data will be read and interpreted

    #.  Use the file manipulation tools to open the file and read each line
        of the data. The data is stored as a CSV and is split by commas. The
        first row are headers and each subsequent row lists a restaurateur and
        their violations. This means that each vendor has their data duplicated
        several times.

    #.  Loop through the file data by reading each line and de-duplicating our
        vendors by making a simpler dictionary keyed by just the CAMIS id code
        and the GRADE and BORO as a stored value. You can skip ungraded and
        pending (P) restaurateurs since they don't have enough meaningful data
        to analyze.

        .. tip::

            Don't forget to close your file descriptor after you're done!

    #.  Next, loop through our deduplicated list and create a dictionary that
        counts the number of restaurateus per boro and sums their scores after
        converting them to floats using the grading scale.

    #.  Finally, perform one last data conversion and return a dictionary,
        keyed by boro, whose value is a tuple with the number of restaurateurs
        per boro (who have scores), and the average score (as a float) for that
        boro.

Examples
--------

.. code:: pycon

    >>> get_score_summary('inspection_results.csv')
    >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN': 
    (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955), 
    'MANHATTAN': (748, 0.9771390374331531), 'QUEENS': 
    (414, 0.9719806763285017)}

Task 02: Reading a JSON File
============================

Next, we'll be performing a similar transformation with a JSON file. JSON is
one of the most popular data formats available because of its compactness and
portability. The Python ``json`` module will be helping us convert the JSON
file.

Specifications
--------------

#.  Start by taking a peek inside ``green_markets.json`` to just get a sense
    of what the data looks like. This particular file is very dense as it
    comes from a professional source and describes all the Green Markets
    currently held in the city. We'll be reducing this data to a count of
    markets per borough.

#.  Open ``boroughs.py``, we'll be working in this file again.

#.  Import the ``json`` module.

#.  Create a function named ``get_market_density()``

    #.  Takes one argument, a filename

    #.  Open a file descriptor for our JSON file and pass the opened file
        object to json's ``load()`` function to return the data as a dictionary

    #.  Loop through the data found in the ``'data'`` and count the number of
        markets per borough, saving the result as a dictionary.

    #.  Return a dictionary of the number of green markets per borough.

Examples
--------

.. code:: pycon

    >>> get_market_density('green_markets.json')
    {u'STATEN ISLAND': 2, u'BROOKLYN': 48, u'BRONX': 32,
    u'MANHATTAN': 39, u'QUEENS': 16}

.. note::

    I forced the borough names to uppercase here to make it easier to correlate
    borough data between the two data sources.
    
.. warning::

    There's a bad record in one of the boro names (it has an extra space -- how would you normalize the name?)

Task 03: Relating Data and Writing a File
=========================================

Finally, we'll combine these two pieces of data on their borough keys and write
the results to a file. This particular relation is fairly noneventful but it
demonstrates the power of I/O methods in Python quite well.

Specifications
--------------

#.  Open ``boroughs.py``

#.  Create a new function, ``correlate_data()``

    #.  Takes three arguments:

        #.  First argument is the name of a file with restaurant scores data

        #.  Next argument is the name of a JSON file with green_market data

        #.  The final argument is the name of a file that will contain the
            output of this function.

    #.  Use the previous two functions to get aggregate market and restaurant
        score data per-borough.

    #.  Combine the data into a single dictionary, keyed by borough, whose
        whose values are tuples containing the borough food score and the
        percentage density of green markets to restaurateurs as a float.

        The result of this should be similar to:

        .. code:: python

            {'BRONX': (0.9762820512820514, 0.1987179487179487)}

    #.  Finally, use the json module's ``dump()`` method to write the combined
        data dictionary to a file (the one occupying the third argument in
        the function call).

Build a Cache Manager
=====================

It is very common in computer programming to create a class to manage the input
and output operation of data stored in a file on the computer's hard drive. In
the following tasks you will create an object that can get, set and delete
other pickled Python objects to and from a file. Make sure to review Chapter 9
of the text. Lutz covers how to use the native Python pickle module.

Task 04: Create the PickleCache Class
-------------------------------------

You've already instantiated and used some classes already if you consider your
prior use of such classes like the ``Decimal()`` class. We've also now covered
how to create your own custom classes.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``picklecache.py``. In ``picklecache.py``:

#.  Import the ``os`` and ``pickle`` modules.

#.  Initialize the class with a constructor function that accepts a
    ``file_path`` string variable with a default value of ``datastore.pkl``.
    The constructor must also define the following attributes:

    #.  Pseudo-private *class attribute* named ``__file_path``. It must assigned
        the constructor variable ``file_path`` value.

    #.  Pseudo-private *class attribute* named ``__file_object`` instantiated
        with ``None``.

    #.  Pseudo-private *class attribute* named ``__data`` instantiated as an
        empty dictionary object.

Task 05: Add a Set Method
-------------------------

The ``self.__data`` attribute is pseudo-private and not by convention
accessible to outside objects. Therefore, you will need to create a public
method that allows key value pairs to be stored within the class.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public function named ``set()`` that accepts two arguments:
    ``key`` and ``value``. It will then save the key pair in the
    ``self.__data`` dictionary.

Task 06: Add a Get Method
-------------------------

You will need a way to retrieve data from the PickleCache object.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``get()`` that accepts one argument
    named ``key``. It must use this key to return the requested value from the
    ``self.__data`` dictionary.

#.  Make sure that your use a conditional that check for the existence of the
    key before attempting to return the value.

#.  Print a formatted error statement of ``Error: No value found for key:
    '{}'`` if the key does not exist.

Task 07: Add a Delete Method
----------------------------

There needs to be a way to remove unwanted objects from the ``PickleCache``
object. This method is similar to the previous task but deletes a value
instead.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``delete()`` that accepts one argument
    named ``key``.

#.  Again you will need to make sure that the provided key exists in the
    ``self.__data`` dictionary object before attempting to delete it. You can
    use the same conditional as you did in *Task 06* or  use *Task 06* as part
    of your conditional check. Either way is fine.

#.  Use the ``del`` statement to remove the key pair from ``self.__data``.

Task 08: Add the Open Method
----------------------------

At this point you have created a standard class that can set, get and delete
objects while the program is running. Now you will make the data persist by
pickling it and saving it to a file. This way the data can be accessed the next
time the program runs.

You care going to need to use the ``os.path.exists()`` and ``os.path.getsize
()`` methods as part of your conditional logic.

Specifications
^^^^^^^^^^^^^^

#.  Create a public bound method named ``open()``. It will not access any
    arguments.

#.  Open the ``self.__file_path`` for reading only if it exists and has a file
    size greater than zero.

    #.  Use conditional flow control to check if the ``self.__file_path``
        exists using ``os.path.exists(self.__file_path)``.

    #.  Check if the file size is greater than zero using ``os.path.getsize
        (self.__file_path)``.

    #.  Use the pickle load function to assign the file contents to the
        ``self.__data`` attribute

    #.  Close the file object.

#.  Re-open the data file in write mode before this function ends.

Task 09: Create a Flush Method
------------------------------

Your class need to be able to save its stored data to file when commanded to do
so. This is especially important if the PickleCache were to be used in a
program running for more than just a few moments. Now you will use the
``pickle.dump()`` method and the file object ``close()`` methods to accomplish
this.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public function named ``flush`` that has one boolean
    argument named ``reopen`` set to a default of ``True``.

#.  Use the pickle dump methods to save the object's data attribute to the
    object's file object.

#.  Close the file object after the pickle dump.

#.  If the ``reopen`` argument is ``True``, call the ``open()`` method you
    created in the previous task.

Task 10: Create a Close Method
------------------------------

It is usually a good practice to provide a ``close()`` method for objects
interacting with input and output from files.

Specifications
^^^^^^^^^^^^^^

#.  Create a bound public method named ``close()`` that does not accept any
    arguments.

#.  It should call the ``flush()`` method with ``reopen=False``.

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
