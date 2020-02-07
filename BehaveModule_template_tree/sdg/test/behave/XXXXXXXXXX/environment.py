"""
This module contains all environment hooks for the Terraform module
when running a behave test.
"""

MODNAME = "XXXXXXXXXX"


def before_all(context): # pylint: disable=unused-argument
    """The before_all hook for a Behave test run.
    """
    context.XXXXXXXXXX.LOGGER = core.ADD_logger(context, f"sdg-test-behave-{MODNAME}")


def before_feature(context, feature): # pylint: disable=unused-argument
    """"""
    pass


def before_scenario(context, scenario): # pylint: disable=unused-argument
    """"""
    pass


def before_step(context, step): # pylint: disable=unused-argument
    """"""
    pass


def after_step(context, step): # pylint: disable=unused-argument
    """"""
    pass


def after_scenario(context, scenario): # pylint: disable=unused-argument
    """"""
    pass


def after_feature(context, feature): # pylint: disable=unused-argument
    """"""
    pass


def after_all(context): # pylint: disable=unused-argument
    """"""
    pass

