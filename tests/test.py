import unittest
import os
import sys
sys.path.append('./')


def run():
    testmodules = []
    for root, dirs, files in os.walk('tests'):
        # print root
        for filename in files:
            if filename.endswith('.py'):
                if filename not in ['test.py']:
                    if root[6:]:
                        testmodules.append(
                            "{}.{}".format(
                                root[6:], filename[:-3]).replace("/", "."))
                    else:
                        testmodules.append(filename[:-3])

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run()
