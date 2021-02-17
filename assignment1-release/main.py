import atexit
import math
import multiprocessing
import os
import sys
import time
import pickle
import functools

import numpy as np

import mp520

unit_score = 1


def run_function_with_timeout(func, parameters, timeout=10):
    try:
        pool = multiprocessing.Pool(1)
        solver = pool.apply_async(func, parameters)
        ret_val = solver.get(timeout=timeout)
    except multiprocessing.TimeoutError:
        pool.terminate()
        raise multiprocessing.TimeoutError
    return ret_val


def auto_grade_unit(grading_func, test_cases_dir):
    with open(test_cases_dir, "r") as test_cases_file:
        test_cases = test_cases_file.readlines()
    num_passed = 0
    for test_case in test_cases:
        while not test_case[-1].isdigit():
            test_case = test_case[:-1]
        print("\033[0mTesting:", test_case)
        try:
            grading_func(test_case)
        except TimeoutError:
            print("\t\033[93mSolver time out: your function is too slow!")
        except Exception as e:
            if "answer correct" in str(e):
                print("\t\033[93mWarning:", e)
                num_passed += unit_score
            else:
                print("\t\033[91mError:", e)
        else:
            print("\t\033[92mPassed.")
            num_passed += unit_score
    return float(num_passed) / len(test_cases)


def auto_grade_unit_problem1(test_case):
    global unit_score
    unit_score = 1
    num_a, num_b, gcd_ab = [int(i) for i in test_case.split(" ")]
    result = run_function_with_timeout(mp520.gcd, [num_a, num_b])
    if result[0] != gcd_ab:
        raise Exception(
            "".join(
                [
                    "incorrect GCD. Expected: ",
                    str(gcd_ab),
                    ". Got: ",
                    str(result[0]),
                    ".",
                ]
            )
        )
    if result[1] * num_a + result[2] * num_b != gcd_ab:
        raise Exception("GCD correct, but error tracing back.")


def auto_grade_unit_problem2(test_case):
    global unit_score
    unit_score = 1
    dimension, num_rects = [int(i) for i in test_case.split(" ")]
    result = run_function_with_timeout(mp520.rubiks, [dimension])
    if result != num_rects:
        raise Exception("wrong answer")


def initialize():
    p3p4_data = np.array([0, 0, 0])  # the_number, guess_count, large_count
    np.save("p3p4_data.npy", p3p4_data)


def _is_this_it(candidate):
    p3p4_data = np.load("p3p4_data.npy")
    return candidate == p3p4_data[0]


def _is_this_smaller(candidate):
    p3p4_data = np.load("p3p4_data.npy")
    p3p4_data[1] += 1
    if candidate >= p3p4_data[0]:
        p3p4_data[2] += 1
    np.save("p3p4_data.npy", p3p4_data)
    return candidate < p3p4_data[0]


def auto_grade_unit_problem3(test_case):
    global unit_score
    unit_score = 1
    p3p4_data = np.load("p3p4_data.npy")
    upper_bound, the_number = [int(i) for i in test_case.split(" ")]
    p3p4_data = np.array([the_number, 0, 0])
    np.save("p3p4_data.npy", p3p4_data)
    result = run_function_with_timeout(
        mp520.guess_unlimited, [upper_bound, _is_this_it]
    )
    if result != the_number:
        raise Exception("wrong answer")


def auto_grade_unit_problem4(test_case):
    global unit_score
    unit_score = 1
    p3p4_data = np.load("p3p4_data.npy")
    upper_bound, the_number, max_guess_num = [int(i) for i in test_case.split(" ")]
    p3p4_data = np.array([the_number, 0, 0])
    np.save("p3p4_data.npy", p3p4_data)
    result = run_function_with_timeout(
        mp520.guess_limited, [upper_bound, _is_this_smaller]
    )
    p3p4_data = np.load("p3p4_data.npy")
    if result != the_number:
        raise Exception("wrong answer")
    elif p3p4_data[2] >= 3:
        unit_score = 0
        raise Exception(
            "answer correct, but you made "
            + str(p3p4_data[2])
            + " (>=3) guesses that return False."
        )
    elif p3p4_data[1] > max_guess_num + 2:
        unit_score = float(2) / 3
        raise Exception(
            "answer correct, but you made "
            + str(p3p4_data[1] - max_guess_num)
            + " extra guesses."
        )


