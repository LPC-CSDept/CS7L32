import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '50'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*F[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '65'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*D[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '75'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*C[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_4():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '85'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*B[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_5():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '90'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*A[\w,\W]*', lines[0])
    assert res != None
    print(res.group())
