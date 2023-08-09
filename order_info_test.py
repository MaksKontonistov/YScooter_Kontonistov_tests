# Максим Контонистов, 7 когорта — Финальный проект. Инженер по тестированию плюс

import stand_request
import data


def test_order_info_by_track():
    track = stand_request.post_new_order(data.order_body).json()["track"]
    response = stand_request.get_order_by_track(track)
    assert response.status_code == 200
