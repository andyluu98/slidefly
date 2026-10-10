# Đề xuất dọn các style trùng của SlideFly

**Trạng thái: ĐÃ DUYỆT VÀ THỰC HIỆN (10/10/2026).** Người dùng duyệt cả 6 nhóm, nhóm 4 giữ `swiss-modern`; giữ `monochrome`, `blue-professional`, `raw-grid`. 6 style nghỉ (`cartesian`, `mat`, `bold-signal`, `electric-studio`, `pin-and-paper`, `vellum`) đã chuyển vào các thư mục `_backup/` trên máy, không xóa.

Phạm vi: 57 style cũ (số 01 tới 57 trong `skill/slidefly/assets/styles/index.json`). 6 style hai lớp mới (58 tới 63: blueprint, thuy-mac, mau-nuoc, iso-infographic, risograph, cat-giay-do) không đưa vào diện gộp.

## 1. Tóm tắt

| Hạng mục | Số lượng |
|---|---|
| Style xét | 57 |
| Nhóm trùng đề xuất gộp | 6 (4 nhóm độ tin cậy cao, 2 nhóm trung bình) |
| Style đề xuất cho nghỉ | 6 |
| Style cũ còn lại sau khi gộp | 51 |
| Tổng thư viện sau khi gộp (cộng 6 style hai lớp) | 57 (từ 63) |
| Cụm gần nhau nhưng đề xuất giữ cả hai | 3 cụm (mục 4) |
| Style yếu cần lưu ý | 4, trong đó 2 đã nằm sẵn trong danh sách nghỉ (mục 5) |

Style đề xuất cho nghỉ: `cartesian` (15), `mat` (25), `bold-signal` (44), `electric-studio` (01), `pin-and-paper` (29), `vellum` (41).

## 2. Cách làm

1. Ghép bảng ảnh bìa và slide 4 của 57 style, nhìn bằng mắt: `p0/sheet-all.jpg` (và 4 bảng chia nhỏ `sheet-part1..4.jpg` cho dễ đọc).
2. Trích token từ khối `.deck-stage` của mỗi file CSS (`--bg`, `--fg`, `--accent`, `--font-display`, `--font-body`, danh sách `--actors`) vào `p0/features.json`. Tính khoảng cách màu Lab (ΔE) và trùng font giữa mọi cặp (`p0/pairs.json`).
3. Vì nhiều style đặt màu nền ở từng bố cục chứ không ở token gốc (nhiều ô token trống), em tính thêm ΔE theo màu chủ đạo lấy từ ảnh chụp (`p0/imgsim.json`). Số liệu chỉ dùng để gợi ý cặp ứng viên; quyết định cuối dựa trên nhìn bìa và slide 4 cạnh nhau.
4. Chưa đo tương phản chữ bằng công thức WCAG. Nhận xét "chữ rõ, chữ nhạt" là nhìn bằng mắt ở 1280x720.

Thư mục nháp: `C:/Users/Admin/AppData/Local/Temp/claude/F--GitHub-Video-ai-claude/473767e5-0d60-4271-8ab1-c058e1a3b1b8/scratchpad/p0/` (thư mục tạm của phiên, có thể bị hệ thống dọn; cần giữ ảnh thì chép ra chỗ khác).

## 3. Sáu nhóm đề xuất gộp

Ghi chú về số đo: "nền ΔE" là khoảng cách Lab giữa hai màu nền chủ đạo trên ảnh bìa (dưới 5 gần như mắt thường không phân biệt, 5 tới 15 hơi lệch, trên 15 thấy rõ).

### Nhóm 1: be tối giản có vòng tròn mảnh (tin cậy cao)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 15 | `cartesian` | **Nghỉ** |
| 55 | `wabi` | **Giữ** |

- **Vì sao giống:** nền be gần như trùng (`#ede9e0` và `#f5f0ea`, nền ΔE 3.0), chữ đen, hình chủ đạo đều là vòng tròn nét mảnh bên phải bìa, đường kẻ mảnh, tiêu đề serif nhẹ cỡ lớn, bố cục chữ bên trái. Khoảng cách trung bình theo ảnh của cặp này là thấp nhất trong 1596 cặp.
- **Khác:** `cartesian` dùng Playfair Display + Inter, 8 diễn viên, không có màu nhấn; `wabi` dùng Noto Serif + Be Vietnam Pro, 4 diễn viên, có dấu triện đỏ `#c8102e` và vòng "enso" đậm hơn.
- **Lý do giữ `wabi`:** có một điểm nhấn đỏ làm điểm nhìn, vòng tròn đậm nên bìa không bị trống; `cartesian` ở slide 4 là khung xám lớn trống, chữ gạch đầu dòng nhạt.
- **Ảnh nhóm:** `p0/nhom-1.jpg`

