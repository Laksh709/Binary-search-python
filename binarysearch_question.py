#!/usr/bin/env python
# coding: utf-8

# In[118]:


def count_rotations(nums):
    pass


# In[119]:


test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


# In[120]:


from timeit import default_timer as timer
from textwrap import dedent
import math

def _str_trunc(data, size=100):
    data_str = str(data)
    if len(data_str) > size + 3:
        return data_str[:size] + '...'
    return data_str


def _show_test_case(test_case):
    inputs = test_case['input']

    if 'outputs' in test_case:
        expected_text = "Outputs"
        expected = test_case.get('outputs')
    else:
        expected_text = "Output"
        expected = test_case.get('output')

    print(dedent("""
Input:
{}

Expected {}:
{}
""".format(_str_trunc(inputs), expected_text, _str_trunc(expected))))


def _show_result(result):
    actual_output, passed, runtime = result
    message = "\033[92mPASSED\033[0m" if passed else "\033[91mFAILED\033[0m"
    print(dedent("""
Actual Output:
{}

Execution Time:
{} ms

Test Result:
{}
""".format(_str_trunc(actual_output), runtime, message)))


def evaluate_test_case(function, test_case, display=True):
    """Check if `function` works as expected for `test_case`"""
    inputs = test_case['input']

    if display:
        _show_test_case(test_case)

    start = timer()
    actual_output = function(**inputs)
    end = timer()

    runtime = math.ceil((end - start)*1e6)/1000
    if 'outputs' in test_case:
        passed = actual_output in test_case.get('outputs')
    else:
        passed = actual_output == test_case.get('output')

    result = actual_output, passed, runtime

    if display:
        _show_result(result)

    return result


def evaluate_test_cases(function, test_cases, error_only=False, summary_only=False):
    results = []
    for i, test_case in enumerate(test_cases):
        if not error_only:
            print("\n\033[1mTEST CASE #{}\033[0m".format(i))
        result = evaluate_test_case(function, test_case, display=False)
        results.append(result)
        if error_only and not result[1]:
            print("\n\033[1mTEST CASE #{}\033[0m".format(i))
        if not error_only or not result[1]:
            _show_test_case(test_case)
            _show_result(result)

    total = len(results)
    num_passed = sum([r[1] for r in results])
    print("\n\033[1mSUMMARY\033[0m")
    print("\nTOTAL: {}, \033[92mPASSED\033[0m: {}, \033[91mFAILED\033[0m: {}".format(
        total, num_passed, total - num_passed))
    return results


# In[121]:


evaluate_test_case(count_rotations,test)


# In[122]:


test0 = test


# In[123]:


# A list of size 8 rotated 5 times.
test1 = {
    'input': {

        'nums':[8,10,11,17,18,3,5,6]

    },
    'output': 5
}


# In[124]:


# A list of size 10 rotated 7 times.
test2 = {
    'input': {

        'nums': [4,5,6,7,8,9,10,1,2,3]
    },
    'output': 7
}


# In[125]:


# A list of size n(5)rotated n-1(4) times.
test3 = {
    'input': {

        'nums': [4,7,8,9,3]
    },
    'output': 4
}


# In[126]:


#List has 5 items and 5 rotations
test4 = {
    'input': {

        'nums': [3,4,7,8,9]
    },
    'output': 5
}


# In[127]:


#Empty list
test5 = {
    'input': {
        'nums': [ ]

    },
    'output':-1
}


# In[128]:


#No rotation
test6 = {
    'input': {
        'nums': [ 3,4,7,8,9],

    },
    'output':0
}


# In[129]:


#Single element only
test7 = {
    'input': {
        'nums': [3],

    },
    'output':0
}


# In[130]:


tests = [test0, test1, test2, test3, test3, test5, test6, test7]


# In[131]:


tests


# In[132]:


def count_rotations_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] <nums[position-1]:
            return position
        position +=1
    return -1    


# In[133]:


linear_search_result = evaluate_test_cases(count_rotations_linear,tests)


# In[147]:


def count_rotations_binary(nums):
 lo, hi = 0, len(nums) - 1

 if not nums:
     return -1


 if nums[lo] < nums[hi]:
     return lo

 while lo < hi:
     mid = (lo + hi) // 2

     if nums[mid] > nums[hi]:
         lo = mid + 1
     else:
         hi = mid

 return lo


# In[148]:


binary_search_result = evaluate_test_cases(count_rotations_binary,tests)


# In[ ]:




