"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class EventSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable``."""

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the event calculated property.'
        url = f'/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the calculated property dependent task results.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type``."""

    def get(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the event regex property for changing type of field for it.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertiesDependentsDisableResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable``."""

    def get(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the event regex property for disabling it.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterAllowedValuesResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values``."""

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a dsm paramater allowed value by ID.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a dsm parameter allowed value by id.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve dsm parameter allowed values.'
        url = '/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a dsm parameter allowed value by id.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_many(self, body: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create new dsm parameter allowed values or Update available dsm parameter allowed values.\n\nThe following fields can be provided in the body of this request, all other dsm parameter allowed value fields will be ignored:\n>'
        url = '/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values'
        headers = {'fields': fields, 'filter': filter}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, range_header=range_header, json_body=body, **kwargs)


class EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterDefinitionResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition``."""

    def get(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve dsm parameter definitions.'
        url = '/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParametersResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters``."""

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a dsm paramater by ID.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a dsm parameter by id.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve dsm parameters.'
        url = '/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a dsm parameter by id.'
        url = f'/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_many(self, body: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create new dsm parameters or Update available dsm parameters.\n\nThe following fields can be provided in the body of this request, all other dsm parameter fields will be ignored:'
        url = '/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters'
        headers = {'fields': fields, 'filter': filter}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, range_header=range_header, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable``."""

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the flow calculated property.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the calculated property dependent task results.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type``."""

    def get(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the flow regex property for changing type of field for it.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertiesDepResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}``."""

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a calculated event property based on the supplied calculated property ID.'
        url = f'/config/event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertiesDependentsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.disable: EventSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource = EventSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource(session)

    def list(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the event calculated property.'
        url = f'/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource = EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the event calculated property dependent task status.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the calculated property dependent task.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the calculated property dependent task results.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertiesDependentsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.change_field_type: EventSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource = EventSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource(session)
        self.disable: EventSourcesCustomPropertiesRegexPropertiesDependentsDisableResource = EventSourcesCustomPropertiesRegexPropertiesDependentsDisableResource(session)

    def list(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the event regex property.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the event regex property dependent task status.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the regex property dependent task.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the event regex property dependent task status.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the regex property dependent task.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesLogSourceManagementAutodetectionConfigRecordsResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/autodetection/config_records``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates an Autodetection Config Record.'
        url = '/config/event_sources/log_source_management/autodetection/config_records'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, config_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual Autodetection Config Record by id.'
        url = f'/config/event_sources/log_source_management/autodetection/config_records/{config_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of Autodetection Config Records.'
        url = '/config/event_sources/log_source_management/autodetection/config_records'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, config_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an Autodetection Config Record.'
        url = f'/config/event_sources/log_source_management/autodetection/config_records/{config_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationResource(ResourceBase):
    """Operations below ``/event_sources/log_source_management/log_source_types/dsm_parameter_configuration``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dsm_parameter_allowed_values: EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterAllowedValuesResource = EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterAllowedValuesResource(session)
        self.dsm_parameter_definition: EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterDefinitionResource = EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParameterDefinitionResource(session)
        self.dsm_parameters: EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParametersResource = EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationDsmParametersResource(session)


