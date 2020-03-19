# Copyright (c) 2020 Slavfox
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
snecs - the straightforward, nimble ECS for Python.

Remind me to stick a proper docstring here.
"""
from snecs.component import Component, RegisteredComponent, register_component
from snecs.ecs import (
    add_component,
    add_components,
    delete_entity,
    delete_entity_immediately,
    deserialize_world,
    entity_component,
    entity_components,
    has_component,
    has_components,
    process_pending_deletions,
    remove_component,
    serialize_world,
)
from snecs.world import World

__all__ = [
    "World",
    "Component",
    "RegisteredComponent",
    "register_component",
    # Functions to interact with the actual ECS
    "add_component",
    "add_components",
    "entity_component",
    "entity_components",
    "has_component",
    "has_components",
    "remove_component",
    "delete_entity",
    "delete_entity_immediately",
    "process_pending_deletions",
    "serialize_world",
    "deserialize_world",
]

__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
