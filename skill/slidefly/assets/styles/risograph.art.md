# Risograph: luật vẽ minh họa SVG cho từng slide

Đi kèm `risograph.css`. Lớp sân khấu (diễn viên) đã lo nền; file này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, theo đúng nội dung slide đó, trông như được in trên máy in stencil: mỗi màu là một bản in riêng, chồng lên nhau và lệch nhau vài px.

## 1. Tinh thần

- **Ít mực:** chỉ ba mực spot (hồng huỳnh quang, xanh dương, vàng) trên giấy kem. Mọi màu khác là **màu chồng** của hai mực hoặc **tram** của một mực.
- **Màu chồng tạo màu thứ ba:** hồng chồng xanh ra tím, xanh chồng vàng ra lục, hồng chồng vàng ra cam, đủ ba mực ra gần đen. Màu đậm nhất để dành cho khoảnh khắc đáng giá nhất của deck.
- **Lệch đăng (misregistration):** mỗi bản in rơi lệch 3 đến 6 px, mép hình lộ một vệt giấy hoặc một viền màu của bản kia. Lệch cố định trong một hình, không rung liên tục.
- **Hình phẳng, không nét viền:** vật là mảng màu và bóng đổ phẳng; độ sáng tối làm bằng chấm tram theo vài bậc (20, 40, 60, 100 phần trăm), mỗi mực một góc tram riêng.
- **Mực không hoàn hảo:** lỗ kim trong mảng đặc, vệt dọc theo chiều kéo giấy. Khác `retro-zine` (giấy kaki, xanh lá với đen, băng keo, con dấu) và `biennale-yellow` (một mực chàm với vàng, chữ serif, lưới gạch): ở đây là ba mực trong, chồng màu và lệch đăng.

## 2. Bảng màu, nét, chất liệu

| Vai trò | Biến CSS | Ghi chú |
|---|---|---|
| Giấy (không mực) | `var(--paper)` | khoảng trống, thẻ trắng khoét, chữ trên nền mực |
| Mực 1 hồng | `var(--pink)` | mảng lớn, đĩa mặt trời, vệt in đôi dưới tiêu đề |
| Mực 2 xanh | `var(--blue)` | đường, thanh, tram nền; mực duy nhất đủ đậm cho đường mảnh |
| Mực 3 vàng | `var(--yellow)` | dải ngang, quầng; không dùng cho chi tiết nhỏ |
| Hồng + xanh | `var(--violet)` | lõi hai bản in |
| Xanh + vàng | `var(--green)` | đồi, lá, vùng giao |
| Hồng + vàng | `var(--coral)` | vùng giao nóng |
| Đủ ba mực | `var(--ink3)` | lõi đậm nhất, dùng một lần mỗi slide |
| Tram nhạt | `var(--pink-tint)`, `var(--yellow-tint)` | nền thẻ, dải phụ |

- Tô màu bằng **class trong khối `<style>` của deck** (`.ri-p { fill: var(--pink) }`), không ghi `fill="var(...)"` trong thuộc tính: trình duyệt bỏ qua và script xuất PPTX chỉ đọc màu từ class.
- Nét: chỉ dùng cho đường dẫn, trục, vệt chấm. Xanh dày 6 px, ghost hồng dày 3 px lệch (8, 6) px. Đầu nét tròn. Vệt chấm: `stroke-dasharray: 0 20` với nét 9 px tròn đầu.
- Tram: `<pattern>` chấm tròn, ô 9 đến 16 px. Góc tram: xanh 15°, vàng 45°, hồng 75° (`patternTransform="rotate(..)"`). Một vùng tối đa hai bản in, trong đó tối đa một bản là tram.
- **Màu chồng vẽ tường minh**, không dùng `mix-blend-mode`: vẽ hình A, hình B, rồi vẽ lại hình B bằng màu chồng và cắt theo hình A bằng `clipPath`. Hình tròn lệch đăng thì vẽ nhanh: tròn xanh lệch (-5, +4), tròn hồng lệch (+5, -4), tròn màu chồng ở giữa bán kính nhỏ hơn 4 đến 5 px.
- Filter SVG nhẹ được phép trong bản HTML (hạt mực bằng `feTurbulence` độ mờ thấp) nhưng PowerPoint có thể bỏ qua; đừng để ý chính phụ thuộc vào filter.
- Mọi `id` trong SVG phải duy nhất trong cả deck: đặt tiền tố theo số slide (`ri4-hy`, `ri7-b1`).

