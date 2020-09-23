from behave import *

@given("I have filled in correct username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("Let's go")

@when("I hit login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("You have hit login button")


@step("My credentials have been authenticated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("Successfully Authorised")

@then("I should be directed to profile home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("Welcome Home")

@given("I am on dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("Let's go")

@when("I hit Register")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("You have hit register button")


@then("I should be redirected to Register page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print ("Please register")




