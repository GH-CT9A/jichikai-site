from app import cloud_json_load, cloud_json_save

cloud_json_save("test_ping", {"ok": True, "msg": "こんにちは"})
result = cloud_json_load("test_ping", {"fallback": True})
print("結果:", result)