def pickle_multi_loader(dir_list):
    ret_val = list()
    for pickle_dir in dir_list:
        with open(pickle_dir, "rb") as pickle_file:
            ret_val.append(pickle.load(pickle_file))
    return ret_val


def auto_grade_unit_problem5(test_case, func=None):
    global unit_score
    unit_score = 1
    graph, args, expected_result = pickle_multi_loader(test_case.split(" "))
    result = run_function_with_timeout(
        func, [graph] + args, max(1, len(graph.keys()) * 0.005)
    )
    if result != expected_result:
        raise Exception("wrong answer")


def auto_grade(test_cases_dir):
    initialize()
    atexit.register(cleanup)
    scores = []
    print("\n\033[95mTesting problem 1.")
    scores.append(
        15
        * auto_grade_unit(
            auto_grade_unit_problem1, os.path.join(test_cases_dir, "test1.txt")
        )
    )
    print("\n\033[95mTesting problem 2.")
    scores.append(
        15
        * auto_grade_unit(
            auto_grade_unit_problem2, os.path.join(test_cases_dir, "test2.txt")
        )
    )
    print("\n\033[95mTesting problem 3.")
    scores.append(
        15
        * auto_grade_unit(
            auto_grade_unit_problem3, os.path.join(test_cases_dir, "test3.txt")
        )
    )
    print("\n\033[95mTesting problem 4.")
    scores.append(
        15
        * auto_grade_unit(
            auto_grade_unit_problem4, os.path.join(test_cases_dir, "test4.txt")
        )
    )
    print("\n\033[95mTesting problem 5: add vertex.")
    unit_test_func = functools.partial(auto_grade_unit_problem5, func=mp520.add_vertex)
    scores.append(
        5 * auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_1.txt"))
    )
    print("\n\033[95mTesting problem 5: delete vertex.")
    unit_test_func = functools.partial(
        auto_grade_unit_problem5, func=mp520.delete_vertex
    )
    scores.append(
        5 * auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_2.txt"))
    )
    print("\n\033[95mTesting problem 5: add edge.")
    unit_test_func = functools.partial(auto_grade_unit_problem5, func=mp520.add_edge)
    scores.append(
        5 * auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_3.txt"))
    )
    print("\n\033[95mTesting problem 5: delete edge.")
    unit_test_func = functools.partial(auto_grade_unit_problem5, func=mp520.delete_edge)
    scores.append(
        5 * auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_4.txt"))
    )
    print("\n\033[95mTesting problem 5: is connected.")
    unit_test_func = functools.partial(
        auto_grade_unit_problem5, func=mp520.is_connected
    )
    scores.append(
        10
        * max(
            auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_5.txt"))
            - 0.5,
            0,
        )
        * 2
    )
    print("\n\033[95mTesting problem 5: has cycles.")
    unit_test_func = functools.partial(auto_grade_unit_problem5, func=mp520.has_cycle)
    scores.append(
        10
        * max(
            auto_grade_unit(unit_test_func, os.path.join(test_cases_dir, "test5_6.txt"))
            - 0.5,
            0,
        )
        * 2
    )
    print("\n\033[95mFinished grading.")
    print("\033[0mItemized scores:", scores)
    print("\033[0mFinal score:", np.sum(np.array(scores)))


def cleanup():
    os.remove("p3p4_data.npy")


if __name__ == "__main__":
    if os.path.isdir("testcases") and "demo" not in sys.argv:
        auto_grade("testcases")
    else:
        auto_grade("testcases-demo")
