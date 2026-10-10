# Hoạt hình giữa thế kỷ (midcentury-toon): luật vẽ minh họa SVG cho từng slide

Dùng cùng `midcentury-toon.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một "tấm thẻ hướng dẫn" của phim lớp học thập niên 50. Deck mẫu: `gallery/88_demo-midcentury-toon.html`.

## 1. Tinh thần
- Cả deck là **một tờ giấy in màu phẳng**: mỗi mảng màu là một "cel" in lệch khỏi nét mực 4 đến 7 px (xuống phải), nên hình luôn có khe giấy hở ở mép trên trái và có vệt màu thò ra ở mép dưới phải.
- **Hình học thay cho chi tiết:** vật là hộp bo tròn, đĩa, bumerang, sao nổ, tia nắng. Không đổ bóng chuyển sắc, không 3D, không ảnh.
- **Một hình, một ý, có đánh số:** huy hiệu tròn số 1, 2, 3 nối vào vật bằng đường dẫn mảnh, như sách hướng dẫn máy móc thời đó. Người trình bày đọc theo số.
- **Vật được vẽ, không phải người.** Minh họa là đồ dùng (máy chiếu, màn, thẻ, hình khối). Không vẽ nhân vật có sẵn của hãng phim nào, không chép chữ ký hay logo.
- Khác `retro-windows` (cửa sổ máy tính) và `pastel-geometry` (hình khối phấn không nét mực): ở đây luôn có **nét mực nâu đen** và **màu lệch đăng**.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Biến CSS | Dùng cho |
|---|---|---|
| Nét mực | `var(--ink)` #261D18 | mọi đường viền, chữ, huy hiệu |
| Giấy, thẻ | `var(--paper)`, `var(--cream)` | thân vật sáng, thẻ, chữ trên nền ngọc |
| Cam cháy | `var(--orange)` | vật chính, chấm bullet, mặt trời |
| Xanh ngọc | `var(--teal)`, `var(--teal-deep)` | mảng nền của hình (như mảng màu của phim), bóng đổ lệch của thẻ |
| Vàng mù tạt | `var(--mustard)` | sao nổ, mặt bàn, tia sáng, bóng lệch phụ |

- **Ba màu cộng mực, không thêm hue khác.** Không neon, không đen tuyền, không trắng tinh.
- Nét: 4 px cho đường bao vật, 2,5 px cho chi tiết, 3,5 px cho mũi tên cong (nét đứt `10 8`). Đầu nét và góc nét `round`. Thanh chữ giả dùng nét 7 px đầu tròn.
- **Lệch đăng:** vẽ mảng màu trước, bọc `<g class="mc-o" transform="translate(6 5)">`, rồi vẽ nét mực cùng đường dẫn lên trên, không tô. Mảng nền lớn (thẻ ngọc) lệch 7 đến 8 px, vật nhỏ lệch 3 đến 4 px.
- Tô màu bằng **class trong khối `<style>` của deck** (`.mc-o`, `.mc-t`, `.mc-m`, `.mc-c`, `.mc-k`, nét `.mc-l`, `.mc-lt`, `.mc-bar`), không ghi `fill="var(...)"` trong thuộc tính để bản PPTX đọc được màu.
- Chữ trong hình: tiêu đề nhãn dùng `var(--font-display)` (Alfa Slab One, in hoa, 19 đến 25 px); mô tả ngắn dùng `var(--font-body)` đậm 20 px. Chữ sáng (kem) chỉ đặt trên nền ngọc, chữ mực đặt trên thẻ kem.

## 3. Bộ hình mẫu lặp lại
**Bumerang** (bóng dáng của style, thân ống cong có hai đầu tròn), đặt vào hộp 100x100:
```svg
<g transform="translate(298 66) scale(1.75) rotate(14 50 50)">
  <g class="mc-o" transform="translate(4 4)"><path d="M..."/></g><path class="mc-l" d="M..."/></g>
```
Đường dẫn bumerang lấy nguyên từ deck mẫu (hình 2, `TƯ THẾ B`); phiên bản "bóng ma" của tư thế cũ dùng `class="mc-gh"` (nét đứt kem, không tô).

**Huy hiệu số** (vị trí khuyên dùng ở góc vật, nối đường dẫn kem hoặc mực):
```svg
<g class="fx fx-pop mc-pop"><circle class="mc-k" cx="60" cy="356" r="24"/>
  <circle class="mc-lc" style="stroke-width:2" cx="60" cy="356" r="18"/>
  <text class="mc-n" x="60" y="365" text-anchor="middle">1</text></g>
