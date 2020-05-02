## Introduction

By this point in the book, you should have observed
that we have written a number of _tests_ for our data.

## Why test?

### If you like it, put a ring on it...

...and if you rely on it, test it.

I am personally a proponent of writing tests for our data
because as data scientists,
the fields of our data, and their correct values,
form the "data programming interface" (DPI)
much like function signatures form
the "application programming interface" (API).
Since we test the APIs that we rely on,
we probably should test the DPIs that we rely on too.

## What to test

When thinking about what part of the data to test,
it can be confusing.
After all, data are seemingly generated
from random processes
(my Bayesian foxtail has been revealed),
and it seems difficult to test random processes.

That said, from my experience handling data,
I can suggest a few principles.

### Test invariants

Firstly, we test __invariant properties__ of the data.
Put in plain language, things we know _ought_ to be true.

Using the Divvy bike dataset example,
we know that every node ought to have a station name.
Thus, the minimum that we can test
is that the `station_name` attribute is present on every node.
As an example:

```python
def test_divvy_nodes(G):
    """Test node metadata on Divvy dataset."""
    for n, d in G.nodes(data=True):
        assert "station_name" in d.keys()
```

### Test nullity

Secondly, we can test that values that ought **not** to be null
should not be null.

Using the Divvy bike dataset example again,
if we _also_ know that the station name
cannot be null or an empty string,
then we can bake that into the test.

```python
def test_divvy_nodes(G):
    """Test node metadata on Divvy dataset."""
    for n, d in G.nodes(data=True):
        assert "station_name" in d.keys()
        assert bool(d["station_name"])
```

### Test boundaries

We can also test boundary values.
For example, within the city of Chicago,
we know that latitude and longitude values
ought to be within the vicinity of
`41.85003, -87.65005`.
If we get data values that are, say,
outside the range of `[41, 42]; [-88, -87]`,
then we know that we have data issues as well.

Here's an example:

```python
def test_divvy_nodes(G):
    """Test node metadata on Divvy dataset."""
    for n, d in G.nodes(data=True):
        # Test for station names.
        assert "station_name" in d.keys()
        assert bool(d["station_name"])

        # Test for longitude/latitude
        assert d["latitude"] >= 41 and d["latitude"] <= 42
        assert d["longitude"] >= -88 and d["longitude"] <= -87
```

??? note "An apology to geospatial experts"

    I genuinely don't know the bounding box lat/lon coordinates of Chicago,
    so if you know those coordinates, please reach out
    so I can update the test.

## Continuous data testing

The key idea with testing is to have tests that continuously run
all the time in the background
without you ever needing to intervene to kickstart it off.
It's like having a bot in the background always running checks for you
so you don't have to kickstart them.

To do so, you should be equipped with a few tools.
I won't go into them in-depth here,
as I will be writing
a "continuous data testing" essay in the near future.
That said, here is the gist.

Firstly, **use `pytest` to get set up with testing.**
You essentially write a `test_something.py` file
in which you write your test suite,
and your test functions are all nothinng more than simple functions.

```python
# test_data.py
def test_divvy_nodes(G):
    """Test node metadata on Divvy dataset."""
    for n, d in G.nodes(data=True):
        # Test for station names.
        assert "station_name" in d.keys()
        assert bool(d["station_name"])

        # Test for longitude/latitude
        assert d["latitude"] >= 41 and d["latitude"] <= 42
        assert d["longitude"] >= -88 and d["longitude"] <= -87
```

At the command line, if you ran `pytest`,
it will automatically discover all functions prefixed with `test_`
in all `.py` files underneath the current working directory.

Secondly, **set up a continuous pipelining system**
to continuously run data tests.
For example, you can set up
[Jenkins](https://www.jenkins.io/),
[Travis](https://travis-ci.org/),
[Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/),
[Prefect](https://www.prefect.io/),
and more,
depending on what your organization has bought into.

Sometimes data tests take longer than software tests,
especially if you are pulling dumps from a database,
so you might want to run this portion of tests
in a separate pipeline instead.

## Further reading

- In my essays collection, I wrote about [testing data](https://ericmjl.github.io/essays-on-data-science/software-skills/testing/#tests-for-data).
- Itamar Turner-Trauring has written about [keeping tests quick and speedy](https://pythonspeed.com/articles/slow-tests-fast-feedback/), which is extremely crucial to keeping yourself motivated to write tests.
