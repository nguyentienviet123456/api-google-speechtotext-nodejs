# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The main command group for cloud dataproc."""

from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.core import properties


# TODO(b/62883827): Move this into the docstring along with other places
# where this pattern currently occurs.
DETAILED_HELP = {
    'DESCRIPTION': """\
        The gcloud dataproc command group lets you create and manage Google
        Cloud Dataproc clusters and jobs.

        Cloud Dataproc is an Apache Hadoop, Apache Spark, Apache Pig, and Apache
        Hive service. It easily processes big datasets at low cost, creating
        managed clusters of any size that scale down once processing is
        complete.

        More information on Cloud Dataproc can be found here:
        https://cloud.google.com/dataproc and detailed documentation can be
        found here: https://cloud.google.com/dataproc/docs/

        ## EXAMPLES

        To see how to create and manage clusters, run:

            $ {command} clusters

        To see how to submit and manage jobs, run:

            $ {command} jobs
        """,
}


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.GA)
class Dataproc(base.Group):
  """Create and manage Google Cloud Dataproc clusters and jobs."""
  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    region_prop = properties.VALUES.dataproc.region
    parser.add_argument(
        '--region',
        help=region_prop.help_text,
        # Don't set default, because it would override users' property setting.
        action=actions.StoreProperty(region_prop))
