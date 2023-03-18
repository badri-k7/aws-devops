import json
import time
from codeguru_profiler_agent import Profiler


def some_operations(num_iterations):
    data = []
    for i in range(num_iterations):
        data.append(i ** 2)
    return data


def another_function(num_iterations):
    result = 0
    for i in range(num_iterations):
        result += i * 2
    return result


def lambda_handler(event, context):
    profiler = Profiler(profiling_group_name='study')
    profiler.start()

    print('Hello world from profiler lambda!')

    num_iterations = 10000

    # Perform some operations
    data = some_operations(num_iterations)

    # Call another function
    result = another_function(num_iterations)

    profiler.stop()

    return {
        'statusCode': 200,
        'body': json.dumps(f'Result: {result}')
    }
