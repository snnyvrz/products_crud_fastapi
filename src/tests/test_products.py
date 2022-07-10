import json

import pytest

from app.api import crud


def test_create_product(test_app, monkeypatch):
    test_request_payload = {
        "title": "something",
        "description": "something else",
        "category": "foo",
        "image": "bar.jpg",
        "price": 2.24,
    }
    test_response_payload = {
        "id": 1,
        "title": "something",
        "description": "something else",
        "category": "foo",
        "image": "bar.jpg",
        "price": 2.24,
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post(
        "/products/",
        data=json.dumps(test_request_payload),
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_product_invalid_json(test_app):
    response = test_app.post(
        "/products/", data=json.dumps({"title": "something"})
    )
    assert response.status_code == 422
