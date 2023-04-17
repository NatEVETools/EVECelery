"""
Task directory module for adding task objects as attributes to a namespace for easy access and code inspection.

This module was automatically generated from Jinja templates with the codegen tool included in the root of this repo.
You should not directly modify this module but instead modify the template 'codegen/Templates/TaskDirectory.py'.
"""

from .get_characters_character_id_attributes import (
    get_characters_character_id_attributes,
)


class TaskDirectory(object):
    """
    Directory for quickly finding tasks with easy access to documentation and code inspection

    This task directory contains all tasks as attributes that are categorized with 'Skills'.
    """

    @property
    def get_characters_character_id_attributes(
        self,
    ) -> get_characters_character_id_attributes:
        """
        Get character attributes


        Reference the docstrings for :func:`~EVECelery.tasks.ESI.Skills.get_characters_character_id_attributes.get_characters_character_id_attributes.get_sync`,
        :func:`~EVECelery.tasks.ESI.Skills.get_characters_character_id_attributes.get_characters_character_id_attributes.run`, and
        :class:`~EVECelery.tasks.ESI.Skills.get_characters_character_id_attributes.get_characters_character_id_attributes`
        for usage of this task, the required parameters, and additional information.


        :return: The Celery task
        """
        return get_characters_character_id_attributes()
