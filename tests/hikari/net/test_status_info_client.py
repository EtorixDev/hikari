#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
import datetime
from unittest import mock

import pytest

from hikari.net import status_info_client
from tests.hikari import _helpers


@pytest.fixture
def active_scheduled_maintenances_pl(page_pl):
    return {
        "page": page_pl,
        "scheduled_maintenances": [],
    }


@pytest.fixture
def component_pl():
    return {
        "id": "rhznvxg4v7yh",
        "name": "API",
        "status": "operational",
        "created_at": "2015-07-30T18:55:43.739-07:00",
        "updated_at": "2019-05-31T15:49:13.651-07:00",
        "position": 1,
        "description": None,
        "showcase": True,
        "group_id": None,
        "page_id": "srhpyqt94yxb",
        "group": False,
        "only_show_if_degraded": False,
    }


@pytest.fixture
def components_pl(component_pl, page_pl):
    return {
        "page": page_pl,
        "components": [
            component_pl,
            {
                "id": "0cwvg0jp5cbg",
                "name": "EU West",
                "status": "operational",
                "created_at": "2015-07-30T20:36:41.891-07:00",
                "updated_at": "2018-07-17T13:00:35.378-07:00",
                "position": 1,
                "description": None,
                "showcase": False,
                "group_id": "jk03xttfcz9b",
                "page_id": "srhpyqt94yxb",
                "group": False,
                "only_show_if_degraded": False,
            },
            {
                "id": "jk03xttfcz9b",
                "name": "Voice",
                "status": "operational",
                "created_at": "2015-07-30T20:39:36.003-07:00",
                "updated_at": "2017-09-29T06:48:54.042-07:00",
                "position": 5,
                "description": None,
                "showcase": False,
                "group_id": None,
                "page_id": "srhpyqt94yxb",
                "group": True,
                "only_show_if_degraded": False,
                "components": [
                    "0cwvg0jp5cbg",
                    "fc8y53dfg85y",
                    "q0lbnfc59j35",
                    "qbt7ryjc5tcd",
                    "nhlpbmmcffcl",
                    "kdz8bp5dp08v",
                    "gmppldfdghcd",
                    "334vzyzzwlfs",
                    "sg02vq1rbfrr",
                    "0ysw0jy8hnsr",
                    "ccgfj3l84lvt",
                    "xggnf9hnngkt",
                    "b5v9r9bdppvm",
                ],
            },
        ],
    }


@pytest.fixture
def incidents_pl(page_pl, incident_pl):
    return {
        "page": page_pl,
        "incidents": [incident_pl],
    }


@pytest.fixture
def incident_pl(incident_update_pl):
    return {
        "id": "2gztsrksff0v",
        "name": "Global Unavailability",
        "status": "investigating",
        "created_at": "2019-06-24T05:25:57.666-07:00",
        "updated_at": "2019-06-24T06:07:14.465-07:00",
        "monitoring_at": None,
        "resolved_at": None,
        "impact": "none",
        "shortlink": "http://stspg.io/15e073752",
        "started_at": "2019-06-24T05:25:57.659-07:00",
        "page_id": "srhpyqt94yxb",
        "incident_updates": [
            incident_update_pl,
            {
                "id": "jvrfncktc4yp",
                "status": "investigating",
                "body": "Discord is affected by the general internet outage. Hang tight.  Pet your cats.",
                "incident_id": "2gztsrksff0v",
                "created_at": "2019-06-24T05:25:57.698-07:00",
                "updated_at": "2019-06-24T05:25:57.698-07:00",
                "display_at": "2019-06-24T05:25:57.698-07:00",
                "affected_components": None,
                "deliver_notifications": False,
                "custom_tweet": None,
                "tweet_id": None,
            },
        ],
        "components": [],
    }


@pytest.fixture
def page_pl():
    return {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "http://status.discordapp.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2019-06-24T06:07:14.473-07:00",
    }


