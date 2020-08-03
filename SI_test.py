import SI;

def test_SI():
    assert SI.si(1000,10,2) == 200.0
    assert SI.amount(2000,10,2)==2400.0
