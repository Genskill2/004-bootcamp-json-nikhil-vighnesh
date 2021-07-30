import pickle as _p

import pytest

import correlation

@pytest.fixture
def _datum():
    return _p.load(open(".data.json", "rb"))

def test_load_journal():
    "Test to see if the journal file is being loaded"
    ret = correlation.load_journal("journal.json")
    assert(isinstance(ret,list))
    assert(len(ret)) == 91
    assert(all(isinstance(x, dict) for x in ret))
    assert(all("squirrel" in x for x in ret))
    assert(all("events" in x for x in ret))

def test_compute_phi(_datum):
    "Test to verify the phi computation"
    vals = _datum 
    for k,v in vals.items():
        corr = correlation.compute_phi("journal.json", k)
        msg = f"Incorrect value for {k}. Expected {v}. Got {corr}."
        assert (abs(corr - v) < 0.0001), msg

def test_compute_correlations(_datum):
    vals = _datum
    corr = correlation.compute_correlations("journal.json")
    assert corr == vals

def test_diagnose():
    event_max, event_min = correlation.diagnose("journal.json")
    assert event_max == "".join(reversed("stunaep"))
    assert event_min == "".join(reversed('hteet dehsurb'))