class FlowSourcesCustomPropertiesCalculatedPropertiesDepResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}``."""

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a calculated flow property based on the supplied calculated property ID.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertiesDependentsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.disable: FlowSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource = FlowSourcesCustomPropertiesCalculatedPropertiesDependentsDisableResource(session)

    def list(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the flow calculated property.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource = FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the flow calculated property dependent task status.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the calculated property dependent task.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the calculated property dependent task results.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertiesDependentsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.change_field_type: FlowSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource = FlowSourcesCustomPropertiesRegexPropertiesDependentsChangeFieldTypeResource(session)

    def list(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the flow regex property.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertiesDisablingDependentsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents``."""

    def list(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the flow regex property.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the flow regex property dependent task status.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the regex property dependent task.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the flow regex property dependent task status.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the regex property dependent task.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the regex property dependent task results.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class AccessTenantManagementTenantsResource(ResourceBase):
    """Operations below ``/config/access/tenant_management/tenants``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new tenant.'
        url = '/config/access/tenant_management/tenants'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, tenant_id, **kwargs: Any) -> Any:
        'Delete a tenant.'
        url = f'/config/access/tenant_management/tenants/{tenant_id}'
        return self._s.delete(url, **kwargs)

    def get(self, tenant_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a tenant by tenant id.'
        url = f'/config/access/tenant_management/tenants/{tenant_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the list of all tenants ordered by tenant id.'
        url = '/config/access/tenant_management/tenants'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, tenant_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a tenant'
        url = f'/config/access/tenant_management/tenants/{tenant_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AccessUserDependentTasksResultsResource(ResourceBase):
    """Operations below ``/config/access/user_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the user dependent task results.'
        url = f'/config/access/user_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class AccessUsersDependentsResource(ResourceBase):
    """Operations below ``/config/access/users/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the user.'
        url = f'/config/access/users/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class CertificatesEndCertificatesFullChainResource(ResourceBase):
    """Operations below ``/config/certificates/end_certificates/{id}/full_chain``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the full chain of the certificate. The chain hierarchy includes the content of the end certificate, and the content of the issuer chain certificates, up to and including the root certificate.\nThis endpoint might not return the root certificate if it was uploaded in the last 24 hours'
        url = f'/config/certificates/end_certificates/{id}/full_chain'
        return self._s.get(url, fields=fields, **kwargs)


class CertificatesRootCertificatesGetDependantIdsResource(ResourceBase):
    """Operations below ``/config/certificates/root_certificates/{id}/get_dependant_ids``."""

    def list(self, id, **kwargs: Any) -> Any:
        'Gets a list of end certificate IDs that depend on the root certificate. This endpoint\nmight not return the dependent IDs of the certificates that were uploaded in the last 24 hours.You\nmust have System Administrator or Security Administrator permissions to use this\nendpoint.'
        url = f'/config/certificates/root_certificates/{id}/get_dependant_ids'
        return self._s.get(url, **kwargs)


class DeploymentHostsTunnelsResource(ResourceBase):
    """Operations below ``/config/deployment/hosts/{id}/tunnels``."""

    def list(self, id, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of tunnels for the host.'
        url = f'/config/deployment/hosts/{id}/tunnels'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertiesResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dep: EventSourcesCustomPropertiesCalculatedPropertiesDepResource = EventSourcesCustomPropertiesCalculatedPropertiesDepResource(session)
        self.dependents: EventSourcesCustomPropertiesCalculatedPropertiesDependentsResource = EventSourcesCustomPropertiesCalculatedPropertiesDependentsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new calculated event property.'
        url = '/config/event_sources/custom_properties/calculated_properties'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes the event calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a calculated event property based on the supplied calculated property identifier.'
        url = f'/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of calculated event properties.'
        url = '/config/event_sources/custom_properties/calculated_properties'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, calculated_property_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing calculated event property.'
        url = f'/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property/{calculated_property_name}``."""

    def get(self, calculated_property_name, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of event calculated properties.'
        url = f'/config/event_sources/custom_properties/calculated_property/{calculated_property_name}'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of the event calculated property delete task.'
        url = f'/config/event_sources/custom_properties/calculated_property_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.disable: EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource = EventSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource(session)
        self.results: EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource = EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of the event calculated property dependents task.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the event calculated property dependent task.'
        url = f'/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesCalculatedPropertyOperandsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/calculated_property_operands``."""

    def list(self, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of available options for calculated event property operand.'
        url = '/config/event_sources/custom_properties/calculated_property_operands'
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)


class EventSourcesCustomPropertiesPropertyAqlExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_aql_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Custom Property AQL expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = '/config/event_sources/custom_properties/property_aql_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a Custom Property AQL expression based on the supplied expression ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_aql_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets a Custom Property AQL Expression by ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_aql_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of Custom Property AQL Expressions. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = '/config/event_sources/custom_properties/property_aql_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a Custom Property AQL expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_aql_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyCalculatedExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_calculated_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Custom Property Calculated Expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = '/config/event_sources/custom_properties/property_calculated_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a Custom Property Calculated Expression based on the supplied expression ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets a Custom Property Calculated Expression by ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of Custom Property Calculated Expressions. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = '/config/event_sources/custom_properties/property_calculated_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a Custom Property Calculated Expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission.'
        url = f'/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyCefExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_cef_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new CEF expression.'
        url = '/config/event_sources/custom_properties/property_cef_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a CEF expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_cef_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a CEF expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_cef_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of CEF expressions.'
        url = '/config/event_sources/custom_properties/property_cef_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing CEF expression.'
        url = f'/config/event_sources/custom_properties/property_cef_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new event regex property expression.'
        url = '/config/event_sources/custom_properties/property_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes an event regex property expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a event regex property expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of event regex property expressions.'
        url = '/config/event_sources/custom_properties/property_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing event regex property expression.'
        url = f'/config/event_sources/custom_properties/property_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyGenericlistExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_genericlist_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Generic List expression.'
        url = '/config/event_sources/custom_properties/property_genericlist_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a Generic List expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a Generic List expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of Generic List expressions.'
        url = '/config/event_sources/custom_properties/property_genericlist_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing Generic List expression.'
        url = f'/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyJsonExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_json_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new JSON expression.'
        url = '/config/event_sources/custom_properties/property_json_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a JSON expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_json_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a JSON expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_json_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of JSON expressions.'
        url = '/config/event_sources/custom_properties/property_json_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing JSON expression.'
        url = f'/config/event_sources/custom_properties/property_json_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyLeefExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_leef_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new LEEF Expression.'
        url = '/config/event_sources/custom_properties/property_leef_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a LEEF Expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_leef_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a LEEF Expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_leef_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of LEEF Expressions.'
        url = '/config/event_sources/custom_properties/property_leef_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing LEEF Expression.'
        url = f'/config/event_sources/custom_properties/property_leef_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyNvpExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_nvp_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Name Value Pair expression.'
        url = '/config/event_sources/custom_properties/property_nvp_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a Name Value Pair expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a Name Value Pair expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of Name Value Pair expressions.'
        url = '/config/event_sources/custom_properties/property_nvp_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing Name Value Pair expression.'
        url = f'/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesPropertyXmlExpressionsResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/property_xml_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new XML expression.'
        url = '/config/event_sources/custom_properties/property_xml_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes an XML expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_xml_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a XML expression based on the supplied identifier.'
        url = f'/config/event_sources/custom_properties/property_xml_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of XML expressions.'
        url = '/config/event_sources/custom_properties/property_xml_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing XML expression.'
        url = f'/config/event_sources/custom_properties/property_xml_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesRegexPropertiesResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: EventSourcesCustomPropertiesRegexPropertiesDependentsResource = EventSourcesCustomPropertiesRegexPropertiesDependentsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new event regex property.'
        url = '/config/event_sources/custom_properties/regex_properties'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes an event regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a event regex property based on the supplied regex property ID.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of event regex properties.'
        url = '/config/event_sources/custom_properties/regex_properties'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, regex_property_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing event regex property.'
        url = f'/config/event_sources/custom_properties/regex_properties/{regex_property_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDeleteTasksResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the event regex property delete task status.'
        url = f'/config/event_sources/custom_properties/regex_property_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class EventSourcesCustomPropertiesRegexPropertyDependentTasksResource(ResourceBase):
    """Operations below ``/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.change_field_type: EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource(session)
        self.disable: EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource(session)
        self.results: EventSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the event regex property dependent task status.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the regex property dependent task.'
        url = f'/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementAutodetectionResource(ResourceBase):
    """Operations below ``/event_sources/log_source_management/autodetection``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.config_records: EventSourcesLogSourceManagementAutodetectionConfigRecordsResource = EventSourcesLogSourceManagementAutodetectionConfigRecordsResource(session)


class EventSourcesLogSourceManagementLogSourceBulkTasksResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_bulk_tasks/{id}``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source bulk task by ID.'
        url = f'/config/event_sources/log_source_management/log_source_bulk_tasks/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        "Updates a log source bulk task.\n\nThe only field that can be updated is the 'status' field, and the only allowed value is 'CANCELLED'."
        url = f'/config/event_sources/log_source_management/log_source_bulk_tasks/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementLogSourceExtensionsResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_extensions``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source extension by ID.'
        url = f'/config/event_sources/log_source_management/log_source_extensions/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of log source extensions.'
        url = '/config/event_sources/log_source_management/log_source_extensions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesLogSourceManagementLogSourceGroupsResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_groups``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new log source group. A log source group contains the following fields:'
        url = '/config/event_sources/log_source_management/log_source_groups'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source group by ID.'
        url = f'/config/event_sources/log_source_management/log_source_groups/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of log source groups.'
        url = '/config/event_sources/log_source_management/log_source_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesLogSourceManagementLogSourceLanguagesResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_languages``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source language by ID.'
        url = f'/config/event_sources/log_source_management/log_source_languages/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of log source languages.'
        url = '/config/event_sources/log_source_management/log_source_languages'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesLogSourceManagementLogSourceStatisticsResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_statistics``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates log source statistics Log source statistics contains the following fields:\nLogSourceFieldValueStatistic contains the following fields:'
        url = '/config/event_sources/log_source_management/log_source_statistics'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementLogSourceTypesResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_source_types``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dsm_parameter_configuration: EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationResource = EventSourcesLogSourceManagementLogSourceTypesDsmParameterConfigurationResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new custom log source type. Log source types do not need to be deployed. The\nfollowing fields can be provided in the body of this request, all other log source type fields will\nbe ignored:'
        url = '/config/event_sources/log_source_management/log_source_types'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a custom log source type by ID.'
        url = f'/config/event_sources/log_source_management/log_source_types/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source type by ID. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned for the log source type. If called by a less privileged client, only name and ID are returned for the log source type.'
        url = f'/config/event_sources/log_source_management/log_source_types/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of log source types. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned in each log source type. If called by a less privileged client, only name and ID are returned in each log source type.'
        url = '/config/event_sources/log_source_management/log_source_types'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a log source type by ID. The following fields can be provided in the body of this\nrequest, all other log source type fields will be ignored:'
        url = f'/config/event_sources/log_source_management/log_source_types/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementLogSourcesResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/log_sources``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new log source.\n\nA log source contains the following fields:'
        url = '/config/event_sources/log_source_management/log_sources'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a log source by ID.'
        url = f'/config/event_sources/log_source_management/log_sources/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, x_qrd_encryption_algorithm: Optional[Any]=None, x_qrd_encryption_password: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a log source by ID.'
        url = f'/config/event_sources/log_source_management/log_sources/{id}'
        headers = {'x-qrd-encryption-algorithm': x_qrd_encryption_algorithm, 'x-qrd-encryption-password': x_qrd_encryption_password}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, fields=fields, **kwargs)

    def list(self, x_qrd_encryption_algorithm: Optional[Any]=None, x_qrd_encryption_password: Optional[Any]=None, sort: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of log sources.'
        url = '/config/event_sources/log_source_management/log_sources'
        headers = {'x-qrd-encryption-algorithm': x_qrd_encryption_algorithm, 'x-qrd-encryption-password': x_qrd_encryption_password}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a log source by ID.'
        url = f'/config/event_sources/log_source_management/log_sources/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_many(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Patches an array of log sources. Capable of creating, updating and deleting multiple log sources in the same transaction.'
        url = '/config/event_sources/log_source_management/log_sources'
        return self._s.patch(url, json_body=body, **kwargs)


class EventSourcesLogSourceManagementProtocolTypesResource(ResourceBase):
    """Operations below ``/config/event_sources/log_source_management/protocol_types``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a protocol type by ID. Requires the System Administrator, Security Admin, or Manage Log Sources permission.'
        url = f'/config/event_sources/log_source_management/protocol_types/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of protocol types. Requires the System Administrator, Security Admin, or Manage Log Sources permission.'
        url = '/config/event_sources/log_source_management/protocol_types'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesWincollectWincollectAgentsResource(ResourceBase):
    """Operations below ``/config/event_sources/wincollect/wincollect_agents``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a WinCollect agent by ID.'
        url = f'/config/event_sources/wincollect/wincollect_agents/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of WinCollect agents.'
        url = '/config/event_sources/wincollect/wincollect_agents'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesWincollectWincollectDestinationsResource(ResourceBase):
    """Operations below ``/config/event_sources/wincollect/wincollect_destinations``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a WinCollect destination by ID.'
        url = f'/config/event_sources/wincollect/wincollect_destinations/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of WinCollect destinations.'
        url = '/config/event_sources/wincollect/wincollect_destinations'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class ExtensionManagementExtensionExportTasksExtensionExportResource(ResourceBase):
    """Operations below ``/config/extension_management/extension_export_tasks/{task_id}/extension_export``."""

    def get(self, task_id, **kwargs: Any) -> Any:
        'Retrieves the exported extension based on the task_id.'
        url = f'/config/extension_management/extension_export_tasks/{task_id}/extension_export'
        return self._s.get(url, **kwargs)


class ExtensionManagementExtensionExportTasksResultsResource(ResourceBase):
    """Operations below ``/config/extension_management/extension_export_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the tasks status results based on the task_id.'
        url = f'/config/extension_management/extension_export_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class ExtensionManagementExtensionsMetadataResource(ResourceBase):
    """Operations below ``/config/extension_management/extensions/{extension_id}/metadata``."""

    def create(self, extension_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds metadata to the Extension corresponding to the supplied extension_id.'
        url = f'/config/extension_management/extensions/{extension_id}/metadata'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class ExtensionManagementExtensionsTaskStatusResultsResource(ResourceBase):
    """Operations below ``/config/extension_management/extensions_task_status/{status_id}/results``."""

    def list(self, status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the tasks status results based on the status_id.'
        url = f'/config/extension_management/extensions_task_status/{status_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class FlowApplicationsActiveApplicationsResource(ResourceBase):
    """Operations below ``/config/flow/applications/active_applications``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual active flow application that is currently deployed in the system, as specified by the application ID.\n\nActive applications are flow applications that are currently in-use by the system.\nChanges or modifications to a flow application should always be made to the active applications list. Do not update the default applications.\n\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = f'/config/flow/applications/active_applications/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of active flow applications.'
        url = '/config/flow/applications/active_applications'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class FlowApplicationsDefaultApplicationsResource(ResourceBase):
    """Operations below ``/config/flow/applications/default_applications``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual default flow application, as specified by an ID.'
        url = f'/config/flow/applications/default_applications/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of default flow applications.'
        url = '/config/flow/applications/default_applications'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class FlowCommonDestinationPortsActiveConfigurationsResource(ResourceBase):
    """Operations below ``/config/flow/common_destination_ports/active_configurations``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new active configuration.'
        url = '/config/flow/common_destination_ports/active_configurations'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Removes the active configuration for the specified ID from the system.'
        url = f'/config/flow/common_destination_ports/active_configurations/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, **kwargs: Any) -> Any:
        'Gets the active configuration for a common destination port, as specified by an ID.'
        url = f'/config/flow/common_destination_ports/active_configurations/{id}'
        return self._s.get(url, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of active configurations for common destination ports.'
        url = '/config/flow/common_destination_ports/active_configurations'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the active configuration for a common destination port, as specified by the ID.'
        url = f'/config/flow/common_destination_ports/active_configurations/{id}'
        return self._s.post(url, json_body=body, **kwargs)


class FlowCommonDestinationPortsDefaultConfigurationsResource(ResourceBase):
    """Operations below ``/config/flow/common_destination_ports/default_configurations``."""

    def get(self, id, **kwargs: Any) -> Any:
        'Gets the default configuration for a common destination port, as specified by an ID.'
        url = f'/config/flow/common_destination_ports/default_configurations/{id}'
        return self._s.get(url, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of default configurations for common destination ports.'
        url = '/config/flow/common_destination_ports/default_configurations'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertiesResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dep: FlowSourcesCustomPropertiesCalculatedPropertiesDepResource = FlowSourcesCustomPropertiesCalculatedPropertiesDepResource(session)
        self.dependents: FlowSourcesCustomPropertiesCalculatedPropertiesDependentsResource = FlowSourcesCustomPropertiesCalculatedPropertiesDependentsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new calculated flow property.'
        url = '/config/flow_sources/custom_properties/calculated_properties'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes the flow calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, calculated_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a calculated flow property based on the supplied calculated property ID.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of calculated flow properties.'
        url = '/config/flow_sources/custom_properties/calculated_properties'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, calculated_property_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing calculated flow property.'
        url = f'/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property/{calculated_property_name}``."""

    def get(self, calculated_property_name, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of flow calculated properties.'
        url = f'/config/flow_sources/custom_properties/calculated_property/{calculated_property_name}'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of the flow calculated property delete task.'
        url = f'/config/flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.disable: FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource = FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksDisableResource(session)
        self.results: FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource = FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of the flow calculated property dependents task.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the flow calculated property dependent task.'
        url = f'/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesCalculatedPropertyOperandsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/calculated_property_operands``."""

    def list(self, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of available options for calculated flow property operand.'
        url = '/config/flow_sources/custom_properties/calculated_property_operands'
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)


class FlowSourcesCustomPropertiesPropertyExpressionsResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/property_expressions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new flow regex property expression.'
        url = '/config/flow_sources/custom_properties/property_expressions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, expression_id, **kwargs: Any) -> Any:
        'Deletes a flow regex property expression based on the supplied expression ID.'
        url = f'/config/flow_sources/custom_properties/property_expressions/{expression_id}'
        return self._s.delete(url, **kwargs)

    def get(self, expression_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a flow regex property expression based on the supplied expression ID.'
        url = f'/config/flow_sources/custom_properties/property_expressions/{expression_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of flow regex property expressions.'
        url = '/config/flow_sources/custom_properties/property_expressions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, expression_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing flow regex property expression.'
        url = f'/config/flow_sources/custom_properties/property_expressions/{expression_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertiesResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: FlowSourcesCustomPropertiesRegexPropertiesDependentsResource = FlowSourcesCustomPropertiesRegexPropertiesDependentsResource(session)
        self.disabling_dependents: FlowSourcesCustomPropertiesRegexPropertiesDisablingDependentsResource = FlowSourcesCustomPropertiesRegexPropertiesDisablingDependentsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new flow regex property.'
        url = '/config/flow_sources/custom_properties/regex_properties'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes a flow regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, regex_property_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a flow regex property based on the supplied regex property ID.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of flow regex properties.'
        url = '/config/flow_sources/custom_properties/regex_properties'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, regex_property_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing flow regex property.'
        url = f'/config/flow_sources/custom_properties/regex_properties/{regex_property_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDeleteTasksResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the flow regex property delete task status.'
        url = f'/config/flow_sources/custom_properties/regex_property_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class FlowSourcesCustomPropertiesRegexPropertyDependentTasksResource(ResourceBase):
    """Operations below ``/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.change_field_type: FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksChangeFieldTypeResource(session)
        self.disable: FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksDisableResource(session)
        self.results: FlowSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the flow regex property dependent task status.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the flow regex property dependent task.'
        url = f'/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesFlowSourceManagementFlowSourcesResource(ResourceBase):
    """Operations below ``/config/flow_sources/flow_source_management/flowSources``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual Flow Source as specified by the ID.'
        url = f'/config/flow_sources/flow_source_management/flowSources/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of flow sources that are available to the current user.'
        url = '/config/flow_sources/flow_source_management/flowSources'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class AccessAuthorizedServicesResource(ResourceBase):
    """Operations below ``/config/access/authorized_services``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        "Creates an authorized service. The response to this API invocation will contain the API token. This will be the only time the token value is available.\nAny user or authorized service can call this endpoint. To create an authorized service with any user role, security profile, or tenant, the caller must have the Administrator Manager permission. Callers who don't have the Administrator Manager permission can only create an authorized service with their own user role, security profile and tenant. An authorized service that is created by a caller who doesn't have the Administrator Manager permission expires no later than the default expiration time, even if the caller enters a later time. The default expiration time is also what is set as the expiration date for the authorized service if the expiration_date is not set in the request. This default expiration time can be configured using the Authentication Settings API found here: /api/system/authorization/settings.\nOnly the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be set when creating an authorized service. All other fields are ignored."
        url = '/config/access/authorized_services'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        "Deletes an authorized service.\nAny user or authorized service can call this endpoint. If the caller has the Administrator Manager permission, then they can delete any authorized service. If the caller does not have the Administrator Manager permission, then they can only delete authorized services that they've created."
        url = f'/config/access/authorized_services/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        "Retrieves an authorized service.  For security reasons, the token field will never be populated in this endpoint.\nTo view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the authorized services that they've created. An authorized service can see itself and other authorized services it created, but the Administrator Manager permission is needed to see the complete list of authorized services."
        url = f'/config/access/authorized_services/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, current_authorized_service: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        "Retrieves a list of authorized services. For security reasons, the token field will never be populated in this endpoint.\nTo view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the list of authorized services that they've created. An authorized service can see itself and other authorized services that it created, but the Administrator Manager permission is needed to see the complete list of authorized services."
        url = '/config/access/authorized_services'
        params = {'current_authorized_service': current_authorized_service}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        "Updates an authorized service. Only the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be updated.\nTo view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the authorized services that they've created. An authorized service can see itself and other authorized services it created, but the Administrator Manager permission is needed to see the complete list of authorized services.\nOnly the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be set when creating an authorized service. All other fields are ignored."
        url = f'/config/access/authorized_services/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AccessSecurityProfilesResource(ResourceBase):
    """Operations below ``/config/access/security_profiles``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a deployed security profile by ID.'
        url = f'/config/access/security_profiles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, tenant_id: Optional[Any]=None, current_security_profile: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the list of deployed security profiles available in the system.'
        url = '/config/access/security_profiles'
        params = {'tenant_id': tenant_id, 'current_security_profile': current_security_profile}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class AccessTenantManagementResource(ResourceBase):
    """Operations below ``/access/tenant_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.tenants: AccessTenantManagementTenantsResource = AccessTenantManagementTenantsResource(session)


class AccessUserDependentTasksResource(ResourceBase):
    """Operations below ``/config/access/user_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: AccessUserDependentTasksResultsResource = AccessUserDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent user task status.'
        url = f'/config/access/user_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels a dependent user task.'
        url = f'/config/access/user_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AccessUserRolesResource(ResourceBase):
    """Operations below ``/config/access/user_roles``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a deployed user role by ID.'
        url = f'/config/access/user_roles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, current_user_role: Optional[Any]=None, contains: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the list of deployed user roles available in the system.'
        url = '/config/access/user_roles'
        params = {'current_user_role': current_user_role, 'contains': contains}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class AccessUsersResource(ResourceBase):
    """Operations below ``/config/access/users``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: AccessUsersDependentsResource = AccessUsersDependentsResource(session)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a deployed user.'
        url = f'/config/access/users/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, current_user: Optional[Any]=None, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve Deployed Users.'
        url = '/config/access/users'
        params = {'current_user': current_user}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a deployed user.'
        url = f'/config/access/users/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class BackupAndRestoreScheduledBackupConfigurationsResource(ResourceBase):
    """Operations below ``/config/backup_and_restore/scheduled_backup_configurations``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a Backup Configuration by ID.'
        url = f'/config/backup_and_restore/scheduled_backup_configurations/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of Backup Configurations.'
        url = '/config/backup_and_restore/scheduled_backup_configurations'
        return self._s.get(url, fields=fields, **kwargs)


class CertificatesComponentsResource(ResourceBase):
    """Operations below ``/config/certificates/components``."""

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of registered components.'
        url = '/config/certificates/components'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class CertificatesEndCertificatesResource(ResourceBase):
    """Operations below ``/config/certificates/end_certificates``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.full_chain: CertificatesEndCertificatesFullChainResource = CertificatesEndCertificatesFullChainResource(session)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets information about a specific deployed certificate, as specified the certificate ID.'
        url = f'/config/certificates/end_certificates/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of deployed certificates.'
        url = '/config/certificates/end_certificates'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class CertificatesRootCertificatesResource(ResourceBase):
    """Operations below ``/config/certificates/root_certificates``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.get_dependant_ids: CertificatesRootCertificatesGetDependantIdsResource = CertificatesRootCertificatesGetDependantIdsResource(session)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets details of a deployed root certificate, as specified by the ID.\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = f'/config/certificates/root_certificates/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of all root certificates that have been uploaded and deployed.\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = '/config/certificates/root_certificates'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class DeploymentHostsResource(ResourceBase):
    """Operations below ``/config/deployment/hosts``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.tunnels: DeploymentHostsTunnelsResource = DeploymentHostsTunnelsResource(session)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a deployed host by ID.'
        url = f'/config/deployment/hosts/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all deployed hosts.'
        url = '/config/deployment/hosts'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a host by ID and sends a JMS message to update the pipeline.'
        url = f'/config/deployment/hosts/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class DeploymentLicensePoolResource(ResourceBase):
    """Operations below ``/config/deployment/license_pool``."""

    def get(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the deployed license pool information.'
        url = '/config/deployment/license_pool'
        return self._s.get(url, fields=fields, **kwargs)


class DomainManagementDomainsResource(ResourceBase):
    """Operations below ``/config/domain_management/domains``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new domain.'
        url = '/config/domain_management/domains'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, domain_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes a domain by domain id.'
        url = f'/config/domain_management/domains/{domain_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, domain_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual domain by ID'
        url = f'/config/domain_management/domains/{domain_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of domains.'
        url = '/config/domain_management/domains'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, domain_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing domain.'
        url = f'/config/domain_management/domains/{domain_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesCustomPropertiesResource(ResourceBase):
    """Operations below ``/event_sources/custom_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.calculated_properties: EventSourcesCustomPropertiesCalculatedPropertiesResource = EventSourcesCustomPropertiesCalculatedPropertiesResource(session)
        self.calculated_property: EventSourcesCustomPropertiesCalculatedPropertyResource = EventSourcesCustomPropertiesCalculatedPropertyResource(session)
        self.calculated_property_delete_tasks: EventSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource = EventSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource(session)
        self.calculated_property_dependent_tasks: EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResource = EventSourcesCustomPropertiesCalculatedPropertyDependentTasksResource(session)
        self.calculated_property_operands: EventSourcesCustomPropertiesCalculatedPropertyOperandsResource = EventSourcesCustomPropertiesCalculatedPropertyOperandsResource(session)
        self.property_aql_expressions: EventSourcesCustomPropertiesPropertyAqlExpressionsResource = EventSourcesCustomPropertiesPropertyAqlExpressionsResource(session)
        self.property_calculated_expressions: EventSourcesCustomPropertiesPropertyCalculatedExpressionsResource = EventSourcesCustomPropertiesPropertyCalculatedExpressionsResource(session)
        self.property_cef_expressions: EventSourcesCustomPropertiesPropertyCefExpressionsResource = EventSourcesCustomPropertiesPropertyCefExpressionsResource(session)
        self.property_expressions: EventSourcesCustomPropertiesPropertyExpressionsResource = EventSourcesCustomPropertiesPropertyExpressionsResource(session)
        self.property_genericlist_expressions: EventSourcesCustomPropertiesPropertyGenericlistExpressionsResource = EventSourcesCustomPropertiesPropertyGenericlistExpressionsResource(session)
        self.property_json_expressions: EventSourcesCustomPropertiesPropertyJsonExpressionsResource = EventSourcesCustomPropertiesPropertyJsonExpressionsResource(session)
        self.property_leef_expressions: EventSourcesCustomPropertiesPropertyLeefExpressionsResource = EventSourcesCustomPropertiesPropertyLeefExpressionsResource(session)
        self.property_nvp_expressions: EventSourcesCustomPropertiesPropertyNvpExpressionsResource = EventSourcesCustomPropertiesPropertyNvpExpressionsResource(session)
        self.property_xml_expressions: EventSourcesCustomPropertiesPropertyXmlExpressionsResource = EventSourcesCustomPropertiesPropertyXmlExpressionsResource(session)
        self.regex_properties: EventSourcesCustomPropertiesRegexPropertiesResource = EventSourcesCustomPropertiesRegexPropertiesResource(session)
        self.regex_property_delete_tasks: EventSourcesCustomPropertiesRegexPropertyDeleteTasksResource = EventSourcesCustomPropertiesRegexPropertyDeleteTasksResource(session)
        self.regex_property_dependent_tasks: EventSourcesCustomPropertiesRegexPropertyDependentTasksResource = EventSourcesCustomPropertiesRegexPropertyDependentTasksResource(session)


class EventSourcesDisconnectedLogCollectorsResource(ResourceBase):
    """Operations below ``/config/event_sources/disconnected_log_collectors``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new disconnected log collector. A disconnected log collector contains the\nfollowing fields:'
        url = '/config/event_sources/disconnected_log_collectors'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a Disconnected Log Collector by ID.'
        url = f'/config/event_sources/disconnected_log_collectors/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, **kwargs: Any) -> Any:
        'Retrieves an disconnected log collector by ID..'
        url = '/config/event_sources/disconnected_log_collectors/{id}'
        return self._s.get(url, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        'Retrieves a list of disconnected log collectors.'
        url = '/config/event_sources/disconnected_log_collectors'
        return self._s.get(url, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a disconnected log collector by ID. A disconnected log collector contains the\nfollowing fields:'
        url = f'/config/event_sources/disconnected_log_collectors/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesEventCollectorsResource(ResourceBase):
    """Operations below ``/config/event_sources/event_collectors``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an event collector by ID..'
        url = f'/config/event_sources/event_collectors/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of event collectors..'
        url = '/config/event_sources/event_collectors'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class EventSourcesGeneratedRegexesResource(ResourceBase):
    """Operations below ``/config/event_sources/generated_regexes``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a regex pattern'
        url = '/config/event_sources/generated_regexes'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesLogSourceManagementResource(ResourceBase):
    """Operations below ``/event_sources/log_source_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.autodetection: EventSourcesLogSourceManagementAutodetectionResource = EventSourcesLogSourceManagementAutodetectionResource(session)
        self.log_source_bulk_tasks: EventSourcesLogSourceManagementLogSourceBulkTasksResource = EventSourcesLogSourceManagementLogSourceBulkTasksResource(session)
        self.log_source_extensions: EventSourcesLogSourceManagementLogSourceExtensionsResource = EventSourcesLogSourceManagementLogSourceExtensionsResource(session)
        self.log_source_groups: EventSourcesLogSourceManagementLogSourceGroupsResource = EventSourcesLogSourceManagementLogSourceGroupsResource(session)
        self.log_source_languages: EventSourcesLogSourceManagementLogSourceLanguagesResource = EventSourcesLogSourceManagementLogSourceLanguagesResource(session)
        self.log_source_statistics: EventSourcesLogSourceManagementLogSourceStatisticsResource = EventSourcesLogSourceManagementLogSourceStatisticsResource(session)
        self.log_source_types: EventSourcesLogSourceManagementLogSourceTypesResource = EventSourcesLogSourceManagementLogSourceTypesResource(session)
        self.log_sources: EventSourcesLogSourceManagementLogSourcesResource = EventSourcesLogSourceManagementLogSourcesResource(session)
        self.protocol_types: EventSourcesLogSourceManagementProtocolTypesResource = EventSourcesLogSourceManagementProtocolTypesResource(session)


class EventSourcesPropertyDiscoveryProfilesResource(ResourceBase):
    """Operations below ``/config/event_sources/property_discovery_profiles``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile JSON object.'
        url = '/config/event_sources/property_discovery_profiles'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes the specified PropertyDiscoveryProfile.'
        url = f'/config/event_sources/property_discovery_profiles/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile corresponding to the supplied ID.'
        url = f'/config/event_sources/property_discovery_profiles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets all PropertyDiscoveryProfiles currently in the system.'
        url = '/config/event_sources/property_discovery_profiles'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a PropertyDiscoveryProfile based on the information supplied via the property_discovery_profile JSON object.'
        url = f'/config/event_sources/property_discovery_profiles/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesWincollectResource(ResourceBase):
    """Operations below ``/event_sources/wincollect``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.wincollect_agents: EventSourcesWincollectWincollectAgentsResource = EventSourcesWincollectWincollectAgentsResource(session)
        self.wincollect_destinations: EventSourcesWincollectWincollectDestinationsResource = EventSourcesWincollectWincollectDestinationsResource(session)


class ExtensionManagementExtensionExportTasksResource(ResourceBase):
    """Operations below ``/config/extension_management/extension_export_tasks``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.extension_export: ExtensionManagementExtensionExportTasksExtensionExportResource = ExtensionManagementExtensionExportTasksExtensionExportResource(session)
        self.results: ExtensionManagementExtensionExportTasksResultsResource = ExtensionManagementExtensionExportTasksResultsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Exports an extension.'
        url = '/config/extension_management/extension_export_tasks'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the tasks status based on the task_id.'
        url = f'/config/extension_management/extension_export_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class ExtensionManagementExtensionsResource(ResourceBase):
    """Operations below ``/config/extension_management/extensions``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.metadata: ExtensionManagementExtensionsMetadataResource = ExtensionManagementExtensionsMetadataResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Uploads the supplied extension file to the QRadar system.'
        url = '/config/extension_management/extensions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, extension_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Uninstall an extension based on the supplied extension_id. This is an asynchronous action.'
        url = f'/config/extension_management/extensions/{extension_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.delete(url, headers=headers, json_body=body, **kwargs)

    def get(self, extension_id, content_limit: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an extension based on the supplied extension_id.'
        url = f'/config/extension_management/extensions/{extension_id}'
        params = {'content_limit': content_limit}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)

    def list(self, content_limit: Optional[Any]=None, sort: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of extensions.'
        url = '/config/extension_management/extensions'
        params = {'content_limit': content_limit}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, extension_id, action_type: Optional[Any]=None, overwrite: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Install an extension based on the supplied extension_id. This is an asynchronous action.'
        url = f'/config/extension_management/extensions/{extension_id}'
        params = {'action_type': action_type, 'overwrite': overwrite}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class ExtensionManagementExtensionsTaskStatusResource(ResourceBase):
    """Operations below ``/config/extension_management/extensions_task_status/{status_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: ExtensionManagementExtensionsTaskStatusResultsResource = ExtensionManagementExtensionsTaskStatusResultsResource(session)

    def get(self, status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the tasks status based on the status_id.'
        url = f'/config/extension_management/extensions_task_status/{status_id}'
        return self._s.get(url, fields=fields, **kwargs)


class FlowApplicationsResource(ResourceBase):
    """Operations below ``/flow/applications``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.active_applications: FlowApplicationsActiveApplicationsResource = FlowApplicationsActiveApplicationsResource(session)
        self.default_applications: FlowApplicationsDefaultApplicationsResource = FlowApplicationsDefaultApplicationsResource(session)


class FlowCommonDestinationPortsResource(ResourceBase):
    """Operations below ``/flow/common_destination_ports``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.active_configurations: FlowCommonDestinationPortsActiveConfigurationsResource = FlowCommonDestinationPortsActiveConfigurationsResource(session)
        self.default_configurations: FlowCommonDestinationPortsDefaultConfigurationsResource = FlowCommonDestinationPortsDefaultConfigurationsResource(session)


class FlowSourcesCustomPropertiesResource(ResourceBase):
    """Operations below ``/flow_sources/custom_properties``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.calculated_properties: FlowSourcesCustomPropertiesCalculatedPropertiesResource = FlowSourcesCustomPropertiesCalculatedPropertiesResource(session)
        self.calculated_property: FlowSourcesCustomPropertiesCalculatedPropertyResource = FlowSourcesCustomPropertiesCalculatedPropertyResource(session)
        self.calculated_property_delete_tasks: FlowSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource = FlowSourcesCustomPropertiesCalculatedPropertyDeleteTasksResource(session)
        self.calculated_property_dependent_tasks: FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResource = FlowSourcesCustomPropertiesCalculatedPropertyDependentTasksResource(session)
        self.calculated_property_operands: FlowSourcesCustomPropertiesCalculatedPropertyOperandsResource = FlowSourcesCustomPropertiesCalculatedPropertyOperandsResource(session)
        self.property_expressions: FlowSourcesCustomPropertiesPropertyExpressionsResource = FlowSourcesCustomPropertiesPropertyExpressionsResource(session)
        self.regex_properties: FlowSourcesCustomPropertiesRegexPropertiesResource = FlowSourcesCustomPropertiesRegexPropertiesResource(session)
        self.regex_property_delete_tasks: FlowSourcesCustomPropertiesRegexPropertyDeleteTasksResource = FlowSourcesCustomPropertiesRegexPropertyDeleteTasksResource(session)
        self.regex_property_dependent_tasks: FlowSourcesCustomPropertiesRegexPropertyDependentTasksResource = FlowSourcesCustomPropertiesRegexPropertyDependentTasksResource(session)


class FlowSourcesFlowSourceManagementResource(ResourceBase):
    """Operations below ``/flow_sources/flow_source_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.flowSources: FlowSourcesFlowSourceManagementFlowSourcesResource = FlowSourcesFlowSourceManagementFlowSourcesResource(session)


class NetworkHierarchyNetworksResource(ResourceBase):
    """Operations below ``/config/network_hierarchy/networks``."""

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the deployed network hierarchy.'
        url = '/config/network_hierarchy/networks'
        return self._s.get(url, fields=fields, **kwargs)


class NetworkHierarchyStagedNetworksResource(ResourceBase):
    """Operations below ``/config/network_hierarchy/staged_networks``."""

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the staged network hierarchy.'
        url = '/config/network_hierarchy/staged_networks'
        return self._s.get(url, fields=fields, **kwargs)

    def replace(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Replaces the current network hierarchy with the input that is provided.'
        url = '/config/network_hierarchy/staged_networks'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)


class ResilientTestResource(ResourceBase):
    """Operations below ``/config/resilient/test``."""

    def create(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Perform asynchronous test Resilient connection'
        url = '/config/resilient/test'
        return self._s.post(url, fields=fields, **kwargs)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the test Resilient connection task status\nYou must have the System Administrator or Security Admin permission (ADMIN | SAASADMIN capability) to use this endpoint.'
        url = f'/config/resilient/test/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Test the Resilient connection by using the connection ID.\nYou must have the System Administrator or Security Admin permission (ADMIN | SAASADMIN capability) to use this endpoint.'
        url = f'/config/resilient/test/{id}'
        return self._s.post(url, fields=fields, **kwargs)


class StoreAndForwardPoliciesResource(ResourceBase):
    """Operations below ``/config/store_and_forward/policies``."""

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a store and forward policy.'
        url = f'/config/store_and_forward/policies/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a store and forward policy.'
        url = f'/config/store_and_forward/policies/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of store and forward policies.'
        url = '/config/store_and_forward/policies'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the store and forward policy owner only.'
        url = f'/config/store_and_forward/policies/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AccessResource(ResourceBase):
    """Operations below ``/access``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.authorized_services: AccessAuthorizedServicesResource = AccessAuthorizedServicesResource(session)
        self.security_profiles: AccessSecurityProfilesResource = AccessSecurityProfilesResource(session)
        self.tenant_management: AccessTenantManagementResource = AccessTenantManagementResource(session)
        self.user_dependent_tasks: AccessUserDependentTasksResource = AccessUserDependentTasksResource(session)
        self.user_roles: AccessUserRolesResource = AccessUserRolesResource(session)
        self.users: AccessUsersResource = AccessUsersResource(session)


class BackupAndRestoreResource(ResourceBase):
    """Operations below ``/backup_and_restore``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.scheduled_backup_configurations: BackupAndRestoreScheduledBackupConfigurationsResource = BackupAndRestoreScheduledBackupConfigurationsResource(session)


class CertificatesResource(ResourceBase):
    """Operations below ``/certificates``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.components: CertificatesComponentsResource = CertificatesComponentsResource(session)
        self.end_certificates: CertificatesEndCertificatesResource = CertificatesEndCertificatesResource(session)
        self.root_certificates: CertificatesRootCertificatesResource = CertificatesRootCertificatesResource(session)


class DeploymentResource(ResourceBase):
    """Operations below ``/deployment``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.hosts: DeploymentHostsResource = DeploymentHostsResource(session)
        self.license_pool: DeploymentLicensePoolResource = DeploymentLicensePoolResource(session)


class DomainManagementResource(ResourceBase):
    """Operations below ``/domain_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.domains: DomainManagementDomainsResource = DomainManagementDomainsResource(session)


class EventRetentionBucketsResource(ResourceBase):
    """Operations below ``/config/event_retention_buckets``."""

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes an event retention bucket.'
        url = f'/config/event_retention_buckets/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an event retention bucket.'
        url = f'/config/event_retention_buckets/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of event retention buckets.'
        url = '/config/event_retention_buckets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the event retention bucket owner or enabled/disabled only.'
        url = f'/config/event_retention_buckets/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EventSourcesResource(ResourceBase):
    """Operations below ``/event_sources``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.custom_properties: EventSourcesCustomPropertiesResource = EventSourcesCustomPropertiesResource(session)
        self.disconnected_log_collectors: EventSourcesDisconnectedLogCollectorsResource = EventSourcesDisconnectedLogCollectorsResource(session)
        self.event_collectors: EventSourcesEventCollectorsResource = EventSourcesEventCollectorsResource(session)
        self.generated_regexes: EventSourcesGeneratedRegexesResource = EventSourcesGeneratedRegexesResource(session)
        self.log_source_management: EventSourcesLogSourceManagementResource = EventSourcesLogSourceManagementResource(session)
        self.property_discovery_profiles: EventSourcesPropertyDiscoveryProfilesResource = EventSourcesPropertyDiscoveryProfilesResource(session)
        self.wincollect: EventSourcesWincollectResource = EventSourcesWincollectResource(session)


class ExtensionManagementResource(ResourceBase):
    """Operations below ``/extension_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.extension_export_tasks: ExtensionManagementExtensionExportTasksResource = ExtensionManagementExtensionExportTasksResource(session)
        self.extensions: ExtensionManagementExtensionsResource = ExtensionManagementExtensionsResource(session)
        self.extensions_task_status: ExtensionManagementExtensionsTaskStatusResource = ExtensionManagementExtensionsTaskStatusResource(session)


class FlowResource(ResourceBase):
    """Operations below ``/flow``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.applications: FlowApplicationsResource = FlowApplicationsResource(session)
        self.common_destination_ports: FlowCommonDestinationPortsResource = FlowCommonDestinationPortsResource(session)


class FlowRetentionBucketsResource(ResourceBase):
    """Operations below ``/config/flow_retention_buckets``."""

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a flow retention bucket.'
        url = f'/config/flow_retention_buckets/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a flow retention bucket.'
        url = f'/config/flow_retention_buckets/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of flow retention buckets.'
        url = '/config/flow_retention_buckets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the flow retention bucket owner, or enabled/disabled only.'
        url = f'/config/flow_retention_buckets/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSourcesResource(ResourceBase):
    """Operations below ``/flow_sources``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.custom_properties: FlowSourcesCustomPropertiesResource = FlowSourcesCustomPropertiesResource(session)
        self.flow_source_management: FlowSourcesFlowSourceManagementResource = FlowSourcesFlowSourceManagementResource(session)


class NetworkHierarchyResource(ResourceBase):
    """Operations below ``/network_hierarchy``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.networks: NetworkHierarchyNetworksResource = NetworkHierarchyNetworksResource(session)
        self.staged_networks: NetworkHierarchyStagedNetworksResource = NetworkHierarchyStagedNetworksResource(session)


class RemoteNetworksResource(ResourceBase):
    """Operations below ``/config/remote_networks``."""

    def get(self, network_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a deployed remote network by ID.'
        url = f'/config/remote_networks/{network_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of deployed remote networks.'
        url = '/config/remote_networks'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class RemoteServicesResource(ResourceBase):
    """Operations below ``/config/remote_services``."""

    def get(self, service_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a deployed remote service by ID.'
        url = f'/config/remote_services/{service_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of deployed remote services.'
        url = '/config/remote_services'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class ResilientResource(ResourceBase):
    """Operations below ``/resilient``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.test: ResilientTestResource = ResilientTestResource(session)


class ResourceRestrictionsResource(ResourceBase):
    """Operations below ``/config/resource_restrictions``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new resource restriction.'
        url = '/config/resource_restrictions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, resource_restriction_id, **kwargs: Any) -> Any:
        'Deletes a resource restriction consumer by ID.'
        url = f'/config/resource_restrictions/{resource_restriction_id}'
        return self._s.delete(url, **kwargs)

    def get(self, resource_restriction_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a resource restriction consumer by ID.'
        url = f'/config/resource_restrictions/{resource_restriction_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all resource restrictions.'
        url = '/config/resource_restrictions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def replace(self, resource_restriction_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a resource restriction consumer by ID.'
        url = f'/config/resource_restrictions/{resource_restriction_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)


class StoreAndForwardResource(ResourceBase):
    """Operations below ``/store_and_forward``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.policies: StoreAndForwardPoliciesResource = StoreAndForwardPoliciesResource(session)


class ConfigAPI(ResourceBase):
    """Resource-oriented client for the ``config`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.access: AccessResource = AccessResource(session)
        self.backup_and_restore: BackupAndRestoreResource = BackupAndRestoreResource(session)
        self.certificates: CertificatesResource = CertificatesResource(session)
        self.deployment: DeploymentResource = DeploymentResource(session)
        self.domain_management: DomainManagementResource = DomainManagementResource(session)
        self.event_retention_buckets: EventRetentionBucketsResource = EventRetentionBucketsResource(session)
        self.event_sources: EventSourcesResource = EventSourcesResource(session)
        self.extension_management: ExtensionManagementResource = ExtensionManagementResource(session)
        self.flow: FlowResource = FlowResource(session)
        self.flow_retention_buckets: FlowRetentionBucketsResource = FlowRetentionBucketsResource(session)
        self.flow_sources: FlowSourcesResource = FlowSourcesResource(session)
        self.network_hierarchy: NetworkHierarchyResource = NetworkHierarchyResource(session)
        self.remote_networks: RemoteNetworksResource = RemoteNetworksResource(session)
        self.remote_services: RemoteServicesResource = RemoteServicesResource(session)
        self.resilient: ResilientResource = ResilientResource(session)
        self.resource_restrictions: ResourceRestrictionsResource = ResourceRestrictionsResource(session)
        self.store_and_forward: StoreAndForwardResource = StoreAndForwardResource(session)
