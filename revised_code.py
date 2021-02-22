"""
Alternative implementation of functions for the computation of a
confusion matrix.
"""


def conf(tars, preds, case):
    return sum(1 for t, p in zip(tars, preds) if (t, p) == case)


def conf_mat(tars, preds, labels=(1, 0)):
    return [[conf(tars, preds, (t, p)) for t in labels] for p in labels]


def example1(tars, preds):
    # Case constants
    TP = 1, 1
    FP = 0, 1
    FN = 1, 0
    TN = 0, 0

    print('TP:', conf(tars, preds, TP))
    print('TN:', conf(tars, preds, TN))
    print('FP:', conf(tars, preds, FP))
    print('FN:', conf(tars, preds, FN))


def example2(tars, preds):
    # lambda functions
    true_positive = lambda tars, preds: conf(tars, preds, (1, 1))
    true_negative = lambda tars, preds: conf(tars, preds, (0, 0))
    false_positive = lambda tars, preds: conf(tars, preds, (0, 1))
    false_negative = lambda tars, preds: conf(tars, preds, (1, 0))

    print('TP:', true_positive(tars, preds))
    print('TN:', true_negative(tars, preds))
    print('FP:', false_positive(tars, preds))
    print('FN:', false_negative(tars, preds))


def example3(tars, preds):
    # partial functions
    from functools import partial as pf
    true_positive = pf(conf, case=(1, 1))
    true_negative = pf(conf, case=(0, 0))
    false_positive = pf(conf, case=(0, 1))
    false_negative = pf(conf, case=(1, 0))

    print('TP:', true_positive(tars, preds))
    print('TN:', true_negative(tars, preds))
    print('FP:', false_positive(tars, preds))
    print('FN:', false_negative(tars, preds))


def example4():
    # Strings as class labels
    tars = 'cat', 'cat', 'dog', 'dog'
    preds = 'cat', 'dog', 'dog', 'dog'
    labels = 'cat', 'dog'

    cm = conf_mat(tars, preds, labels)
    for l, r in zip(labels, cm):
        print(l, r)


def example5():
    # More than two classes
    tars = [1, 1, 2, 0, 1, 2, 1, 0, 1]
    preds = [1, 0, 2, 0, 1, 2, 1, 0, 2]
    labels = 0,1,2

    for r in conf_mat(tars, preds, labels):
        print(r)


if __name__ == '__main__':
    tars = [1, 1, 0, 0, 1, 1, 1, 0, 1]
    preds = [1, 0, 1, 0, 1, 1, 1, 0, 0]

    for r in conf_mat(tars, preds):
        print(r)

    example1(tars, preds)
    example2(tars, preds)
    example3(tars, preds)
    example4()
    example5()