### Nhóm 2: xanh rừng đậm kèm tấm kem (tin cậy cao)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 23 | `grove` | **Giữ** |
| 25 | `mat` | **Nghỉ** |

- **Vì sao giống:** nền xanh rừng gần như cùng một màu (`#1a2b1b` và `#252f27`, nền ΔE 7.2), chữ kem, slide nội dung đều là nền xanh với một tấm kem phủ bên phải, đường kẻ mảnh màu cam đất, cùng dùng Be Vietnam Pro cho chữ thân, có 3 tên diễn viên trùng (`alt`, `rule`, `mark`).
- **Khác:** `grove` dùng Playfair Display và hình vòng tròn đồng tâm; `mat` dùng Bricolage Grotesque đậm và vệt sáng nâu gỗ.
- **Lý do giữ `grove`:** vòng đồng tâm là dấu riêng, serif trang nhã nên khác hẳn các style sans đậm; `mat` ở bìa là tấm kem trơn và nửa vòng tròn, dễ lẫn với `grove`.
- **Không bị gộp theo:** `editorial-forest` (xanh lá kèm hồng) và `art-deco` (xanh đen kèm vàng kim) khác rõ về màu và hình, giữ nguyên.
- **Ảnh nhóm:** `p0/nhom-2.jpg`

### Nhóm 3: cam kèm than đen, sans đậm (tin cậy cao)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 13 | `broadside` | **Giữ** |
| 44 | `bold-signal` | **Nghỉ** |

- **Vì sao giống:** màu cam gần nhau (`#e85d26` và `#ff5722`, bìa ΔE 11.6), slide nội dung đều là nền than `#111` tới `#222` với một mảng cam bên phải, tiêu đề sans đậm, gạch cam nhỏ dưới tiêu đề.
- **Khác:** `broadside` dùng Barlow với vệt gạch chéo lớn; `bold-signal` dùng Be Vietnam Pro + Space Grotesk với thẻ cam có đổ bóng và khung vuông ở góc.
- **Lý do giữ `broadside`:** gạch chéo là dấu riêng rất dễ nhận, chữ chắc; `bold-signal` slide 4 nền xám than hơi nhợt và hình chung chung hơn.
- **Lưu ý:** `references/style-presets.md` dòng 31 đang có ghi chú so sánh `bold-signal` với `signal`; khi nghỉ phải bỏ ghi chú đó. `studio` cũng dùng Barlow chữ in hoa nhưng màu vàng trên đen, khác tâm trạng, giữ.
- **Ảnh nhóm:** `p0/nhom-3.jpg`

### Nhóm 4: trắng kèm một mảng màu lớn và khối đen (tin cậy cao về cấu trúc, khác màu nhấn)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 42 | `swiss-modern` | **Giữ** |
| 01 | `electric-studio` | **Nghỉ** |

- **Vì sao giống:** nền trắng (nền ΔE 0), chữ đen `#0a0a0a`, cùng một công thức: bìa trắng, tiêu đề sans đậm, một mảng màu bão hòa chiếm khoảng một phần ba và một khối đen ở góc, slide 4 nền trắng với khối đen chứa icon. Chỉ khác màu nhấn: đỏ cam `#ff3300` và xanh `#4361ee`.
- **Khác:** `swiss-modern` có lưới 12 cột mờ và hình tròn; `electric-studio` có dấu ngoặc góc.
- **Lý do giữ `swiss-modern`:** có lưới và hình tròn nên có nét riêng. Nhu cầu màu xanh vẫn còn đủ ở `blue-professional`, `bento-light`, `xanh-dai-hoc`.
- **Cần người dùng cân nhắc:** `electric-studio` là style số 01, đứng đầu danh sách, và được nêu trong nhóm "Doanh nghiệp" của `style-presets.md`. Nếu muốn giữ một style trắng xanh kiểu tương phản cao thì giữ `electric-studio` và cho `swiss-modern` nghỉ cũng chấp nhận được, hai style đổi chỗ cho nhau.
- **Ảnh nhóm:** `p0/nhom-4.jpg`

