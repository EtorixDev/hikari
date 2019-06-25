#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asynctest
import pytest


@pytest.fixture()
def http_client(event_loop):
    from hikari_tests.test_net.test_http import ClientMock

    return ClientMock(token="foobarsecret", loop=event_loop)


@pytest.mark.asyncio
async def test_create_webhook_without_avatar(http_client):
    http_client.request = asynctest.CoroutineMock()
    await http_client.create_webhook("424242", "asdf")
    http_client.request.assert_awaited_once_with(
        "post", "/channels/{channel_id}/webhooks", channel_id="424242", json={"name": "asdf"}
    )


@pytest.mark.asyncio
async def test_create_webhook_with_avatar(http_client):
    http_client.request = asynctest.CoroutineMock()
    await http_client.create_webhook("424242", "asdf", avatar=b"")
    http_client.request.assert_awaited_once_with(
        "post", "/channels/{channel_id}/webhooks", channel_id="424242", json={"name": "asdf", "avatar": b""}
    )