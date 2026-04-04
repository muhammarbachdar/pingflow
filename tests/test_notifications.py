import pytest

@pytest.mark.asyncio
async def test_create_notification_success(client, auth_token):
    response = await client.post(
        "/notifications/",
        json={
            "channel": "email",
            "recipient": "someone@example.com",
            "subject": "Test",
            "body": "Hello!"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "pending"
    assert data["channel"] == "email"

@pytest.mark.asyncio
async def test_create_notification_unauthorized(client):
    response = await client.post(
        "/notifications/",
        json={
            "channel": "email",
            "recipient": "someone@example.com",
            "subject": "Test",
            "body": "Hello!"
        }
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_get_notifications(client, auth_token):
    await client.post(
        "/notifications/",
        json={
            "channel": "email",
            "recipient": "someone@example.com",
            "subject": "Test",
            "body": "Hello!"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    response = await client.get(
        "/notifications/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1