## 3. Bộ hình mẫu lặp lại

**Đĩa hai bản in lệch đăng** (diễn viên, điểm nhấn, nút quy trình):
```svg
<circle cx="245" cy="244" r="50" class="ri-b"/><circle cx="255" cy="236" r="50" class="ri-p"/>
<circle cx="250" cy="240" r="45" class="ri-v"/>
```

**Màu chồng cắt chính xác** (thanh xanh đi qua đĩa hồng thành tím đúng chỗ giao):
```svg
<defs><clipPath id="ri1-dc"><circle cx="-70" cy="-10" r="42"/></clipPath></defs>
<circle cx="-70" cy="-10" r="42" class="ri-p"/>
<rect x="-126" y="-30" width="236" height="16" class="ri-b"/>
<rect x="-126" y="-30" width="236" height="16" class="ri-v" clip-path="url(#ri1-dc)"/>
```

**Tờ giấy khoét** (thẻ, slide thu nhỏ, nhãn): hình chữ nhật màu giấy, phía sau là cùng hình đó bằng một mực, lệch 4 px để lộ viền.
```svg
<rect x="-144" y="-80" width="300" height="169" class="ri-b"/>
<rect x="-150" y="-84" width="300" height="169" class="ri-paper"/>
```

**Ô tram theo bậc** (mật độ, mức độ, tỷ lệ không cần số):
```svg
<pattern id="ri7-b2" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(15)">
  <circle cx="8" cy="8" r="4.6" class="ri-b"/></pattern>
<rect x="640" y="12" width="400" height="96" fill="url(#ri7-b2)"/>
```
Bán kính 2,8 / 4,6 / 6,6 px trên ô 16 px cho ba bậc nhạt, vừa, đậm.

**Thẻ tên giống nhau**: dải giấy 60x16 có gạch xanh 4 px ở đáy, đặt dưới mỗi lần xuất hiện của cùng một vật để nói "cùng tên".

## 4. Bốn công thức minh họa

Khung 1920x1080, lề an toàn 80 px hai bên, 60 px trên dưới. SVG là con trực tiếp của `<section>`, có `class="ri-art"`, `style="left: ..px; top: ..px;"` và thuộc tính `width`, `height`, `viewBox` (script xuất PPTX cần đủ ba thứ này).

**4.1. Hình chính cho bìa.** Cột chữ bìa chiếm x 120..1080, nên hình nằm trong x 1160..1860, y 120..940, chồng lên phong cảnh của diễn viên (mặt trời hồng, dải vàng, đồi lục, ruộng tram xanh). Lớp vẽ: (1) vệt chấm xanh nối các vật; (2) hai đến ba vật chính của đề tài, nhỏ dần hoặc lớn dần theo đường cong; (3) vật sau nhiều bản in hơn vật trước để kể chuyện "thêm mực". Không chữ trong hình; tiêu đề đã ở cột trái.

**4.2. Sơ đồ khái niệm (3 đến 5 thành phần).** Trên slide `content`, đặt trong vùng điểm nhấn x 1260..1800, y 280..800 (trên tấm giấy khoét của diễn viên `strip`); câu chốt là một `<p>` HTML đặt tuyệt đối bên dưới (y khoảng 820) để sửa được trong PPTX. Lớp vẽ: nền tram vàng làm "sân khấu"; các thành phần là đĩa hoặc khối lệch đăng; quan hệ là một đường xanh vẽ dần (`class="draw" pathLength="1"`); nhãn giống nhau hay khác nhau thể hiện bằng thẻ tên. Thành phần quan trọng nhất mang lõi `--ink3`.

