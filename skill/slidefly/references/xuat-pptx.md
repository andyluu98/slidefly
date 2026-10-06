# Xuất PowerPoint có Morph

`scripts/export-pptx.py` ghi một file .pptx **sửa được**, có hiệu ứng **Morph** khi chuyển slide. Chỉ dùng thư viện chuẩn của Python 3.10+, không cần trình duyệt, không cần cài gói.

```bash
python "$SK/scripts/export-pptx.py" deck.html deck.pptx
```

Đầu vào là file nguồn (có `<link>` tới CSS) hoặc file đã gộp bằng `inline-assets.py`, cả hai đều được.

## Vì sao Morph chạy được

PowerPoint Morph khớp hai hình ở hai slide liền nhau khi chúng **cùng tên bắt đầu bằng `!!`**: hình trượt, đổi cỡ, đổi màu sang chỗ mới. Đây đúng là cơ chế diễn viên của SlideFly. Script làm như sau:

- Mỗi diễn viên của style thành một shape tên `!!<tên diễn viên>` trên **mọi** slide. Shape được đặt đúng tư thế của slide đó, đọc thẳng từ CSS của style (`--x --y --w --h --r --s --o`). Diễn viên đứng ngoài khung ở slide nào thì shape vẫn nằm ngoài khung, để Morph có chỗ bay vào, bay ra.
- Đổi đơn vị: 1px = 6350 EMU; cỡ chữ px × 0,5 = pt.
- Hình tròn thành ellipse, bo góc thành roundRect. `clip-path: polygon()` thành hình tự vẽ. Gradient lấy màu đầu. Hoa văn (lưới kẻ, chấm, ảnh) bỏ qua.
- Mọi slide gắn chuyển cảnh Morph (theo đối tượng). PowerPoint đời cũ không có Morph thì dùng fade.
- Chữ thân slide hiện dần (fade) lần lượt sau khi chuyển slide, giống `reveal` của bản HTML. Tiêu đề và diễn viên bay bằng Morph nên không có hiệu ứng riêng.

## Giữ được và đơn giản hóa

| Giữ được | Đơn giản hóa |
|---|---|
| Chữ sửa được: tiêu đề, gạch đầu dòng, hai cột, số liệu, dòng thời gian, mục lục, trích dẫn | Sơ đồ tự vẽ (`.viz`) thành khung có danh sách nhãn |
| 12 kiểu mới: số lớn, bento, quy trình, bảng so sánh, đếm ngược, trước và sau, hỏi đáp, tuyên bố, ảnh chia đôi... | Khung giao diện (`.mock`) thành cửa sổ tối có chữ dạng code |
| 12 khung `data-frame`: mảng màu, dải ngang, mảng chéo, thẻ so le, số lớn... | Chữ gõ dần, chấm chạy, rung, đóng dấu: thành hiện dần |
| Icon Tabler thành hình vẽ thật của PowerPoint (đổi màu, phóng to không vỡ) | Quy tắc style phụ thuộc nội dung (`:has(...)`): hình giữ tư thế chuẩn |
| Ảnh nền, ảnh chia đôi, nguồn ảnh | Font: nếu máy không có font của style, PowerPoint dùng font thay thế |
| Màu theo từng kiểu slide, màu riêng của style cho tiêu đề, nhãn, số | Slide tự thiết kế bằng CSS riêng: phần chữ vẫn vào, vị trí lấy theo `left/top` ghi trong `style` |

## Sau khi xuất

- Mở bằng PowerPoint 2019 hoặc 365 để có Morph. Google Slides và Keynote không có Morph, khi đó chỉ thấy chuyển cảnh thường.
- Cài font của style lên máy trình chiếu (Google Fonts, miễn phí) để chữ đúng dáng.
- Kiểm nhanh bằng PowerPoint (Windows): mở file, bấm **Slide Show**, đi qua vài slide xem hình bay và chữ hiện dần.
