import aoc_02

def test_slow_continuous_increase_1():
    # Setup
    t_list = [1, 2, 3, 4]
    expected = True
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_cont_increase_3():
    # Setup
    t_list = [1, 4, 7, 10]
    expected = True
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_cont_quick_inc():
    # Setup
    t_list = [1, 5, 9, 13]
    expected = False
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_cont_no_change():
    # Setup
    t_list = [1, 2, 2, 4]
    expected = False
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_continuous_decrease_1():
    # Setup
    t_list = [4, 3, 2, 1]
    expected = True
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_cont_decrease_3():
    # Setup
    t_list = [10, 7, 4, 1]
    expected = True
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected

def test_slow_cont_quick_dec():
    # Setup
    t_list = [13, 9, 5, 1]
    expected = False
    # Invoke
    actual = aoc_02.slow_continuous(t_list)
    # Analyze
    assert actual == expected