@pytest.fixture
def scheduled_maintenances_pl(page_pl, scheduled_maintenance_pl):
    return {
        "page": page_pl,
        "scheduled_maintenances": [scheduled_maintenance_pl],
    }


@pytest.fixture
def scheduled_maintenance_pl(incident_update_pl):
    return {
        "id": "ymm0202y77k6",
        "name": "Potentially Disruptive Upgrade",
        "status": "completed",
        "created_at": "2016-10-16T16:57:33.416-07:00",
        "updated_at": "2016-10-19T02:39:00.299-07:00",
        "monitoring_at": None,
        "resolved_at": "2016-10-19T02:39:00.274-07:00",
        "impact": "maintenance",
        "shortlink": "http://stspg.io/4ERc",
        "started_at": "2016-10-16T16:57:00.000-07:00",
        "page_id": "srhpyqt94yxb",
        "incident_updates": [
            incident_update_pl,
            {
                "id": "jd5jjsflj0x5",
                "status": "in_progress",
                "body": "This maintenance is currently in progress.",
                "incident_id": "ymm0202y77k6",
                "created_at": "2016-10-19T02:07:00.712-07:00",
                "updated_at": "2016-10-19T02:07:00.712-07:00",
                "display_at": "2016-10-19T02:07:00.712-07:00",
                "affected_components": [{"name": "No components were affected by this update."}],
                "deliver_notifications": True,
                "custom_tweet": None,
                "tweet_id": None,
            },
            {
                "id": "vw800012grtl",
                "status": "scheduled",
                "body": "On September 23rd we attempted to release a code upgrade that involved "
                "some of our real-time servers that we upgrade without disruption using "
                'a method called "handoffs." After over a year of working fine, Discord\'s '
                "growth revealed flaws in the handoff implementation at our current scale. "
                "We have implemented changes in the handoff system and will attempt to do a "
                "code upgrade without disruption, but if something goes wrong we might have "
                "to force everyone to reconnect which can cause up to 30 minutes of disruption.",
                "incident_id": "ymm0202y77k6",
                "created_at": "2016-10-16T16:57:33.923-07:00",
                "updated_at": "2016-10-16T16:59:23.526-07:00",
                "display_at": "2016-10-16T16:57:00.000-07:00",
                "affected_components": [{"name": "No components were affected by this update."}],
                "deliver_notifications": True,
                "custom_tweet": None,
                "tweet_id": None,
            },
        ],
        "components": [],
        "scheduled_for": "2016-10-19T02:00:00.000-07:00",
        "scheduled_until": "2016-10-19T03:00:00.000-07:00",
    }


@pytest.fixture
def subscription_pl(subscriber_pl):
    return {"subscriber": subscriber_pl}


@pytest.fixture
def subscriber_pl():
    return {
        "created_at": "2019-06-24T07:29:43.684-07:00",
        "skip_confirmation_notification": False,
        "quarantined_at": None,
        "id": "82kp04j58dhm",
        "mode": "email",
        "purge_at": None,
        "email": "xxx@yyy.com",
    }


@pytest.fixture
def summary_pl(page_pl):
    return {
        "page": page_pl,
        "components": [
            {
                "id": "rhznvxg4v7yh",
                "name": "API",
                "status": "operational",
                "created_at": "2015-07-30T18:55:43.739-07:00",
                "updated_at": "2019-05-31T15:49:13.651-07:00",
                "position": 1,
                "description": None,
                "showcase": True,
                "group_id": None,
                "page_id": "srhpyqt94yxb",
                "group": False,
                "only_show_if_degraded": False,
            },
            {
                "id": "0cwvg0jp5cbg",
                "name": "EU West",
                "status": "operational",
                "created_at": "2015-07-30T20:36:41.891-07:00",
                "updated_at": "2018-07-17T13:00:35.378-07:00",
                "position": 1,
                "description": None,
                "showcase": False,
                "group_id": "jk03xttfcz9b",
                "page_id": "srhpyqt94yxb",
                "group": False,
                "only_show_if_degraded": False,
            },
            {
                "id": "fc8y53dfg85y",
                "name": "EU Central",
                "status": "operational",
                "created_at": "2015-12-10T23:45:29.114-08:00",
                "updated_at": "2018-12-03T09:58:22.515-08:00",
                "position": 2,
                "description": None,
                "showcase": False,
                "group_id": "jk03xttfcz9b",
                "page_id": "srhpyqt94yxb",
                "group": False,
                "only_show_if_degraded": False,
            },
        ],
    }


