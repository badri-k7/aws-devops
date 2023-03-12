# Handson with SWF

1. Import the necessary modules
    ```python
    import boto3
    import uuid
    ```
    This script imports the Boto3 library to interact with AWS services and the uuid module to generate unique IDs.

2. Create a SWF client
    ```python
    swf = boto3.client('swf')
    ```
    This creates a SWF client using the default credentials in your environment.

3. Define the domain, task list, and workflow type
    ```python
    domain = 'my-domain'
    task_list = 'my-task-list'
    workflow_type = {
        'name': 'my-workflow-type',
        'version': '1.0'
    }
    ```
    This sets the name of the domain, task list, and workflow type that will be used in the subsequent steps.
4. Register the workflow type
    ```python
    swf.register_workflow_type(
        domain=domain,
        name=workflow_type['name'],
        version=workflow_type['version'],
        defaultTaskList={
            'name': task_list
        },
        defaultExecutionStartToCloseTimeout='600',
        defaultTaskStartToCloseTimeout='60'
    )
    ```
    This registers the workflow type with SWF, which allows it to be used in future workflow executions.
5. Start a workflow execution:
    ```python
    workflow_id = str(uuid.uuid4())
    swf.start_workflow_execution(
        domain=domain,
        workflowId=workflow_id,
        workflowType=workflow_type,
        taskList={
            'name': task_list
        },
        input='{"message": "Hello, World!"}'
    )
    ```
    This starts a new workflow execution with a randomly generated `workflow_id`, using the previously defined `domain`, `task list`, and `workflow type`. The input parameter passes in an example input to the workflow.
6. Poll for decision tasks
    ```python
    while True:
        task = swf.poll_for_decision_task(
            domain=domain,
            taskList={
                'name': task_list
            }
        )
        if 'taskToken' in task:
            # Handle decision task
            swf.respond_decision_task_completed(
                taskToken=task['taskToken'],
                decisions=[
                    {
                        'decisionType': 'CompleteWorkflowExecution',
                        'completeWorkflowExecutionDecisionAttributes': {
                            'result': 'success'
                        }
                    }
                ]
            )
        else:
            # No decision tasks available
            time.sleep(1)
    ```
    This starts a loop that polls for decision tasks in the specified task list. When a decision task is received, the script responds by completing the workflow execution with a success message. If no decision tasks are available, the script waits for one second before trying again.

Overall, this script registers a workflow type with AWS SWF, starts a new workflow execution with an example input, and polls for decision tasks. When a decision task is received, the script completes the workflow execution with a success message. This is a basic example of how to use AWS SWF to create and manage workflows.