# Bách Khoa LTD - Demo giao diện GitHub Pages

Bản demo tĩnh nhiều trang để duyệt nhận diện, bố cục, nội dung và luồng sử dụng trước khi triển khai Django + Wagtail. Mọi dự án, số liệu, chứng chỉ, đối tác, hình ảnh và thông tin liên hệ trong demo đều là **dữ liệu minh họa** hoặc **đang cập nhật**.

## Chạy local

Yêu cầu Python 3 đã có trong PATH. Mở PowerShell tại thư mục dự án:

```powershell
python -m http.server 8000
```

Mở `http://127.0.0.1:8000/`. Không mở file HTML bằng `file://` vì trình duyệt có thể xử lý PDF hoặc lịch sử URL khác với máy chủ HTTP.

Để mô phỏng đúng GitHub Pages tại đường dẫn con `/<repo>/`, chạy server từ thư mục cha:

```powershell
Set-Location ..
python -m http.server 8001
```

Sau đó mở `http://127.0.0.1:8001/bachkhoa-github-pages-demo/` và thử tải lại các URL chi tiết.

## Đưa lên GitHub Pages

1. Tạo repository GitHub mới và đưa toàn bộ nội dung trong thư mục này lên nhánh `main`. `index.html` phải nằm ngay ở root repository.
2. Vào **Settings → Pages**.
3. Tại **Build and deployment**, chọn **Deploy from a branch**.
4. Chọn branch **main**, thư mục **/(root)**, rồi bấm **Save**.
5. Đợi GitHub tạo URL dạng `https://<username>.github.io/<repo>/`.
6. Mở URL và kiểm tra lại menu, trang chi tiết, bộ lọc dự án và PDF.

Demo dùng đường dẫn tương đối và tính base URL từ vị trí `assets/js/site.js`, nên hoạt động cả ở domain gốc và repository subpath. File `.nojekyll` được giữ để GitHub Pages phục vụ nguyên trạng.

## Cấu trúc và nơi thay nội dung

- `assets/images/logo-mark.svg`: biểu trưng demo. Thay bằng logo chính thức và cập nhật `alt` nếu cần.
- `assets/images/*.png`: ảnh minh họa AI. Thay bằng ảnh có quyền sử dụng và đúng dự án thực tế.
- `assets/documents/ho-so-nang-luc-demo.pdf`: PDF demo; thay bằng hồ sơ được duyệt nhưng giữ nguyên tên file hoặc sửa link trong `assets/js/site.js`.
- `assets/js/data.js`: dữ liệu lĩnh vực, dự án và tin tức mẫu. Đây là nguồn chính để thay dữ liệu trong demo.
- `assets/js/site.js`: component dùng chung, luồng banner, lọc dự án, form demo và nội dung các trang.
- `assets/css/site.css`: màu thương hiệu, layout, responsive và trạng thái tương tác.
- Thông tin địa chỉ/hotline/email xuất hiện trong footer và trang liên hệ trong `assets/js/site.js`.

## Trang đã dựng

- Trang chủ với 3 banner, số liệu, lĩnh vực, dự án, tin tức và CTA.
- Giới thiệu và hồ sơ năng lực.
- Tổng quan lĩnh vực và 7 trang lĩnh vực riêng.
- Dự án chọn năm trước, lọc kết hợp, trạng thái rỗng và trang chi tiết.
- Tin tức, danh mục cha/con và trang chi tiết.
- Chứng chỉ/hồ sơ năng lực, xem và tải PDF.
- Liên hệ với validation trình duyệt và thông báo không gửi dữ liệu.
- Tuyển dụng và trang chi tiết vị trí mẫu.
- Trang 404.

## Nội dung phải thay trước khi công bố

- Logo, bộ nhận diện và favicon chính thức.
- Địa chỉ, hotline, email, Zalo và bản đồ.
- Số liệu kinh nghiệm, nhân sự, thiết bị và năng lực đã xác thực.
- Dự án được phép công khai, ảnh dự án và thông tin chủ đầu tư/địa điểm.
- Chứng chỉ còn hiệu lực, hồ sơ năng lực và logo đối tác được phép sử dụng.
- Bài viết, tuyển dụng, chính sách bảo mật và thông tin pháp lý.

## Giới hạn có chủ đích

Form không gửi hoặc lưu dữ liệu. Không có CMS, database, đăng nhập, `/admin-bachkhoa`, phân quyền, tracking hoặc tích hợp ngoài. Tất cả trang có `noindex,nofollow` trong giai đoạn duyệt.
