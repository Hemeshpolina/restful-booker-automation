import pytest
import json
from utils.api_client import RestfulBookerClient
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def client():
    client = RestfulBookerClient("https://restful-booker.herokuapp.com")
    client.authenticate("admin", "password123")
    return client

@pytest.fixture(scope="module")
def test_data():
    with open('testdata.json') as f:
        data = json.load(f)
    return data

@pytest.fixture(scope="module")
def create_bookings(client, test_data):
    bookings = test_data['bookings']
    booking_ids = []
    for booking in bookings:
        response = client.create_booking(booking)
        booking_ids.append(response['bookingid'])
        logger.info(f"Created booking: {response}")
    return booking_ids

def test_create_bookings(create_bookings):
    booking_ids = create_bookings
    assert len(booking_ids) == 3
    logger.info(f"All booking IDs: {booking_ids}")

def test_modify_bookings(client, create_bookings, test_data):
    booking_ids = create_bookings
    updates = test_data['updates']
    for i, booking_id in enumerate(booking_ids[:2]):
        response = client.update_booking(booking_id, updates[i])
        logger.info(f"Updated booking {booking_id}: {response}")

def test_delete_booking(client, create_bookings):
    booking_ids = create_bookings
    response = client.delete_booking(booking_ids[0])
    logger.info(f"Deleted booking {booking_ids[0]}: Status {response}")