### Nhóm 5: giấy ghi chú ghim lên nền (tin cậy trung bình)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 36 | `scatterbrain` | **Giữ** |
| 29 | `pin-and-paper` | **Nghỉ** |

- **Vì sao giống:** cùng ý tưởng tờ giấy hoặc note ghim lên nền, màu vàng làm chủ đạo (`#fdd652` và `#e4da6c`, bìa ΔE 16.8), có kim ghim, tem hoặc nhãn nhỏ, cùng dùng font viết tay Patrick Hand, chữ thân đọc ổn.
- **Khác:** `scatterbrain` là bảng nút chai với nhiều note nhiều màu (Lobster + Roboto Slab); `pin-and-paper` là một tập giấy vàng nét mực xanh (Space Grotesk + Patrick Hand).
- **Lý do giữ `scatterbrain`:** nhiều màu và nhận diện mạnh hơn, slide 4 có thêm ghi chú xanh. `pin-and-paper` có thể coi là phiên bản nền vàng phẳng hơn của cùng ý tưởng.
- **Độ tin cậy trung bình vì:** bề ngoài hai style khác nhau khá rõ (nền nút chai và nền vàng); gộp là do ý tưởng trùng, không phải do ảnh gần giống.
- **Ảnh nhóm:** `p0/nhom-5.jpg`

### Nhóm 6: xanh navy kèm serif nghiêng (tin cậy trung bình)

| | Style | Giữ / Nghỉ |
|---|---|---|
| 37 | `signal` | **Giữ** |
| 41 | `vellum` | **Nghỉ** (cũng có trong danh sách yếu) |

- **Vì sao giống:** nền navy (`#1c2546` và `#29386f`, nền ΔE 16.1), serif có nghiêng nhấn vàng đồng, khung hoặc vòng nét mảnh, cùng nằm trong nhóm "trang trọng, học thuật" của `style-presets.md`. Cả hai đều có phụ đề nhỏ màu nhạt.
- **Khác:** `signal` tối hơn, có tấm kem và vòng tròn nét mảnh làm điểm nhìn (Source Serif 4); `vellum` nền phẳng một màu, bìa chỉ có tiêu đề vàng nghiêng và một khung mờ (Cormorant Garamond).
- **Lý do giữ `signal`:** bìa có hình, slide 4 có tấm kem tạo điểm nhấn. `vellum` bìa trống, phụ đề và khung nhạt.
- **Độ tin cậy trung bình vì:** `vellum` có xanh dương sáng hơn `signal`; nếu muốn giữ gam xanh dương sáng này thì giữ `vellum` và cho `signal` nghỉ.
- **Ảnh nhóm:** `p0/nhom-6.jpg`

## 4. Các cụm gần nhau nhưng đề xuất GIỮ cả hai

Những cặp này có số liệu hoặc hình dáng gần, em đã so ảnh và thấy khác đủ để không gộp. Ghi lại để người dùng thấy đã được cân nhắc.

| Cụm | Giống | Vì sao giữ | Ảnh |
|---|---|---|---|
| `neo-grid-bold` (27) và `raw-grid` (32) | nền trắng kem, chữ đen in hoa, ô khối kiểu lưới | `neo-grid-bold` có vàng chanh, mã QR, chữ mono; `raw-grid` có hồng và xanh nhạt, mũi tên. Nếu cần gọn hơn nữa thì ứng viên nghỉ là `raw-grid` | `p0/nhom-7.jpg` |
| `clay-3d` (57), `pastel-geometry` (04), `split-pastel` (05) | nền pastel, bố cục thẻ giữa hoặc chia đôi, bo tròn; `pastel-geometry` và `split-pastel` cùng Plus Jakarta Sans | `clay-3d` có khối đất nặn 3D riêng; `split-pastel` có bố cục chia đôi và bong bóng chat; `pastel-geometry` đang được `templates/deck-giao-dien.html` dùng nên nghỉ sẽ phải đổi template | `p0/nhom-8.jpg` |
| `soft-editorial` (38), `restorative` (54), `vintage-editorial` (06) | nền be kem, hình mềm, serif | mỗi style khác hình chủ đạo (hình chữ nhật pastel, khối hữu cơ, khung viền); `soft-editorial` đang được 2 template (`deck-bo-cuc.html`, `deck-khung.html`) dùng | `p0/nhom-9.jpg` |

