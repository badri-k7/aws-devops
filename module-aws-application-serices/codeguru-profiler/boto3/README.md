# Lambda Function with AWS CodeGuru Profiler

This Python script demonstrates the use of AWS CodeGuru Profiler with an AWS Lambda function. It includes two custom functions, `some_operations` and `another_function`, that perform calculations with a given number of iterations. The `lambda_handler` function calls these two custom functions.

## Requirements
- Python 3.8+
- AWS CodeGuru Profiler activated for your lambda function

## Usage

1. Set up the required AWS CodeGuru Profiler profiling group and environment variables for your Lambda function.

2. Deploy your Lambda function and start invoking it. The CodeGuru Profiler will collect and analyze runtime performance data from your Lambda function.

3. View the collected data and generated recommendations in the AWS CodeGuru Profiler dashboard.