# 57 style: chọn theo mục đích

Dữ liệu đầy đủ (tên, nền, nhãn tâm trạng, hợp với, font) nằm ở `assets/styles/index.json`. Xem trực quan: chạy `scripts/build-gallery.py <thu-muc>` rồi mở `00-gallery.html`.

Đổi style = thay 1 dòng `<link href=".../styles/<slug>.css">`. Mọi style dùng font có tiếng Việt và đã qua `check-deck.py` (RESULT: OK) trên deck mẫu 10 slide.

## Nhóm theo mục đích

| Mục đích | Style (slug) |
|---|---|
| Doanh nghiệp, báo cáo, tư vấn | `swiss-modern`, `blue-professional`, `electric-studio`, `signal`, `cartesian`, `monochrome`, `cobalt-grid`, `emerald-editorial` |
| Đào tạo, giáo dục, nội bộ | `xanh-dai-hoc`, `pastel-geometry`, `notebook-tabs`, `daisy-days`, `scatterbrain`, `split-pastel` |
| Pitch, ra mắt sản phẩm, keynote mạnh | `bold-signal`, `bold-poster`, `broadside`, `coral`, `neo-grid-bold`, `raw-grid`, `block-frame`, `studio`, `creative-voltage`, `creative-mode` |
| Công nghệ, AI, lập trình | `neon-cyber`, `terminal-green`, `8-bit-orbit`, `retro-windows` |
| Sang trọng, thời trang, thương hiệu cao cấp | `dark-botanical`, `pink-script`, `editorial-tri-tone`, `vellum`, `soft-editorial` |
| Văn hóa, kể chuyện, nghiên cứu | `paper-ink`, `vintage-editorial`, `editorial-forest`, `grove`, `mat`, `biennale-yellow`, `long-table` |
| Thủ công, cộng đồng, sáng tạo vui | `capsule`, `playful`, `pin-and-paper`, `retro-zine`, `sakura-chroma`, `stencil-tablet`, `peoples-platform` |
| Bản sắc Việt: Tết, văn hóa, du lịch, thương hiệu Việt | `son-mai` (nền tối, sơn son thếp vàng), `dong-ho` (giấy dó, tranh khắc gỗ), `hoi-an` (tường vàng, đèn lồng) |
| Xu hướng 2026 | `aurora` (cực quang, AI và công nghệ), `bento-light` (thẻ trắng kiểu Apple, báo cáo sản phẩm), `bauhaus` (hình học nguyên sắc, giáo dục thiết kế), `restorative` (màu đất chữa lành, sức khỏe, nhân sự), `wabi` (tối giản Nhật, nghiên cứu, chiêm nghiệm) |
| Dịp đặc biệt | `art-deco` (gala, trao giải, tất niên), `clay-3d` (đất nặn 3D, trẻ em, edtech) |

## Gợi ý chọn 3 bản xem trước
- 1 bản **an toàn** trong nhóm đúng mục đích (ví dụ doanh nghiệp: `swiss-modern` hoặc `blue-professional`; sinh viên: `xanh-dai-hoc`).
- 1 bản **khác nền**: nếu bản an toàn nền sáng thì lấy một bản nền tối (`scheme` trong index.json) và ngược lại.
- 1 bản **cá tính** theo chủ đề nội dung (công nghệ, thời trang, cộng đồng...).
- Bài nói dày chữ, khán giả lớn tuổi: tránh style chữ viết tay hoặc chữ in hoa toàn bộ (`retro-zine`, `coral`, `studio`, `peoples-platform`, `scatterbrain`).

## Lưu ý riêng
- `xanh-dai-hoc` có thêm 4 tư thế `dh1..dh4` tái tạo một mẫu PowerPoint Morph 4 slide (dùng `data-pose="dh1"` .. `"dh4"`).
- `bold-signal` (than đen + cam) khác `signal` (navy + vàng đồng, trang trọng).
- `bento-light` đặt chữ trong thẻ trắng: slide số liệu có 2, 3 hoặc 4 số thì thẻ tự chia theo số ô.
- `aurora` dùng vệt sáng mờ (filter blur): máy chiếu yếu vẫn chạy, nhưng nên thử trước trên máy trình chiếu.
- Ký tự hiếm (≤, ≥, →) có thể không có trong font hiển thị; trình duyệt tự lấy font khác, vẫn đọc được.
