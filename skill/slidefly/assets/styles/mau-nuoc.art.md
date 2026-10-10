# Màu nước: luật vẽ minh họa cho từng slide

Đi kèm `mau-nuoc.css`. Mỗi slide đáng nhớ (bìa, sơ đồ, quy trình, con số, slide kết) có một minh họa SVG inline vẽ riêng theo nội dung, như một trang sổ tay thực địa tự tô màu: giấy cotton ấm, mảng màu loang trong suốt, nét chì mảnh phác trước, ghi chú viết tay bên cạnh.

## 1. Tinh thần

- **Một tờ giấy ấm có vân dưới mọi thứ.** Giấy là màu trắng: chỗ sáng là chỗ chưa tô, không bao giờ tô trắng tinh.
- **Mọi thứ là mảng màu trong suốt.** Mỗi mảng tô 2 đến 3 lượt lệch nhau một chút, mép đọng màu đậm hơn (tide line). Hai mảng chồng lên nhau thì chỗ chồng đậm hơn, như màu thật. Không viền vector đen quanh hình; "nét" duy nhất là mép đọng của chính mảng màu.
- **Phác chì trước, tô màu sau.** Nét chì xám mảnh (đường chân trời, khung, mũi tên) hiện trước, rồi màu loang lên theo thứ tự cấu trúc trước, chi tiết sau: nền, khối lớn, vật chính, điểm nhấn.
- **Mẫu vật kèm ghi chú.** Một vật chính mỗi hình, nhãn ngắn đặt bên cạnh bằng chữ viết tay hoặc mono nhỏ, có đường dẫn chì. Nhãn không che vật.
- **Giọng điềm tĩnh, tò mò, chính xác.** Số là số thật; màu có thể mang dữ liệu (chuyển màu theo bậc, không chuyển mượt kiểu phần mềm).

## 2. Bảng màu, nét, chất liệu

| Biến | Dùng cho |
|---|---|
| `var(--paper)` `#F3ECDD`, `var(--sheet)` `#FBF8F1` | giấy nền, tờ giấy mép xé |
| `var(--ink)` `#2F2922`, `var(--ink-2)` `#6E5D4B` | thân cây, cành, nét cọ khô; không dùng cho mảng lớn |
| `var(--graphite)` `#7E7871` | nét chì phác, mũi tên, khung |
| `var(--sage)` `#7F9F6A`, `var(--leaf)` `#4E6E3C` | lá, đồi gần, mảng chính |
| `var(--straw)` `#D6B36A` | đất, nắng, mảng ấm |
| `var(--rain)` `#8FA9BE`, `var(--slate)` `#5F7486` | trời, nước, đồi xa |
| `var(--vermilion)` `#C2462B` | điểm nhấn duy nhất: một vật lặp lại (mặt trời, giọt màu, bước cuối) |

- Mỗi hình 3 đến 5 màu cộng mực. Đậm hơn là tô thêm lượt, không đổi sang màu tối hơn.
- Độ trong suốt: lượt 1 `fill-opacity` .34 đến .42, lượt 2 .16 đến .2, mép đọng `stroke-opacity` .5 đến .85, dày 1,6 đến 2,4px.
- Nét chì: `stroke-width` 1,6, đầu tròn, chỉ màu graphite. Nét cọ khô: 1 đến 2,4px, `stroke-dasharray` ngẫu nhiên để có chỗ đứt (flying white).
- Màu gán bằng class (`.f-sage { fill: var(--sage) }`, `.t-sage { fill: none; stroke: var(--sage) }`), vì thuộc tính `fill="var(...)"` trên SVG không chạy. Script xuất PPTX đọc được class và đổi ra màu thật.
- Chất liệu bằng SVG: lượt chồng, mép đọng, chấm hạt (granulation) là vài `circle` r .6 đến 1,5 cùng màu. Được dùng `linearGradient`, `radialGradient`, `pattern` nhẹ. Bộ lọc (`feTurbulence`, `feGaussianBlur`) chỉ để trang trí bản HTML: khi xuất PPTX tên thẻ bị viết thường và có thể làm mất hình, nên mặc định không dùng.

