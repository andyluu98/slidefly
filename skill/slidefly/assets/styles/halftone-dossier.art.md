# Hồ sơ halftone: luật vẽ minh họa SVG cho từng slide

Dùng cùng `halftone-dossier.css`. Lớp sân khấu (diễn viên) đã lo giấy kem, bìa hồ sơ, ảnh dán, băng keo, kẹp giấy, thước và con dấu; file này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, như một "vật chứng" nằm trong hồ sơ. Deck mẫu: `gallery/72_demo-halftone-dossier.html`.

## 1. Tinh thần
- **Cả deck là một hồ sơ in kiểu truyện tranh cũ:** giấy kem, mực navy đậm, vài mực phẳng (xanh cobalt, hồng, vàng) và một màu đỏ riêng cho con dấu. Nghiêm trang ở khung (số hồ sơ, vật chứng, nhãn), vui ở nội dung.
- **Độ đậm nhạt chỉ làm bằng chấm tram**, không gradient: chấm to dần là tối dần, chấm biến mất là sáng. Hai lớp chấm khác góc chồng nhau tạo cảm giác "in".
- **Nhân vật và vật chắc, viền navy dày 7px, tô phẳng**; mắt bóng (một elip trắng viền navy, một đồng tử, hai điểm sáng) để vật có hồn. Vật chính của bìa được phép có mắt; phần còn lại (sơ đồ, bảng) thì không.
- Khác `retro-zine` (giấy kaki, xanh lá với đen, cắt dán) và `pin-and-paper` (ghim, giấy nhớ): ở đây là nét dày kiểu truyện tranh, chấm tram có mật độ theo vùng, ảnh vật chứng và nhãn tiếng Việt.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Biến CSS | Ghi chú |
|---|---|---|
| Mực, mọi nét viền, chữ | `var(--ink)` | viền dày 4 đến 7px, đầu nét tròn |
| Giấy trắng (thẻ, ảnh) | `var(--paper-2)` | nền của vật chứng |
| Xanh cobalt | `var(--cobalt)` | mảng lớn, tram nền, vật chính thứ hai |
| Hồng | `var(--pink)` | mũi tên, chấm bóng đổ, lệch đăng |
| Vàng | `var(--yellow)` | nhãn dán, thẻ, huy hiệu |
| Đỏ | `var(--red)` | chỉ cho con dấu và trạm kết (phán quyết) |

- Tô màu bằng **lớp trong khối `<style>` của deck** (`.ht-cobalt { fill: var(--cobalt) }`), không ghi `fill="var(...)"` trong thuộc tính (script xuất PPTX chỉ đọc màu từ lớp).
- **Chấm tram vẽ gọn:** mỗi chấm là một nét dài 0,1px đầu tròn, gom theo cỡ vào một `<path>`; độ dày nét chính là đường kính chấm. Khoảng cách 11 đến 22px, góc 45 độ cho tram chính, 15 hoặc 75 độ cho lớp thứ hai.
- **Bóng đổ lệch đăng:** cùng hình đó tô `var(--ink)` mờ 28%, lệch (+6, +7)px, vẽ trước hình; tiêu đề đã có sẵn bóng hồng nên không thêm vào hình.
- Chữ trong SVG: nhãn ngắn `var(--font-mono)` (JetBrains Mono 800) hoặc `var(--font-display)` (Alfa Slab One), 17 đến 28px. Dấu tiếng Việt đủ.
- Mọi `id` trong SVG phải duy nhất trong cả deck (tiền tố theo số slide).

