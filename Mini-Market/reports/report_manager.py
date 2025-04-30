# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 10:03:34 2025

@author: DavrServis
"""

# reports/report_manager.py

import psycopg2
from config import DB_CONFIG
from datetime import date

def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

def generate_daily_sales_report(sana: date):
    """
    Kiritilgan sana bo‘yicha savdolar ro‘yxatini qaytaradi.
    """
    report = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT s.id, s.vaqt, s.jami_summa, s.tolov_turi
                FROM savdo s
                WHERE DATE(s.vaqt) = %s
                ORDER BY s.vaqt ASC;
            """, (sana,))
            results = cur.fetchall()
            for row in results:
                report.append({
                    "id": row[0],
                    "vaqt": row[1],
                    "summa": row[2],
                    "tolov": row[3]
                })
    return report

def generate_credit_report():
    """
    Qarzga olingan savdolar va mijozlar.
    """
    report = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.ism, c.id_karta, cr.summa, cr.vaqt
                FROM qarzlar cr
                JOIN mijozlar c ON cr.mijoz_id = c.id
                ORDER BY cr.vaqt DESC;
            """)
            results = cur.fetchall()
            for row in results:
                report.append({
                    "ism": row[0],
                    "id_karta": row[1],
                    "summa": row[2],
                    "vaqt": row[3]
                })
    return report

def export_report_to_txt(report_data, filename):
    """
    Berilgan report_data ro‘yxatini matn fayliga eksport qiladi.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for entry in report_data:
            for key, value in entry.items():
                f.write(f"{key.capitalize()}: {value}\n")
            f.write("-" * 30 + "\n")
    print(f"✅ Hisobot saqlandi: {filename}")