## 3. Hình mẫu lặp lại

**Mảng màu ba lượt (wash).** Cùng một đường cong kín vẽ 3 lần: thân, lượt lệch nhỏ hơn, mép đọng.
```svg
<path class="f-sage" fill-opacity=".36" d="M57 3C58 18 52 30 30 40C10 48-30 44-50 30C-68 16-66-14-46-35C-28-50 10-52 30-40C48-30 56-14 57 3Z"/>
<path class="f-sage" fill-opacity=".18" d="M51 5C50 22 40 34 20 38C-10 40-40 36-50 18C-56 0-46-20-26-30C-8-38 24-36 40-24C50-14 52-6 51 5Z"/>
<path class="t-sage" stroke-opacity=".75" stroke-width="2" d="M57 3C58 18 52 30 30 40C10 48-30 44-50 30C-68 16-66-14-46-35C-28-50 10-52 30-40C48-30 56-14 57 3Z"/>
```
**Giọt màu nở (bloom).** Mép gợn nhiều sóng nhỏ, lõi nhạt, vài hạt bắn ngoài; chỉ dùng màu vermilion, một lần mỗi hình.
```svg
<path class="f-ver" fill-opacity=".45" d="M86 50C88 62 80 74 70 80C60 88 44 90 32 84C20 78 12 64 13 50C14 36 22 22 34 16C46 10 62 12 72 20C80 28 85 38 86 50Z"/>
<path class="t-ver" stroke-opacity=".9" stroke-width="2.6" d="M86 50C88 62 80 74 70 80C60 88 44 90 32 84C20 78 12 64 13 50C14 36 22 22 34 16C46 10 62 12 72 20C80 28 85 38 86 50Z"/>
<circle class="f-ver" fill-opacity=".6" cx="94" cy="40" r="1.6"/>
```

**Nét cọ khô.** Một dải có mép răng cưa (`fill-opacity` .45) và 2 đến 3 vệt lông cọ đứt quãng chạy dọc, kết thúc sớm hơn dải.
```svg
<path class="br" stroke-width="1.2" stroke-opacity=".4" stroke-dasharray="60 8 30 5 90 12" d="M20 41 L1700 42"/>
```
**Khung chì phác.** Bốn cạnh vượt nhẹ qua góc, lượt hai mảnh và nhạt hơn, lệch 2 đến 3px.

**Tờ giấy mép xé.** Hình chữ nhật có cạnh răng cưa nhỏ (điểm cách 7px, lệch 0 đến 2,4px), tô `var(--sheet)` đặc, làm nền cho vật mẫu.

**Cành lá.** Cuống một nét cọ, lá là hình thoi cong tô một lượt kèm gân giữa mảnh; lá xa nhạt hơn lá gần.

## 4. Bốn công thức minh họa (khung 1920x1080)

**Hình chính cho bìa.** Đặt trong tờ giấy của diễn viên `sheet` (tư thế cover: x 1080 đến 1800, y 120 đến 960), SVG khoảng 660x640 ở `left:1110px; top:160px`. Chữ bìa ở cột trái x 140 đến 1020, không vẽ sang. Lớp vẽ: (1) chì phác đường chân trời, vòng tròn mặt trời, trục thân cây; (2) trời `rain` .22; (3) mặt trời vermilion; (4) ba lớp đồi xa `slate`, giữa `sage`, gần `leaf`, xa nhạt gần đậm; (5) vật chính theo nội dung (cây, tòa nhà, dụng cụ) bằng nhiều mảng chồng; (6) vài nét cọ khô ở tiền cảnh. Lưu ý: kiểu `cover` không xuất SVG sang PPTX, nên bìa bản PPTX chỉ còn diễn viên; muốn có hình trong PPTX thì làm bìa bằng `data-layout="free"` kèm `data-stage="cover"`.