@pytest.fixture
def incident_update_pl():
    return {
        "id": "xxqwgv42dnx5",
        "status": "investigating",
        "body": "We are working on resolving some internal technical problems now.",
        "incident_id": "2gztsrksff0v",
        "created_at": "2019-06-24T06:07:14.463-07:00",
        "updated_at": "2019-06-24T06:07:14.463-07:00",
        "display_at": "2019-06-24T06:07:14.463-07:00",
        "affected_components": None,
        "deliver_notifications": False,
        "custom_tweet": None,
        "tweet_id": None,
    }


@pytest.fixture
def unresolved_pl(page_pl, incident_update_pl):
    return {
        "page": page_pl,
        "incidents": [
            {
                "id": "2gztsrksff0v",
                "name": "Global Unavailability",
                "status": "investigating",
                "created_at": "2019-06-24T05:25:57.666-07:00",
                "updated_at": "2019-06-24T06:07:14.465-07:00",
                "monitoring_at": None,
                "resolved_at": None,
                "impact": "none",
                "shortlink": "http://stspg.io/15e073752",
                "started_at": "2019-06-24T05:25:57.659-07:00",
                "page_id": "srhpyqt94yxb",
                "incident_updates": [
                    incident_update_pl,
                    {
                        "id": "jvrfncktc4yp",
                        "status": "investigating",
                        "body": "Discord is affected by the general internet outage. Hang tight.  Pet your cats.",
                        "incident_id": "2gztsrksff0v",
                        "created_at": "2019-06-24T05:25:57.698-07:00",
                        "updated_at": "2019-06-24T05:25:57.698-07:00",
                        "display_at": "2019-06-24T05:25:57.698-07:00",
                        "affected_components": None,
                        "deliver_notifications": False,
                        "custom_tweet": None,
                        "tweet_id": None,
                    },
                ],
                "components": [],
            }
        ],
    }


@pytest.fixture
def upcoming_scheduled_maintenances_pl(page_pl):
    return {
        "page": page_pl,
        "scheduled_maintenances": [],
    }


@pytest.fixture
def status_pl():
    return {"indicator": "none", "description": "All Systems Operational"}


@pytest.fixture
def overall_status_pl(status_pl):
    return {
        "page": {
            "id": "srhpyqt94yxb",
            "name": "Discord",
            "url": "http://status.discordapp.com",
            "time_zone": "America/Tijuana",
            "updated_at": "2019-06-24T06:07:14.473-07:00",
        },
        "status": status_pl,
    }


def date_time(*args):
    return datetime.datetime(*args, tzinfo=datetime.timezone(datetime.timedelta(hours=-7)))


def test_Subscriber_from_dict(subscription_pl):
    subscriber_obj = status_info_client.Subscriber.from_dict(subscription_pl)

    assert subscriber_obj.id == "82kp04j58dhm"
    assert subscriber_obj.mode == "email"
    assert subscriber_obj.is_skipped_confirmation_notification is False
    assert subscriber_obj.quarantined_at is None
    assert subscriber_obj.purge_at is None
    assert subscriber_obj.email == "xxx@yyy.com"
    assert subscriber_obj.created_at == date_time(2019, 6, 24, 7, 29, 43, 684000)


def test_Subscription_from_dict(subscription_pl):
    subscription_obj = status_info_client.Subscriber.from_dict(subscription_pl)
    assert isinstance(subscription_obj, status_info_client.Subscriber)


