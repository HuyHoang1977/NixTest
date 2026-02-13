# NixTest - Vietnamese Telex Counter
## Chương trình đếm số lượng chữ cái Tiếng Việt có dấu theo quy tắc gõ Telex từ chuỗi Latinh.
## Tính năng
- **Validation:** Chặn khoảng trắng/ký tự đặc biệt; cho phép nhập số.
- **Tối ưu:** Sử dụng Regex xử lý chuỗi cực nhanh ($O(n)$).
- **UX:** Tự động yêu cầu nhập lại nếu dữ liệu lỗi.

## Cách dùng
1. Chạy file: `test.py`
2. Nhập chuỗi cần kiểm tra.

## Ví dụ
- **Input:** `hwfdawhwhcoomddfgwdc`
- **Output:** `6 (w, aw, w, oo, dd, w)`