Các cặp khác đã xét và để nguyên vì khác rõ: `broadside` với `studio` (chung Barlow nhưng khác màu và hình), `coral` với `capsule` (màu nhấn đỏ san hô gần nhau nhưng hình khác hẳn), `bauhaus` với `creative-mode` và `stencil-tablet` (đều hình học nguyên sắc nhưng bố cục khác), `neon-cyber`, `aurora`, `8-bit-orbit`, `terminal-green` (cùng nền tối công nghệ nhưng mỗi style một tâm trạng), `blue-professional`, `bento-light`, `monochrome` (nền sáng nhạt nhưng khác hình).

## 5. Style chất lượng yếu

Không có style nào có chữ không đọc được (nhìn ở 1280x720). Bốn style đáng lưu ý vì nhạt hoặc ít điểm nhấn:

| Style | Vấn đề | Đề xuất |
|---|---|---|
| `cartesian` (15) | slide 4 có khung xám lớn trống, gạch đầu dòng nhạt, bìa gần như không có màu | Nghỉ (nhóm 1) |
| `vellum` (41) | bìa trống, phụ đề và khung mảnh nhạt trên nền xanh | Nghỉ (nhóm 6) |
| `monochrome` (26) | rất nhạt: nền vàng nhạt, đường kẻ xám, không màu nhấn; nội dung đọc được nhưng bìa ít điểm nhìn | Chưa đề xuất nghỉ; để người dùng quyết |
| `blue-professional` (11) | bìa rộng và nhạt, hình chung chung (một chấm xanh trên nền xám) | Chưa đề xuất nghỉ; để người dùng quyết |

## 6. Chỗ phải sửa khi gộp

Áp cho từng style nghỉ (`cartesian`, `mat`, `bold-signal`, `electric-studio`, `pin-and-paper`, `vellum`). Theo quy tắc của máy, không xóa: các file chuyển vào thư mục `_backup/` cạnh file gốc.

### 6.1. File riêng của từng style (chuyển vào `_backup/`)

| Loại | Đường dẫn |
|---|---|
| CSS | `skill/slidefly/assets/styles/<slug>.css` (6 file) |
| Deck demo | `gallery/15_demo-cartesian.html`, `gallery/25_demo-mat.html`, `gallery/44_demo-bold-signal.html`, `gallery/01_demo-electric-studio.html`, `gallery/29_demo-pin-and-paper.html`, `gallery/41_demo-vellum.html` |
| Ảnh chụp | `gallery/anh/<slug>-1.jpg` và `gallery/anh/<slug>-4.jpg` (12 file) |

Số thứ tự các file demo còn lại sẽ có chỗ trống (ví dụ không còn 15, 25...). `site/build-gallery.py` đọc số từ tên file nên vẫn chạy; không cần đổi tên file còn lại.

### 6.2. Dữ liệu và trang sinh tự động

| File | Chỗ sửa |
|---|---|
| `skill/slidefly/assets/styles/index.json` | xóa 6 mục: `electric-studio` (dòng 3), `cartesian` (dòng 185), `mat` (dòng 315), `pin-and-paper` (dòng 367), `vellum` (dòng 523), `bold-signal` (dòng 560) |
| `gallery/00-gallery.html` | **không sửa tay**, chạy lại `python site/build-gallery.py` (sinh lại thẻ, số 63 thành 57 ở dòng 21) |
| `index.html` | cũng do `site/build-gallery.py` sinh lại phần kệ style và số đếm (theo ghi chú đầu file script). Sau khi chạy phải rà lại các chỗ có "63 style": dòng 7, 9, 54, 150, 176, 341; nếu script không đổi hết thì sửa tay |
| `docs/gallery.jpg` | ảnh ghép dùng ở README và thẻ og:image, cần chụp lại sau khi dọn |

Lưu ý: hiện cây làm việc đang có thay đổi chưa commit ở `gallery/00-gallery.html`, `index.html`, `site/landing.js`, `site/sections.css` và `site/build-gallery.py` chưa theo dõi. Nên commit hoặc chốt các thay đổi đó trước khi dọn style, để khỏi lẫn.