def test_Page_from_dict(page_pl):
    page_obj = status_info_client.Page.from_dict(page_pl)
    assert page_obj.id == "srhpyqt94yxb"
    assert page_obj.name == "Discord"
    assert page_obj.url == "http://status.discordapp.com"
    assert page_obj.updated_at == date_time(2019, 6, 24, 6, 7, 14, 473000)


def test_Status_from_dict(status_pl):
    status_obj = status_info_client.Status.from_dict(status_pl)

    assert status_obj.description == "All Systems Operational"
    assert status_obj.indicator == "none"


def test_Component_from_dict(component_pl):
    component_obj = status_info_client.Component.from_dict(component_pl)

    assert component_obj.id == "rhznvxg4v7yh"
    assert component_obj.name == "API"
    assert component_obj.status == "operational"
    assert component_obj.created_at == date_time(2015, 7, 30, 18, 55, 43, 739000)
    assert component_obj.updated_at == date_time(2019, 5, 31, 15, 49, 13, 651000)
    assert component_obj.page_id == "srhpyqt94yxb"
    assert component_obj.position == 1
    assert component_obj.description is None


def test_Components_from_dict(components_pl):
    components_obj = status_info_client.ComponentsPage.from_dict(components_pl)

    assert isinstance(components_obj.page, status_info_client.Page)
    for component in components_obj.components:
        assert isinstance(component, status_info_client.Component)


def test_IncidentUpdate_from_dict(incident_update_pl):
    obj = status_info_client.IncidentUpdate.from_dict(incident_update_pl)

    assert obj.id == "xxqwgv42dnx5"
    assert obj.status == "investigating"
    assert obj.body == "We are working on resolving some internal technical problems now."
    assert obj.incident_id == "2gztsrksff0v"
    date = date_time(2019, 6, 24, 6, 7, 14, 463000)
    assert obj.created_at == date
    assert obj.updated_at == date
    assert obj.display_at == date


def test_Incident_from_dict(incident_pl):
    obj = status_info_client.Incident.from_dict(incident_pl)

    assert obj.id == "2gztsrksff0v"
    assert obj.name == "Global Unavailability"
    assert obj.status == "investigating"
    assert obj.created_at == date_time(2019, 6, 24, 5, 25, 57, 666000)
    assert obj.updated_at == date_time(2019, 6, 24, 6, 7, 14, 465000)
    assert obj.monitoring_at is None
    assert obj.resolved_at is None
    assert obj.impact == "none"  # says it all, really, for a global unavailability event lol
    assert obj.shortlink == "http://stspg.io/15e073752"
    assert obj.started_at == date_time(2019, 6, 24, 5, 25, 57, 659000)
    assert obj.page_id == "srhpyqt94yxb"
    for key, update in obj.incident_updates.items():
        assert key == update.id
        assert isinstance(update, status_info_client.IncidentUpdate)


def test_Incidents_from_dict(incidents_pl):
    obj = status_info_client.IncidentsPage.from_dict(incidents_pl)

    for key, incident in obj.incidents.items():
        assert key == incident.id
        assert isinstance(incident, status_info_client.Incident)
    assert isinstance(obj.page, status_info_client.Page)


def test_ScheduledMaintenance_from_dict(scheduled_maintenance_pl):
    obj = status_info_client.ScheduledMaintenance.from_dict(scheduled_maintenance_pl)

    assert obj.id == "ymm0202y77k6"
    assert obj.name == "Potentially Disruptive Upgrade"
    assert obj.status == "completed"
    assert obj.created_at == date_time(2016, 10, 16, 16, 57, 33, 416000)
    assert obj.updated_at == date_time(2016, 10, 19, 2, 39, 0, 299000)
    assert obj.monitoring_at is None
    assert obj.resolved_at == date_time(2016, 10, 19, 2, 39, 0, 274000)
    assert obj.impact == "maintenance"
    assert obj.shortlink == "http://stspg.io/4ERc"
    assert obj.started_at == date_time(2016, 10, 16, 16, 57, 0, 0)
    assert obj.page_id == "srhpyqt94yxb"
    for key, incident in obj.incident_updates.items():
        assert key == incident.id
        assert isinstance(incident, status_info_client.IncidentUpdate)
    assert obj.scheduled_for == date_time(2016, 10, 19, 2, 0, 0, 0)
    assert obj.scheduled_until == date_time(2016, 10, 19, 3, 0, 0, 0)