**Sơ đồ khái niệm (3 đến 5 thành phần).** Mỗi thành phần là một mảng màu riêng hoặc một vật mẫu; quan hệ là mũi tên chì cong. Trên slide `content`: SVG đặt trong vùng x 1260 đến 1800, y 270 đến 860; bỏ khối `.highlight`, ghi `style="left:120px; width:1040px"` trên `.bullets` để PPTX không kéo chữ sang phải. Nhãn và câu chốt là thẻ `<p>` đặt tuyệt đối ngoài SVG, nằm trên giấy trống cạnh mảng màu. Cùng một vật xuất hiện nhiều lần thì giữ nguyên đường cong, chỉ đổi vị trí, cỡ, màu.

**Quy trình hoặc dòng thời gian.** Trên slide `timeline`: một dòng sông màu `rain` chạy dọc trục y 630 (SVG cao khoảng 90px, `top:584px`), mỗi bước một vũng màu đặt đúng tâm chấm của bước: x = 136 + 342,4 × i với 5 bước (khoảng cách cột 32px, vùng 120 đến 1800). Màu vũng đi theo bậc: rơm, xô thơm, mưa, lá, và vermilion cho bước cuối. Giữ trống dải y 585 đến 675 ngoài sông, chữ bước nằm trên và dưới.

**Con số hoặc so sánh.** Không vẽ đè lên số (PPTX đặt hình lên trên chữ). Trên slide `stats`: một dải SVG cao khoảng 160px ngay dưới tiêu đề (`top:282px`), mỗi cột số một hình nhỏ minh họa ý so sánh (ví dụ trang thu nhỏ có 3, 5, 7 nét cọ). Tâm các cột với 3 số: x 384, 960, 1536. Màu hình trùng màu số của cột đó.

## 5. Chuyển động

- Nét chì: `class="draw" pathLength="1"` (có sẵn trong `morph-motion.css`), trễ bằng `style="--d:.3"`. Bản PPTX chuyển thành hiệu ứng quét.
- Màu loang: bọc từng lớp trong `<g class="wc-in" style="--d:...">`; CSS của deck:
```css
.slide .wc-in { opacity: 0; transform: translateY(10px); transition: opacity 1s ease, transform 1.2s var(--morph-ease); }
.slide.active .wc-in { opacity: 1; transform: none; transition-delay: calc(var(--reveal-base) + var(--d, 0) * 1s); }
```
- Thứ tự trễ: chì 0 đến .3 giây, nền .5, khối lớn .8 đến 1,4, vật chính 1,6 đến 2, chi tiết sau cùng. Không rung, không lắc, không lặp vô hạn.
- Xuất PPTX: SVG phải là con trực tiếp của `<section>`, có `width`, `height` và `style="left:..px; top:..px"`; khi đó nó thành một hình vector, hiện mờ dần. Chữ cần sửa được thì để ngoài SVG (thẻ `<p>` có `left/top/width/height` trong `style`). Kiểu `cover`, `closing`, `section`, `quote` không xuất SVG.

## 6. Cấm

- Màu ngoài bảng trên; trắng tinh; đen tuyền; nhiều hơn một điểm nhấn vermilion mỗi hình.
- Viền vector đậm quanh hình, hình phẳng một màu đặc như clip-art, 3D, bóng đổ, ánh kim, gradient cầu vồng.
- Chữ nằm trong SVG (trừ ký hiệu một hai ký tự), chữ đè lên mảng màu đậm, nhãn che vật.
- Số liệu tự đặt trong hình: hình minh họa ý, số lấy từ slide và có nguồn.
- Bộ lọc nặng, `mix-blend-mode`, ảnh bitmap nhúng giả màu nước.

Nguồn: Phỏng theo lemo-opuscar `styles/watercolor/STYLE.md` (MIT) qua MotionFly.
