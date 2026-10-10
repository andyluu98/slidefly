# Thủy mặc: luật vẽ minh họa SVG cho từng slide

Lớp sân khấu là `thuy-mac.css` (diễn viên bloom, far, near, stroke, bamboo, boat, seal). File này là luật để vẽ thêm **một minh họa SVG inline riêng cho từng slide**, theo đúng nội dung slide đó, cùng chất với sân khấu. Deck mẫu: `gallery/59_demo-thuy-mac.html`.

## 1. Tinh thần

- Tranh thủy mặc vẽ trên giấy xuyến ngà: mực tàu năm sắc độ, thêm **một** màu son duy nhất cho con dấu.
- Khoảng trắng là chất liệu: 60 đến 80 phần trăm khung là giấy trống (trời, nước, sương). Thấy rối thì bỏ bớt mực, không thêm sắc độ.
- Không có đường viền kiểu vector. Hình thành từ nét bút lông có lực (mép đậm của nét chính là đường bao), từ mảng loang ướt và nét khô quét nhanh để lộ giấy (phi bạch).
- Xa thì nhạt và mềm, gần thì đậm và có kết cấu. Núi tan dần xuống thành dải sương, nước là giấy trống với vài vệt khô.
- Hình được "vẽ ra" theo thứ tự nét, không cắt ghép.

## 2. Bảng màu, nét, chất liệu

| Vai | Giá trị (biến của style) | Dùng cho |
|---|---|---|
| Giấy | `var(--paper)` #F2ECDE | nền, sương, phi bạch (nét giấy đè lên mực) |
| Mực tiêu (cháy) | `var(--ink-jiao)` độ đặc 0,96 | chấm rêu, nét quyết định, nhân của giọt mực |
| Mực nùng (đặc) | `var(--ink-nong)` 0,82 | mép đậm của nét, đường sống núi gần |
| Mực trọng | `var(--ink-zhong)` 0,6 | nét phụ, nếp gấp |
| Mực đạm (nhạt) | `var(--ink-dan)` 0,34 | thân núi, nét thuân (cun) |
| Mực thanh (trong) | `var(--ink-qing)` 0,16 | núi xa, mặt nước, vệt sóng |
| Mực lạnh | `var(--ink-cool)` #3A4044 | núi xa nhất (mực loãng ngả xám lạnh) |
| Son | `var(--son)` #B02E22 | chỉ con dấu, tối đa một điểm nhỏ mỗi slide |

- Gốc mực là `var(--ink)` #1B1A17; sắc độ tạo bằng `fill-opacity`, `stroke-opacity`, không pha màu khác.
- Nét: chính 5 đến 7px, phụ 3 đến 4px, thuân và vệt nước 2 đến 3px; luôn `stroke-linecap="round"`.
- Chất liệu được phép: `linearGradient` dọc cho núi tan vào sương (đậm trên, 0 ở chân), `radialGradient` cho vết loang (giữa nhạt, mép đậm hơn rồi tắt hẳn), chấm rêu bằng `circle`, phi bạch bằng nét màu giấy mảnh đè lên nét mực. Filter nhẹ (`feGaussianBlur` dưới 2px) chỉ dùng trong bản HTML; PowerPoint có thể bỏ qua.
- Trong SVG ghi màu bằng mã hex ở thuộc tính (`fill="#1B1A17"`, `stop-color`) để bản xuất PPTX giữ đúng; `var(--...)` chỉ dùng trong CSS của deck.

## 3. Bộ hình mẫu lặp lại

**Núi một nét** (khung chuẩn 100x80, phóng bằng `transform`): thân loang + mép đậm bên trái + chấm rêu.
```svg
<path fill="url(#m)" d="M0 80C10 66 18 52 28 40C34 32 38 22 44 12C47 7 51 6 54 11C58 20 62 28 68 34C74 40 80 38 86 44C92 52 96 66 100 80Z"/>
<path fill="url(#e)" d="M3 79C12 64 22 50 31 39C37 30 41 20 45 12C47 9 50 8 52 10C47 20 42 32 35 42C26 55 17 67 12 80Z"/>
```
`#m`: stop 0 mực 0,6; 0,7 mực 0,22; 1 mực 0. `#e`: stop 0 mực 0,9; 1 mực 0,1.

**Nét bút có phi bạch**: nét mực đặc rồi hai ba nét màu giấy mảnh đè ở nửa sau.
```svg
<path class="draw" pathLength="1" stroke="#1B1A17" stroke-opacity=".88" stroke-width="30" stroke-linecap="round" fill="none" d="M20 60C120 46 280 48 380 62"/>
<path stroke="#F2ECDE" stroke-width="2" fill="none" d="M200 52L370 58M240 62L372 66"/>
```

**Vết loang có ngấn mép**: elip với gradient tròn, nghiêng nhẹ cho khỏi tròn đều.
```svg
<radialGradient id="g"><stop offset="0" stop-color="#1B1A17" stop-opacity="0"/><stop offset=".5" stop-color="#1B1A17" stop-opacity=".22"/><stop offset=".93" stop-color="#1B1A17" stop-opacity=".9"/><stop offset="1" stop-color="#1B1A17" stop-opacity="0"/></radialGradient>
<ellipse cx="60" cy="60" rx="35" ry="29" transform="rotate(-8 60 60)" fill="url(#g)" fill-opacity=".5"/>
```

**Dải sương**: elip màu giấy, gradient tròn từ 0,96 ở giữa về 0 ở mép, đặt ngang chân núi.