def test_ScheduledMaintenances_from_dict(scheduled_maintenances_pl):
    obj = status_info_client.ScheduledMaintenancesPage.from_dict(scheduled_maintenances_pl)

    for key, event in obj.scheduled_maintenances.items():
        assert key == event.id
        assert isinstance(event, status_info_client.ScheduledMaintenance)
    assert isinstance(obj.page, status_info_client.Page)


def test_OverallStatus_from_dict(overall_status_pl):
    obj = status_info_client.StatusPage.from_dict(overall_status_pl)

    assert isinstance(obj.page, status_info_client.Page)
    assert isinstance(obj.status, status_info_client.Status)


def test_Summary_from_dict(summary_pl):
    obj = status_info_client.Summary.from_dict(summary_pl)
    assert isinstance(obj.page, status_info_client.Page)
    for component in obj.components:
        assert isinstance(component, status_info_client.Component)

    for incident in obj.incidents:
        assert isinstance(incident, status_info_client.Incident)

    for scheduled_maintenance in obj.incidents:
        assert isinstance(scheduled_maintenance, status_info_client.ScheduledMaintenance)


def test_IncidentsPage_unresolved_incidents():
    investigating = _helpers.mock_model(status_info_client.Incident, status="investigating", id="8008135")
    identified = _helpers.mock_model(status_info_client.Incident, status="identified", id="e")
    monitoring = _helpers.mock_model(status_info_client.Incident, status="monitoring", id="floof")
    resolved = _helpers.mock_model(status_info_client.Incident, status="resolved", id="69")
    postmortem = _helpers.mock_model(status_info_client.Incident, status="postmortem", id="2b")

    summary = status_info_client.IncidentsPage(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        incidents={i.id: i for i in (investigating, identified, monitoring, resolved, postmortem)},
    )

    assert summary.unresolved_incidents == {
        investigating.id: investigating,
        identified.id: identified,
        monitoring.id: monitoring,
    }


def test_IncidentsPage_resolved_incidents():
    investigating = _helpers.mock_model(status_info_client.Incident, status="investigating", id="8008135")
    identified = _helpers.mock_model(status_info_client.Incident, status="identified", id="e")
    monitoring = _helpers.mock_model(status_info_client.Incident, status="monitoring", id="floof")
    resolved = _helpers.mock_model(status_info_client.Incident, status="resolved", id="69")
    postmortem = _helpers.mock_model(status_info_client.Incident, status="postmortem", id="2b")

    summary = status_info_client.IncidentsPage(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        incidents={i.id: i for i in (investigating, identified, monitoring, resolved, postmortem)},
    )

    assert summary.resolved_incidents == {
        resolved.id: resolved,
        postmortem.id: postmortem,
    }


@pytest.fixture
def mock_client(event_loop):
    assert event_loop

    class Response:
        def __init__(self, session):
            self.session = session
            self.real_url = "http://a-real-url"
            self.status = 200
            self.reason = "OK"
            self.content_type = "application/json"

        def raise_for_status(self):
            pass

        async def json(self):
            return self.session.mock_response_body

        def __call__(self, *args, **kwargs):
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    class ClientSession:
        def __init__(self, **_):
            self.request = mock.MagicMock(wraps=Response(self))
            self.mock_response_body = mock.MagicMock()

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

        def close(self):
            pass

    with mock.patch("aiohttp.ClientSession", new=ClientSession):
        yield _helpers.unslot_class(status_info_client.StatusInfoClient)()