**4.3. Quy trình hoặc dòng thời gian.** Trên slide `timeline`, SVG là một dải cao khoảng 90 px phủ trục y 630 (ví dụ `top: 586px`, cao 88). Tâm các nút phải trùng chấm của layout: với N bước trong x 120..1800, nút thứ i ở x = 136 + i × (1680 + 32) / N. Lớp vẽ: ghost hồng mảnh lệch dưới, trục xanh vẽ dần, mỗi nút **thêm một bản in** so với nút trước (tram một mực, đặc một mực, hai mực, thêm quầng vàng, đủ ba mực). Chữ bước để nguyên trong HTML phía trên và dưới dải.

**4.4. Con số hoặc so sánh.** Trên slide `stats`, số ở giữa vùng y 460..800 trên dải vàng của diễn viên `band` (y 270..830), nên hình đặt dưới: y 850..970, mỗi hình căn giữa cột của số. Dùng ô tram theo bậc để nói "ít, vừa, nhiều"; bậc cao nhất có thể chồng thêm một bản tram thứ hai lệch đăng để cố ý tạo vẻ "bết", hợp ý "quá nhiều". Không vẽ biểu đồ có số nếu không có nguồn.

## 5. Chuyển động trong bản HTML

- Vẽ nét: `class="draw"` với `pathLength="1"` (có sẵn trong `morph-motion.css`), trễ bằng `style="--d: 0.3"`.
- Lệch đăng rồi khớp: bọc từng bản in trong `<g class="ri-kick" style="--kx: 10px; --ky: -8px; --d: 0.4">`, keyframes dịch chuyển bằng thuộc tính CSS `translate` từ (kx, ky) về 0 có rung nhẹ, chỉ chạy khi `.slide.active`. Dùng `translate` (không dùng `transform`) để không đè thuộc tính `transform` của SVG.
- Cả hình hiện bằng `reveal` hoặc `reveal-scale` trên thẻ `<svg>`.
- Tắt `ri-kick` trong `@media (prefers-reduced-motion: reduce)`.

Khối CSS mẫu cho deck:
```css
@keyframes ri-kick { 0% { translate: var(--kx) var(--ky); } 55% { translate: calc(var(--kx) * -0.25) calc(var(--ky) * -0.25); } 100% { translate: 0 0; } }
.slide.active .ri-kick { animation: ri-kick 0.9s cubic-bezier(.3, .7, .4, 1) calc(var(--reveal-base) + var(--d, 0) * 1s) both; }
```

**Khi xuất PPTX:** SVG inline thành ảnh vector (PowerPoint 365), màu lấy từ class, nét `draw` thành hiệu ứng quét. Chuyển động `ri-kick` không sang PPTX (hình đứng ở vị trí đã khớp). SVG inline xuất trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`. Chữ cần sửa được thì để ngoài SVG.

## 6. Cấm

- Màu ngoài bảng trên, gradient mượt (chỉ được tram theo bậc), bóng đổ mờ, 3D, ánh kim.
- Ba bản tram chồng lên nhau trong một vùng (thành bùn), trừ khi cố ý minh họa "quá tải".
- Nét viền đen quanh vật, `mix-blend-mode`, `filter: blur` nặng.
- Chữ trong ảnh (trừ số ngắn khi thật cần), logo hay hình máy in của hãng RISO.
- Lệch đăng ngẫu nhiên mỗi khung hình; lệch quá 14 px khi đứng yên.
- Hình đè lên chữ hoặc nằm trong hàng tiêu đề y 90..165.

Nguồn: Phỏng theo lemo-opuscar `styles/risograph/STYLE.md` (MIT) qua MotionFly.
