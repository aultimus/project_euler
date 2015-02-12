# Regression testing suite
# Record answers in answers.txt after you discover them
# This test suite will compare these answers with all python solutions in cwd
# Optimisation: Run tests in seperate threads
# TODO: Run all doctests for all python files in cwd
import glob
import subprocess
import time

with open("answers.txt") as f:
    answers = [line.strip().split(", ") for line in f.readlines()]
    answers = [ans for ans in answers if ans[1] != "?"]

py_files = glob.glob("*.py")

# shitty running time here
tests = [(f_name, ans[1]) for ans in answers for f_name in py_files
          if f_name.startswith(ans[0] + "_")]

failures = []
count = 0
for f_name, ans in tests:
    mod_name = f_name.split(".")[0]
    try:
        mod = __import__(mod_name)
    except ImportError as e:
        print e
        failures.append((f_name, "ImportException", e))
        count += 1
        continue
    if "main" in dir(mod):
        print "Testing %s..." % f_name
        try:
            start = time.time()
            result = mod.main()
        except Exception as e:
            result = e
        if result == ans or str(result) == ans:
            print "PASSED, took %d secs" % (time.time() - start)
        else:
            got = "got: %s" % str(result)
            expected = "expected %s" % ans
            print "failures:"
            print got
            print expected
            failures.append((f_name, got, expected))
        count += 1
    else:
        print f_name, "not compatible, no main func"
    print

print "-" * 70
print "SUMMARY"
print "%d / %d succeeded" % (count - len(failures), count)
print "FAILURES:"
for fail in failures:
    print "%s\n%s\n%s\n" % (fail[0], fail[1], fail[2])