def test_Summary_unresolved_incidents():
    investigating = _helpers.mock_model(status_info_client.Incident, status="investigating", id="8008135")
    identified = _helpers.mock_model(status_info_client.Incident, status="identified", id="e")
    monitoring = _helpers.mock_model(status_info_client.Incident, status="monitoring", id="floof")
    resolved = _helpers.mock_model(status_info_client.Incident, status="resolved", id="69")
    postmortem = _helpers.mock_model(status_info_client.Incident, status="postmortem", id="2b")

    summary = status_info_client.Summary(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        components=mock.create_autospec(list),
        incidents=[investigating, identified, monitoring, resolved, postmortem],
        scheduled_maintenances=[],
    )

    assert summary.unresolved_incidents == {
        investigating.id: investigating,
        identified.id: identified,
        monitoring.id: monitoring,
    }


def test_Summary_resolved_incidents():
    investigating = _helpers.mock_model(status_info_client.Incident, status="investigating", id="8008135")
    identified = _helpers.mock_model(status_info_client.Incident, status="identified", id="e")
    monitoring = _helpers.mock_model(status_info_client.Incident, status="monitoring", id="floof")
    resolved = _helpers.mock_model(status_info_client.Incident, status="resolved", id="69")
    postmortem = _helpers.mock_model(status_info_client.Incident, status="postmortem", id="2b")

    summary = status_info_client.Summary(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        components=mock.create_autospec(list),
        incidents=[investigating, identified, monitoring, resolved, postmortem],
        scheduled_maintenances=[],
    )

    assert summary.resolved_incidents == {
        resolved.id: resolved,
        postmortem.id: postmortem,
    }


def test_Summary_upcoming_scheduled_maintenances():
    scheduled = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="scheduled", id="1")
    in_progress = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="in progress", id="2")
    verifying = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="verifying", id="3")
    completed = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="completed", id="4")

    summary = status_info_client.Summary(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        components=mock.create_autospec(list),
        incidents=[],
        scheduled_maintenances=[scheduled, in_progress, verifying, completed],
    )

    assert summary.upcoming_scheduled_maintenances == {
        scheduled.id: scheduled,
    }


def test_Summary_ongoing_scheduled_maintenances():
    scheduled = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="scheduled", id="1")
    in_progress = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="in progress", id="2")
    verifying = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="verifying", id="3")
    completed = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="completed", id="4")

    summary = status_info_client.Summary(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        components=mock.create_autospec(list),
        incidents=[],
        scheduled_maintenances=[scheduled, in_progress, verifying, completed],
    )

    assert summary.ongoing_scheduled_maintenances == {
        in_progress.id: in_progress,
        verifying.id: verifying,
    }


def test_Summary_completed_scheduled_maintenances():
    scheduled = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="scheduled", id="1")
    in_progress = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="in progress", id="2")
    verifying = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="verifying", id="3")
    completed = _helpers.mock_model(status_info_client.ScheduledMaintenance, status="completed", id="4")

    summary = status_info_client.Summary(
        page=mock.create_autospec(status_info_client.Page, spec_set=True),
        components=mock.create_autospec(list),
        incidents=[],
        scheduled_maintenances=[scheduled, in_progress, verifying, completed],
    )

    assert summary.completed_scheduled_maintenances == {completed.id: completed}


@pytest.mark.parametrize(
    "model",
    [
        status_info_client.Subscriber,
        status_info_client.Page,
        status_info_client.Component,
        status_info_client.IncidentUpdate,
        status_info_client.Incident,
        status_info_client.ScheduledMaintenance,
    ],
)
def test_model_is_hashable_on_id(model):
    instance1 = _helpers.mock_model(model, id=1234)
    instance2 = _helpers.mock_model(model, id=1234)
    instance3 = _helpers.mock_model(model, id=1235)

    assert hash(instance1) == hash(instance2)
    assert hash(instance2) != hash(instance3)


