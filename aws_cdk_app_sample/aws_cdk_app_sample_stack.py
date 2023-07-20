import os
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as api_gw_
)
from constructs import Construct

DIRNAME = os.path.dirname(__file__)

class AwsCdkAppSampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        fn = lambda_.Function(
            self, "HelloWorldFn",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="index.handler",
            code=lambda_.Code.from_asset(os.path.join(DIRNAME, "src")),
            environment={}
        )

        api = api_gw_.LambdaRestApi(
            self, "HelloWorldAPI",
            handler=fn,
            proxy=False
        )

        hello_world = api.root.add_resource("hi")
        hello_world.add_method("GET")
