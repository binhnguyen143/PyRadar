"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class AdeRulesAdeRuleDependentTasksResultsResource(ResourceBase):
    """Operations below ``/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the ADE rule dependent task results.'
        url = f'/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class BuildingBlocksBuildingBlockDependentTasksResultsResource(ResourceBase):
    """Operations below ``/analytics/building_blocks/building_block_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the building block rule dependent task results.'
        url = f'/analytics/building_blocks/building_block_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class RulesRuleDependentTasksResultsResource(ResourceBase):
    """Operations below ``/analytics/rules/rule_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the rule dependent task results.'
        url = f'/analytics/rules/rule_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class AdeRulesAdeRuleDeleteTasksResource(ResourceBase):
    """Operations below ``/analytics/ade_rules/ade_rule_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete the ADE rule task status.'
        url = f'/analytics/ade_rules/ade_rule_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class AdeRulesAdeRuleDependentTasksResource(ResourceBase):
    """Operations below ``/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: AdeRulesAdeRuleDependentTasksResultsResource = AdeRulesAdeRuleDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent the ADE rule task status.'
        url = f'/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels a dependent the ADE rule task.'
        url = f'/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AdeRulesDependentsResource(ResourceBase):
    """Operations below ``/analytics/ade_rules/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the ADE rule.'
        url = f'/analytics/ade_rules/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class BuildingBlocksBuildingBlockDeleteTasksResource(ResourceBase):
    """Operations below ``/analytics/building_blocks/building_block_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete the building block rule task status.'
        url = f'/analytics/building_blocks/building_block_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class BuildingBlocksBuildingBlockDependentTasksResource(ResourceBase):
    """Operations below ``/analytics/building_blocks/building_block_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: BuildingBlocksBuildingBlockDependentTasksResultsResource = BuildingBlocksBuildingBlockDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent the building block rule task status.'
        url = f'/analytics/building_blocks/building_block_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent the building block rule task.'
        url = f'/analytics/building_blocks/building_block_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class BuildingBlocksDependentsResource(ResourceBase):
    """Operations below ``/analytics/building_blocks/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the building block rule.'
        url = f'/analytics/building_blocks/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class CustomActionsActionsResource(ResourceBase):
    """Operations below ``/analytics/custom_actions/actions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new custom action with the supplied fields.'
        url = '/analytics/custom_actions/actions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, action_id, **kwargs: Any) -> Any:
        'Deletes an existing custom action.'
        url = f'/analytics/custom_actions/actions/{action_id}'
        return self._s.delete(url, **kwargs)

    def get(self, action_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a custom action based on the supplied action_id.'
        url = f'/analytics/custom_actions/actions/{action_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of available custom actions.'
        url = '/analytics/custom_actions/actions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, action_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing custom action.'
        url = f'/analytics/custom_actions/actions/{action_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class CustomActionsInterpretersResource(ResourceBase):
    """Operations below ``/analytics/custom_actions/interpreters``."""

    def get(self, interpreter_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a custom action interpreter based on supplied interpreter_id.'
        url = f'/analytics/custom_actions/interpreters/{interpreter_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of available custom action interpreters.'
        url = '/analytics/custom_actions/interpreters'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class CustomActionsScriptsResource(ResourceBase):
    """Operations below ``/analytics/custom_actions/scripts``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new custom action script file. Newly created custom action script files require a deployment before using.'
        url = '/analytics/custom_actions/scripts'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, script_id, **kwargs: Any) -> Any:
        'Deletes an existing custom action script file.'
        url = f'/analytics/custom_actions/scripts/{script_id}'
        return self._s.delete(url, **kwargs)

    def get(self, script_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves meta-data of a custom action script file based on supplied script_id.'
        url = f'/analytics/custom_actions/scripts/{script_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of meta-data for available custom action script files.'
        url = '/analytics/custom_actions/scripts'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, script_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing custom action script file. Updated custom action script files require a deployment before using.'
        url = f'/analytics/custom_actions/scripts/{script_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class RulesDependentsResource(ResourceBase):
    """Operations below ``/analytics/rules/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the rule.'
        url = f'/analytics/rules/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class RulesRuleDeleteTasksResource(ResourceBase):
    """Operations below ``/analytics/rules/rule_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete the rule task status.'
        url = f'/analytics/rules/rule_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class RulesRuleDependentTasksResource(ResourceBase):
    """Operations below ``/analytics/rules/rule_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: RulesRuleDependentTasksResultsResource = RulesRuleDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent rule task status.'
        url = f'/analytics/rules/rule_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent the rule task.'
        url = f'/analytics/rules/rule_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AdeRulesResource(ResourceBase):
    """Operations below ``/analytics/ade_rules``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.ade_rule_delete_tasks: AdeRulesAdeRuleDeleteTasksResource = AdeRulesAdeRuleDeleteTasksResource(session)
        self.ade_rule_dependent_tasks: AdeRulesAdeRuleDependentTasksResource = AdeRulesAdeRuleDependentTasksResource(session)
        self.dependents: AdeRulesDependentsResource = AdeRulesDependentsResource(session)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes an ADE rule. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check.'
        url = f'/analytics/ade_rules/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an ADE rule.'
        url = f'/analytics/ade_rules/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of ADE rules.'
        url = '/analytics/ade_rules'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the ADE rule owner or enabled/disabled only.'
        url = f'/analytics/ade_rules/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class BuildingBlocksResource(ResourceBase):
    """Operations below ``/analytics/building_blocks``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.building_block_delete_tasks: BuildingBlocksBuildingBlockDeleteTasksResource = BuildingBlocksBuildingBlockDeleteTasksResource(session)
        self.building_block_dependent_tasks: BuildingBlocksBuildingBlockDependentTasksResource = BuildingBlocksBuildingBlockDependentTasksResource(session)
        self.dependents: BuildingBlocksDependentsResource = BuildingBlocksDependentsResource(session)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes the building block rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/analytics/building_blocks/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a building block rule.'
        url = f'/analytics/building_blocks/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of building block rules.'
        url = '/analytics/building_blocks'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the building block rule owner or enabled/disabled only.'
        url = f'/analytics/building_blocks/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class CustomActionsResource(ResourceBase):
    """Operations below ``/custom_actions``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.actions: CustomActionsActionsResource = CustomActionsActionsResource(session)
        self.interpreters: CustomActionsInterpretersResource = CustomActionsInterpretersResource(session)
        self.scripts: CustomActionsScriptsResource = CustomActionsScriptsResource(session)


class RuleGroupsResource(ResourceBase):
    """Operations below ``/analytics/rule_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/analytics/rule_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a rule group.'
        url = f'/analytics/rule_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of the rule groups.'
        url = '/analytics/rule_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a rule group.'
        url = f'/analytics/rule_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class RulesResource(ResourceBase):
    """Operations below ``/analytics/rules``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: RulesDependentsResource = RulesDependentsResource(session)
        self.rule_delete_tasks: RulesRuleDeleteTasksResource = RulesRuleDeleteTasksResource(session)
        self.rule_dependent_tasks: RulesRuleDependentTasksResource = RulesRuleDependentTasksResource(session)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Delete the rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/analytics/rules/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a rule.'
        url = f'/analytics/rules/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of rules.'
        url = '/analytics/rules'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the rule owner or enabled/disabled only.'
        url = f'/analytics/rules/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class RulesOffenseContributionsResource(ResourceBase):
    """Operations below ``/analytics/rules_offense_contributions``."""

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves Rule Offense contributions \n\nRetieves Rule and Offense references in the system.'
        url = '/analytics/rules_offense_contributions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class AnalyticsAPI(ResourceBase):
    """Resource-oriented client for the ``analytics`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.ade_rules: AdeRulesResource = AdeRulesResource(session)
        self.building_blocks: BuildingBlocksResource = BuildingBlocksResource(session)
        self.custom_actions: CustomActionsResource = CustomActionsResource(session)
        self.rule_groups: RuleGroupsResource = RuleGroupsResource(session)
        self.rules: RulesResource = RulesResource(session)
        self.rules_offense_contributions: RulesOffenseContributionsResource = RulesOffenseContributionsResource(session)