```
**Thẻ nổi bóng lệch** (khung chữ, thẻ slide thu nhỏ): hình chữ nhật bo 10 đến 14 px, bóng ngọc hoặc mù tạt lệch (6, 5), viền mực 4 px, nền kem.
**Sao 4 cánh** (lấp lánh, nơi chuyển biến) và **sao nổ 14 đến 16 cánh** (kết quả, đích đến, trạm cuối): mù tạt lệch, viền mực.
**Mũi tên cong kiểu sách hướng dẫn:** cung bậc hai, nét đứt, đầu mũi tên đặc mực; đặt đỉnh cung cao 30 đến 50 px so với hai điểm nối.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở trái (x 120 đến 1040). Hình nằm trong x 1120 đến 1840, y 180 đến 780, đặt **đúng lên mảng ngọc** của diễn viên `plane` (x 1150 đến 1810, y 190 đến 760), chân vật chạm đường chân trời (y 760 trên slide, y 580 trong SVG) của `floor`. Deck mẫu: máy chiếu slide đặt trên bàn, tia sáng kem nhạt tới tấm màn có ba hình biến đổi (tròn, bumerang, sao) nối nhau bằng cung nét đứt. Huy hiệu 1 chỉ vào máy, huy hiệu 2 chỉ vào màn. Mọi vật có mảng kem hoặc cam lệch (6, 5).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất trong vùng highlight của `content` (x 1260 đến 1800), SVG đặt tại `left:1260px; top:280px`, rộng 540, cao 700. **Chừa dải y 310 đến 390 (trong SVG) cho `hl-text`**. Nửa trên: một thẻ ngọc 540x290 như màn phim, trong đó cùng một vật ở hai tư thế (bóng ma kem và bản cam đặc), cung nét đứt đi qua sao vàng, nhãn `TƯ THẾ A/B`, ba huy hiệu số. Nửa dưới: danh sách ba thẻ kem đánh số khớp huy hiệu (y 410, 510, 610, mỗi thẻ cao 78).
- Cùng một vật thì cùng số (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.** Diễn viên `plane` ở slide `timeline` là thanh ngọc dày 28 px đúng trục y 630, nên SVG chỉ vẽ **trạm** và **mũi tên cong**. SVG đặt `left:120px; top:560px`, cao 140, trục ở y 70. Trạm tại x = 16 + i x 342,4 (5 bước): đĩa mực r 27, vòng kem r 19, chấm cam lệch r 10. Cung nối giữa hai trạm cao tối đa 36 px trên y 50 (đỉnh y 32), kèm mũi tên đặc. **Trạm cuối là sao nổ** mù tạt mang đích đến. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ nét vào vùng chữ (trên y 26, dưới y 114 trong SVG).

**d. Con số hoặc so sánh.** Slide `stats`: dải đáy y 836 đến 986 dưới ba con số, tâm cột x 384, 960, 1536. Mỗi cột một thẻ slide thu nhỏ 192x108: càng nhiều ý, thanh chữ càng mảnh (dày 9, 6, 4 px; chấm bullet nhỏ dần), cột thứ ba bị cắt đôi bằng đường đứt dọc và hai mũi tên tách ra hai bên. Sao vàng nhỏ ở góc thẻ cuối. So sánh hai phương án: hai thẻ cạnh nhau cùng cỡ, cùng bóng lệch, khác màu bóng (ngọc và cam).

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1" style="--d:.3"` (cần `morph-motion.css`). Thứ tự: đường bao vật, tới thẻ, tới cung mũi tên. Không gắn `draw` vào nét đứt vì `draw` ghi đè `stroke-dasharray`.
- Huy hiệu và sao hiện kiểu **bật ra** (`fx fx-pop mc-pop`, khai báo `.mc-pop { transform-box: fill-box; transform-origin: center; }`); nhóm có `transform="translate(...)"` thì bọc thêm một `<g>` ngoài, vì lớp `fx` ghi đè thuộc tính `transform`.
- Nhãn, danh sách, chữ phụ bọc `<g class="reveal">`. Không dùng animation lặp, không rung.
- Nhịp gợi ý: đường bao `--d:0`, thẻ `--d:.25`, huy hiệu `--d:.35 đến .7`; cả hình xong trong khoảng 2 giây.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.mc-o`), nên đặt tên lớp có tiền tố. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn, câu cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, chân vật chạm đúng đường chân trời của `floor`, hình nằm trong mảng ngọc.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ có `mc-o`, `mc-t`, `mc-m`, `mc-c`, `mc-k`, `mc-p`, `mc-d` và nét mực hoặc kem.
- Soi lệch đăng: bóng lệch (6, 5) phải thấy rõ ở 100 phần trăm phóng, nhưng không quá 8 px kẻo trông như hình sai tọa độ.
- Số huy hiệu khớp danh sách; hai huy hiệu cùng số chỉ cùng một vật.

## Mẫu nhanh khi vẽ hình mới
**Trạm quy trình** (đĩa mực, vòng kem, chấm cam lệch):
```svg
<circle class="mc-k" cx="16" cy="70" r="27"/><circle class="mc-c" cx="16" cy="70" r="19"/>
<g class="mc-o" transform="translate(3 3)"><circle cx="16" cy="70" r="10"/></g><circle class="mc-lt" cx="16" cy="70" r="10"/>
```
**Thẻ kem có bóng ngọc lệch** (thẻ ý, khung chữ):
```svg
<g class="mc-t" transform="translate(7 6)"><rect x="168" y="20" width="192" height="108" rx="10"/></g>
<rect class="mc-c" x="168" y="20" width="192" height="108" rx="10"/><rect class="mc-l" x="168" y="20" width="192" height="108" rx="10"/>
```
**Thanh chữ giả** (khi không cần chữ thật): `<path class="mc-bar" d="M208 40H320"/>`; chấm bullet đứng trước là đĩa cam r 3 đến 6 px.

## 6. Cấm
- Màu ngoài bảng, gradient trên vật, bóng đổ mờ, 3D, glow, màu neon.
- Vẽ nhân vật có sẵn của một hãng phim, chép bố cục khung hình, chữ ký hay logo thật.
- Đè hình lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165 và vùng `hl-text`.
- Nét mực sạch bong khép kín 100 phần trăm và màu khớp tuyệt đối với nét (mất chất in lệch đăng).
- Ghi số liệu bịa lên hình: dùng chữ ký hiệu (A, B, 1, 2, 3) hoặc nhãn `VÍ DỤ`.
- Câu dài trong SVG; người máy hay nhân vật có mặt thay cho vật được vẽ.

Phỏng theo lemo-opuscar `styles/midcentury-toon/STYLE.md` (MIT) qua MotionFly.
