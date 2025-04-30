# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 10:04:39 2025

@author: DavrServis
"""

# tests/test_report_manager.py

import sys
import os
sys.path.append(os.path.abspath(".."))

import unittest
from unittest.mock import patch, MagicMock
from datetime import date
from reports import report_manager

class TestReportManager(unittest.TestCase):
    def setUp(self):
        print("\n🔧 Test muhitini sozlash: test sanasi va soxta ma'lumotlar tayyorlanmoqda...")
        self.test_date = date(2025, 4, 12)
        self.mock_sales = [
            (1, "2025-04-12 10:00:00", 24000, "naqd"),
            (2, "2025-04-12 12:00:00", 15000, "karta")
        ]
        self.mock_credits = [
            ("Ali", "ID123", 20000, "2025-04-11 14:00:00"),
            ("Vali", "ID456", 18000, "2025-04-12 09:00:00")
        ]

    @patch("reports.report_manager.psycopg2.connect")
    def test_generate_daily_sales_report(self, mock_connect):
        print("🧾 Savdo hisobotini olish testi: generate_daily_sales_report")

        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = self.mock_sales
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn

        report = report_manager.generate_daily_sales_report(self.test_date)
        self.assertEqual(len(report), 2)
        self.assertEqual(report[0]["id"], 1)
        self.assertEqual(report[1]["summa"], 15000)
        self.assertEqual(report[0]["tolov"], "naqd")

    @patch("reports.report_manager.psycopg2.connect")
    def test_generate_credit_report(self, mock_connect):
        print("💳 Qarzlar hisobotini olish testi: generate_credit_report")

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = self.mock_credits
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn

        report = report_manager.generate_credit_report()
        self.assertEqual(len(report), 2)
        self.assertEqual(report[0]["ism"], "Ali")
        self.assertEqual(report[1]["id_karta"], "ID456")

    def test_export_report_to_txt(self):
        print("📁 Hisobotni faylga yozish testi: export_report_to_txt")
        test_data = [
            {"id": 1, "summa": 12000, "tolov": "naqd"},
            {"id": 2, "summa": 8000, "tolov": "karta"}
        ]
        filename = "test_report.txt"
        report_manager.export_report_to_txt(test_data, filename)
        self.assertTrue(os.path.exists(filename))

        with open(filename, encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Summa", content)
            self.assertIn("Tolov", content)

        os.remove(filename)

if __name__ == '__main__':
    unittest.main(verbosity=2)