def test_Subscriber_eq():
    inst1 = status_info_client.Subscriber("id1", "blah", "blah", datetime.datetime.now(), None, None, None, None)
    inst2 = status_info_client.Subscriber("id1", "blah", "blah", datetime.datetime.now(), None, None, None, None)
    inst3 = status_info_client.Subscriber("id3", "blah", "blah", datetime.datetime.now(), None, None, None, None)
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 != inst4


def test_Page_eq():
    inst1 = status_info_client.Page("id1", "foo", "goo.gl", datetime.datetime.now())
    inst2 = status_info_client.Page("id1", "foo", "goo.gl", datetime.datetime.now())
    inst3 = status_info_client.Page("id3", "foo", "goo.gl", datetime.datetime.now())
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 != inst4


def test_Component_eq():
    inst1 = status_info_client.Component(
        "id1", "foo", datetime.datetime.now(), "12a", 12, datetime.datetime.now(), None, None
    )
    inst2 = status_info_client.Component(
        "id1", "foo", datetime.datetime.now(), "12a", 12, datetime.datetime.now(), None, None
    )
    inst3 = status_info_client.Component(
        "id3", "foo", datetime.datetime.now(), "12a", 12, datetime.datetime.now(), None, None
    )
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 != inst4


def test_IncidentUpdate_eq():
    inst1 = status_info_client.IncidentUpdate("id1", "foo", datetime.datetime.now(), None, "1a2", "foo", None)
    inst2 = status_info_client.IncidentUpdate("id1", "foo", datetime.datetime.now(), None, "1a2", "foo", None)
    inst3 = status_info_client.IncidentUpdate("id3", "foo", datetime.datetime.now(), None, "1a2", "foo", None)
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 != inst4


