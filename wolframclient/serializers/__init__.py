# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.serializers.serializable import WLSerializable
from wolframclient.utils.importutils import API

__all__ = ['export', 'WLSerializable']

DEFAULT_FORMAT = 'wl'

available_formats = API(
    wl  = 'wolframclient.serializers.wl.WLSerializer',
    wxf = 'wolframclient.serializers.wxf.WXFSerializer',
)

def export(data, stream=None, target_format=DEFAULT_FORMAT, **options):
    """Serialize input `data` to a target format.

    An output stream can be provided, in which case the output bytes are written to it.
    Input `data` must be serializable, i.e extends :class:`WLSerializable <wolframclient.serializers.serializable.WLSerializable>`,
    or be one of the native Python types supported directly including: :class:`list`, :class:`dict`, etc::

        >>> export(wl.Range(3))
        'Range[3]'

    """
    if not target_format in available_formats:
        raise ValueError('Invalid export format %s. Choices are: %s' % (
            target_format,
            ', '.join(available_formats.keys())
        ))
    return available_formats[target_format](**options).export(data, stream=stream)