**Thuyền nan, cành trúc, con dấu**: đã có sẵn là diễn viên `boat`, `bamboo`, `seal`; minh họa không vẽ lại, chỉ chừa chỗ cho chúng.

## 4. Bốn công thức minh họa

Khung 1920x1080. Vùng an toàn: lề 80px hai bên, 60px trên dưới. Hàng tiêu đề y 90 đến 165 để trống. SVG đặt `class="ink-art"`, `position: absolute`, ghi `left`, `top` trong `style` và `width`, `height` ở thuộc tính.

**4.1. Hình chính cho bìa** (`data-layout="cover"`, chữ bên trái x 200 đến 980)
- Vị trí: x 1010 đến 1870, y 120 đến 920.
- Lớp: (1) thân núi chính và núi phụ loang; (2) mép đậm bên trái núi chính; (3) đường sống núi vẽ dần bằng `.draw`; (4) nét thuân mảnh; (5) chấm rêu; (6) dải sương che chân núi; (7) vài vệt nước khô phía dưới.
- Lưu ý: đỉnh núi tránh góc phải trên (chỗ cành trúc), chừa mặt nước trống cho thuyền ở khoảng y 900.

**4.2. Sơ đồ khái niệm** (3 đến 5 thành phần, đặt ở vùng highlight x 1260 đến 1800 của `content`)
- Ví dụ trong deck mẫu: cùng một ngọn núi ở hai tư thế (xa nhạt nhỏ, gần đậm lớn) nối bằng một nét cong có phi bạch, đầu nét chấm vào đỉnh núi.
- Lớp: thành phần nhạt trước, thành phần chính đậm sau, nét nối vẽ dần cuối cùng.
- Nhãn và câu chốt là thẻ `<p>` HTML đặt tuyệt đối dưới từng hình (font `var(--font-display)` nghiêng, 26px, màu `var(--muted)`), không viết chữ trong SVG. Danh sách bên trái ghi `style="left:120px; width:1040px"` để bản PPTX không chồng lên hình.

**4.3. Quy trình hoặc dòng thời gian** (`timeline`, trục y 630)
- Diễn viên `stroke` đã nằm làm trục. Minh họa đặt `left:100px; top:570px`, cao 120px, gồm một vết loang quanh mỗi mốc, sắc độ tăng dần từ 0,25 tới 0,85 (mực đậm dần qua từng bước) và vài hạt mực bắn ở các bước sau.
- Đặt SVG trước khối `.timeline` trong HTML để chữ nằm trên. Mốc thứ i của 5 cột: x = 132 + i x 342,4.
- Lưu ý: chừa trống tâm mỗi vết loang cho chấm mốc của style.

**4.4. Con số hoặc so sánh** (`stats` hoặc slide kết)
- Ví dụ trong deck mẫu: dưới mỗi con số là một nét bút, nhạt và thưa (ít ý) tới đặc và loang (nhiều ý). Vị trí: `left:120px; top:836px`, cao 120px, giữa các cột ở x 264, 840, 1416 (tọa độ trong SVG).
- Lớp: nét chính `.draw` theo thứ tự trái sang phải, nét khô mảnh, phi bạch màu giấy, hạt mực cho mức đậm nhất.
- Không thêm số mới vào hình; số chỉ nằm trong chữ của slide và phải có nguồn.

## 5. Chuyển động và xuất PPTX

- Nét vẽ dần: `<path class="draw" pathLength="1" style="--d:0.4">` (cần `morph-motion.css`); chạy khi slide có lớp `.slide.active`, `--d` là độ trễ giây. Thứ tự: đường sống núi, nét phụ, vệt nước.
- Hiện dần cả bức: `class="reveal"` trên `<svg>`; từng cụm: `class="reveal-scale"` trên `<g>` kèm `style="--i:n"` và CSS `transform-box: fill-box; transform-origin: center`.
- Không dùng chuyển động lặp vô hạn, không rung, không xoay liên tục.
- Khi xuất: SVG inline là con trực tiếp của slide, có `left/top` trong `style` và `width/height` thì thành ảnh vector (PowerPoint 365), hiệu ứng `draw` thành vẽ quét. Chữ cần sửa được thì để ngoài SVG.
- SVG nhúng trong CSS (diễn viên) phải mã hóa `(` `)` thành `%28` `%29`, nếu không trình xuất cắt `url(...)` sai chỗ và hình biến mất. Đặt id gradient riêng (ví dụ `tmFa`) để khỏi trùng.

## 6. Cấm

- Màu ngoài bảng trên; son làm mảng lớn, son tô chữ, hơn một điểm son trên một slide.
- Viền kín kiểu vector, mảng phẳng không gradient, bóng đổ, 3D, ánh kim, hiệu ứng thủy tinh.
- Chữ trong ảnh (kể cả chữ Hán thật hay giả làm họa tiết); con dấu chỉ là ký hiệu chữ 山 đã có trong diễn viên `seal`.
- Màu nước (wash màu), hoa văn khắc gỗ viền dày kiểu Đông Hồ, vòng enso kiểu wabi.
- Minh họa đè lên chữ, lấn vào hàng tiêu đề, phủ kín khung làm mất khoảng trắng.
- `mix-blend-mode`, filter nặng, ảnh bitmap thay cho nét vẽ.

Nguồn: Phỏng theo lemo-opuscar `styles/ink-wash/STYLE.md` (MIT) qua MotionFly.
