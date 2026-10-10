# 85 style: chọn theo mục đích

Dữ liệu đầy đủ (tên, nền, nhãn tâm trạng, hợp với, font) nằm ở `assets/styles/index.json`. Xem trực quan: trang thư viện style trên GitHub Pages của SlideFly.

Đổi style = thay 1 dòng `<link href=".../styles/<slug>.css">`. Mọi style dùng font có tiếng Việt và đã qua `deck.audit()` trên các deck mẫu.

## Nhóm theo mục đích

| Mục đích | Style (slug) |
|---|---|
| Doanh nghiệp, báo cáo, tư vấn | `swiss-modern`, `blue-professional`, `signal`, `monochrome`, `cobalt-grid`, `emerald-editorial` |
| Đào tạo, giáo dục, nội bộ | `xanh-dai-hoc`, `pastel-geometry`, `notebook-tabs`, `daisy-days`, `scatterbrain`, `split-pastel` |
| Pitch, ra mắt sản phẩm, keynote mạnh | `bold-poster`, `broadside`, `coral`, `neo-grid-bold`, `raw-grid`, `block-frame`, `studio`, `creative-voltage`, `creative-mode` |
| Công nghệ, AI, lập trình | `neon-cyber`, `terminal-green`, `8-bit-orbit`, `retro-windows` |
| Sang trọng, thời trang, thương hiệu cao cấp | `dark-botanical`, `pink-script`, `editorial-tri-tone`, `soft-editorial` |
| Văn hóa, kể chuyện, nghiên cứu | `paper-ink`, `vintage-editorial`, `editorial-forest`, `grove`, `biennale-yellow`, `long-table` |
| Thủ công, cộng đồng, sáng tạo vui | `capsule`, `playful`, `retro-zine`, `sakura-chroma`, `stencil-tablet`, `peoples-platform` |
| Bản sắc Việt: Tết, văn hóa, du lịch, thương hiệu Việt | `son-mai` (nền tối, sơn son thếp vàng), `dong-ho` (giấy dó, tranh khắc gỗ), `hoi-an` (tường vàng, đèn lồng) |
| Xu hướng 2026 | `aurora` (cực quang, AI và công nghệ), `bento-light` (thẻ trắng kiểu Apple, báo cáo sản phẩm), `bauhaus` (hình học nguyên sắc, giáo dục thiết kế), `restorative` (màu đất chữa lành, sức khỏe, nhân sự), `wabi` (tối giản Nhật, nghiên cứu, chiêm nghiệm) |
| Dịp đặc biệt | `art-deco` (gala, trao giải, tất niên), `clay-3d` (đất nặn 3D, trẻ em, edtech) |
| **Style hai lớp** (sân khấu CSS + minh họa SVG vẽ riêng từng slide theo `<slug>.art.md`) | `blueprint` (bản vẽ kỹ thuật, xây dựng, kiến trúc), `thuy-mac` (tranh thủy mặc, văn hóa, chiêm nghiệm), `mau-nuoc` (màu nước, thiên nhiên, kể chuyện), `iso-infographic` (khối isometric, hệ thống, quy trình), `risograph` (in hai mực lệch đăng, sáng tạo, sự kiện trẻ), `cat-giay-do` (cắt giấy đỏ, Tết, lễ hội); giải thích, đào tạo: `whiteboard`, `dataviz`, `midcentury-toon`, `one-line`; công nghệ, ra mắt: `dark-keynote`, `hologram-hud`, `pictogram`, `spy-titles`, `cel-anime-80s`; in ấn, nghệ thuật: `engraving`, `woodcut`, `halftone-dossier`, `silkscreen-poster`, `stained-glass`, `impasto`, `urban-sketch`; trẻ em, vui: `crayon-book`, `paper-popup`, `brick-toy`, `game-show`, `rubber-hose`, `scifi-toon`; game: `pixel-rpg`, `hd-2d`; hoài cổ: `silent-film`; Á Đông: `ukiyoe`, `den-long-giay` (Trung thu), `roi-bong` (múa rối bóng) |

## Gợi ý chọn 3 bản xem trước
- 1 bản **an toàn** trong nhóm đúng mục đích (ví dụ doanh nghiệp: `swiss-modern` hoặc `blue-professional`; sinh viên: `xanh-dai-hoc`).
- 1 bản **khác nền**: nếu bản an toàn nền sáng thì lấy một bản nền tối (`scheme` trong index.json) và ngược lại.
- 1 bản **cá tính** theo chủ đề nội dung (công nghệ, thời trang, cộng đồng...).
- Bài nói dày chữ, khán giả lớn tuổi: tránh style chữ viết tay hoặc chữ in hoa toàn bộ (`retro-zine`, `coral`, `studio`, `peoples-platform`, `scatterbrain`).

## Lưu ý riêng
- `xanh-dai-hoc` có thêm 4 tư thế `dh1..dh4` tái tạo một mẫu PowerPoint Morph 4 slide (dùng `data-pose="dh1"` .. `"dh4"`).
- `bento-light` đặt chữ trong thẻ trắng: slide số liệu có 2, 3 hoặc 4 số thì thẻ tự chia theo số ô.
- `aurora` dùng vệt sáng mờ (filter blur): máy chiếu yếu vẫn chạy, nhưng nên thử trước trên máy trình chiếu.
- Ký tự hiếm (≤, ≥, →) có thể không có trong font hiển thị; trình duyệt tự lấy font khác, vẫn đọc được.

## Style hai lớp (thêm ngày 11/10/2026)

34 style phỏng theo bộ style của lemo-opuscar (MIT) qua MotionFly (6 style thí điểm và 28 style mở rộng). Ngoài file CSS còn có `assets/styles/<slug>.art.md`: bản luật để vẽ một minh họa SVG riêng cho từng slide (bảng màu, nét, hình mẫu, 4 công thức: bìa, sơ đồ khái niệm, quy trình, con số). Đọc file `.art.md` trước khi dựng; chế độ đẹp và nhanh xem `SKILL.md` Bước 3. Minh họa đánh dấu `aria-hidden="true"` để `deck.audit()` cho phép tràn mép có chủ ý.