def test_Incident_eq():
    inst1 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    inst2 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    inst3 = status_info_client.Incident(
        "id3", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.IncidentUpdate("id1", "foo", datetime.datetime.now(), None, "1a2", "foo", None)
    assert inst1 != inst4


def test_ScheduledMaintenance_eq():
    inst1 = status_info_client.ScheduledMaintenance(
        "id1",
        "foo",
        "bar",
        {},
        datetime.datetime.now(),
        None,
        "1a2b",
        None,
        None,
        None,
        "oof",
        datetime.datetime.now(),
        "goo.gl",
        None,
    )
    inst2 = status_info_client.ScheduledMaintenance(
        "id1",
        "foo",
        "bar",
        {},
        datetime.datetime.now(),
        None,
        "1a2b",
        None,
        None,
        None,
        "oof",
        datetime.datetime.now(),
        "goo.gl",
        None,
    )
    inst3 = status_info_client.ScheduledMaintenance(
        "id3",
        "foo",
        "bar",
        {},
        datetime.datetime.now(),
        None,
        "1a2b",
        None,
        None,
        None,
        "oof",
        datetime.datetime.now(),
        "goo.gl",
        None,
    )
    assert inst1 == inst2
    assert inst1 != inst3
    inst4 = status_info_client.Incident(
        "id1", "foo", "bar", {}, datetime.datetime.now(), None, "12", None, "goo.gl", "??", None, None
    )
    assert inst1 != inst4


@pytest.fixture
def stubbed_client(mock_client):
    def perform_request(_, cast, *__, **___):
        return _helpers.mock_model(cast)

    mock_client._perform_request = mock.AsyncMock(wraps=perform_request)
    return mock_client


@pytest.mark.asyncio
class TestServiceStatusClient:
    async def test_DiscordServiceStatusClient___init__(self, event_loop):
        assert event_loop
        async with status_info_client.StatusInfoClient() as client:
            assert client.url == "https://status.discordapp.com/api/v2"

    @pytest.mark.parametrize("method", [None, "get", "post", "patch", "delete", "put"])
    async def test_DiscordServiceStatusClient__perform_request(self, mock_client, method):
        class FromDictable:
            @staticmethod
            def from_dict(_):
                ...

        cast = _helpers.create_autospec(FromDictable)
        cast.from_dict = _helpers.create_autospec(FromDictable.from_dict, return_value=FromDictable())
        data = mock.MagicMock()

        resp = await mock_client._perform_request("/foo/bar", cast, data, method)
        cast.from_dict.assert_called_once_with(mock_client.client_session.mock_response_body)
        assert isinstance(resp, FromDictable)

    @pytest.mark.parametrize(
        ["expected_route", "expected_cast", "name"],
        [
            ("/summary.json", status_info_client.Summary, "fetch_summary"),
            ("/status.json", status_info_client.StatusPage, "fetch_status"),
            ("/components.json", status_info_client.ComponentsPage, "fetch_components"),
            ("/incidents.json", status_info_client.IncidentsPage, "fetch_all_incidents"),
            ("/incidents/unresolved.json", status_info_client.IncidentsPage, "fetch_unresolved_incidents"),
            (
                "/scheduled-maintenances.json",
                status_info_client.ScheduledMaintenancesPage,
                "fetch_all_scheduled_maintenances",
            ),
            (
                "/scheduled-maintenances/upcoming.json",
                status_info_client.ScheduledMaintenancesPage,
                "fetch_upcoming_scheduled_maintenances",
            ),
            (
                "/scheduled-maintenances/active.json",
                status_info_client.ScheduledMaintenancesPage,
                "fetch_active_scheduled_maintenances",
            ),
        ],
        ids=lambda route: route,
    )
    async def test_fetch_calls_perform_request(self, stubbed_client, expected_cast, expected_route, name):
        coro_fn = getattr(stubbed_client, name)
        assert isinstance(await coro_fn(), expected_cast)
        stubbed_client._perform_request.assert_called_with(expected_route, expected_cast)

    @pytest.mark.parametrize(
        "incident", ["1a2b3c", _helpers.mock_model(status_info_client.Incident, id="1a2b3c"), None]
    )
    async def test_subscribe_email_to_incident(self, incident, stubbed_client):
        if incident is None:
            body = {"subscriber[email]": "somebody@example.com"}
        else:
            body = {"subscriber[email]": "somebody@example.com", "subscriber[incident]": "1a2b3c"}

        subscriber = await stubbed_client.subscribe_email_to_incidents("somebody@example.com", incident)
        assert subscriber is not None
        args, kwargs = stubbed_client._perform_request.call_args
        assert args == ("/subscribers.json", status_info_client.Subscriber, body, "post")

    @pytest.mark.parametrize(
        "incident", ["1a2b3c", _helpers.mock_model(status_info_client.Incident, id="1a2b3c"), None]
    )
    async def test_subscribe_webhook_to_incident(self, incident, stubbed_client):
        if incident is None:
            body = {"subscriber[endpoint]": "http://example.com"}
        else:
            body = {"subscriber[endpoint]": "http://example.com", "subscriber[incident]": "1a2b3c"}

        subscriber = await stubbed_client.subscribe_webhook_to_incidents("http://example.com", incident)
        assert subscriber is not None
        stubbed_client._perform_request.assert_called_with(
            "/subscribers.json", status_info_client.Subscriber, body, "post"
        )

    @pytest.mark.parametrize("subscriber", ["1a2b3c", _helpers.mock_model(status_info_client.Subscriber, id="1a2b3c")])
    async def test_unsubscribe(self, subscriber, stubbed_client):
        await stubbed_client.unsubscribe(subscriber)
        stubbed_client._perform_request.assert_called_with("/subscribers/1a2b3c.json", None, None, "delete")

    @pytest.mark.parametrize("subscriber", ["1a2b3c", _helpers.mock_model(status_info_client.Subscriber, id="1a2b3c")])
    async def test_resend_confirmation_email(self, subscriber, stubbed_client):
        await stubbed_client.resend_confirmation_email(subscriber)
        stubbed_client._perform_request.assert_called_with(
            "/subscribers/1a2b3c/resend_confirmation", None, None, "post"
        )