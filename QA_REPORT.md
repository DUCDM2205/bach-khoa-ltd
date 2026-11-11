# Báo cáo kiểm tra demo giao diện

Ngày kiểm tra: 11/11/2026. Phạm vi: website tĩnh HTML/CSS/JavaScript, không có backend.

## Kết quả tự động và trình duyệt

| Hạng mục | Kết quả | Bằng chứng |
|---|---|---|
| Cú pháp JavaScript | PASS | `node --check assets/js/data.js` và `node --check assets/js/site.js` |
| HTTP ở root | PASS | 27 tài nguyên công khai, 27/27 phản hồi 200 |
| HTTP ở subpath `/<repo>/` | PASS | 27 tài nguyên công khai, 27/27 phản hồi 200 |
| Desktop 1440×900 | PASS | Header, hero, CTA và số liệu hiển thị đúng |
| Mobile 390×844 | PASS | Menu mở/đóng, viewport không tràn ngang (`scrollWidth = clientWidth = 375`) |
| Banner | PASS | 3 ảnh, tự chuyển, nút chọn thủ công; tôn trọng reduced motion |
| Bộ lọc dự án | PASS | Năm 2025 + điện mặt trời trả đúng 1 kết quả; URL giữ `year` và `service` |
| Trang dự án chi tiết | PASS | Mở trực tiếp và reload giữ đúng dự án; ảnh ở đúng repository subpath |
| Trạng thái không kết quả | PASS | Có thông báo và nút đặt lại bộ lọc |
| Trang lĩnh vực | PASS | Tổng quan + 7 URL riêng, dự án liên quan từ dữ liệu mẫu |
| Tin tức | PASS | Danh mục cha/con, danh sách và chi tiết theo query ID |
| PDF | PASS | PDF 3 trang A4 render không lỗi; iframe đúng URL; tải file thành công |
| Form liên hệ | PASS | HTML validation và thông báo “chưa được gửi hoặc lưu” |
| Console | PASS | Không có error/warning khi kiểm tra subpath và trang chi tiết |
| `noindex` | PASS | Tất cả trang nội dung có `noindex,nofollow` |

## Giới hạn

- Chưa kiểm thử trên Safari/iOS thật; responsive được kiểm tra bằng viewport trình duyệt.
- Hotline, email, địa chỉ, dự án, số liệu và tài liệu đều là dữ liệu minh họa.
- Không có gửi form, CMS, database, đăng nhập, tracking hoặc triển khai GitHub thực tế.
