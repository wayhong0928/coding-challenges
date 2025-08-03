from HackerRank.python.algorithms.warm_up.staircase import staircase


def test_staircase_output(capsys):
    staircase(1)
    captured = capsys.readouterr()
    assert captured.out == "#\n"

    staircase(3)
    captured = capsys.readouterr()
    assert captured.out == "  #\n ##\n###\n"

    staircase(5)
    captured = capsys.readouterr()
    assert captured.out == "    #\n   ##\n  ###\n ####\n#####\n"
