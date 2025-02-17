import os

from metric_providers.base import BaseMetricProvider

class NetworkIoCgroupContainerProvider(BaseMetricProvider):
    def __init__(self, resolution, rootless=False):
        super().__init__(
            metric_name='network_io_cgroup_container',
            metrics={'time': int, 'value': int, 'container_id': str},
            resolution=resolution,
            unit='Bytes',
            current_dir=os.path.dirname(os.path.abspath(__file__)),
        )
        self._rootless = rootless
