# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:18:26 2025

@author: DavrServis
"""

# modules/shift_manager.py

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id

# Hozirgi ochiq smenani olish
def get_current_shift():
    query = """
        SELECT id FROM shifts
        WHERE status = 'open'
        ORDER BY opened_at DESC
        LIMIT 1;
    """
    result = fetch_one(query)
    if result:
        return result["id"]
    return None

# Smenani ochilgan-ochilmaganligini tekshirish
def is_shift_open():
    return get_current_shift() is not None

# Smena ochish
def start_shift(user_id):
    if is_shift_open():
        raise Exception("❗ Hozirda ochiq smena bor. Avval uni yopish kerak.")

    query = """
        INSERT INTO shifts (opened_by, status)
        VALUES (%s, 'open')
        RETURNING id;
    """
    shift_id = execute_returning_id(query, (user_id,))
    print(f"✅ Yangi smena ochildi: #{shift_id}")
    return shift_id

# Smena yopish
def end_shift(user_id):
    current_shift_id = get_current_shift()
    if not current_shift_id:
        raise Exception("❗ Ochiq smena mavjud emas.")

    query = """
        UPDATE shifts
        SET closed_at = CURRENT_TIMESTAMP,
            closed_by = %s,
            status = 'closed'
        WHERE id = %s;
    """
    execute_query(query, (user_id, current_shift_id))
    print(f"✅ Smena yopildi: #{current_shift_id}")
    return current_shift_id