### 6.3. Tài liệu viết tay

| File | Dòng | Việc |
|---|---|---|
| `README.md` | 3, 5, 7, 17, 80, 85 | đổi "63 style" thành "57 style" (dòng 85 là "63 deck demo" thành 57). Dòng 17 chia nguồn "12 preset và 34 bold template, 1 mẫu Morph, 10 style mới, 6 style hai lớp": phải đếm lại phần "12 preset" và "34 bold template" sau khi trừ 6 style, em chưa tự đoán style nào thuộc nhóm nào |
| `skill/slidefly/SKILL.md` | 3 | trong `description` đổi "63 style" thành "57 style" |
| `skill/slidefly/references/style-presets.md` | 1 | tiêu đề "63 style" thành "57 style" |
| | 11 | bỏ `electric-studio`, `cartesian` khỏi hàng "Doanh nghiệp, báo cáo, tư vấn" |
| | 13 | bỏ `bold-signal` khỏi hàng "Pitch, ra mắt sản phẩm" |
| | 15 | bỏ `vellum` khỏi hàng "Sang trọng, thời trang" |
| | 16 | bỏ `mat` khỏi hàng "Văn hóa, kể chuyện" |
| | 17 | bỏ `pin-and-paper` khỏi hàng "Thủ công, cộng đồng" |
| | 31 | bỏ ghi chú so sánh `bold-signal` với `signal` |
| `skill/slidefly/references/layouts.md` | 211, 239 | câu "đã kiểm trên cả 57 style" là kết quả kiểm cũ, cần quyết định giữ nguyên hay kiểm lại; không phải lỗi, chỉ là con số lịch sử |

### 6.4. Đã kiểm tra, KHÔNG bị ảnh hưởng

- `examples/ai-agent-stencil-tablet-20-slide.html` và `examples/ai-agent-swiss-15-slide.html` dùng `stencil-tablet` và `swiss-modern`, đều được giữ.
- `skill/slidefly/templates/deck-giao-dien.html` (dùng `pastel-geometry`), `deck-bo-cuc.html` và `deck-khung.html` (dùng `soft-editorial`): cả hai style này đều không nằm trong danh sách nghỉ.
- `skill/slidefly/scripts/pick-styles.py` đọc `index.json` nên tự cập nhật; không có tên 6 style này viết cứng trong script.
- `THIRD_PARTY.md` và các file `.art.md`: không nhắc tới 6 style nghỉ.
- Không file CSS nào `@import` một trong 6 style nghỉ (chỉ có chữ "mat frame" trong ghi chú của `vellum.css`, không liên quan).

## 7. Quyết định cần người dùng

1. Duyệt cả 6 nhóm, hay chỉ 4 nhóm tin cậy cao (1 tới 4) trước, để nhóm 5 và 6 lại cân nhắc?
2. Nhóm 4: giữ `swiss-modern` hay `electric-studio`?
3. `monochrome` và `blue-professional`: giữ hay cho nghỉ?
4. Cụm cần gọn hơn nữa (mục 4): có muốn cho `raw-grid` nghỉ không?

## Nguồn dữ liệu kiểm chứng

| Số liệu | Nguồn |
|---|---|
| Danh sách 57 + 6 style, mô tả, font | `skill/slidefly/assets/styles/index.json` (63 mục, 6 mục cuối có `art: true`) |
| Token màu, font, diễn viên | khối `.deck-stage` trong `skill/slidefly/assets/styles/<slug>.css`, lưu ở `p0/features.json` |
| Nền ΔE, màu chủ đạo | em tự tính từ `gallery/anh/<slug>-1.jpg` và `-4.jpg` (lượng tử hóa 5 màu, khoảng cách Lab CIE76), lưu ở `p0/imgsim.json` |
| Hạng khoảng cách ảnh (cặp `cartesian` và `wabi` đứng thứ 1 trong 1596 cặp) | em tự tính, `p0/imgsim.json` |
| Dòng tham chiếu cần sửa | tìm bằng grep trên toàn repo ngày 10/10/2026 (số dòng đúng với trạng thái làm việc lúc đó) |
| Ảnh nhóm | `p0/nhom-1.jpg` tới `p0/nhom-9.jpg`; ảnh toàn bộ `p0/sheet-all.jpg` |
