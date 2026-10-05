# Icon: Tabler Icons

SlideFly dùng **Tabler Icons** (MIT, 5.166 icon nét viền, 1.054 icon tô đặc, có 376 logo đơn sắc như `brand-python`, `brand-github`, `brand-openai`). Phiên bản được ghim trong `scripts/icons.py` (`TABLER_VERSION`), nên icon không tự đổi theo thời gian.

## 1. Nạp file

```html
<link rel="stylesheet" href=".../assets/morph-icons.css">
...
<script src=".../assets/morph-icons.js"></script>   <!-- cuối body, sau các script khác -->
```

Khi đang soạn, `morph-icons.js` tự tải icon từ jsDelivr. Khi gộp bằng `inline-assets.py`, SVG được nhúng thẳng vào file, nên deck cuối chạy được khi không có mạng. Lần gộp đầu cần mạng; icon đã tải được lưu ở `~/.cache/slidefly/`.

## 2. Tìm icon

```bash
python "$SK/scripts/icons.py" search làm sạch dữ liệu      # từ tiếng Việt
python "$SK/scripts/icons.py" search database security     # tag tiếng Anh
python "$SK/scripts/icons.py" suggest nguon.html           # gợi ý tối đa 3 icon cho mỗi slide
```

Gợi ý chỉ là gợi ý. Chọn icon theo **ý chính** của slide, không theo từ xuất hiện nhiều nhất. Bảng từ tiếng Việt nằm ở `assets/icons/vi-keywords.json`, thêm từ mới thì ghi tên icon có thật (kiểm bằng `search`).

## 3. Khai báo

```html
<i class="ico" data-icon="database"></i>                       <!-- nét viền, to bằng chữ xung quanh -->
<i class="ico" data-icon="star" data-style="filled"></i>       <!-- tô đặc: dành cho đúng 1 chỗ nhấn -->
<i class="ico ico-lg accent" data-icon="microscope"></i>       <!-- 96px, màu nhấn của style -->
<div class="hl-icon"><i class="ico" data-icon="shield-check"></i></div>   <!-- icon lớn ở cột nổi bật -->
<span class="ico-badge"><i class="ico" data-icon="flask"></i></span>      <!-- icon trong vòng tròn -->
<div class="ico-row">                                                     <!-- dải công cụ, cùng cỡ -->
  <div><i class="ico" data-icon="brand-python"></i>Python</div>
  <div><i class="ico" data-icon="brand-git"></i>Git</div>
</div>
```

Cỡ: `ico-sm` 32px, `ico-md` 56px, `ico-lg` 96px, `ico-xl` 200px (nét tự mảnh lại khi icon to). Màu: chữ xung quanh (mặc định), `accent`, `muted`.

## 4. Luật chống rối (audit tự kiểm phần đếm)

- Mỗi slide chọn **một** cách dùng: một icon chính, **hoặc** một dải tối đa 6 icon cùng cỡ, **hoặc** icon làm nút trong sơ đồ.
- **Không gắn icon vào từng gạch đầu dòng.** Danh sách đã có dấu đầu dòng của style.
- Icon tô đặc chỉ dùng cho một chỗ nhấn mỗi slide.
- Logo `brand-*` chỉ để gọi đúng tên công cụ đang nói tới, không dùng làm hình trang trí và không đặt cạnh nội dung có thể hiểu là hãng đó bảo trợ.
- Slide trưng bày (cover, section, quote) thường không cần icon.

| Audit báo | Cách sửa |
|---|---|
| `quá nhiều icon (n, tối đa 6)` | bỏ icon ở các ý phụ, giữ icon cho ý chính |
| `icon không tồn tại: tên` | `icons.py search` để tìm đúng tên |
| `inline-assets` báo `Icons not found in Tabler` | như trên; file vẫn được ghi nhưng icon đó trống |

## 5. Ghi nguồn

Tabler Icons, MIT License, Copyright (c) 2020-2026 Paweł Kuna, https://tabler.io/icons. Logo thương hiệu thuộc về chủ sở hữu tương ứng.