## 3. Bộ hình mẫu lặp lại
**Dải chấm tram** (ba bậc to dần = tối dần):
```svg
<path d="M20 20h.1M42 20h.1M64 20h.1" stroke="#1b2144" stroke-width="5" stroke-linecap="round" fill="none"/>
<path d="M31 36h.1M53 36h.1" stroke="#1b2144" stroke-width="8" stroke-linecap="round" fill="none"/>
```
**Mắt bóng** (để vật chính có hồn):
```svg
<ellipse cx="332" cy="277" rx="13" ry="15" fill="#fffdf5" stroke="#1b2144" stroke-width="4"/>
<ellipse cx="334" cy="279" rx="6.5" ry="9" class="ht-i"/><circle cx="337" cy="274" r="3.2" fill="#fffdf5"/>
```
**Nhãn số vật chứng:** vòng vàng bán kính 19 viền navy 4px, số `var(--font-num)` 22px ở giữa; cùng số là cùng một vật.
**Thẻ vật chứng:** hình chữ nhật bo góc 10, tô vàng hoặc giấy trắng, viền 6px, tram navy ở góc dưới phải; tư thế cũ là cùng hình viền đứt `stroke-dasharray: 11 8`.
**Mũi tên hồng dày:** nét `.ht-arrow` 11px kèm mũi tên tam giác tô hồng; mũi tên chỉ ra "đi từ A sang B", không trang trí.
**Nhãn chip:** hình viên thuốc vàng 140x30 chữ mono 17px in hoa, đặt dưới vật để gọi tên ("THOÁNG", "VỪA", "DÀY").
**Ảnh dán nhỏ** (vật chứng thứ hai, thẻ người, hình minh họa trong ghi chú): khung giấy trắng viền navy 5px, bóng lệch (+8, +10), cửa sổ ảnh có tram một mực, nhãn đáy chữ in hoa; nghiêng 3 đến 7 độ, một mảnh băng keo vàng ở một góc.
**Con dấu:** hộp bo góc hai viền đỏ (8px và 3px), chữ in hoa đậm, rắc vài chấm giấy để mực không đều; xoay 7 đến 12 độ, chỉ ở góc hoặc ngoài chữ. Nội dung dấu viết tiếng Việt, ngắn: TUYỆT MẬT, ĐÃ ĐÓNG HỒ SƠ, ĐÃ DUYỆT.
**Vệt tốc độ:** ba nét ngắn song song (9px, đầu tròn) phía sau vật đang chuyển động; không dùng cho vật đứng yên.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Ảnh dán (`photo`, x 1170, y 230, rộng 520, cao 620, xoay -3 độ) nằm trên bìa hồ sơ `folder`. SVG đặt đúng khung ảnh (left 1170, top 230, 520x620) và nghiêng cùng ảnh bằng `<g transform="rotate(-3 260 310)">`.
- Cửa sổ ảnh là x 28 đến 484, y 28 đến 498 (bầu trời tram xanh, mặt trời vàng, đồi navy đã có sẵn); vẽ vật chính trong vùng này, cách mép ít nhất 30px.
- Lớp vẽ: vài nét chạy tốc độ, hai đa giác phẳng của vật (một trắng, một cobalt có tram navy), viền, đường gấp, mắt. Không chữ trong hình; nhãn "VẬT CHỨNG A" đã ở mép ảnh.
**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Trên slide `content`, hình nằm trong bìa hồ sơ `folder` (x 1230 đến 1840, y 282 đến 982): SVG left 1260, top 372, rộng 540, cao 600.
- Chừa dải y 560 đến 680 cho `hl-text`. Nửa trên: tư thế cũ viền đứt, tư thế mới thẻ vàng có tram và một đĩa cobalt, nối bằng mũi tên hồng, nhãn số vàng.
- Nửa dưới: bảng kê khung trắng, hàng đầu navy chữ giấy (SỐ, TÊN, DẤU), mỗi hàng một nhãn số, tên và một dấu hiệu.
**c. Quy trình hoặc dòng thời gian.** Diễn viên `ruler` nằm ngang (x 120 đến 1800, y 602 đến 658) làm trục; SVG left 120, top 560, cao 140, trạm ở x = 136 + i x 342,4.
- Trạm là huy hiệu tròn bán kính 30, viền navy 6px, **mỗi huy hiệu thêm một bậc tram** (trơn, 55%, 65%, 75% rồi dấu tích); cuối cùng tô đỏ vì là phán quyết.
- Mũi tên hồng cong cao tối đa 34px phía trên thước. Ẩn chấm mặc định bằng `.step::before { display: none; }` (đã có trong style).
**d. Con số hoặc so sánh.** Trên slide `stats`, dải y 836 đến 986, mỗi cột một "tờ vật chứng" 220x104 tâm tại x 384, 960, 1536.
- Trong tờ là các thanh navy bo tròn thay dòng chữ: 3 thanh dày, 5 thanh vừa, 7 thanh mảnh, kèm chấm hồng đầu dòng. Dưới tờ là nhãn chip vàng.
- Đĩa tram hồng phía sau con số giữa là của diễn viên `dots`; không vẽ thêm trong hình.

## 5. Chuyển động và xuất PPTX
- Cả hình bọc trong `<g class="reveal">` để hiện sau diễn viên. **Không đặt thuộc tính `transform` trực tiếp lên phần tử có lớp `reveal`** (CSS của lớp này ghi đè và mất vị trí): bọc thêm một `<g transform>` bên trong.
- Nét có `stroke` (mũi tên, đường dẫn) có thể vẽ dần: `class="draw" pathLength="1"` với `style="--d:.3"` (cần `morph-motion.css`); tram và hình tô thì không.
- Không animation lặp, không rung. Con dấu đã có hiệu ứng đóng dấu riêng khi diễn viên vào.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì thành hình vector. Chấm tram dạng nét 0,1px vẫn sang được. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.

## Kiểm trước khi giao
- Phóng ảnh chụp lên 100%: chấm tram đều, không bị dính thành mảng bùn; viền navy liền, không đứt.
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, con dấu không đè lên chữ.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`.
- Rà màu trong SVG: chỉ các lớp `ht-*` và `var(--ink)`, `var(--paper-2)`, `var(--cobalt)`, `var(--pink)`, `var(--yellow)`, `var(--red)`.

## 6. Cấm
- Gradient mượt (chỉ có tram), bóng đổ mờ, 3D, ánh kim, màu ngoài bảng.
- Màu đỏ ngoài con dấu và trạm kết; hai họ tram dày chồng lên chữ.
- Hình đè lên chữ, hay cho nét chạy qua hàng tiêu đề.
- Số liệu bịa trên thẻ, nhãn hay bảng kê: dùng số thứ tự (1, 2, 3), "A", "B" hoặc chữ ngắn.
- Logo, tên người hay vụ án có thật; con dấu giả cơ quan nhà nước.
- Đặt mắt lên mọi vật: chỉ vật chính của bìa (hoặc một vật nhân hóa có chủ đích).

Phỏng theo lemo-opuscar `styles/halftone-dossier/STYLE.md` (MIT) qua MotionFly.
