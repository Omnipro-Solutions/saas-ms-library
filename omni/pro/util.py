import pkg_resources
from omni_pro_base.util import *

logger = logging.getLogger(__name__)


def libraries_versions_installed():
    """
    Returns a dictionary with the installed versions of the libraries.
    """
    libraries = ["omni-pro", "omni-pro-base", "omni-pro-redis", "omni-pro-grpc"]
    versions = {}
    for library in libraries:
        try:
            version = pkg_resources.get_distribution(library).version
            versions[library.replace("-", "_")] = version
        except pkg_resources.DistributionNotFound:
            versions[library.replace("-", "_")] = "Not installed"
    return versions
